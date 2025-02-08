import tkinter as tk
from tkinter import ttk, messagebox
from utils import validar_texto

def lanzar_manipulador_texto():
    text_window = tk.Toplevel()
    text_window.title("Manipulación de Texto")
    text_window.geometry("500x450")
    
    frame = ttk.Frame(text_window, padding="20")
    frame.pack(expand=True, fill="both")
    
    ttk.Label(frame, text="Ingresa un texto:", font=("Helvetica", 12)).pack(pady=5)
    text_entry = tk.Text(frame, height=10, width=40, font=("Helvetica", 12))
    text_entry.pack(pady=5)
    
    def convertir_mayusculas():
        texto = text_entry.get("1.0", tk.END)
        if not validar_texto(texto):
            messagebox.showerror("Error", "Ingresa un texto válido.")
            return
        messagebox.showinfo("Resultado", texto.upper())
    
    def convertir_minusculas():
        texto = text_entry.get("1.0", tk.END)
        if not validar_texto(texto):
            messagebox.showerror("Error", "Ingresa un texto válido.")
            return
        messagebox.showinfo("Resultado", texto.lower())
    
    def contar_palabras():
        texto = text_entry.get("1.0", tk.END)
        if not validar_texto(texto):
            messagebox.showerror("Error", "Ingresa un texto válido.")
            return
        palabras = texto.split()
        messagebox.showinfo("Resultado", f"El texto tiene {len(palabras)} palabra(s).")
    
    btn_frame = ttk.Frame(frame)
    btn_frame.pack(pady=10)
    
    ttk.Button(btn_frame, text="Mayúsculas", command=convertir_mayusculas).grid(row=0, column=0, padx=10, pady=5)
    ttk.Button(btn_frame, text="Minúsculas", command=convertir_minusculas).grid(row=0, column=1, padx=10, pady=5)
    ttk.Button(btn_frame, text="Contar Palabras", command=contar_palabras).grid(row=0, column=2, padx=10, pady=5)
    
    ttk.Button(frame, text="Cerrar", command=text_window.destroy).pack(pady=5)
