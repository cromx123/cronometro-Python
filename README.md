# 📝 **Temporizador con Barras de Progreso** ⏳  

Un script en Python que muestra **dos barras de progreso simultáneas**:  
✅ **Progreso total** (tiempo completo)  
🔄 **Progreso por minuto** (se reinicia cada 60 segundos)  

---

## 🚀 **Características**  
✨ **Interfaz clara** con dos barras de carga visual.  
⏱️ **Temporizador configurable** (minutos como argumento).  
🔄 **Barra de minuto actual** se reinicia automáticamente.  
🛑 **Manejo de interrupciones** (Ctrl+C para cancelar).  
📊 **Porcentaje preciso** en ambas barras.  

---

## 📥 **Instalación y Uso**  

### **Requisitos**  
- Python 3.6+ (`python3 --version` para verificar).  

### **Ejecución**  
1. Clona el repositorio o descarga `tiempo.py`.  
2. Ejecuta desde la terminal:  
   ```bash
   python3 tiempo.py [minutos]
   ```
   **Ejemplo:**  
   ```bash
   python3 tiempo.py 5  # Temporizador de 5 minutos
   ```

---

**Salida en consola:**  
```
Iniciando temporizador de 12 minutos...

Progreso:

Total:  |███████████████████████████████████████---------| 85.0% | 10.4 mins.
Minuto: |████████████████████████████████----------------| 60.0% | 45 seg  
```

---

## 🛠️ **Cómo funciona**  

### **Lógica principal**  
1. **Barra de progreso total** (`Total:`):  
   - Avanza desde 0% hasta 100% en el tiempo total ingresado.  

2. **Barra de minuto actual** (`Minuto:`):  
   - Empieza en 0% y llega a 100% cada 60 segundos.  
   - Se reinicia automáticamente al completar un minuto.  

---

## 📌 **Notas adicionales**  
- Probado en Linux (Ubuntu) y Windows (con terminales modernas).  
- Para mejor visualización, usa una terminal con soporte para caracteres Unicode (como █).  

---

### 📁 **Estructura del repositorio**  
```
temporizador/
├── tiempo.py         # Script principal
└── README.md         # Este archivo
```

---

### 🔄 **Posibles mejoras**  
- [ ] Añadir sonido al completarse el tiempo.  
- [ ] Mostrar tiempo restante en formato HH:MM:SS.  

---

¡Espero que te sea útil! 😊
