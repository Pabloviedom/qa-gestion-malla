Ejecución de Pruebas — Gestión de Materias

Módulo: Materias
Tipo de pruebas: Testing funcional manual
Entorno: Local — Django Development Server
Ejecutor: Pablo Oviedo Martínez

MAT-001 — Crear materia con datos válidos

Resultado esperado:
La materia debe registrarse correctamente y aparecer en el listado.

Resultado obtenido:
La materia QA101 - Fundamentos de Testing fue registrada correctamente y apareció en el listado de materias.

Estado: PASS ✅

MAT-002 — Crear materia con código duplicado

Resultado esperado:
El sistema debe impedir el registro de una segunda materia con el mismo código.

Resultado obtenido:
El sistema rechazó el registro al detectar que el código QA101 ya estaba siendo utilizado.

Estado: PASS ✅

MAT-003 — Crear materia sin código

Resultado esperado:
El sistema debe impedir el registro e indicar que el campo Código es obligatorio.

Resultado obtenido:
El sistema no permitió guardar la materia sin completar el campo Código.

Estado: PASS ✅

MAT-004 — Crear materia sin nombre

Resultado esperado:
El sistema debe impedir el registro e indicar que el campo Nombre es obligatorio.

Resultado obtenido:
El sistema no permitió guardar la materia sin completar el campo Nombre.

Estado: PASS ✅

MAT-005 — Código superior al límite permitido

Resultado esperado:
El sistema debe impedir ingresar o guardar un código superior a 20 caracteres.

Resultado obtenido:
El campo limita la entrada a un máximo de 20 caracteres y no permite ingresar un carácter adicional.

Estado: PASS ✅

Resumen de ejecución

Casos ejecutados: 5
PASS: 5
FAIL: 0
Bugs encontrados: 0

Conclusión

Las validaciones evaluadas en el módulo de Materias funcionaron de acuerdo con el comportamiento esperado en los cinco casos ejecutados.

Se validaron escenarios positivos, negativos y de límite relacionados con creación de materias, campos obligatorios, duplicación de códigos y longitud máxima permitida.

## USR-001 — Validar permisos de eliminación de Materias

**Objetivo:**  
Verificar que un usuario sin permiso de eliminación no pueda eliminar materias.

**Precondiciones:**  
- Existe un usuario staff llamado `qa_tester`.
- El usuario posee permisos para visualizar, crear y modificar materias.
- El usuario no posee permiso para eliminar materias.

**Pasos:**
1. Iniciar sesión con el usuario `qa_tester`.
2. Acceder al módulo Materias.
3. Verificar que puede consultar materias.
4. Crear la materia `QA200 - Prueba de Permisos`.
5. Modificar la materia creada.
6. Intentar eliminar la materia.

**Resultado esperado:**  
El usuario debe poder visualizar, crear y modificar materias, pero no debe tener disponible la opción de eliminación ni poder eliminar registros.

# Ejecución de Pruebas Automatizadas

**Framework:** Django TestCase  
**Lenguaje:** Python  
**Entorno:** Local  
**Ejecutor:** Pablo Oviedo Martínez  

## Casos automatizados

- MAT-001 — Creación de materia válida → PASS ✅
- MAT-002 — Validación de código duplicado → PASS ✅
- MAT-005 — Validación de longitud máxima del código → PASS ✅
- FAC-001 — Eliminación en cascada e integridad referencial → PASS ✅
- USR-001 — Validación de permisos de eliminación → PASS ✅

## Resultado

**Tests ejecutados:** 5  
**PASS:** 5  
**FAIL:** 0  

La suite automatizada finalizó correctamente sin errores.

**Resultado obtenido:**  
El usuario pudo visualizar, crear y modificar materias. La opción de eliminación no estuvo disponible debido a que no poseía el permiso correspondiente.

**Estado:** PASS