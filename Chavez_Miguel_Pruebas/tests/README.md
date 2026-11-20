# Pruebas Unitarias - Microaplicación de Videojuegos

## Cobertura de pruebas
- **Modelos (`test_models.py`)**: Verifica la conexión exitosa a la base de datos MySQL y la correcta ejecución de consultas a la tabla `juegos`.
- **Rutas (`test_routes.py`)**: Utiliza el cliente de pruebas de Flask para verificar que las rutas de la aplicación respondan correctamente.
- **Controlador (`test_api.py`)**: Prueba la función `insertar_juego` del controlador, verificando que el registro se guarde correctamente en la base de datos y limpiando los datos temporales al finalizar.

## Retos encontrados y soluciones
- **Importación de módulos**: Se presentaron errores de `ModuleNotFoundError` al intentar ejecutar las pruebas desde la carpeta `tests`. Se solucionó utilizando `sys.path.append` para que Python reconociera los archivos de la carpeta raíz (`bd.py`, `controlador_juegos.py`).
- **Falsos positivos en pruebas**: Al inicio la prueba de inserción fallaba porque la base de datos ya tenía registros de pruebas anteriores. Se solucionó ajustando el `setUp` y `tearDown` para limpiar el registro "Juego Test" antes y después de cada prueba.
- **Warnings de Deprecación**: Apareció un aviso amarillo sobre `'bd' is deprecated`. Se documentó que es solo una advertencia de versión de Python y no afecta el funcionamiento de las pruebas.

## Ejecución
Para correr las pruebas y generar el reporte:
```bash
python -m unittest discover -v tests > results.txt 2>&1