import struct
import re

class IEEE754Converter:
    """Clase que maneja las conversiones entre números decimales y IEEE 754"""
    
    @staticmethod
    def float_to_bin32(num):
        """Convierte un número de punto flotante a su representación IEEE 754 de 32 bits"""
        try:
            # se usa struct para obtener la representación binaria exacta
            binary = struct.unpack('!I', struct.pack('!f', num))[0]
            # se convierte a una cadena binaria de 32 bits
            binary_str = format(binary, '032b')
            
            # se extrae signo, exponente y mantisa
            sign = binary_str[0]
            exponent = binary_str[1:9]
            mantissa = binary_str[9:]
            
            return binary_str, sign, exponent, mantissa
        except Exception as e:
            raise ValueError(f"Error al convertir a IEEE 754 de 32 bits: {e}")
    
    @staticmethod
    def float_to_bin64(num):
        """Convierte un número de punto flotante a su representación IEEE 754 de 64 bits"""
        try:
            # se usas struct para obtener la representación binaria exacta
            binary = struct.unpack('!Q', struct.pack('!d', num))[0]
            # se convierte a cadena binaria de 64 bits
            binary_str = format(binary, '064b')
            
            # se extrae signo, exponente y mantisa
            sign = binary_str[0]
            exponent = binary_str[1:12]
            mantissa = binary_str[12:]
            
            return binary_str, sign, exponent, mantissa
        except Exception as e:
            raise ValueError(f"Error al convertir a IEEE 754 de 64 bits: {e}")
    
    @staticmethod
    def bin32_to_float(binary_str):
        """Convierte una cadena binaria IEEE 754 de 32 bits a un número decimal"""
        try:
            # verificar  cadena binaria válida de 32 bits
            if not re.match(r'^[01]{32}$', binary_str):
                raise ValueError("Debe ingresar exactamente 32 bits (0s y 1s)")
            
            # se convierte cadena binaria a  entero y luego a float
            binary_int = int(binary_str, 2)
            float_num = struct.unpack('!f', struct.pack('!I', binary_int))[0]
            
            # se extrae signo, exponente y mantisa
            sign = binary_str[0]
            exponent = binary_str[1:9]
            mantissa = binary_str[9:]
            
            return float_num, sign, exponent, mantissa
        except Exception as e:
            raise ValueError(f"Error al convertir desde IEEE 754 de 32 bits: {e}")
    
    @staticmethod
    def bin64_to_float(binary_str):
        """Convierte una cadena binaria IEEE 754 de 64 bits a un número decimal"""
        try:
            # verificacion cadena binaria válida de 64 bits
            if not re.match(r'^[01]{64}$', binary_str):
                raise ValueError("Debe ingresar exactamente 64 bits (0s y 1s)")
            
            # Convertir  cadena binaria a entero y luego a float
            binary_int = int(binary_str, 2)
            float_num = struct.unpack('!d', struct.pack('!Q', binary_int))[0]
            
            # se extrae signo, exponente y mantisa
            sign = binary_str[0]
            exponent = binary_str[1:12]
            mantissa = binary_str[12:]
            
            return float_num, sign, exponent, mantissa
        except Exception as e:
            raise ValueError(f"Error al convertir desde IEEE 754 de 64 bits: {e}")
    
    @staticmethod
    def analyze_ieee754_components(sign, exponent, mantissa, precision):
        """Analiza los componentes de IEEE 754 y proporciona información detallada"""
        result = []
         
        # info del signo
        sign_value = "Positivo (0)" if sign == "0" else "Negativo (1)"
        result.append(f"Signo: {sign} → {sign_value}")
        
        # info del exponente
        if precision == 32:
            bias = 127
            exp_bits = 8
        else:  # 64 bits
            bias = 1023
            exp_bits = 11
            
        if all(bit == '0' for bit in exponent):
            result.append(f"Exponente: {exponent} → Número desnormalizado o cero")
        elif all(bit == '1' for bit in exponent):
            result.append(f"Exponente: {exponent} → Infinito o NaN")
        else:
            exp_value = int(exponent, 2)
            unbiased_exp = exp_value - bias
            result.append(f"Exponente: {exponent} → {exp_value} (valor almacenado)")
            result.append(f"Exponente real: {unbiased_exp} (sin sesgo)")
        
        # información de la mantisa
        if precision == 32:
            implicit_bit = "1" if not all(bit == '0' for bit in exponent) and not all(bit == '1' for bit in exponent) else "0"
        else:  # 64 bits
            implicit_bit = "1" if not all(bit == '0' for bit in exponent) and not all(bit == '1' for bit in exponent) else "0"
            
        result.append(f"Mantisa: {mantissa}")
        result.append(f"Bit implícito: {implicit_bit}")
        
        if all(bit == '0' for bit in exponent) and all(bit == '0' for bit in mantissa):
            if sign == "0":
                result.append("Caso especial: Cero positivo (+0)")
            else:
                result.append("Caso especial: Cero negativo (-0)")
        elif all(bit == '1' for bit in exponent):
            if all(bit == '0' for bit in mantissa):
                if sign == "0":
                    result.append("Caso especial: Infinito positivo (+∞)")
                else:
                    result.append("Caso especial: Infinito negativo (-∞)")
            else:
                result.append("Caso especial: NaN (Not a Number)")
                
        return "\n".join(result)