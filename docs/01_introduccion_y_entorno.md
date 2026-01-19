# 1. Introducción y Entorno

## ¿Qué es Python?

Python es un lenguaje de programación **interpretado**, **multiparadigma** y de **propósito general** creado por Guido van Rossum en 1991. Se caracteriza por:

- **Sintaxis clara y legible**: Es fácil de leer y aprender
- **Versátil**: Se usa en ciencia de datos, web, automatización, inteligencia artificial, etc.
- **Comunidad activa**: Millones de usuarios y miles de librerías disponibles
- **Open source**: Código abierto y libre para usar

### ¿Por qué aprender Python?

✅ Lenguaje más popular en ciencia de datos e IA
✅ Sintaxis amigable para principiantes
✅ Enorme cantidad de librerías especializadas
✅ Demanda laboral muy alta
✅ Versátil: desde scripts simples hasta aplicaciones complejas

---

## Instalación de Python

### En Windows

1. **Descargar**: Ve a [python.org](https://www.python.org/downloads/) y descarga la versión más reciente (3.11+)
2. **Instalar**: Ejecuta el instalador
   - ⚠️ **IMPORTANTE**: Marca la opción "Add Python to PATH"
   - Selecciona "Install Now" o personaliza la instalación
3. **Verificar**: Abre `cmd` o `PowerShell` y escribe:
   ```bash
   python --version
   ```

### En macOS

1. **Con Homebrew** (recomendado):
   ```bash
   brew install python3
   ```
2. **O descargar desde python.org**

3. **Verificar**:
   ```bash
   python3 --version
   ```

### En Linux (Ubuntu/Debian)

1. **Instalar**:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```
2. **Verificar**:
   ```bash
   python3 --version
   ```

---

## La Terminal: Tu herramienta de trabajo

### ¿Qué es la terminal?

La terminal (también llamada consola o línea de comandos) es una interfaz de texto para interactuar con tu computadora usando comandos.

### Comandos básicos

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `pwd` | Muestra el directorio actual | `pwd` |
| `ls` (Linux/Mac) o `dir` (Windows) | Lista archivos y carpetas | `ls` |
| `cd` | Cambia de directorio | `cd Desktop` |
| `cd ..` | Sube un nivel de directorio | `cd ..` |
| `mkdir` | Crea una carpeta nueva | `mkdir miproyecto` |
| `touch` | Crea un archivo | `touch script.py` |
| `cat` o `type` | Muestra contenido de archivo | `cat script.py` |

### Navegación básica en terminal

```bash
# Ver dónde estoy
pwd

# Ver contenido de la carpeta actual
ls

# Entrar a una carpeta
cd Desktop

# Volver atrás
cd ..

# Crear una carpeta
mkdir Python_basico

# Entrar a esa carpeta
cd Python_basico
```

---

## Entornos Virtuales (venv)

### ¿Por qué necesitamos entornos virtuales?

Un **entorno virtual** es una carpeta aislada donde instalamos las librerías específicas de un proyecto. Esto evita conflictos entre proyectos con versiones diferentes.

**Ventajas:**
- ✅ Aislar dependencias por proyecto
- ✅ Evitar conflictos de versiones
- ✅ Facilitar colaboración (archivo `requirements.txt`)
- ✅ Proyecto portátil y reproducible

### Crear un entorno virtual

#### En Windows (PowerShell o CMD):

```bash
# Crear el entorno virtual
python -m venv env

# Activar el entorno
env\Scripts\activate

# Deberías ver (env) al inicio de la línea de comando
```

#### En macOS y Linux:

```bash
# Crear el entorno virtual
python3 -m venv env

# Activar el entorno
source env/bin/activate

# Verás (env) al inicio
```

### ¿Cómo sé que está activado?

Cuando veas algo como esto en tu terminal, el entorno está activado:

```bash
(env) usuario@computadora:~/proyecto$
```

### Desactivar el entorno

```bash
deactivate
```

---

## pip: Gestor de Paquetes

### ¿Qué es pip?

`pip` es el gestor de paquetes de Python. Te permite instalar, actualizar y desinstalar librerías.

### Comandos básicos de pip

```bash
# Ver versión de pip
pip --version

# Instalar una librería
pip install requests

# Instalar una versión específica
pip install numpy==1.21.0

# Instalar múltiples librerías
pip install flask pandas matplotlib

# Actualizar una librería
pip install --upgrade numpy

# Desinstalar una librería
pip uninstall requests

# Ver librerías instaladas
pip list

# Generar requirements.txt (lista de dependencias)
pip freeze > requirements.txt

# Instalar desde requirements.txt
pip install -r requirements.txt
```

### Archivo `requirements.txt`

Es un archivo que lista todas las dependencias de tu proyecto:

```txt
requests==2.28.1
pandas==1.5.2
matplotlib==3.6.2
flask==2.2.2
```

Para recrear el entorno en otra máquina:
```bash
pip install -r requirements.txt
```

---

## Tu Primer Script: `hola_mundo.py`

### Paso 1: Crear el archivo

En la terminal, en tu proyecto:

```bash
# Crear el archivo (puedes usar cualquier editor)
touch hola_mundo.py
```

O crea un archivo llamado `hola_mundo.py` en tu carpeta del proyecto.

### Paso 2: Escribir el código

Abre el archivo en tu editor favorito (VS Code, PyCharm, etc.) y escribe:

```python
# Mi primer programa en Python
print("¡Hola Mundo!")
```

### Paso 3: Ejecutar el script

```bash
# En Windows
python hola_mundo.py

# En macOS/Linux
python3 hola_mundo.py
```

**Resultado:**
```
¡Hola Mundo!
```

### Script más interactivo

```python
# Programa interactivo
nombre = input("¿Cuál es tu nombre? ")
print(f"¡Hola {nombre}! Bienvenido a Python.")

edad = int(input("¿Cuántos años tienes? "))
print(f"En 10 años tendrás {edad + 10} años.")
```

**Ejecución:**
```
¿Cuál es tu nombre? Juan
¡Hola Juan! Bienvenido a Python.
¿Cuántos años tienes? 20
En 10 años tendrás 30 años.
```

---

## Flujo de Trabajo Completo

### Resumen paso a paso

```bash
# 1. Crear carpeta del proyecto
mkdir mi_proyecto
cd mi_proyecto

# 2. Crear entorno virtual
python -m venv env

# 3. Activar entorno
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate

# 4. Instalar librerías necesarias
pip install requests pandas

# 5. Guardar dependencias
pip freeze > requirements.txt

# 6. Crear y editar tu script
# (Crea hola_mundo.py en tu editor)

# 7. Ejecutar el script
python hola_mundo.py

# 8. Desactivar cuando termines
deactivate
```

---

## Editores Recomendados

| Editor | Pros | Contras |
|--------|------|---------|
| **VS Code** | Ligero, extensiones, excelente para Python | Requiere configuración |
| **PyCharm** | IDE poderoso, muchas features | Pesado, versión pro de pago |
| **Thonny** | Perfecto para principiantes | Menos features |
| **Jupyter Notebook** | Interactivo, excelente para exploración | No ideal para scripts grandes |

---

## Errores Comunes

### ❌ "python: command not found"
**Solución**: Python no está en PATH. En Windows, reinstala marcando "Add Python to PATH"

### ❌ "ModuleNotFoundError: No module named 'requests'"
**Solución**: No activaste el entorno virtual o no instalaste la librería
```bash
pip install requests
```

### ❌ "No such file or directory: hola_mundo.py"
**Solución**: Asegúrate de estar en la carpeta correcta con `pwd` o `cd`

---

## Próximos Pasos

Ahora que tienes Python listo, estás preparado para:

1. ✅ Aprender **tipos de datos** (int, str, float, bool)
2. ✅ Usar **input/output** para interacción
3. ✅ Crear **condicionales** (if/else)
4. ✅ Implementar **ciclos** (for/while)
5. ✅ Trabajar con **listas y diccionarios**

---

## Recursos Útiles

- 📚 [Python.org Documentation](https://docs.python.org/3/)
- 🎓 [Real Python Tutorials](https://realpython.com/)
- 🔗 [Python Package Index (PyPI)](https://pypi.org/)
- 💻 [Stack Overflow](https://stackoverflow.com/questions/tagged/python)

---

## Resumen

| Concepto | Descripción |
|----------|-------------|
| **Python** | Lenguaje interpretado, versátil y fácil de aprender |
| **Terminal** | Interfaz de texto para ejecutar comandos |
| **Entorno Virtual** | Carpeta aislada para dependencias del proyecto |
| **pip** | Gestor de paquetes para instalar librerías |
| **Script** | Archivo .py con código Python ejecutable |
| **requirements.txt** | Archivo que lista todas las dependencias |

¡Felicidades! Ya tienes todo lo necesario para comenzar tu viaje en Python. 🚀
