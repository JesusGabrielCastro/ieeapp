import tkinter as tk
from tkinter import ttk, messagebox
from modelo import IEEE754Converter

class IEEEConverterApp:
    """Clase principal de la aplicación de conversión IEEE 754"""
    
    def __init__(self, root):
        """Inicializa la aplicación con la ventana root dada"""
        self.root = root
        self.root.title("Conversor IEEE 754")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        self.converter = IEEE754Converter()
        
        self.create_widgets()
        
    def create_widgets(self):
        """Crea todos los widgets de la interfaz"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Notebook (pestañas)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña: Decimal a IEEE 754
        self.create_decimal_to_ieee_tab()
        
        # Pestaña: IEEE 754 a Decimal
        self.create_ieee_to_decimal_tab()
    
    def create_decimal_to_ieee_tab(self):
        """Crea la pestaña para convertir de decimal a IEEE 754"""
        dec_to_ieee_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(dec_to_ieee_frame, text="Decimal a IEEE 754")
        
        # Título
        ttk.Label(dec_to_ieee_frame, text="Convertir de Decimal a IEEE 754", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)
        
        # Entrada para el número decimal
        ttk.Label(dec_to_ieee_frame, text="Número decimal:").grid(row=1, column=0, sticky="w", pady=5)
        self.decimal_entry = ttk.Entry(dec_to_ieee_frame, width=30)
        self.decimal_entry.grid(row=1, column=1, sticky="w", pady=5)
        
        # Selector de precisión
        ttk.Label(dec_to_ieee_frame, text="Precisión:").grid(row=2, column=0, sticky="w", pady=5)
        self.precision_var = tk.StringVar(value="32")
        precision_frame = ttk.Frame(dec_to_ieee_frame)
        precision_frame.grid(row=2, column=1, sticky="w", pady=5)
        ttk.Radiobutton(precision_frame, text="32 bits", variable=self.precision_var, value="32").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(precision_frame, text="64 bits", variable=self.precision_var, value="64").pack(side=tk.LEFT, padx=5)
        
        # Botón de conversión
        ttk.Button(dec_to_ieee_frame, text="Convertir", command=self.decimal_to_ieee).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Marco para resultados
        result_frame = ttk.LabelFrame(dec_to_ieee_frame, text="Resultados", padding="10")
        result_frame.grid(row=4, column=0, columnspan=3, sticky="nsew", pady=10)
        dec_to_ieee_frame.columnconfigure(0, weight=1)
        dec_to_ieee_frame.rowconfigure(4, weight=1)
        
        # Resultados
        ttk.Label(result_frame, text="Representación IEEE 754:").grid(row=0, column=0, sticky="w", pady=5)
        self.ieee_result = ttk.Entry(result_frame, width=80)
        self.ieee_result.grid(row=0, column=1, sticky="w", pady=5)
        
        # Botón para copiar resultado
        ttk.Button(result_frame, text="Copiar", command=lambda: self.copy_to_clipboard(self.ieee_result.get())).grid(row=0, column=2, padx=5)
        
        # Detalles de componentes
        ttk.Label(result_frame, text="Componentes:").grid(row=1, column=0, sticky="nw", pady=5)
        self.components_text = tk.Text(result_frame, width=70, height=12, wrap=tk.WORD)
        self.components_text.grid(row=1, column=1, columnspan=2, sticky="nsew", pady=5)
        
        # Configurar el estiramiento
        result_frame.columnconfigure(1, weight=1)
        result_frame.rowconfigure(1, weight=1)
    
    def create_ieee_to_decimal_tab(self):
        """Crea la pestaña para convertir de IEEE 754 a decimal"""
        ieee_to_dec_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(ieee_to_dec_frame, text="IEEE 754 a Decimal")
        
        # Título
        ttk.Label(ieee_to_dec_frame, text="Convertir de IEEE 754 a Decimal", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)
        
        # Entrada para la representación binaria
        ttk.Label(ieee_to_dec_frame, text="Representación binaria:").grid(row=1, column=0, sticky="w", pady=5)
        self.binary_entry = ttk.Entry(ieee_to_dec_frame, width=80)
        self.binary_entry.grid(row=1, column=1, sticky="w", pady=5)
        
        # Selector de precisión
        ttk.Label(ieee_to_dec_frame, text="Precisión:").grid(row=2, column=0, sticky="w", pady=5)
        self.bin_precision_var = tk.StringVar(value="32")
        bin_precision_frame = ttk.Frame(ieee_to_dec_frame)
        bin_precision_frame.grid(row=2, column=1, sticky="w", pady=5)
        ttk.Radiobutton(bin_precision_frame, text="32 bits", variable=self.bin_precision_var, value="32").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(bin_precision_frame, text="64 bits", variable=self.bin_precision_var, value="64").pack(side=tk.LEFT, padx=5)
        
        # Botón de conversión
        ttk.Button(ieee_to_dec_frame, text="Convertir", command=self.ieee_to_decimal).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Marco para resultados
        result_frame = ttk.LabelFrame(ieee_to_dec_frame, text="Resultados", padding="10")
        result_frame.grid(row=4, column=0, columnspan=3, sticky="nsew", pady=10)
        ieee_to_dec_frame.columnconfigure(0, weight=1)
        ieee_to_dec_frame.rowconfigure(4, weight=1)
        
        # Resultados
        ttk.Label(result_frame, text="Valor decimal:").grid(row=0, column=0, sticky="w", pady=5)
        self.decimal_result = ttk.Entry(result_frame, width=30)
        self.decimal_result.grid(row=0, column=1, sticky="w", pady=5)
        
        # Botón para copiar resultado
        ttk.Button(result_frame, text="Copiar", command=lambda: self.copy_to_clipboard(self.decimal_result.get())).grid(row=0, column=2, padx=5)
        
        # Detalles de componentes
        ttk.Label(result_frame, text="Componentes:").grid(row=1, column=0, sticky="nw", pady=5)
        self.bin_components_text = tk.Text(result_frame, width=70, height=12, wrap=tk.WORD)
        self.bin_components_text.grid(row=1, column=1, columnspan=2, sticky="nsew", pady=5)
        
        # Configurar el estiramiento
        result_frame.columnconfigure(1, weight=1)
        result_frame.rowconfigure(1, weight=1)
    
    def decimal_to_ieee(self):
        """Maneja la conversión de decimal a IEEE 754"""
        try:
            # Obtener el número decimal ingresado
            decimal_str = self.decimal_entry.get().strip()
            if not decimal_str:
                messagebox.showerror("Error", "Por favor ingrese un número decimal")
                return
                
            decimal_num = float(decimal_str)
            precision = int(self.precision_var.get())
            
            # Convertir según la precisión seleccionada
            if precision == 32:
                binary_str, sign, exponent, mantissa = self.converter.float_to_bin32(decimal_num)
            else:  # 64 bits
                binary_str, sign, exponent, mantissa = self.converter.float_to_bin64(decimal_num)
            
            # Mostrar resultados
            self.ieee_result.delete(0, tk.END)
            self.ieee_result.insert(0, binary_str)
            
            # Mostrar componentes
            components_info = self.converter.analyze_ieee754_components(sign, exponent, mantissa, precision)
            self.components_text.delete(1.0, tk.END)
            self.components_text.insert(1.0, components_info)
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
    
    def ieee_to_decimal(self):
        """Maneja la conversión de IEEE 754 a decimal"""
        try:
            # Obtener la representación binaria ingresada
            binary_str = self.binary_entry.get().strip()
            if not binary_str:
                messagebox.showerror("Error", "Por favor ingrese una representación binaria")
                return
                
            # Eliminar espacios y caracteres no binarios
            binary_str = ''.join([c for c in binary_str if c in '01'])
            
            precision = int(self.bin_precision_var.get())
            
            # Convertir según la precisión seleccionada
            if precision == 32:
                if len(binary_str) != 32:
                    messagebox.showerror("Error", f"La representación debe tener 32 bits. Tiene {len(binary_str)} bits.")
                    return
                decimal_num, sign, exponent, mantissa = self.converter.bin32_to_float(binary_str)
            else:  # 64 bits
                if len(binary_str) != 64:
                    messagebox.showerror("Error", f"La representación debe tener 64 bits. Tiene {len(binary_str)} bits.")
                    return
                decimal_num, sign, exponent, mantissa = self.converter.bin64_to_float(binary_str)
            
            # Mostrar resultados
            self.decimal_result.delete(0, tk.END)
            self.decimal_result.insert(0, str(decimal_num))
            
            # Mostrar componentes
            components_info = self.converter.analyze_ieee754_components(sign, exponent, mantissa, precision)
            self.bin_components_text.delete(1.0, tk.END)
            self.bin_components_text.insert(1.0, components_info)
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
    
    def copy_to_clipboard(self, text):
        """Copia el texto dado al portapapeles"""
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        messagebox.showinfo("Copiado", "Texto copiado al portapapeles")


   

if __name__ == "__main__":
    root = tk.Tk()
    app = IEEEConverterApp(root)
    root.mainloop()