import tkinter as tk
import ctypes
import win32con
import win32gui
import win32api

def mostrar_escritorio():
    ctypes.windll.user32.keybd_event(0x5B, 0, 0, 0)  # Tecla Win
    ctypes.windll.user32.keybd_event(0x44, 0, 0, 0)  # Tecla D
    ctypes.windll.user32.keybd_event(0x44, 0, 2, 0)  # Soltar D
    ctypes.windll.user32.keybd_event(0x5B, 0, 2, 0)  # Soltar Win

# Crear ventana
root = tk.Tk()
root.overrideredirect(True)  # Sin borde ni barra
root.geometry("120x40+10+10")
root.attributes("-topmost", True)

# Obtener el handle de la ventana
hwnd = ctypes.windll.user32.GetForegroundWindow()

# Establecer estilo para que no se minimice
ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style | win32con.WS_EX_TOOLWINDOW)

# # Botón
# boton = tk.Button(root, text="Escritorio", command=mostrar_escritorio)
# boton.pack(expand=True, fill="both")
boton = tk.Button(
    root,
    text="🖥️ Escritorio",
    command=mostrar_escritorio,
    font=("Segoe UI", 10, "bold"),
    bg="#2E8B57",       # Verde oscuro
    fg="white",
    activebackground="#3CB371",  # Verde más claro al presionar
    activeforeground="white",
    relief="flat",
    bd=0
)
boton.pack(expand=True, fill="both")

root.mainloop()
