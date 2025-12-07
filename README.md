
# Escritorio (simula Win + D)

Pequeña utilidad en **Tkinter** para Windows que muestra un botón flotante. Al hacer clic, 
simula la combinación de teclas **Win + D** para mostrar el escritorio.

## Características
- Ventana **sin bordes** y **siempre al frente**.
- Botón estilizado (fuente *Segoe UI*, colores verde/blanco).
- Usa `ctypes` para disparar eventos de teclado en Windows.
- Evita que la ventana se minimice configurando el estilo extendido.

## Requisitos
- Windows 10/11.
- Python 3.8+.
- Paquetes: `tkinter` (incluido con Python), `pywin32` (`win32con`, `win32gui`, `win32api`).

## Instalación de dependencias
```bash
pip install pywin32
```

## Ejecución
1. Clona o descarga el archivo `escritorio(simula Win D).py`.
2. Ejecuta:
   ```bash
   python "escritorio(simula Win D).py"
   ```
3. Haz clic en el botón **🖥️ Escritorio** para mostrar el escritorio.

## Personalización rápida
- **Texto del botón**: modifica `text="🖥️ Pollo"`.
- **Tamaño/posición** de la ventana: cambia `root.geometry("120x40+10+10")`.
- **Colores**: ajusta `bg`, `fg`, `activebackground`, `activeforeground`.

## Limitaciones y notas
- Requiere privilegios suficientes para enviar eventos de teclado.
- Solo funciona en **Windows** (usa APIs de `user32` y `pywin32`).
- Algunos antivirus/EDR podrían bloquear la simulación de teclado.

## Licencia
MIT (puedes adaptarlo libremente; créditos apreciados).
