# Estado del proyecto

Última actualización: 21 de septiembre de 2026

---

## Terminado

**Analizador de Cartera** → `herramientas/analizador-cartera.html`
([guía de uso](USO-ANALIZADOR-CARTERA.md))

Lee el informe CARTERA POR EDADES de Oceanic y entrega:

- Informe de gerencia: indicadores, distribución por edades, concentración del
  riesgo, panel de decisiones automático y mayores deudores
- Hojas de cobro por vendedor, ordenadas por monto pesado por la mora
- Comparativo contra el corte anterior
- Cuatro formas de compartir: enlace publicado, archivo autónomo, PDF e imagen

Validado con el archivo real: 100 clientes, 539 facturas, total $1.958.576.098,
idéntico al que reporta el propio Oceanic.

---

## Pendiente de confirmar con el usuario

Ninguna bloquea el uso de la herramienta; son afinamientos.

1. **¿El corte de 15 días es el correcto?** Hoy los tramos son
   por vencer / 1-15 / 16-30 / 31-60 / 61-90 / +90. Se cambian editando la lista
   `TRAMOS` al inicio del script y corriendo `./build.sh`.

2. **¿Qué decide gerencia con el informe?** (bloquear despachos, pasar a cobro
   jurídico, evaluar vendedores, provisionar). Define qué alerta va primero en
   el panel de decisiones.

3. **¿Las comisiones de los vendedores dependen del recaudo?** Si sí, agregar a
   cada hoja de vendedor el impacto de la mora en su comisión.

4. **¿Existe meta de recaudo semanal o mensual?** Si sí, agregar avance vs. meta
   al informe de gerencia.

---

## Pendiente del lado de la empresa

- Autorizar con TI los conectores de Gmail y Drive para Claude en el Workspace
  corporativo. Conectar el correo personal, no el buzón compartido del área.
- Revisar en el menú *Compartir* del enlace publicado qué opciones de acceso
  ofrece la cuenta, para saber si sirve para gerencia o hay que enviar siempre
  el archivo.

---

## Siguiente herramienta: Flujo de Caja a 13 semanas

Acordado con el usuario para la próxima sesión.

### Qué traer

1. **Export de cuentas por pagar de Oceanic**, en Excel, **crudo, sin limpiar**.
   Basta con 15-20 filas. Anonimizar los proveedores si se quiere (Proveedor A,
   B, C): lo que se necesita es la estructura, no los datos.
2. **Saldo actual en bancos.** Un número por cuenta.
3. **Costos fijos mensuales** y el día aproximado en que salen: nómina,
   parafiscales, impuestos, arriendos, servicios, cuotas de créditos.

### Preguntas para esa sesión

- ¿Oceanic tiene un informe de cuentas por pagar por vencimientos, parecido al
  de cartera por edades? Si sí, ese sirve mejor.
- ¿Cómo se decide hoy a quién se le paga primero cuando no alcanza la caja?
- ¿Hay proveedores que den descuento por pronto pago? ¿Cuánto y a cuántos días?
- ¿Hay créditos o leasings con cuota fija? ¿Cuántos y de qué valor?
- ¿Se manejan varias cuentas bancarias o una sola bolsa?
- ¿Qué porcentaje de la cartera se recauda realmente en la fecha de
  vencimiento? (Determina qué tan optimista es la proyección de ingresos.)

### Ventaja de partida

La cartera por cobrar ya se sabe leer, así que la mitad de los ingresos de la
proyección sale del analizador que ya existe. Conviene que las dos herramientas
compartan el mismo lector del formato Oceanic.

---

## Cómo retomar

Abrir una sesión nueva sobre este repositorio y decir:

> "Lee el README.md y docs/ARRANQUE.md para ponerte al día."

El código de la herramienta está en `src/app.core.html`; `./build.sh` genera las
dos salidas. No editar directamente los archivos generados.
