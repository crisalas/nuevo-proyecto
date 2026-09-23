# Estado del proyecto

Última actualización: 23 de septiembre de 2026

---

## Herramientas terminadas

### 1. Analizador de Cartera
`herramientas/analizador-cartera.html` · [guía](USO-ANALIZADOR-CARTERA.md)

Lee el informe CARTERA POR EDADES y produce el informe de gerencia y las hojas
de cobro por vendedor. Tramos: por vencer / 1-15 / 16-30 / 31-60 / 61-90 / +90.

Validado: 100 clientes, 539 facturas, $1.958.576.098 — idéntico al total que
reporta el propio Oceanic.

### 2. Flujo de Caja 13 Semanas
`herramientas/flujo-de-caja.html` · [guía](USO-FLUJO-DE-CAJA.md)

Cruza la cartera, las cuentas por pagar y los costos fijos. Proyecta el saldo
semana a semana, ordena a quién pagar, evalúa los descuentos por pronto pago y
simula escenarios.

Validado con el corte del 22/09: caja $103.168.295, punto más bajo −$508.036.290
en la semana 3.

Ambas comparten las mismas formas de compartir: enlace publicable, archivo
autónomo, imagen, PDF y texto.

---

## Pendiente de confirmar (no bloquea el uso)

1. **Saldo de Bancolombia.** El usuario escribió "90.348.52 millones"; se asumió
   **$90.348.520**. Confirmar.
2. **"EDO" (10% de pronto pago)** no aparece en el archivo de cuentas por pagar.
   Falta el nombre exacto como está en Oceanic.
3. **Retención en la fuente:** ¿qué día del mes se paga? Está puesto el 15.
4. **Retraso real de pago de los clientes.** Está en 15 días, estimado. Es el
   supuesto que más mueve la proyección.
5. Del Analizador: ¿el corte de 15 días es el correcto? ¿Qué decide gerencia?
   ¿Las comisiones dependen del recaudo? ¿Hay meta de recaudo?

---

## Pendiente del lado de la empresa

- Autorizar con TI los conectores de Gmail y Drive (correo personal, no el buzón
  compartido del área).
- Revisar en el menú *Compartir* de los enlaces qué opciones de acceso ofrece la
  cuenta, para saber si gerencia puede abrirlos o hay que enviar el archivo.

---

## Lo que dijeron los primeros números

Vale la pena tenerlo presente al revisar los cortes nuevos:

- Cartera vencida: **44,2%** del total. Cinco clientes concentran el **56%** de
  lo vencido.
- Flujo de caja: la caja no alcanza en las primeras semanas de octubre. El punto
  más bajo es la semana 3.
- **Vender más no resuelve octubre.** Una venta tarda unos 45 días en volverse
  plata. Lo único que mueve la caja a corto plazo es el recaudo: en el simulador,
  cobrar sin retraso lleva el punto más bajo de −$508 M a −$76 M.
- CEVA concentra el **59%** de todo lo que se debe.
- Hay **$8.548.335** en descuentos por pronto pago sin tomar.

---

## Rutina semanal acordada

```
Lunes  →  Oceanic: exportar CARTERA POR EDADES
       →  Oceanic: exportar CUENTAS POR PAGAR   (el mismo día)
       →  Analizador de Cartera: reportes a vendedores y gerencia
       →  Flujo de Caja: revisar "A quién pagar" antes de girar
```

Hay una rutina programada que avisa de lunes a viernes a las 3:00 pm
(`trig_01Prc9WHPuD1w7x3kUHeUEhm`). La primera vez no llegó la notificación al
usuario; se le recomendó poner además una alarma en el celular.

---

## Siguiente en el roadmap

Nada comprometido. Cuando el usuario lleve unas semanas usando las dos
herramientas, las mejoras saldrán del uso real. Del roadmap original quedan:
conciliador bancario, comparador de cotizaciones, análisis de gasto de compras,
scorecard de proveedores y el Centro de Control que une las tres áreas.

---

## Cómo está organizado el código

| Archivo | Qué es |
|---|---|
| `src/app.core.html` | Fuente del Analizador de Cartera |
| `src/flujo.core.html` | Fuente del Flujo de Caja |
| `build.sh` | Genera las cuatro salidas desde los dos fuentes |
| `herramientas/*.html` | Lo que el usuario abre. **Generado: no editar.** |

Después de editar un fuente hay que correr `./build.sh`.

Las herramientas llevan incrustada una copia de su propio código en base64: eso
es lo que les permite publicarse con los datos del corte dentro.

---

## Cómo retomar

> "Lee el README.md y docs/ARRANQUE.md para ponerte al día."
