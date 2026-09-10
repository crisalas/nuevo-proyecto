# Checklist de arranque

Qué traer a la primera sesión de construcción.

---

## 🎯 Empezamos por: Analizador de Cartera

Es lo más repetitivo de la semana y es la fuente de datos que después alimenta
el flujo de caja.

---

## 📥 Lo que hay que traer

### 1. El export de cartera de Oceanic (imprescindible)

- Exportar de Oceanic el **auxiliar de clientes** o el **informe de edades de cartera**, en **Excel**.
- **Bastan 15-20 filas.** No se necesita el archivo completo.
- **Anonimizar antes de subirlo:**
  - Reemplazar nombres reales por `Cliente A`, `Cliente B`, `Cliente C`...
  - Quitar o truncar NIT/cédula, teléfonos y correos
  - Los montos se pueden alterar — no importan los valores, importa **la estructura**
- **Importante: no limpiar el archivo.** Se necesita tal como sale de Oceanic,
  con sus encabezados, totales intercalados y formato original. Justamente eso
  es lo que la herramienta tiene que aprender a manejar.

### 2. Un pantallazo del informe en Oceanic (opcional, ayuda mucho)

Sirve para ver qué otros informes hay disponibles y con qué filtros.

### 3. Respuestas a estas preguntas

- ¿Cada cuánto se corre este informe? (diario / semanal / mensual)
- ¿Qué se hace hoy manualmente con ese archivo, paso a paso?
- ¿Qué tramos de edad se usan en la empresa? (¿0-30/31-60/61-90/+90, u otros?)
- ¿Los plazos de pago son iguales para todos los clientes o varían por cliente?
- ¿Existe un cupo de crédito por cliente registrado en Oceanic?
- ¿Qué se le entrega a gerencia hoy y en qué formato?

---

## 🧱 Estructura que probablemente trae el export

Si no se alcanza a traer el archivo, con confirmar qué columnas existen se puede
ir adelantando el esqueleto:

| Columna típica | ¿La trae? |
|---|---|
| Código / NIT del cliente | ? |
| Nombre del cliente | ? |
| Número de factura o documento | ? |
| Fecha de la factura | ? |
| Fecha de vencimiento | ? |
| Valor original | ? |
| Abonos / pagos aplicados | ? |
| Saldo pendiente | ? |
| Días de vencido | ? |
| Vendedor / asesor | ? |
| Condición o plazo de pago | ? |
| Centro de costo / sucursal | ? |

---

## ⚠️ Nota sobre datos

Las sesiones son temporales y el contenedor se borra al terminar. Aun así, no
subir datos personales de clientes ni información financiera real que no sea
necesaria. Para construir la herramienta **la estructura es suficiente**.

---

## ▶️ Cómo retomar mañana

Abrir una sesión nueva de Claude Code sobre este repositorio y decir:

> "Lee el README.md y docs/ARRANQUE.md. Vamos a construir el Analizador de Cartera.
> Aquí está el export de Oceanic."

Con eso el contexto queda restablecido sin repetir nada.
