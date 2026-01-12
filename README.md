# Curso Basico de Python

Este repositorio aloja la estructura base del curso: carpetas separadas para teoria, notebooks, ejercicios, soluciones, datos y pruebas automatizadas.

## Requisitos rapidos
- Python 3.10+ instalado.
- Git y virtualenv/venv disponibles para aislar dependencias (opcional).

## Puesta en marcha
1) Crear y activar un entorno virtual:
```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
```
2) Instalar dependencias base:
```bash
pip install -r requirements.txt
```
3) Ejecutar las pruebas de verificacion:
```bash
pytest
```

## Estructura del repo
- `src/python_basico/`: contiene codigo de apoyo y ejemplos reutilizables.
- `notebooks/`: alberga los cuadernos Jupyter para las sesiones; se sugiere un notebook por tema (`01_intro.ipynb`, `02_condicionales.ipynb`, etc.).
- `exercises/`: guarda los enunciados y archivos de inicio para practica, organizados por modulo.
- `solutions/`: almacena las soluciones oficiales, separadas de los ejercicios.
- `tests/`: reune pruebas automatizadas (`pytest`) para validar ejercicios y ejemplos.
- `docs/`: concentra material de referencia, guias de instalacion y apuntes.
- `data/raw` y `data/processed`: reservadas para datos de ejemplo; los `.gitkeep` permiten versionar las carpetas vacias.
- `scripts/`: contiene utilidades de automatizacion (instalacion, formateo, etc.).

## Convenciones sugeridas
- Los archivos usan prefijos numericos para mantener el orden del temario (`01_`, `02_`...).
- Cada carpeta mantiene un `README.md` con instrucciones basicas para los alumnos.
- El codigo de ejemplo reside en `src/` y se referencia desde notebooks y ejercicios para evitar duplicar logica.

## Proximos pasos
- El temario inicial se ubica en `docs/` y los notebooks base en `notebooks/`.
- Los primeros ejercicios se colocan en `exercises/` y sus pruebas en `tests/`.
- Puede configurarse CI en GitHub Actions para ejecutar `pytest` en cada push.
