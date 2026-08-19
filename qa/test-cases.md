# Casos de Prueba — Gestión de Materias

## MAT-001 — Crear materia con datos válidos

**Objetivo:**  
Verificar que el sistema permita registrar una materia con datos válidos.

**Precondición:**  
Usuario administrador autenticado.

**Datos de prueba:**  
- Código: QA101
- Nombre: Fundamentos de Testing

**Pasos:**
1. Ingresar a Materias.
2. Seleccionar "Añadir materia".
3. Ingresar el código `QA101`.
4. Ingresar el nombre `Fundamentos de Testing`.
5. Guardar.

**Resultado esperado:**  
La materia debe registrarse correctamente y aparecer en el listado.
MAT-001 = PASS ✅

## MAT-002 — Crear materia con código duplicado

**Objetivo:**  
Verificar que el sistema no permita registrar dos materias con el mismo código.

**Precondición:**  
Debe existir previamente la materia con código `QA101`.

**Datos de prueba:**  
- Código: QA101
- Nombre: Testing de Software II

**Pasos:**
1. Ingresar a Materias.
2. Seleccionar "Añadir materia".
3. Ingresar el código `QA101`.
4. Ingresar el nombre `Testing de Software II`.
5. Guardar.

**Resultado esperado:**  
El sistema debe impedir el registro e informar que ya existe una materia con ese código.
MAT-002 = PASS ✅

## MAT-003 — Crear materia sin código

**Objetivo:**  
Verificar la validación del campo obligatorio Código.

**Datos de prueba:**  
- Código: vacío
- Nombre: Testing Manual

**Pasos:**
1. Ingresar a Materias.
2. Seleccionar "Añadir materia".
3. Dejar vacío el campo Código.
4. Ingresar `Testing Manual` como nombre.
5. Guardar.

**Resultado esperado:**  
El sistema debe impedir el registro e indicar que el código es obligatorio.
MAT-003 = PASS ✅

## MAT-004 — Crear materia sin nombre

**Objetivo:**  
Verificar la validación del campo obligatorio Nombre.

**Datos de prueba:**  
- Código: QA102
- Nombre: vacío

**Pasos:**
1. Ingresar a Materias.
2. Seleccionar "Añadir materia".
3. Ingresar `QA102`.
4. Dejar vacío el campo Nombre.
5. Guardar.

**Resultado esperado:**  
El sistema debe impedir el registro e indicar que el nombre es obligatorio.

MAT-004 = PASS ✅
## MAT-005 — Código superior al límite permitido

**Objetivo:**  
Verificar el comportamiento del sistema cuando el código supera el máximo permitido.

**Datos de prueba:**  
- Código: QA12345678901234567890
- Nombre: Prueba de Límite

**Pasos:**
1. Ingresar a Materias.
2. Seleccionar "Añadir materia".
3. Ingresar el código `QA12345678901234567890`.
4. Ingresar `Prueba de Límite` como nombre.
5. Intentar guardar.

**Resultado esperado:**  
El sistema debe impedir guardar un código que supere el límite permitido.
MAT-005 = PASS ✅

## MAT-006 — Eliminar una materia asociada a una malla curricular

**Resultado esperado:**  
La materia eliminada debe dejar de aparecer en la malla curricular. La malla, la carrera y la facultad relacionadas deben conservarse.

**Resultado obtenido:**  
La materia fue eliminada correctamente y dejó de estar asociada a la malla. La malla curricular, la carrera y la facultad permanecieron sin modificaciones.

**Estado:** PASS ✅

**Validación adicional:**  
Se confirmó la integridad referencial de las entidades relacionadas, ya que la eliminación afectó únicamente a la materia seleccionada.

## FAC-001 — Eliminar una facultad con entidades relacionadas

**Objetivo:**  
Verificar el comportamiento de las relaciones dependientes al eliminar una Facultad.

**Precondiciones:**  
- Existe una Facultad.
- Existe una Carrera asociada a la Facultad.
- Existe una Malla asociada a la Carrera.
- Existe una Materia asociada a la Malla.

**Resultado esperado:**  
Al eliminar la Facultad:
- La Facultad debe eliminarse.
- La Carrera dependiente debe eliminarse.
- La Malla dependiente debe eliminarse.
- La Materia debe conservarse, eliminándose únicamente su relación con la Malla.

**Resultado obtenido:**  
La Facultad, Carrera y Malla fueron eliminadas correctamente.  
La Materia `QA999 - MATERIA SUPERVIVIENTE` permaneció registrada en el módulo Materias.

**Estado:** PASS ✅

**Observación:**  
Durante una ejecución inicial se observó la aparente eliminación de una Materia relacionada. Al repetir la prueba utilizando datos controlados, el comportamiento no pudo reproducirse y la Materia permaneció correctamente registrada. Por lo tanto, no se considera un defecto confirmado.