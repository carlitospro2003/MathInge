import tkinter as tk
import subprocess

AUTOR = "Carlos Eduardo Ramirez Saucedo"
GRADO_SECCION = "8°C"

def abrir_euler_mejorado():
    subprocess.run(["python", "euler_mejorado.py"])

def abrir_runge_kutta():
    subprocess.run(["python", "runge_kutta_4.py"])

def abrir_newton_raphson():
    subprocess.run(["python", "newton_raphson.py"])


root = tk.Tk()
root.title("Aplicación de Métodos Numéricos")
root.geometry("400x250")

tk.Label(root, text="Selecciona el método a ejecutar:", font=("Arial", 12)).pack(pady=10)

tk.Button(root, text="Runge-Kutta de 4to Orden", command=abrir_runge_kutta, font=("Arial", 10), width=25).pack(pady=5)

tk.Button(root, text="Newton-Raphson", command=abrir_newton_raphson, font=("Arial", 10), width=25).pack(pady=5)

tk.Button(root, text="Euler Mejorado", command=abrir_euler_mejorado, font=("Arial", 10), width=25).pack(pady=5)

# Mostrar información del autor
tk.Label(root, text=f"Alumno: {AUTOR}", font=("Arial", 10)).pack(pady=5)
tk.Label(root, text=f"Grado y Sección: {GRADO_SECCION}", font=("Arial", 10)).pack()

root.mainloop()
