import sympy as sp
import tkinter as tk
from tkinter import ttk, messagebox

def newton_raphson(f_expr, x0, tol, precision, max_iter=100):
    x = sp.symbols('x')
    f = sp.sympify(f_expr)
    df = sp.diff(f, x)

    f_lambd = sp.lambdify(x, f, 'numpy')
    df_lambd = sp.lambdify(x, df, 'numpy')

    tabla = []
    procedimiento = []

    for i in range(max_iter):
        f_x0 = f_lambd(x0)
        df_x0 = df_lambd(x0)

        if df_x0 == 0:
            messagebox.showerror("Error", "Derivada igual a cero, no se puede continuar.")
            return None, None

        x1 = x0 - (f_x0 / df_x0)

        # Redondear los valores según la precisión dada
        x0 = round(x0, precision)
        f_x0 = round(f_x0, precision)
        df_x0 = round(df_x0, precision)
        x1 = round(x1, precision)

        procedimiento.append(f"Iteración {i+1}:")
        procedimiento.append(f"  x{i} = {x0}")
        procedimiento.append(f"  f(x{i}) = {f_x0}")
        procedimiento.append(f"  f'(x{i}) = {df_x0}")
        procedimiento.append(f"  x{i+1} = {x0} - ({f_x0} / {df_x0}) = {x1}\n")

        tabla.append([i+1, x0, f_x0, df_x0, x1])

        if abs(x1 - x0) < tol:  # Condición de parada automática
            break

        x0 = x1
    else:
        messagebox.showwarning("Advertencia", "El método no convergió en el número máximo de iteraciones.")

    return tabla, procedimiento

def calcular():
    try:
        expr = sp.sympify(ecuacion_entry.get())
        x0 = float(x0_entry.get())
        tol = float(tol_entry.get())
        precision = int(precision_entry.get())  # Obtener la precisión en decimales

        if precision < 0:
            messagebox.showerror("Error", "La precisión debe ser un número entero positivo.")
            return

        resultados, procedimiento = newton_raphson(expr, x0, tol, precision)

        if resultados is None:
            return

        for row in tree.get_children():
            tree.delete(row)

        for res in resultados:
            tree.insert("", "end", values=res)

        procedimiento_text.delete("1.0", tk.END)
        procedimiento_text.insert(tk.END, "\n".join(procedimiento))
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

root = tk.Tk()
root.title("Método de Newton-Raphson")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Ecuación (en términos de x):").grid(row=0, column=0)
ecuacion_entry = tk.Entry(frame, width=30)
ecuacion_entry.grid(row=0, column=1)

tk.Label(frame, text="x0 (Valor inicial):").grid(row=1, column=0)
x0_entry = tk.Entry(frame)
x0_entry.grid(row=1, column=1)

tk.Label(frame, text="Tolerancia:").grid(row=2, column=0)
tol_entry = tk.Entry(frame)
tol_entry.grid(row=2, column=1)

tk.Label(frame, text="Precisión (decimales):").grid(row=3, column=0)
precision_entry = tk.Entry(frame)
precision_entry.grid(row=3, column=1)

tk.Button(frame, text="Calcular", command=calcular).grid(row=4, columnspan=2, pady=5)

columns = ("Iteración", "x", "f(x)", "f'(x)", "x_nuevo")
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
