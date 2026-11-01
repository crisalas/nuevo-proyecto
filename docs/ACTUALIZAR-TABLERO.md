# Pasos para actualizar el tablero de cobro

Cuando Cristhian diga **"actualiza"**, Claude hace su parte y le entrega el archivo
`index.html` ya cifrado. Cristhian solo tiene que subirlo a GitHub.

## Lo que hace Claude
1. Pide la clave del tablero a Cristhian (no se guarda en ningún archivo ni repositorio).
2. Busca en el Drive la cartera, las ventas y los terceros más recientes.
3. Actualiza la aplicación oficial «Gestión de Cobro Campofértil» (solo cambia lo que cambió).
4. Pasa a la aplicación lo que el equipo anotó. Las anotaciones hechas desde el tablero quedan en la pestaña
   **Gestiones** de la hoja de Google «Registro de gestiones de cobro» (columnas: ID, Registrado, NIT, Cliente,
   Quién registra, Resultado, Fecha prometida, Monto prometido, Nota). Cada fila nueva se guarda en la colección
   `gestiones` de la aplicación con el campo `sid` igual al ID de la fila (así el tablero no las repite) y
   `quien`, `origen: 'hoja'`. Si el resultado es «Promesa de pago», se guarda también `prom`
   (fecha, monto, cumplida: false). Las filas cuyo `sid` ya existe no se vuelven a cargar.
5. Arma el tablero con los datos nuevos (incluidas las gestiones con su `sid`) y lo cifra con la clave
   (`herramientas/cifrar_tablero.py`), prueba que abre y le envía `index.html`.

## Lo que hace Cristhian (2 minutos, mejor desde el computador)
1. Descargar el archivo `index.html` que Claude le envió.
2. Entrar a **github.com/crisalas/tablero-cobro**.
3. Pulsar **Add file** (Agregar archivo) y elegir **Upload files** (Cargar archivos).
4. Arrastrar `index.html`. Debe llamarse igual para que reemplace al anterior.
5. Pulsar el botón verde **Commit changes** (confirmar cambios).
6. Esperar uno o dos minutos, abrir **https://crisalas.github.io/tablero-cobro/**,
   escribir la clave y revisar que arriba diga la fecha de la cartera nueva
   (por ejemplo «Datos al 03/11/2026»).

El enlace no cambia nunca. Después, Cristhian puede avisar a los jefes que ya está al día.

## Nota
Si algún día el tablero hay que quitarlo de internet, se elimina el repositorio
`tablero-cobro` en GitHub (Settings → Danger Zone → Delete this repository).

## Cómo guarda el tablero lo que anotan los jefes
El tablero (página cifrada en GitHub) trae un formulario por cliente. Al guardar, envía la anotación a un
«puente» de Google Apps Script instalado en la hoja de registro, que agrega una fila en la pestaña **Gestiones**.
El tablero vuelve a leer esa pestaña cada minuto, así que todos ven las anotaciones al momento. La dirección del
puente y su código secreto van dentro del tablero cifrado; no se guardan en ningún repositorio. Si el puente se
desactiva (Implementar → Administrar implementaciones → Archivar), el tablero muestra que no hay conexión.
