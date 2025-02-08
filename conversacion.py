import tkinter as tk
from tkinter import ttk, messagebox
import openai
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env (debe estar en el mismo directorio)
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY

def lanzar_conversacion():
    if not OPENAI_API_KEY:
        messagebox.showerror("Error", "API Key de OpenAI no configurada")
        return
    
    conv_window = tk.Toplevel()
    conv_window.title("Asistente de Conversación con OpenAI")
    conv_window.geometry("500x450")
    
    frame = ttk.Frame(conv_window, padding="20")
    frame.pack(expand=True, fill="both")
    
    ttk.Label(frame, text="Ingresa tu pregunta:", font=("Helvetica", 12)).pack(pady=5)
    entry = ttk.Entry(frame, width=60, font=("Helvetica", 12))
    entry.pack(pady=5)
    
    response_area = tk.Text(frame, height=10, width=60, font=("Helvetica", 12))
    response_area.pack(pady=5)
    response_area.config(state=tk.DISABLED)
    
    def mostrar_respuesta(texto):
        response_area.config(state=tk.NORMAL)
        response_area.delete("1.0", tk.END)
        response_area.insert(tk.END, texto)
        response_area.config(state=tk.DISABLED)
    
    def procesar_pregunta():
        pregunta = entry.get().strip()
        if not pregunta:
            messagebox.showerror("Error", "Ingresa una pregunta válida")
            return
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": pregunta}],
                temperature=0.7,
                max_tokens=150
            )
            respuesta = response["choices"][0]["message"]["content"].strip()
            mostrar_respuesta(respuesta)
        except Exception as e:
            messagebox.showerror("Error", f"Error en la conexión: {str(e)}")
    
    btn_frame = ttk.Frame(frame)
    btn_frame.pack(pady=10)
    
    ttk.Button(btn_frame, text="Preguntar", command=procesar_pregunta).grid(row=0, column=0, padx=10)
    ttk.Button(btn_frame, text="Limpiar", command=lambda: mostrar_respuesta("")).grid(row=0, column=1, padx=10)
    
    ttk.Button(frame, text="Cerrar", command=conv_window.destroy).pack(pady=5)


