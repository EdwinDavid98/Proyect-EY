import os
import tkinter as tk
from tkinter import ttk
from calculadora import lanzar_calculadora
from manipulador_texto import lanzar_manipulador_texto
from conversacion import lanzar_conversacion

def main():
    root = tk.Tk()
    root.title("Asistente de IA")
    root.geometry("800x800")
    
    # Aplicar un tema moderno
    style = ttk.Style()
    style.theme_use("clam")
    
    # Configurar el estilo para los botones en escala de amarillo
    style.configure("Yellow.TButton", 
                    foreground="black", 
                    background="#FFD700", 
                    font=("Helvetica", 12, "bold"))
    style.map("Yellow.TButton", 
              background=[("active", "#FFC300")])
    
    # Marco principal para organizar la interfaz
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(expand=True, fill="both")
    
    # Obtener la ruta del directorio actual y construir la ruta a la imagen del banner
    script_dir = os.path.dirname(os.path.abspath(__file__))
    banner_path = os.path.join(script_dir, "banner.png")
    
    # Agregar un banner con imagen
    try:
        banner_img = tk.PhotoImage(file=banner_path)
        banner_label = ttk.Label(main_frame, image=banner_img)
        banner_label.image = banner_img  # Mantener la referencia para que la imagen no se destruya
        banner_label.pack(pady=(0,10))
    except Exception as e:
        print("Error al cargar la imagen del banner:", e)
    
    # Títulos y subtítulos
    title_label = ttk.Label(main_frame, text="¡BIENVENIDOS USUARIOS EY!", font=("Helvetica", 20, "bold"))
    title_label.pack(pady=(0,10))
    
    subtitle_label = ttk.Label(main_frame, text="EN QUE PODEMOS AYUDARTE EL DIA DE HOY", font=("Helvetica", 14))
    subtitle_label.pack(pady=(0,10))
    
    subtitle2_label = ttk.Label(main_frame, text="TENEMOS LOS SIGUIENTES SERVICIOS", font=("Helvetica", 14))
    subtitle2_label.pack(pady=(0,10))
    
    subtitle3_label = ttk.Label(main_frame, text="Selecciona una opción:", font=("Helvetica", 14))
    subtitle3_label.pack(pady=(0,20))
    
    # Botones con estilo amarillo y tamaño uniforme
    btn_width = 40
    ttk.Button(main_frame, text="Calculadora", command=lanzar_calculadora, style="Yellow.TButton", width=btn_width)\
        .pack(pady=5, ipadx=10, ipady=5)
    ttk.Button(main_frame, text="Manipulación de Texto", command=lanzar_manipulador_texto, style="Yellow.TButton", width=btn_width)\
        .pack(pady=5, ipadx=10, ipady=5)
    ttk.Button(main_frame, text="Conversación con uno de nuestros asistentes IA", command=lanzar_conversacion, style="Yellow.TButton", width=btn_width)\
        .pack(pady=5, ipadx=10, ipady=5)
    ttk.Button(main_frame, text="Salir", command=root.quit, style="Yellow.TButton", width=btn_width)\
        .pack(pady=20, ipadx=10, ipady=5)
        
    # Label con tu nombre en la esquina inferior derecha
    name_label = ttk.Label(main_frame, text="By Edwin Montenegro", font=("Helvetica", 10, "italic"))
    name_label.pack(side="bottom", anchor="e", padx=5, pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    main()

