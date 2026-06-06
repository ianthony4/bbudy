# Unit Test Mapping

## 1. Objetivo

Este documento identifica y clasifica las pruebas unitarias existentes en el proyecto Baby Buddy. Su propósito es proporcionar una línea base para actividades de auditoría, análisis de cobertura y mejora de calidad. Se incluyen únicamente pruebas unitarias automatizadas. No se consideran pruebas de integración, funcionales, de interfaz de usuario ni pruebas manuales.

## 2. Resumen de Identificación de Pruebas Unitarias

| Archivo                  | Total de pruebas analizadas | Unitarias puras | Otras pruebas identificadas                                              | Resultado |
| ------------------------ | --------------------------: | --------------: | ------------------------------------------------------------------------ | --------- |
| `tests_forms.py`         |                          46 |               0 | Integración y funcionales de formularios                                 | Excluido  |
| `tests_import_export.py` |                          15 |               0 | Integración de importación/exportación de datos                          | Excluido  |
| `tests_models.py`        |                          32 |               0 | Integración ligera basada en ORM (29) y pruebas cercanas a unitarias (3) | Excluido  |
| `tests_templatetags.py`  |                   9 activas |               7 | Integración ligera (2)                                                   | Incluido  |
| `tests_utils.py`         |                           4 |               4 | Ninguna                                                                  | Incluido  |
| `tests_views.py`         |                          16 |               0 | Integración completa de vistas y rutas                                   | Excluido  |
| total                    |                         122 |              11 |                                                                          |           |

## 3. Estructura del Directorio de Pruebas

Durante el proceso de auditoría se identificó la siguiente estructura dentro del directorio de pruebas del módulo analizado:

```text
tests/
├── import/
├── tests_forms.py
├── tests_import_export.py
├── tests_models.py
├── tests_templatetags.py
├── tests_utils.py
└── tests_views.py
```

### Archivos analizados

| Archivo                  | Descripción general                                                                                 |
| ------------------------ | --------------------------------------------------------------------------------------------------- |
| `tests_forms.py`         | Pruebas relacionadas con formularios y operaciones de creación, edición y eliminación de registros. |
| `tests_import_export.py` | Pruebas relacionadas con funcionalidades de importación y exportación de datos.                     |
| `tests_models.py`        | Pruebas relacionadas con modelos y lógica asociada.                                                 |
| `tests_templatetags.py`  | Pruebas relacionadas con etiquetas y filtros personalizados de plantillas.                          |
| `tests_utils.py`         | Pruebas relacionadas con funciones utilitarias.                                                     |
| `tests_views.py`         | Pruebas relacionadas con vistas y rutas de la aplicación.                                           |

La subcarpeta `import/` fue identificada como parte de la estructura del directorio de pruebas, pero no forma parte del presente análisis debido a que el alcance se limita a los archivos principales de prueba ubicados en la raíz del directorio `tests`.

## 4. Archivo: `test_forms.py`

### 4.1. Resultado del análisis

Se realizó la revisión de las 46 pruebas automatizadas contenidas en el archivo `test_forms.py` con el objetivo de identificar pruebas unitarias que pudieran ser incluidas en el presente inventario.

Tras el análisis de su implementación y comportamiento, se determinó que el archivo no contiene pruebas unitarias puras. En consecuencia, ninguna de las pruebas definidas en este archivo forma parte del alcance del presente documento.

### 4.2. Justificación de la clasificación

Las pruebas analizadas ejercen simultáneamente múltiples componentes de la aplicación, por lo que no aíslan una única unidad de código. Entre las características observadas se encuentran:

- Uso del cliente HTTP de Django (`django.test.Client`) para realizar solicitudes GET y POST.
- Creación, modificación y eliminación de registros en la base de datos de prueba.
- Verificación de respuestas HTTP completas, incluyendo códigos de estado y contenido generado.
- Interacción conjunta entre vistas, formularios, modelos y mecanismos de persistencia.

Debido a estas características, las pruebas se clasifican principalmente como pruebas de integración y pruebas funcionales, en lugar de pruebas unitarias.

### 4.3 Clasificación identificada

| Tipo de prueba                      | Cantidad | Observaciones                                                                          |
| ----------------------------------- | -------- | -------------------------------------------------------------------------------------- |
| Pruebas de integración              | 40       | Operaciones de creación, edición y eliminación de entidades mediante solicitudes HTTP. |
| Pruebas funcionales de formularios  | 6        | Verificación de comportamiento y precarga de valores en formularios.                   |
| Pruebas de validación (integración) | 4        | Validación de reglas de negocio a través del flujo completo de la aplicación.          |
| Pruebas unitarias puras             | 0        | No se identificaron pruebas que aíslen una unidad individual de código.                |

### 4.4. Observación

Para ser consideradas pruebas unitarias puras, las pruebas deberían ejercitar directamente métodos o funciones específicas de formularios, modelos o utilidades, aislando dependencias externas y evitando el uso del cliente HTTP o de flujos completos de persistencia. No se identificaron pruebas con estas características en el archivo analizado.

### 4.5. Resultado

**Archivo excluido del inventario de pruebas unitarias.**

## 5. Archivo: `tests_import_export.py`

### 5.1. Resultado del análisis

Se realizó la revisión de las 15 pruebas automatizadas contenidas en el archivo `tests_import_export.py` con el objetivo de identificar pruebas unitarias que pudieran ser incluidas en el presente inventario.

Tras el análisis de su implementación y comportamiento, se determinó que el archivo no contiene pruebas unitarias puras. En consecuencia, ninguna de las pruebas definidas en este archivo forma parte del alcance del presente documento.

### 5.2. Justificación de la clasificación

Las pruebas analizadas validan el proceso completo de importación de datos, involucrando múltiples componentes de la aplicación de manera simultánea. Durante su ejecución se observó la interacción entre archivos de datos, recursos de importación, lógica de validación, modelos y persistencia en base de datos.

De forma general, las pruebas siguen el flujo:

```text
Archivo CSV → Dataset (tablib) → ImportExportResource → ORM → Base de Datos → Verificación de resultados
```

Debido a este comportamiento, las pruebas no aíslan una unidad individual de código y, por tanto, no cumplen con los criterios de una prueba unitaria.

### 5.3. Clasificación identificada

| Tipo de prueba          | Cantidad | Observaciones                                                                         |
| ----------------------- | -------- | ------------------------------------------------------------------------------------- |
| Pruebas de integración  | 15       | Verifican procesos completos de importación de datos y persistencia en base de datos. |
| Pruebas unitarias puras | 0        | No se identificaron pruebas que aíslen funciones, métodos o clases individuales.      |

### 5.4. Casos representativos identificados

| Prueba               | Propósito principal                                                        |
| -------------------- | -------------------------------------------------------------------------- |
| `test_bmi`           | Verifica la importación de registros de índice de masa corporal.           |
| `test_child`         | Verifica la importación de registros de hijos.                             |
| `test_child_invalid` | Verifica el manejo de errores ante datos inválidos durante la importación. |
| `test_diaperchange`  | Verifica la importación de cambios de pañal.                               |
| `test_feeding`       | Verifica la importación de registros de alimentación.                      |
| `test_sleep`         | Verifica la importación de registros de sueño.                             |
| `test_temperature`   | Verifica la importación de registros de temperatura.                       |
| `test_weight`        | Verifica la importación de registros de peso.                              |

### 5.5. Resultado

**Archivo excluido del inventario de pruebas unitarias.**

## 6 Archivo: `tests_models.py`

### 6.1. Resultado del análisis

Se realizó la revisión de las pruebas automatizadas contenidas en el archivo `tests_models.py` con el objetivo de identificar pruebas unitarias que pudieran ser incluidas en el presente inventario.

A diferencia de los archivos previamente analizados, las pruebas de este módulo interactúan directamente con los modelos de dominio y sus métodos, evitando el uso del cliente HTTP, vistas y formularios. Sin embargo, las pruebas continúan utilizando el ORM de Django y la base de datos de prueba para la creación, consulta y modificación de registros.

Debido a esta dependencia de persistencia, no se identificaron pruebas unitarias puras según los criterios establecidos para el presente análisis.

### 6.2. Justificación de la clasificación

Las pruebas ejercitan directamente métodos, propiedades y comportamientos de los modelos, pero mantienen dependencia con la infraestructura de persistencia proporcionada por Django.

Entre las características observadas se encuentran:

- Creación y consulta de registros mediante el ORM.
- Validación de métodos y propiedades de modelos.
- Verificación de representaciones textuales (`__str__`).
- Validación de relaciones entre entidades.
- Uso de métodos de validación de modelos (`full_clean()`).
- Dependencia de la base de datos de prueba durante la ejecución.

Por esta razón, las pruebas fueron clasificadas principalmente como pruebas de integración ligera orientadas al modelo.

### 6.3. Clasificación identificada

| Tipo de prueba                      | Cantidad | Observaciones                                                                     |
| ----------------------------------- | -------- | --------------------------------------------------------------------------------- |
| Pruebas de integración ligera (ORM) | 29       | Interactúan directamente con modelos y base de datos sin utilizar la capa web.    |
| Pruebas cercanas a unitarias        | 3        | Verifican lógica de negocio específica con mínima dependencia de infraestructura. |
| Pruebas unitarias puras             | 0        | No se identificaron pruebas completamente aisladas de la base de datos.           |

### 6.5. Detalle de Pruebas destacadas

Durante el análisis se identificaron tres casos particularmente cercanos al concepto de prueba unitaria:

| Método                                 | Clase                | Tipo          | Estado | Qué verifica                                                                  | Datos de entrada                                   | Resultado esperado                                | Resultado obtenido                       | Tipo de aserción              |
| -------------------------------------- | -------------------- | ------------- | ------ | ----------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------- | ---------------------------------------- | ----------------------------- |
| test_diaperchange_attributes           | DiaperChangeTestCase | Casi unitaria | PASS   | attributes() devuelve lista de atributos legibles para el usuario             | wet=1, solid=1, color="black", amount=1.25         | ["Wet", "Solid", "Black"] ordenado y capitalizado | ["Wet", "Solid", "Black"]                | assertListEqual               |
| test_tag_complementary_color           | TagTestCase          | Casi unitaria | PASS   | complementary_color devuelve el color de contraste correcto según luminosidad | Caso 1: color="#ffffff" / Caso 2: color="#000000"  | Caso 1: Tag.DARK_COLOR / Caso 2: Tag.LIGHT_COLOR  | DARK_COLOR y LIGHT_COLOR respectivamente | assertEqual x2                |
| test_medication_validation_future_time | MedicationTestCase   | Casi unitaria | PASS   | full_clean() lanza ValidationError cuando time es futura                      | time = now() + 1h — objeto en memoria, sin .save() | Se lanza ValidationError antes de persistir       | ValidationError lanzado correctamente    | assertRaises(ValidationError) |

Estas pruebas validan comportamiento del proyeto de forma más directa que el resto del archivo y constituyen los mejores candidatos para una futura refactorización hacia pruebas unitarias puras.

### 6.6. Observación

El archivo representa el conjunto de pruebas más próximo al nivel unitario identificado hasta el momento. No obstante, la dependencia sistemática de la base de datos de prueba impide clasificar las pruebas como unitarias puras bajo criterios estrictos de aislamiento.

### 6.7. Resultado

**Archivo excluido del inventario de pruebas unitarias puras, aunque identificado como un buen candidato para futuras refactorizaciones orientadas a pruebas unitarias.**

## 7. Archivo: `tests_templatetags.py`

### 7.1. Resultado del análisis

Se realizó la revisión de las pruebas automatizadas contenidas en el archivo `tests_templatetags.py` con el objetivo de identificar pruebas unitarias que pudieran ser incluidas en el presente inventario.

A diferencia de los archivos previamente analizados, la mayoría de las pruebas presentes en este módulo ejercitan directamente funciones auxiliares y etiquetas personalizadas de plantilla sin involucrar solicitudes HTTP, vistas, formularios o persistencia de datos.

Como resultado, este archivo constituye la principal fuente de pruebas unitarias identificada hasta el momento dentro del módulo analizado.

### 7.2. Justificación de la clasificación

Las pruebas unitarias identificadas presentan las siguientes características:

- Invocan directamente funciones Python.
- No utilizan el cliente HTTP de Django.
- No dependen de vistas o formularios.
- No requieren interacción con la base de datos.
- Verifican transformaciones de datos, cálculos y formateo de valores.

Estas características permiten aislar adecuadamente la lógica bajo prueba y reducen significativamente la dependencia de infraestructura externa.

### 7.3. Clasificación identificada

| Tipo de prueba                | Cantidad aproximada | Observaciones                                                                        |
| ----------------------------- | ------------------- | ------------------------------------------------------------------------------------ |
| Pruebas unitarias puras       | 7                   | Validan funciones auxiliares y lógica de transformación de datos.                    |
| Pruebas de integración ligera | 2                   | Requieren interacción con componentes adicionales de Django para generar resultados. |
| Pruebas inactivas             | 1                   | Prueba comentada y actualmente excluida de la ejecución automática.                  |

### 7.4. Pruebas unitarias identificadas

| Método                          | Clase                  | Tipo          | Estado | Qué verifica                                                                        | Datos de entrada                                                              | Resultado esperado                                                                  | Resultado obtenido    | Tipo de aserción                                  |
| ------------------------------- | ---------------------- | ------------- | ------ | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------- | ------------------------------------------------- | --- |
| `test_bootstrap_bool_icon`      | `TemplateTagsTestCase` | Unitaria pura | PASS   | `bool_icon()` devuelve HTML correcto con clase CSS según booleano                   | `True`, `False`                                                               | `icon-true text-success` / `icon-false text-danger`                                 | Coincide con esperado | `assertEqual` x2                                  |
| `test_duration_duration_string` | `TemplateTagsTestCase` | Unitaria pura | PASS   | `duration_string()` formatea un `timedelta` en texto legible con precisión variable | `timedelta(h=1, m=30, s=15)`, precisiones `"m"`, `"h"`, `""`, `"not a delta"` | Cadena formateada por precisión; `""` para entrada vacía; `TypeError` para inválido | Coincide con esperado | `assertEqual` x4, `assertRaises` (uso incorrecto) |
| `test_duration_hours`           | `TemplateTagsTestCase` | Unitaria pura | PASS   | `hours()` extrae las horas de un `timedelta`                                        | `timedelta(hours=1)`, `""`, `"not a delta"`                                   | `1`, `0`, `TypeError`                                                               | Coincide con esperado | `assertEqual` x2, `assertRaises` (uso incorrecto) |
| `test_duration_minutes`         | `TemplateTagsTestCase` | Unitaria pura | PASS   | `minutes()` extrae los minutos de un `timedelta`                                    | `timedelta(minutes=45)`, `""`, `"not a delta"`                                | `45`, `0`, `TypeError`                                                              | Coincide con esperado | `assertEqual` x2, `assertRaises` (uso incorrecto) |
| `test_duration_seconds`         | `TemplateTagsTestCase` | Unitaria pura | PASS   | `seconds()` extrae los segundos de un `timedelta`                                   | `timedelta(seconds=20)`, `""`, `"not a delta"`                                | `20`, `0`, `TypeError`                                                              | Coincide con esperado | `assertEqual` x2, `assertRaises` (uso incorrecto) |
| `test_duration_dayssince`       | `TemplateTagsTestCase` | Unitaria pura | PASS   | `dayssince()` devuelve texto relativo correcto para distintas fechas de referencia  | 3 fechas × 5 deltas: mismo día, -5h, -24h, -48h, -60 días                     | `"today"`, `"yesterday"`, `"2 days ago"`, `"10 days ago"`, `"60 days ago"`          | Coincide con esperado | `assertEqual` x15                                 |
| `test_duration_deltasince`      | `TemplateTagsTestCase` | Unitaria pura | PASS   | `deltasince()` calcula el `timedelta` entre dos `datetime` con `now` fijo           | 3 pares de `datetime` con `now = 2022-01-01 00:00:02`                         | `timedelta(s=1)`, `timedelta(s=3)`, `timedelta(days=19326, s=3)`                    | Coincide con esperado | `assertEqual` dentro de `subTest` x3              |     |

### 7.5. Pruebas clasificadas como integración ligera

| Método                  | Clase                  | Tipo               | Estado | Qué verifica                                                                                    | Datos de entrada                                    | Resultado esperado                                             | Resultado obtenido    | Tipo de aserción |
| ----------------------- | ---------------------- | ------------------ | ------ | ----------------------------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------- | --------------------- | ---------------- |
| `test_instance_add_url` | `TemplateTagsTestCase` | Integración ligera | PASS   | `instance_add_url()` genera URL correcta con y sin `child` asociado al timer                    | Timer sin child / Timer con child `Test Child`      | `"/sleep/add/?timer=ID"` / `"/sleep/add/?timer=ID&child=slug"` | Coincide con esperado | `assertEqual` x2 |
| `test_datetime_short`   | `TemplateTagsTestCase` | Integración ligera | PASS   | `datetime_short()` devuelve `"Today, HH:MM"` para hoy y `"D Mon, HH:MM"` para fechas anteriores | `localtime()` (hoy) / `localtime() - 1 día 6 horas` | Formato `"Today, TIME"` / Formato `"SHORT_MONTH_DAY, TIME"`    | Coincide con esperado | `assertEqual` x2 |

### 7.6. Observaciones

Se identificó una prueba comentada e inactiva:

```text
test_child_age_string
```

La prueba no participa actualmente en la ejecución automática de la suite y, por tanto, la funcionalidad asociada carece de cobertura activa.

El motivo probable es la dependencia de fechas calculadas respecto al momento actual de ejecución, lo que introduce comportamiento no determinista y posibles fallos intermitentes.

### 7.7. Resultado

**Se identificaron 7 pruebas unitarias puras que cumplen los criterios de inclusión definidos para el presente inventario.**

El archivo constituye la principal fuente de cobertura unitaria encontrada durante el análisis realizado hasta esta etapa.

**Unitarias puras:** 7

---

**Integración ligera:** 2

## 8. Archivo: `tests_utils.py`

### 8.1. Resultado del análisis

Se realizó la revisión de las pruebas automatizadas contenidas en el archivo `tests_utils.py` con el objetivo de identificar pruebas unitarias que pudieran ser incluidas en el presente inventario.

El análisis determinó que todas las pruebas presentes en este módulo cumplen con los criterios establecidos para ser clasificadas como pruebas unitarias puras. Las funciones evaluadas son invocadas directamente, sin dependencia de vistas, formularios, cliente HTTP, ORM o base de datos.

Debido a su nivel de aislamiento y enfoque en funciones específicas, este archivo representa el conjunto de pruebas unitarias de mayor calidad identificado durante el análisis realizado hasta el momento.

### 8.2. Justificación de la clasificación

Las pruebas identificadas presentan las siguientes características:

- Invocan funciones auxiliares directamente.
- No utilizan infraestructura web.
- No realizan operaciones de persistencia.
- No dependen de modelos o componentes del ORM.
- Evalúan lógica de transformación, cálculo y validación de datos de forma aislada.

Estas características permiten verificar el comportamiento de cada unidad funcional sin interferencia de componentes externos.

### 8.3. Clasificación identificada

| Tipo de prueba                | Cantidad | Observaciones                                                                 |
| ----------------------------- | -------- | ----------------------------------------------------------------------------- |
| Pruebas unitarias puras       | 4        | Todas las pruebas del archivo cumplen los criterios de aislamiento definidos. |
| Pruebas de integración ligera | 0        | No se identificaron dependencias con infraestructura externa.                 |

### 8.4 Pruebas unitarias identificadas

| Método                         | Clase           | Tipo          | Estado | Qué verifica                                                                                                      | Datos de entrada                                                                                  | Resultado esperado                                                                  | Resultado obtenido    | Tipo de aserción                              |
| ------------------------------ | --------------- | ------------- | ------ | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------- | --------------------------------------------- |
| `test_duration_string`         | `UtilsTestCase` | Unitaria pura | PASS   | `duration_string()` formatea un `timedelta` con distintas precisiones y lanza `TypeError` ante entrada inválida   | `timedelta(h=1, m=30, s=45)` con precisiones por defecto, `"m"`, `"h"` y `"1 hour"` como inválido | `"1 hour, 30 minutes, 45 seconds"`, `"1 hour, 30 minutes"`, `"1 hour"`, `TypeError` | Coincide con esperado | `assertEqual` x3, `assertRaises` con `lambda` |
| `test_duration_parts`          | `UtilsTestCase` | Unitaria pura | PASS   | `duration_parts()` descompone un `timedelta` en tupla `(h, m, s)` y lanza `TypeError` ante entrada inválida       | `timedelta(h=1, m=30, s=45)`, `"1 hour"` como inválido                                            | `(1, 30, 45)`, `TypeError`                                                          | Coincide con esperado | `assertEqual`, `assertRaises` con `lambda`    |
| `test_random_color`            | `UtilsTestCase` | Unitaria pura | PASS   | `random_color()` devuelve un string perteneciente a `utils.COLORS`                                                | Ninguno — función sin parámetros                                                                  | Instancia de `str` contenida en `utils.COLORS`                                      | Coincide con esperado | `assertIsInstance`, `assertIn`                |
| `test_timezone_aware_duration` | `UtilsTestCase` | Unitaria pura | PASS   | `timezone_aware_duration()` calcula correctamente la diferencia entre dos `datetime` con zonas horarias distintas | `start = 2024-10-26 20:30 +01:00`, `end = 2024-10-27 08:30 +00:00`                                | `timedelta(hours=13)`                                                               | Coincide con esperado | `assertEqual`                                 |

### 8.5. Observaciones

Las pruebas `test_duration_string` y `test_duration_parts` verifican adecuadamente la generación de excepciones ante entradas inválidas mediante el uso de una función diferida (`lambda`) dentro de `assertRaises`.

La prueba `test_timezone_aware_duration` constituye uno de los casos más relevantes del módulo, ya que verifica explícitamente el comportamiento de la función ante fechas pertenecientes a distintas zonas horarias.

La utilización de fechas con desplazamientos UTC definidos permite construir una prueba determinista y reproducible, capaz de detectar errores que habitualmente no son cubiertos mediante pruebas basadas en la fecha y hora actual del sistema.

### 8.6. Resultado

**Se identificaron 4 pruebas unitarias puras que cumplen los criterios de inclusión definidos para el presente inventario.**

## 9. Archivo: `tests_views.py`

### 9.1. Resultado del análisis

Se realizó la revisión de las pruebas automatizadas contenidas en el archivo `tests_views.py` con el objetivo de identificar pruebas unitarias que pudieran ser incluidas en el presente inventario.

Tras el análisis de su implementación y comportamiento, se determinó que el archivo no contiene pruebas unitarias puras. Todas las pruebas identificadas ejercitan la capa web de la aplicación mediante solicitudes HTTP reales, interactuando con múltiples componentes del sistema de forma simultánea.

En consecuencia, ninguna de las pruebas definidas en este archivo forma parte del alcance del presente inventario de pruebas unitarias.

### 9.2. Justificación de la clasificación

Las pruebas analizadas presentan características propias de las pruebas de integración completas:

- Utilizan un cliente HTTP real para ejecutar solicitudes GET y POST.
- Interactúan con vistas, modelos, formularios, middleware y sistema de rutas.
- Ejecutan migraciones durante la fase de preparación del entorno de prueba.
- Utilizan datos persistidos en la base de datos de prueba.
- Verifican el comportamiento observable de la aplicación a través de respuestas HTTP.

Asimismo, el método `setUpClass()` ejecuta comandos de inicialización que generan datos de prueba para toda la suite, introduciendo dependencias compartidas entre los distintos casos de prueba.

Debido a estas características, las pruebas no aíslan unidades individuales de código y deben clasificarse como pruebas de integración.

### 9.3. Clasificación identificada

| Tipo de prueba                   | Cantidad | Observaciones                                                                 |
| -------------------------------- | -------- | ----------------------------------------------------------------------------- |
| Pruebas de integración completas | 16       | Validan el funcionamiento de vistas y rutas mediante solicitudes HTTP reales. |
| Pruebas unitarias puras          | 0        | No se identificaron pruebas aisladas de infraestructura.                      |
| Pruebas cercanas a unitarias     | 0        | No se identificaron pruebas con aislamiento parcial significativo.            |

### 9.4. Cobertura funcional observada

Las pruebas del módulo cubren las principales vistas asociadas a las entidades gestionadas por la aplicación.

| Prueba                         | Funcionalidad validada                                                      |
| ------------------------------ | --------------------------------------------------------------------------- |
| `test_bmi_views`               | Vistas relacionadas con registros BMI.                                      |
| `test_child_views`             | Vistas relacionadas con gestión de hijos.                                   |
| `test_diaperchange_views`      | Vistas relacionadas con cambios de pañal.                                   |
| `test_feeding_views`           | Vistas relacionadas con alimentación.                                       |
| `test_headcircumference_views` | Vistas relacionadas con perímetro cefálico.                                 |
| `test_height_views`            | Vistas relacionadas con talla.                                              |
| `test_note_views`              | Vistas relacionadas con notas.                                              |
| `test_pumping_views`           | Vistas relacionadas con extracción de leche.                                |
| `test_sleep_views`             | Vistas relacionadas con sueño.                                              |
| `test_tags_views`              | Vistas relacionadas con etiquetas.                                          |
| `test_temperature_views`       | Vistas relacionadas con temperatura.                                        |
| `test_medication_views`        | Vistas relacionadas con medicación.                                         |
| `test_timer_views`             | Vistas relacionadas con temporizadores.                                     |
| `test_timeline_views`          | Comportamiento de la línea temporal según la cantidad de hijos registrados. |
| `test_tummytime_views`         | Vistas relacionadas con tiempo boca abajo (_tummy time_).                   |
| `test_weight_views`            | Vistas relacionadas con peso.                                               |

### 9.5. Resultado

**Archivo excluido del inventario de pruebas unitarias.**

Las 16 pruebas identificadas fueron clasificadas como pruebas de integración completas debido a su dependencia de la infraestructura web, la base de datos y los mecanismos de inicialización de datos utilizados por la aplicación.

## 10. Conclusión

Del total de 122 pruebas analizadas, únicamente 11 cumplen los criterios definidos para ser clasificadas como pruebas unitarias puras. Estas pruebas se encuentran concentradas en los archivos `tests_templatetags.py` y `tests_utils.py`, los cuales ejercitan funciones de forma directa y con un alto nivel de aislamiento respecto a la infraestructura de la aplicación.

La mayoría de las pruebas existentes corresponden a pruebas de integración, integración ligera basada en ORM o pruebas funcionales, las cuales validan correctamente distintos componentes del sistema, pero no cumplen con los criterios de aislamiento requeridos para ser consideradas pruebas unitarias puras.
