# QA Gestión Malla

Proyecto práctico de Quality Assurance realizado sobre un sistema de gestión académica desarrollado como parte de un proyecto universitario.

Tomé este sistema como entorno de pruebas para profundizar de manera práctica en testing manual y automatizado, documentando los casos ejecutados y analizando el comportamiento del sistema frente a diferentes escenarios.

## Objetivo

El objetivo de este proyecto fue aplicar conceptos básicos de Quality Assurance sobre una aplicación funcional, enfocándome especialmente en:

* Diseño de casos de prueba.
* Testing funcional.
* Casos positivos y negativos.
* Pruebas de valores límite.
* Validación de datos.
* Integridad referencial.
* Control de permisos.
* Automatización de pruebas.
* Documentación de resultados.

## Sistema evaluado

El sistema permite gestionar información académica relacionada con:

* Facultades.
* Carreras.
* Materias.
* Mallas curriculares.
* Usuarios y permisos.

Las principales relaciones del sistema son:

```text
Facultad
   ↓
Carrera
   ↓
Malla Curricular
   ↔
Materias
```

Estas relaciones permitieron realizar pruebas que iban más allá de simplemente crear o modificar registros.

## Testing manual

Comencé realizando pruebas manuales sobre el módulo de Materias.

Entre los escenarios evaluados se encuentran:

* Creación de una materia con datos válidos.
* Intento de registro con código duplicado.
* Validación de campos obligatorios.
* Validación de longitud máxima.
* Modificación de una materia.
* Eliminación de registros.
* Eliminación de una materia asociada a una malla.
* Comportamiento de las relaciones al eliminar una Facultad.
* Restricciones de acceso según los permisos del usuario.

Además de verificar el funcionamiento normal, busqué escenarios donde el usuario pudiera introducir datos incorrectos o realizar operaciones que afectaran información relacionada.

## Integridad referencial

Uno de los escenarios evaluados consistió en eliminar una Facultad que tenía asociadas una Carrera, una Malla Curricular y Materias.

Se verificó que:

* La Facultad fuera eliminada.
* La Carrera dependiente fuera eliminada.
* La Malla asociada también fuera eliminada.
* Las Materias permanecieran registradas de manera independiente.

Durante una primera ejecución observé un comportamiento inesperado relacionado con una Materia. Antes de considerarlo un defecto, repetí el escenario utilizando datos controlados.

El comportamiento no pudo reproducirse, por lo que no lo documenté como bug.

Este proceso me ayudó a comprender la importancia de confirmar la reproducibilidad de un problema antes de reportarlo.

## Pruebas de permisos

También realicé pruebas relacionadas con autorización.

Creé un usuario de prueba con permisos para:

```text
Visualizar materias   Permitido
Crear materias        Permitido
Modificar materias    Permitido
Eliminar materias     No permitido
```

Posteriormente comprobé que el sistema no permitiera al usuario realizar operaciones de eliminación.

El comportamiento coincidió con los permisos configurados.

## Testing automatizado

Después de completar las pruebas manuales, seleccioné algunos escenarios para automatizarlos utilizando Python y las herramientas de testing incluidas en Django.

Actualmente existen cinco pruebas automatizadas:

| Caso    | Validación                                      | Resultado |
| ------- | ----------------------------------------------- | --------- |
| MAT-001 | Creación de materia válida                      | PASS      |
| MAT-002 | Código duplicado                                | PASS      |
| MAT-005 | Límite de caracteres                            | PASS      |
| FAC-001 | Integridad referencial y eliminación en cascada | PASS      |
| USR-001 | Restricción por permisos                        | PASS      |

Resultado actual:

```text
Tests ejecutados: 5
PASS: 5
FAIL: 0
```

Los tests se encuentran en:

```text
academico/tests.py
```

## Documentación

La documentación del proceso de QA está organizada dentro de:

```text
qa/
├── test-cases.md
├── test-execution.md
├── bug-reports.md
└── automated-test-results.txt
```

### test-cases.md

Contiene los escenarios definidos para las pruebas manuales, incluyendo precondiciones, pasos y resultados esperados.

### test-execution.md

Contiene los resultados obtenidos durante la ejecución de las pruebas.

### bug-reports.md

Está preparado para documentar defectos reproducibles.

Hasta el momento no se identificaron defectos reproducibles dentro de los escenarios evaluados.

### automated-test-results.txt

Contiene el resultado de la ejecución de la suite automatizada.

## Ejecutar las pruebas

Crear un entorno virtual:

```bash
python3 -m venv venv
```

Activarlo:

```bash
source venv/bin/activate
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

Configurar la base de datos local:

```bash
export DATABASE_URL=sqlite:///db.sqlite3
```

Ejecutar la suite:

```bash
python manage.py test academico -v 2
```

El resultado esperado actualmente es:

```text
Ran 5 tests

OK
```

## Tecnologías y conceptos utilizados

* Python
* Django
* Django TestCase
* Django ORM
* Git / GitHub
* Testing funcional
* Testing manual
* Testing negativo
* Boundary testing
* Validación de datos
* Integridad referencial
* Testing de permisos
* Automatización de pruebas

## Qué aprendí

Este proyecto me permitió comprender mejor que Quality Assurance no consiste únicamente en comprobar si una funcionalidad funciona.

También implica preguntarse:

* ¿Qué ocurre cuando los datos son incorrectos?
* ¿Qué ocurre en los valores límite?
* ¿Qué información se ve afectada al eliminar un registro?
* ¿Qué puede hacer cada tipo de usuario?
* ¿El comportamiento observado puede reproducirse?
* ¿Qué pruebas conviene automatizar?

También pude experimentar el proceso completo de definir un caso de prueba, ejecutarlo, comparar el resultado obtenido con el esperado y posteriormente automatizar algunos de los escenarios.

## Sobre el uso de Inteligencia Artificial

Utilicé herramientas de Inteligencia Artificial como apoyo durante el desarrollo de este portfolio, principalmente para organizar ideas, revisar documentación, comprender conceptos nuevos y recibir orientación durante el proceso de aprendizaje.

Las pruebas fueron ejecutadas por mí sobre el sistema, analizando personalmente los resultados obtenidos y verificando cada escenario antes de documentarlo.

Considero la IA una herramienta de apoyo para aprender y trabajar de manera más eficiente, no un reemplazo de la comprensión del proceso.

## Autor

**Pablo Oviedo Martínez**

Estudiante de Ingeniería en Informática
Orientación profesional: Quality Assurance / Software Testing

Este proyecto forma parte de mi preparación para comenzar profesionalmente en el área de Quality Assurance.

## Origen del proyecto

La aplicación utilizada como base fue desarrollada como proyecto académico universitario.

Repositorio original:

`MiqCaceres/proyecto-gestion-malla`

Esta versión está orientada específicamente a mi práctica personal de Quality Assurance, incluyendo casos de prueba, ejecución manual, validación de datos y permisos, análisis de relaciones y automatización.
