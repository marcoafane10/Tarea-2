# Tarea-2
Tarea de libreria
# Levantamiento de requerimientos — Biblioteca Digital de Instrucciones (Impresos Múltiples)

**1. Estados posibles**
- versión obsoleta
- vigente, solo lectura
- vigente, edición habilitada
- (casos por defecto) versión inválida, rol no reconocido

**2. Qué define cada estado (según la ficha y el diagrama de flujo)**
- La ficha incluye *historial de versiones* por proceso (fecha y número de versión) y *al menos dos perfiles*: solo consulta/lectura, y lectura + edición.
- El diagrama: "¿Perfil con permiso de edición?" → Sí: crear/editar (y guardar como nueva versión); No: el operario solo consulta.
- Versión < vigente → obsoleta. Versión = vigente + rol `lectura` → solo lectura. Versión = vigente + rol `edicion` → edición habilitada.

**3. Reglas de la ficha reflejadas**
- Dos perfiles (`lectura`, `edicion`), no roles inventados.
- Una versión obsoleta no se edita, sin importar el rol (la edición genera una *nueva* versión a partir de la vigente).

**4. Caso por defecto**
- Versión < 1 o > vigente: `version invalida`. Rol distinto de los dos perfiles: `rol no reconocido`.

**Pendiente de confirmar con el Socio Formador:** el número de versión vigente (`CURRENT_VERSION = 3` es un valor de prueba; en el proyecto real saldrá de la base de datos SQL).
