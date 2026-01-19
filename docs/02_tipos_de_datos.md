# 02 - Fundamentos del Lenguaje: Tipos de Datos

## Introducción

Los **tipos de datos** son la base fundamental de cualquier programa Python. Cada valor en Python tiene un tipo que determina qué operaciones puedes realizar con él y cómo se almacena en memoria.

**Analogía útil**: Es como distinguir entre dinero en efectivo, una tarjeta de crédito y una letra de cambio. Todos representan "valor", pero funcionan de formas muy diferentes.

---

## 1. Conceptos Fundamentales

### ¿Qué es un tipo de dato?

Un **tipo de dato** es una clasificación que define:
- **Qué valores** puede contener una variable
- **Qué operaciones** puedes realizar con él
- **Cómo se almacena** en memoria

### ¿Por qué existen diferentes tipos?

Cada tipo está optimizado para diferentes propósitos:
- **Números** para cálculos
- **Texto** para información alfanumérica
- **Booleanos** para lógica y decisiones

Python es **dinámicamente tipado**, lo que significa que no necesitas declarar el tipo explícitamente; Python lo infiere automáticamente.

---

## 2. Tipos de Datos Primitivos

Python tiene **4 tipos primitivos principales**:

### 2.1 INT (Enteros)

**Definición**: Números sin punto decimal, positivos o negativos.

**Características principales**:
- 📊 Rango ilimitado (en Python 3)
- ➕ Soporta operaciones: +, -, *, //, %, **
- 🎯 Uso: contadores, índices, cantidades, edades

**Ejemplo**:
```python
edad = 25
cantidad = 100
temperatura = -5
resultado = 10 + 5  # 15
```

**Operaciones importantes**:

| Operación | Símbolo | Ejemplo | Resultado |
|-----------|---------|---------|-----------|
| Suma | + | 10 + 3 | 13 |
| Resta | - | 10 - 3 | 7 |
| Multiplicación | * | 10 * 3 | 30 |
| División entera | // | 10 // 3 | 3 |
| Módulo (resto) | % | 10 % 3 | 1 |
| Potencia | ** | 2 ** 3 | 8 |

---

### 2.2 FLOAT (Decimales)

**Definición**: Números con punto decimal. Representan valores reales.

**Características principales**:
- 🔢 Contienen decimales
- ⚠️ Precisión limitada (importante para comparaciones)
- 🎯 Uso: medidas científicas, precios, coordenadas

**Ejemplo**:
```python
precio = 19.99
altura = 1.75  # metros
pi = 3.14159
promedio = 85.5
```

**⚠️ Trampa común - Precisión floating-point**:

```python
# Este problema es común en lenguajes de programación
0.1 + 0.2  # Puede no ser exactamente 0.3

# Comparación mejor:
resultado = 0.1 + 0.2
if abs(resultado - 0.3) < 0.0001:  # Permitir pequeña diferencia
    print("Aproximadamente 0.3")
```

---

### 2.3 STR (Cadenas de Texto)

**Definición**: Secuencia de caracteres (letras, números, símbolos).

**Características principales**:
- 📝 Delimitadas con comillas simples '' o dobles ""
- 🔒 Inmutables (no se pueden cambiar después de crear)
- 📚 Muchos métodos útiles para manipulación
- 🎯 Uso: nombres, mensajes, identificadores

**Ejemplo**:
```python
nombre = "Juan"
email = 'usuario@ejemplo.com'
mensaje = "Hola, bienvenido a Python"
```

**Métodos útiles de strings**:

| Método | Descripción | Ejemplo | Resultado |
|--------|-------------|---------|-----------|
| `.upper()` | Mayúsculas | "hola".upper() | "HOLA" |
| `.lower()` | Minúsculas | "HOLA".lower() | "hola" |
| `.capitalize()` | Primera mayúscula | "hola".capitalize() | "Hola" |
| `.len()` | Largo de string | len("Python") | 6 |
| `.replace()` | Reemplazar texto | "hola".replace("o", "0") | "h0la" |
| `.split()` | Dividir en lista | "a,b,c".split(",") | ["a", "b", "c"] |
| `.strip()` | Eliminar espacios | "  hola  ".strip() | "hola" |
| `.startswith()` | ¿Comienza con...? | "hola".startswith("ho") | True |
| `.endswith()` | ¿Termina con...? | "hola".endswith("la") | True |
| `.find()` | Buscar posición | "hola".find("l") | 2 |

---

### 2.4 BOOL (Booleanos)

**Definición**: Solo dos valores posibles: `True` (verdadero) o `False` (falso).

**Características principales**:
- ✓ Solo 2 valores: True o False
- 🔀 Resultado de comparaciones
- 📍 Fundamental en condicionales
- 🎯 Uso: lógica de programas, decisiones

**Ejemplo**:
```python
es_estudiante = True
tiene_licencia = False
es_mayor_edad = edad >= 18
```

**Generadores de booleanos**:

```python
# Operadores de comparación
5 > 3      # True
10 < 5     # False
7 == 7     # True
8 != 3     # True

# Operadores lógicos
True and False   # False
True or False    # True
not True         # False
```

---

## 3. Identificar Tipos: type()

La función `type()` devuelve el tipo de cualquier valor. Es **invaluable para depuración**.

```python
type(42)           # <class 'int'>
type(3.14)         # <class 'float'>
type("Hola")       # <class 'str'>
type(True)         # <class 'bool'>
```

**Verificar tipos**:
```python
valor = 42
if type(valor) == int:
    print("Es un entero")
```

---

## 4. Input y Output - Comunicación con el Usuario

### 4.1 print() - Salida de Datos

`print()` muestra información en la pantalla. Es tu herramienta para comunicar resultados.

**Formas básicas**:
```python
# Un argumento
print("Hola")

# Múltiples argumentos
print("El número es:", 42)

# Sin salto de línea
print("A", end="")
print("B")  # Resultado: AB

# Personalizando separador
print("a", "b", "c", sep="-")  # Resultado: a-b-c
```

### 4.2 F-Strings - La forma moderna (Recomendado ⭐)

**F-strings** permiten insertar variables dentro de texto de forma legible y potente.

```python
nombre = "María"
edad = 28

# Básico
print(f"Mi nombre es {nombre}")

# Con expresiones
print(f"Tendré {edad + 1} años el próximo año")

# Formateo de números
precio = 19.99
print(f"Precio: ${precio:.2f}")

# Alineación
print(f"|{nombre:>10}|")  # Alineado a la derecha
print(f"|{nombre:<10}|")  # Alineado a la izquierda
print(f"|{nombre:^10}|")  # Centrado
```

### 4.3 input() - Entrada de Datos del Usuario

`input()` pausa el programa y espera que el usuario escriba algo.

**⚠️ Punto crítico**: `input()` **siempre retorna un string**, aunque el usuario escriba números.

```python
nombre = input("¿Cuál es tu nombre?: ")  # Siempre es str

# Si necesitas un número, DEBES convertir
edad_texto = input("¿Cuál es tu edad?: ")
edad = int(edad_texto)  # Convertir a int

# Mejor aún, en una línea:
edad = int(input("¿Cuál es tu edad?: "))
```

---

## 5. Conversión de Tipos (Casting)

Frecuentemente necesitas convertir un tipo a otro. Python proporciona funciones para esto.

### Tabla de Conversiones

| Convertir a | Función | Ejemplo | Resultado | Notas |
|-----------|---------|---------|-----------|-------|
| **int** | `int()` | `int("42")` | 42 | Debe ser número válido |
| **int** | `int()` | `int(3.99)` | 3 | Trunca, no redondea |
| **float** | `float()` | `float("3.14")` | 3.14 | Acepta strings con punto |
| **float** | `float()` | `float(42)` | 42.0 | Agrega .0 |
| **str** | `str()` | `str(42)` | "42" | Funciona con cualquier tipo |
| **str** | `str()` | `str(3.14)` | "3.14" | Funciona con cualquier tipo |
| **bool** | `bool()` | `bool(1)` | True | 0 es False, otros son True |

### Conversiones Válidas vs Inválidas

✅ **VÁLIDAS**:
```python
int("42")      # "42" es número válido
float("3.14")  # "3.14" es número válido
str(42)        # Cualquier cosa → str
int(3.99)      # float → int (trunca)
```

❌ **INVÁLIDAS** (lanzan errores):
```python
int("abc")           # ValueError: "abc" no es número
float("3.14.5")      # ValueError: múltiples puntos
int("3.14")          # ValueError: int() no acepta decimales en string
```

---

## 6. Errores Comunes y Soluciones

### 6.1 TypeError - Operación entre tipos incompatibles

**Causa**: Intentar operación entre tipos que no funcionan juntos.

| Problema | Código | Error | Solución |
|----------|--------|-------|----------|
| Sumar string + número | `"5" + 5` | TypeError | `int("5") + 5` |
| Concatenar mal | `5 + " años"` | TypeError | `str(5) + " años"` |
| Operación inválida | `"texto" * "otro"` | TypeError | `"texto" * 3` |

```python
# ❌ ERROR
resultado = "5" + 5  # TypeError

# ✅ SOLUCIÓN
resultado = int("5") + 5  # Ahora funciona: 10
```

### 6.2 ValueError - Conversión inválida

**Causa**: Intentar convertir texto que no representa un número válido.

```python
# ❌ ERROR
edad = int("veinticinco")  # ValueError: invalid literal

# ✅ SOLUCIÓN 1: Validar primero
texto = "25"
if texto.isdigit():
    edad = int(texto)
else:
    print("Debes ingresar un número")

# ✅ SOLUCIÓN 2: Usar try/except (próxima sesión)
```

### 6.3 ZeroDivisionError - División entre cero

**Causa**: Intentar dividir un número entre cero (operación matemáticamente indefinida).

```python
# ❌ ERROR
resultado = 10 / 0  # ZeroDivisionError

# ✅ SOLUCIÓN
divisor = 0
if divisor != 0:
    resultado = 10 / divisor
else:
    print("No puedes dividir entre cero")
```

### 6.4 NameError - Variable no definida

**Causa**: Usar una variable que no ha sido creada.

```python
# ❌ ERROR
print(nombre)  # NameError: name 'nombre' is not defined

# ✅ SOLUCIÓN
nombre = "Juan"  # Definir primero
print(nombre)
```

### 6.5 AttributeError - Método no existe para ese tipo

**Causa**: Llamar a un método que no pertenece a ese tipo.

```python
# ❌ ERROR
numero = 42
numero.upper()  # AttributeError: 'int' has no attribute 'upper'

# ✅ SOLUCIÓN: Convertir a string
numero_texto = str(numero)
numero_texto.upper()  # "42"
```

### 6.6 Manejo Básico con Try/Except

```python
try:
    numero = int(input("Ingresa un número: "))
    print(f"Ingresaste: {numero}")
except ValueError:
    print("Error: Debes ingresar un número válido")
```

---

## 7. Buenas Prácticas ✅

### Dos órdenes de magnitud de importancia:

#### ⭐⭐⭐ CRÍTICAS:

1. **Siempre convierte `input()` al tipo correcto**
   ```python
   # ❌ MAL
   edad = input("Edad: ")  # Es str, no int
   print(edad + 1)         # Error!
   
   # ✅ BIEN
   edad = int(input("Edad: "))  # Convertir de inmediato
   print(edad + 1)              # 26
   ```

2. **Valida datos antes de operaciones críticas**
   ```python
   divisor = int(input("Divisor: "))
   if divisor != 0:
       resultado = 100 / divisor
   else:
       print("El divisor no puede ser cero")
   ```

3. **Usa f-strings para mejor legibilidad**
   ```python
   # ❌ ANTICUADO
   print("El valor es " + str(valor) + " unidades")
   
   # ✅ MODERNO
   print(f"El valor es {valor} unidades")
   ```

#### ⭐⭐ IMPORTANTES:

4. **Usa `type()` para depuración**
   ```python
   valor = input("Ingresa algo: ")
   print(f"Tipo: {type(valor)}")  # Ayuda a entender qué tienes
   ```

5. **Sé consciente de los límites de cada tipo**
   ```python
   # float tiene precisión limitada
   resultado = 0.1 + 0.2
   print(resultado)  # 0.30000000000000004 (¡no exacto!)
   
   # Solución: comparar con tolerancia
   if abs(resultado - 0.3) < 0.0001:
       print("Aproximadamente 0.3")
   ```

---

## 8. Trampa Común: Confundir Tipos

Muchos errores suceden porque **olvidas qué tipo tienes**:

```python
# Input SIEMPRE es string
edad = input("Edad: ")      # edad es str, ej: "25"
print(edad + 1)             # ERROR: no puedes sumar str + int

# Solución: convertir explícitamente
edad = int(input("Edad: "))  # Ahora es int
print(edad + 1)              # Funciona: 26

# Comparar strings vs números
if "10" > "2":      # True (comparación alfabética!)
    print("10 es mayor que 2")  # Incorrecto

if 10 > 2:          # True (comparación numérica)
    print("10 es mayor que 2")  # Correcto
```

---

## 9. Resumen de Conceptos Clave

### Tabla Rápida de Referencia

| Concepto | Qué es | Cuándo usarlo | Ejemplo |
|----------|--------|---------------|---------|
| **int** | Números enteros | Contadores, edades, cantidades | 42 |
| **float** | Números decimales | Medidas, precios, cálculos | 3.14 |
| **str** | Texto | Nombres, mensajes, entrada del usuario | "Hola" |
| **bool** | Verdadero/Falso | Decisiones, lógica | True, False |
| **type()** | Identifica el tipo | Depuración | type(42) → int |
| **int()** | Convierte a int | Procesar input como número | int("42") |
| **float()** | Convierte a float | Números decimales | float("3.14") |
| **str()** | Convierte a str | Concatenación, salida | str(42) |
| **input()** | Lee del usuario | Entrada interactiva | input("Nombre: ") |
| **print()** | Muestra en pantalla | Salida de datos | print("Hola") |
| **f-strings** | Formato de texto | Mostrar datos claramente | f"Valor: {x}" |

### Errores Principales a Evitar

| Error | Síntoma | Causa | Prevención |
|-------|--------|-------|-----------|
| **TypeError** | "unsupported operand type" | Tipos incompatibles | Convertir al mismo tipo |
| **ValueError** | "invalid literal for int()" | Conversión inválida | Validar antes de convertir |
| **ZeroDivisionError** | "division by zero" | Dividir entre 0 | Verificar divisor ≠ 0 |
| **NameError** | "name is not defined" | Variable no definida | Definir antes de usar |
| **AttributeError** | "has no attribute" | Método no existe en tipo | Verificar tipo correcto |

---

## 10. Recursos y Referencias

### Documentación Oficial
- [Tipos de datos built-in de Python](https://docs.python.org/3/library/stdtypes.html)
- [Funciones de conversión](https://docs.python.org/3/library/functions.html)

### Conceptos Relacionados
- **PEP 8**: Guía de estilo de Python (relevante para nombres de variables)
- **Variables**: Contenedores que almacenan valores con tipo
- **Operadores**: Símbolos que actúan sobre valores

### Próxima Sesión
- **Sesión 3**: Control de flujo (if/elif/else)
  - Usar booleanos en decisiones
  - Condicionales basados en tipos y valores

---

## 📝 Checklist - ¿Estás listo para la Sesión 3?

- [ ] Entiendo los 4 tipos primitivos (int, float, str, bool)
- [ ] Sé cómo usar `input()` y `print()`
- [ ] Puedo convertir entre tipos con `int()`, `float()`, `str()`
- [ ] Reconozco los errores comunes: TypeError, ValueError, NameError
- [ ] Uso f-strings para mostrar datos
- [ ] Valido datos antes de operaciones críticas

**Si marcaste todos estos puntos, ¡estás listo para control de flujo!** 🚀
