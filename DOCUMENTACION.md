
# Documentación Técnica

Este documento explica el funcionamiento interno del script `escritorio(simula Win D).py`, 
sus módulos, flujo, y puntos de extensión.

---

## 1. Arquitectura y módulos usados
- **tkinter**: GUI nativa de Python para crear la ventana y el botón.
- **ctypes**: Puente a funciones de la DLL `user32.dll` para generar eventos de teclado.
- **pywin32**: Constantes y funciones Win32 (`win32con`, `win32gui`, `win32api`) para gestionar estilos de ventana.

## 2. Función principal: `mostrar_escritorio()`
Simula la combinación **Win + D** disparando eventos de teclado en orden correcto:
```python
ctypes.windll.user32.keybd_event(0x5B, 0, 0, 0)  # Press Win (VK_LWIN)
ctypes.windll.user32.keybd_event(0x44, 0, 0, 0)  # Press D
ctypes.windll.user32.keybd_event(0x44, 0, 2, 0)  # Release D (KEYEVENTF_KEYUP)
ctypes.windll.user32.keybd_event(0x5B, 0, 2, 0)  # Release Win
```
- `0x5B` es **VK_LWIN** (tecla Windows izquierda).
- `0x44` es **VK_D** (letra D).

## 3. Construcción de la ventana
```python
root = tk.Tk()
root.overrideredirect(True)        # ventana sin borde ni barra de título
root.geometry("120x40+10+10")     # ancho x alto + x + y
root.attributes("-topmost", True) # siempre al frente
```

## 4. Estilo extendido (no minimizable)
Se obtiene el `hwnd` de la ventana activa y se ajusta el estilo extendido:
```python
hwnd = ctypes.windll.user32.GetForegroundWindow()
ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style | win32con.WS_EX_TOOLWINDOW)
```
- `WS_EX_TOOLWINDOW` hace que la ventana se trate como herramienta, ayudando a evitar que aparezca en la barra de tareas y que sea minimizada por acciones globales.

## 5. Botón y estilo visual
```python
boton = tk.Button(
    root,
    text="🖥️ Pollo",
    command=mostrar_escritorio,
    font=("Segoe UI", 10, "bold"),
    bg="#2E8B57",
    fg="white",
    activebackground="#3CB371",
    activeforeground="white",
    relief="flat",
    bd=0
)
boton.pack(expand=True, fill="both")
```

## 6. Flujo de ejecución
1. Se define `mostrar_escritorio()`.
2. Se crea la ventana `root` sin decoraciones y siempre al frente.
3. Se ajusta el estilo extendido del `hwnd` activo.
4. Se crea y empaqueta el botón.
5. Se inicia el bucle principal con `root.mainloop()`.

## 7. Puntos de extensión
- **Arrastre de ventana**: agregar eventos `<ButtonPress-1>` y `<B1-Motion>` para moverla.
- **Tecla global**: registrar un *hotkey* con `RegisterHotKey` (requiere manejo de mensajes Win32).
- **Icono/Tray**: integrar con `pystray` para mostrar un icono en la bandeja del sistema.
- **Temas**: migrar a `ttk`/`ttkbootstrap` para una estética más moderna.

## 8. Buenas prácticas y seguridad
- Ejecuta el script desde una ubicación confiable.
- Firma/whitelisting si tu entorno corporativo usa AppLocker/EDR.
- Maneja errores (try/except) alrededor de llamadas a `ctypes` y `pywin32`.

## 9. Troubleshooting
- **El botón no muestra el escritorio**: verifica que `pywin32` esté instalado y que tengas permisos.
- **Antivirus bloquea la acción**: añade excepción o ejecuta como administrador.
- **No se ve la ventana**: revisa `geometry` y monitores múltiples.

## 10. Pseudocódigo
```text
INICIAR APP
  DEFINIR funcion mostrar_escritorio:
    PRESIONAR VK_LWIN
    PRESIONAR VK_D
    SOLTAR VK_D
    SOLTAR VK_LWIN

  CREAR ventana sin bordes, topmost, posicion (10,10), tamaño (120x40)
  OBTENER hwnd de la ventana activa
  APLICAR estilo extendido TOOLWINDOW al hwnd
  CREAR botón con estilo que llama a mostrar_escritorio
  INICIAR mainloop
FIN
```

## 11. Licencia
MIT.
