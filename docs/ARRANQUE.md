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

## Siguiente herramienta del roadmap

**Flujo de Caja a 13 semanas.** Necesita dos exports de Oceanic: cartera por
cobrar (ya se sabe leer) y cuentas por pagar (falta ver su estructura), más los
costos fijos mensuales (nómina, impuestos, arriendos).

---

## Cómo retomar

Abrir una sesión nueva sobre este repositorio y decir:

> "Lee el README.md y docs/ARRANQUE.md para ponerte al día."

El código de la herramienta está en `src/app.core.html`; `./build.sh` genera las
dos salidas. No editar directamente los archivos generados.
