<div align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:FFB900,100:FFD700&height=200&section=header&text=Proyect-EY%20Asistente%20de%20IA&fontSize=60&fontColor=FFFFFF&animation=fadeIn"/>
  
  <h2>Aplicación Modular de Asistente de IA en Python</h2>
  <p>Integrando funcionalidades como calculadora, manipulación de texto y chat inteligente con OpenAI.</p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.11-blue.svg" alt="Python">
    <img src="https://img.shields.io/badge/Tkinter-8.6-blueviolet.svg" alt="Tkinter">
    <a href="https://github.com/EdwinDavid98/Proyect-EY">
      <img src="https://img.shields.io/badge/GitHub-Repository-black.svg" alt="GitHub">
    </a>
    <a href="https://www.linkedin.com/in/edwin-montenegro-119570250/">
      <img src="https://img.shields.io/badge/LinkedIn-Edwin-blue.svg" alt="LinkedIn">
    </a>
  </p>
</div>


# Proyect-EY
Asistente de IA en Python Aplicación modular con interfaz gráfica (Tkinter) que integra funcionalidades como una calculadora, herramientas de manipulación de texto y un chat inteligente usando la API de OpenAI. Ideal para demostrar habilidades en desarrollo de software e inteligencia artificial.

## Características

- **Calculadora:** Realiza operaciones matemáticas básicas con validación de expresiones.
- **Manipulación de Texto:** Convierte textos a mayúsculas, minúsculas y cuenta palabras.
- **Conversación:** Chat inteligente que utiliza la API de OpenAI para responder preguntas.
- **Interfaz Profesional:** Interfaz moderna con banner, botones estilizados en escala de amarillo y diseño modular.
- **Ejecutable Local para Windows:** Se incluye un ejecutable (`main.exe`) en la carpeta `dist` para correr la aplicación en una máquina Windows sin necesidad de tener Python instalado.

## Requisitos

- **Python 3.11** (recomendado)
- Librerías:
  - `tkinter` (incluida con Python)
  - `openai`
  - `python-dotenv`
- (Opcional) **PyInstaller** para generar el ejecutable

## Estructura del Proyecto
```
Proyect-EY/
├── mail.py              # Archivo principal (punto de entrada)
├── calculadora.py       # Funcionalidad de la calculadora
├── manipulador_texto.py # Funcionalidad de manipulación de texto
├── conversacion.py      # Funcionalidad de conversación con OpenAI
├── utils.py             # Funciones de validación y utilidades compartidas
├── .env                 # Archivo que contiene la API Key de OpenAI (NO subir a repositorio)
├── banner.png           # Imagen utilizada en el banner de la interfaz
└── dist/
    └── main.exe         # Ejecutable generado con PyInstaller para Windows
```
## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/EdwinDavid98/Proyect-EY.git
   cd Proyect-EY

## Uso / Ejecución

### Ejecutar desde Código Fuente

Asegúrate de que el archivo `.env` esté configurado correctamente.

Desde la raíz del proyecto, ejecuta:

```bash
python3.11 mail.py
```

Esto abrirá la interfaz gráfica, donde podrás seleccionar entre las siguientes funcionalidades:

- Calculadora (calculadora.py)
- Manipulación de Texto (manipulador_texto.py)
- Conversación (conversacion.py)

# Ejecutar el Ejecutable
Descarga y ejecuta el archivo main.exe ubicado en la carpeta`dist `  para correr la aplicación en una máquina Windows sin necesidad de instalar Python.

## Resultados

Puedes ver los resultados de este proyecto en acción en la siguiente página web, creada mediante GitHub Pages:

[Visitar la página de Proyect-EY](https://edwindavid98.github.io/Proyect-EY/)

En esta página se muestra una demostración interactiva de las funcionalidades del asistente de IA.
