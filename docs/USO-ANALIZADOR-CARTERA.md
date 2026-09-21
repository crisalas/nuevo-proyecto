# Analizador de Cartera — guía de uso

Herramienta que lee el informe **CARTERA POR EDADES** de Oceanic y produce el
reporte de gerencia y las hojas de cobro por vendedor.

---

## Rutina semanal (5 minutos)

1. En Oceanic, exporta **CARTERA POR EDADES** a Excel.
2. Abre `herramientas/analizador-cartera.html` en Chrome (doble clic).
3. Arrastra el archivo a la ventana.
4. Revisa la pestaña **Gerencia**.
5. Comparte: **Imprimir / PDF** para gerencia, o *Resumen para WhatsApp* si es algo rápido.
6. En **Vendedores**, *Mensaje para WhatsApp* o *Copiar para Excel* para cada uno.

No hay que limpiar el archivo ni cambiarle el formato. Se carga tal como sale.

---

## Los datos no salen del computador

El archivo se lee **dentro del navegador**. No se sube a ningún servidor, no viaja
por internet y no queda almacenado en ningún sitio externo. La herramienta no
tiene dependencias: lee el `.xlsx` con el descompresor que ya trae el navegador.

Lo único que se guarda es un resumen por corte (totales y saldo por cliente) en el
almacenamiento local del navegador, para poder comparar contra la semana anterior.
Eso vive solo en ese equipo.

---

## Cómo compartir el informe

| Destino | Qué usar |
|---|---|
| **Que vean la herramienta completa** | **Publicar este corte en el enlace** → compartir el enlace |
| WhatsApp rápido | **Enviar como imagen** → adjuntar como foto |
| Correo formal | **Guardar como PDF** → adjuntar |
| Correo o chat escrito | **Como texto** → copiar → pegar |

### El enlace compartido (lo más completo)

En la pestaña **Gerencia**, al final, el botón **Publicar este corte en el
enlace** guarda los datos del corte dentro de la propia página publicada.

A partir de ahí, quien abra el enlace ve **exactamente lo mismo que tú**: las
cuatro pestañas, los indicadores, el detalle de clientes y facturas, y el botón
de imprimir. No tiene que cargar ningún archivo ni instalar nada.

Cada semana, al cargar el archivo nuevo, se vuelve a pulsar el botón y el enlace
queda actualizado. Es el mismo enlace siempre.

**Antes de compartirlo, ten en cuenta:**

- El enlace es **privado**. Solo lo abre quien lo autorices desde el menú
  *Compartir* de la página.
- Quien lo abra ve **todos los clientes con nombre y saldo**. Para gerencia está
  bien; para un vendedor, mejor enviarle su imagen o su lista, no el enlace.
- El botón solo aparece cuando abres la herramienta **desde el enlace**. Desde el
  archivo guardado en el disco no aparece, porque ahí no hay nada que publicar.

### La imagen

Genera un PNG del informe, dibujado igual que en pantalla: indicadores, gráfico
de edades, panel de decisiones y mayores deudores. Se envía como una foto
cualquiera, así que se ve bien en cualquier teléfono sin abrir nada.

- **Copiar imagen** → pegar directo en WhatsApp Web o en el correo
- **Descargar imagen** → queda en Descargas, se adjunta como foto
- **En el celular** → mantener presionada la vista previa para guardarla

Cada vendedor tiene su propia imagen, con su orden de llamada y los teléfonos.
Es lo que mejor funciona: la abre en el celular y llama desde ahí.

> La descarga directa puede no funcionar si abres la herramienta desde el enlace
> compartido. Usa *Copiar imagen*, o mantén presionada la vista previa. Con el
> archivo guardado en tu PC funcionan las dos.

### El texto

Los textos son editables antes de copiar. En WhatsApp los asteriscos se
convierten solos en negrita.

### Sobre el PDF

Las barras del gráfico se dibujan como figura vectorial, no como color de fondo,
porque Chrome por defecto **no imprime los fondos**. Así el gráfico sale siempre,
tenga o no marcada la casilla *Gráficos de fondo* en el diálogo de impresión.

Si algún color se ve pálido en el PDF, marca **Más ajustes → Gráficos de fondo**
en el diálogo de impresión de Chrome.

---

## Tramos de vencimiento

| Tramo | Días vencidos |
|---|---|
| Por vencer | aún no llega la fecha |
| 1 a 15 | 1 – 15 |
| 16 a 30 | 16 – 30 |
| 31 a 60 | 31 – 60 |
| 61 a 90 | 61 – 90 |
| Más de 90 | 91 en adelante |

> Oceanic trae sus propios tramos (1-30, 31-60, 61-90, 91-120, +120), que no
> coinciden con estos. La herramienta **los ignora** y recalcula desde la columna
> de días vencidos de cada factura, así que el corte de 15 días es exacto.

Para cambiar los cortes, edita la lista `TRAMOS` al inicio del script y vuelve a
correr `./build.sh`.

---

## Asignación de vendedores

El informe de Oceanic **no trae el vendedor** de cada cliente, así que hay que
cargarlo una vez:

1. Pestaña **Vendedores** → *Copiar los N clientes*
2. Pegar en Excel, escribir el vendedor en la tercera columna
3. Copiar las tres columnas y pegarlas en el recuadro → *Guardar asignación*

Queda guardada en el navegador y se aplica automáticamente a todos los cortes
siguientes. Los clientes nuevos aparecen como "Sin asignar" hasta que se agreguen.

---

## Comparativo semanal

Cada archivo cargado registra un corte. A partir del segundo, el informe de
gerencia muestra la variación contra el corte anterior: cuánto subió o bajó el
vencido, qué clientes empeoraron y cómo se movió el tramo de más de 90 días.

Se conservan los últimos 14 cortes (unos tres meses).

---

## Qué revisa el panel "Requiere decisión"

| Regla | Cuándo se dispara |
|---|---|
| Cartera vencida crítica | vencido ≥ 35% del total |
| Cartera vencida alta | vencido ≥ 20% del total |
| Más de 90 días | siempre que exista saldo en ese tramo |
| Riesgo concentrado | los 5 mayores deudores suman ≥ 50% del vencido |
| Cartera 100% vencida | cliente sin saldo corriente y monto relevante |
| Facturas de más de un año | cualquier documento con más de 365 días |
| Variación semanal | el vencido se movió más de 1% del total |
| Clientes que empeoraron | su vencido creció frente al corte anterior |

---

## Orden de cobro sugerido

La lista de cada vendedor se ordena por:

```
prioridad = monto vencido × (1 + días de mora ÷ 90)
```

Es decir: pesa el monto, pero castiga la antigüedad. Un cliente de $10 millones a
180 días queda por encima de uno de $15 millones a 20 días.

---

## Archivos

| Archivo | Qué es |
|---|---|
| `herramientas/analizador-cartera.html` | **La herramienta.** Es la que se usa. |
| `src/analizador-cartera.body.html` | El código fuente que se edita |
| `build.sh` | Genera la herramienta a partir del fuente |

Después de editar el fuente hay que correr `./build.sh`.

---

## Si algo falla

| Mensaje | Qué hacer |
|---|---|
| "no parece ser un .xlsx válido" | Se exportó en otro formato. Volver a exportar como Excel. |
| "No se encontraron facturas" | No es el informe CARTERA POR EDADES, o salió vacío. |
| "no soporta descompresión nativa" | Navegador viejo. Usar Chrome o Edge actualizado. |
| Los totales no cuadran | El informe de gerencia avisa cuando cuadra con el total de Oceanic. Si no aparece ese aviso, verificar que el export esté completo. |
