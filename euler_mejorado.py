import sympy as sp
import tkinter as tk
from tkinter import ttk, messagebox

def euler_mejorado(f_expr, x0, y0, h):
    x, y = sp.symbols('x y')
    f = sp.lambdify((x, y), f_expr, 'numpy')
    
    tabla = []
    procedimiento = []
    
    n = int(abs((10 - x0) / h))  # Estimación del número de iteraciones
    
    for i in range(n):
        k1 = f(x0, y0)
        k2 = f(x0 + h, y0 + h * k1)
        
        y_next = y0 + (h / 2) * (k1 + k2)
        
        procedimiento.append(f"Paso {i+1}:")
        procedimiento.append(f"  x{i} = {x0}")
        procedimiento.append(f"  y{i} = {y0}")
        procedimiento.append(f"  k1 = f({x0}, {y0}) = {k1}")
        procedimiento.append(f"  k2 = f({x0 + h}, {y0 + h * k1}) = {k2}")
        procedimiento.append(f"  y{i+1} = {y0} + ({h}/2) * ({k1} + {k2}) = {y_next}\n")
        
        tabla.append([i+1, x0, y0, k1, k2, y_next])
        
        x0 += h
        y0 = y_next
    
    return tabla, procedimiento

def calcular():
    try:
        expr = sp.sympify(ecuacion_entry.get())
        x0 = float(x0_entry.get())
        y0 = float(y0_entry.get())
        h = float(h_entry.get())
        
        resultados, procedimiento = euler_mejorado(expr, x0, y0, h)
        
        # Limpiar resultados anteriores en la tabla
        for row in tree.get_children():
            tree.delete(row)
        
        # Insertar los nuevos resultados
        for res in resultados:
            tree.insert("", "end", values=res)
        
        # Limpiar el área de procedimiento y agregar el nuevo procedimiento
        procedimiento_text.delete("1.0", tk.END)
        procedimiento_text.insert(tk.END, "\n".join(procedimiento))
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def limpiar_resultados():
    # Limpiar tabla de resultados
    for row in tree.get_children():
        tree.delete(row)
    
    # Limpiar área de procedimiento
    procedimiento_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Método de Euler Mejorado")

# Definir una fuente más grande
font_label = ("Arial", 12)
font_entry = ("Arial", 12)
font_button = ("Arial", 12)
font_text = ("Arial", 12)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Ecuación (en términos de x e y):", font=font_label).grid(row=0, column=0)
ecuacion_entry = tk.Entry(frame, width=30, font=font_entry)
ecuacion_entry.grid(row=0, column=1)

tk.Label(frame, text="x0:", font=font_label).grid(row=1, column=0)
x0_entry = tk.Entry(frame, font=font_entry)
x0_entry.grid(row=1, column=1)

tk.Label(frame, text="y0:", font=font_label).grid(row=2, column=0)
y0_entry = tk.Entry(frame, font=font_entry)
y0_entry.grid(row=2, column=1)

tk.Label(frame, text="h (paso):", font=font_label).grid(row=3, column=0)
h_entry = tk.Entry(frame, font=font_entry)
h_entry.grid(row=3, column=1)

# Botón para calcular y limpiar resultados
tk.Button(frame, text="Calcular", font=font_button, command=calcular).grid(row=4, columnspan=2, pady=5)
tk.Button(frame, text="Limpiar Resultado", font=font_button, command=limpiar_resultados).grid(row=5, columnspan=2, pady=5)

columns = ("Paso", "x", "y", "k1", "k2", "y_next")
tree = ttk.Treeview(root, columns=columns, show="headings", style="Treeview")
for col in columns:
    tree.heading(col, text=col, anchor="center")
    tree.column(col, anchor="center")
tree.pack(pady=10)

procedimiento_label = tk.Label(root, text="Procedimiento:", font=font_label)
procedimiento_label.pack()
procedimiento_text = tk.Text(root, height=10, width=80, font=font_text)
procedimiento_text.pack(pady=5)

root.mainloop()
