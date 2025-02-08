import tkinter as tk
from tkinter import ttk, messagebox
from utils import validar_expresion_matematica

def calcular_expresion(expresion):
    if not validar_expresion_matematica(expresion):
        raise ValueError("Expresión inválida. Usa solo números y operadores básicos.")
    try:
        resultado = eval(expresion)
    except Exception as e:
        raise ValueError(f"Error en el cálculo: {str(e)}")
    return resultado

def lanzar_calculadora():
    calc_window = tk.Toplevel()
    calc_window.title("Calculadora")
    calc_window.geometry("450x200")
    
    frame = ttk.Frame(calc_window, padding="20")
    frame.pack(expand=True, fill="both")
    
    ttk.Label(frame, text="Ingresa una expresión matemática:", font=("Helvetica", 12)).pack(pady=5)
    entry = ttk.Entry(frame, width=40, font=("Helvetica", 12))
    entry.pack(pady=5)
    
    def procesar():
        expresion = entry.get()
        try:
            resultado = calcular_expresion(expresion)
            messagebox.showinfo("Resultado", f"Resultado: {resultado}")
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
    
    btn_frame = ttk.Frame(frame)
    btn_frame.pack(pady=10)
    
    ttk.Button(btn_frame, text="Calcular", command=procesar).grid(row=0, column=0, padx=10)
    ttk.Button(btn_frame, text="Cerrar", command=calc_window.destroy).grid(row=0, column=1, padx=10)
