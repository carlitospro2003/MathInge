import sympy as sp
import tkinter as tk
from tkinter import ttk, messagebox

def runge_kutta_4(f_expr, x0, y0, h, x_final):
    x, y = sp.symbols('x y')
    f = sp.lambdify((x, y), f_expr, 'numpy')
    
    n = int((x_final - x0) / h)  # Calcula el número de iteraciones necesarias
    tabla = []
    procedimiento = []
    
    for i in range(n + 1):
        k1 = f(x0, y0)
        k2 = f(x0 + h/2, y0 + (h/2) * k1)
        k3 = f(x0 + h/2, y0 + (h/2) * k2)
        k4 = f(x0 + h, y0 + h * k3)
        
        y_next = y0 + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        
        procedimiento.append(f"Paso {i+1}:")
        procedimiento.append(f"  x{i} = {x0}")
        procedimiento.append(f"  y{i} = {y0}")
        procedimiento.append(f"  k1 = f({x0}, {y0}) = {k1}")
        procedimiento.append(f"  k2 = f({x0 + h/2}, {y0 + (h/2) * k1}) = {k2}")
        procedimiento.append(f"  k3 = f({x0 + h/2}, {y0 + (h/2) * k2}) = {k3}")
        procedimiento.append(f"  k4 = f({x0 + h}, {y0 + h * k3}) = {k4}")
        procedimiento.append(f"  y{i+1} = {y0} + ({h}/6) * ({k1} + 2*{k2} + 2*{k3} + {k4}) = {y_next}\n")
        
        tabla.append([i+1, x0, y0, k1, k2, k3, k4, y_next])
        
        x0 += h
        y0 = y_next
    
    return tabla, procedimiento

def calcular():
    try:
        expr = sp.sympify(ecuacion_entry.get())
        x0 = float(x0_entry.get())
        y0 = float(y0_entry.get())
        h = float(h_entry.get())
        x_final = float(x_final_entry.get())
        
        resultados, procedimiento = runge_kutta_4(expr, x0, y0, h, x_final)
        
        for row in tree.get_children():
            tree.delete(row)
        
        for res in resultados:
            tree.insert("", "end", values=res)
        
        procedimiento_text.delete("1.0", tk.END)
        procedimiento_text.insert(tk.END, "\n".join(procedimiento))
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

root = tk.Tk()
root.title("Método de Runge-Kutta de 4to Orden")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Ecuación (en términos de x e y):").grid(row=0, column=0)
ecuacion_entry = tk.Entry(frame, width=30)
ecuacion_entry.grid(row=0, column=1)

tk.Label(frame, text="x0:").grid(row=1, column=0)
x0_entry = tk.Entry(frame)
x0_entry.grid(row=1, column=1)

tk.Label(frame, text="y0:").grid(row=2, column=0)
y0_entry = tk.Entry(frame)
y0_entry.grid(row=2, column=1)

tk.Label(frame, text="h (paso):").grid(row=3, column=0)
h_entry = tk.Entry(frame)
h_entry.grid(row=3, column=1)

tk.Label(frame, text="x final:").grid(row=4, column=0)
x_final_entry = tk.Entry(frame)
x_final_entry.grid(row=4, column=1)

tk.Button(frame, text="Calcular", command=calcular).grid(row=5, columnspan=2, pady=5)

columns = ("Paso", "x", "y", "k1", "k2", "k3", "k4", "y_next")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")
tree.pack(pady=10)

procedimiento_label = tk.Label(root, text="Procedimiento:")
procedimiento_label.pack()
procedimiento_text = tk.Text(root, height=15, width=80)
procedimiento_text.pack(pady=5)

root.mainloop()