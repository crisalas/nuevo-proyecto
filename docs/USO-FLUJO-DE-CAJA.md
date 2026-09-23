# Flujo de Caja 13 Semanas — guía de uso

Cruza la **cartera por cobrar** y las **cuentas por pagar** de Oceanic con los
costos fijos de la empresa, y proyecta el saldo de caja semana a semana.

---

## Rutina

1. En Oceanic, exporta **CARTERA POR EDADES** y **CUENTAS POR PAGAR** a Excel.
2. Abre `herramientas/flujo-de-caja.html` en Chrome.
3. Arrastra los dos archivos (juntos o uno por uno). La herramienta reconoce
   cuál es cuál por su estructura.
   > **Expórtalos el mismo día.** No es obligatorio, pero sí lo ideal: la
   > herramienta arranca la proyección en el corte más reciente de los dos, y
   > avisa cuando se separan más de 5 días.
4. Revisa **Proyección**, y antes de pagar mira **A quién pagar**.

---

## Las cuatro pestañas

| Pestaña | Qué responde |
|---|---|
| **Proyección** | ¿En qué semana me quedo sin caja y por cuánto? |
| **A quién pagar** | Con la plata que hay, ¿a quién le pago primero? |
| **Pronto pago** | ¿Cuáles descuentos conviene tomar y cuánto rinden? |
| **Parámetros** | Todo lo que no sale de Oceanic: saldos, costos fijos, supuestos |

---

## Reglas que aplica a los proveedores

Vienen de cómo funciona la empresa, no del archivo:

| Regla | Proveedor | Efecto |
|---|---|---|
| Excluido | **Bancolombia** | Su saldo está cargado completo en Oceanic pero es un leasing. Se saca del flujo y entra como cuota fija mensual de $8.000.000. |
| Acuerdo de pago | **Quintero Mejía**, **Cooetransalca** | Combustible. Se pagan el día 5 de cada mes, sin importar el vencimiento que muestre el sistema. |
| Estratégico | **CEVA** | Se paga aunque no dé descuento: la operación depende de él. |
| Pronto pago | Chalver 10%, EDO 10%, Red Agroveterinaria 6%, Bioara 5%, Servinsumos 5%, Ouro Fino 4%, Basic Farm 3%, Coop. de Ganaderos 3%, Desarrollo Químico 3% | Se priorizan en el orden de pago y se evalúan en su pestaña. |

Para cambiar estas reglas hay que editar `PARAMS_BASE` en `src/flujo.core.html`.
Lo demás (valores, días, saldos) se edita desde la pestaña Parámetros.

---

## Los tres supuestos que mandan

Están en **Parámetros** y también como deslizadores en **Proyección**:

| Supuesto | Valor inicial | De dónde sale |
|---|---|---|
| Ventas nuevas por semana | $152.000.000 | Promedio de las últimas 9 semanas del propio archivo de cartera |
| Retraso promedio de pago | 15 días | Estimado. **Conviene ajustarlo**: es el que más mueve la proyección |
| De lo vencido se recupera | 35% en 13 semanas | Estimado |

> El recaudo de lo vencido no se reparte parejo: se cobra más en las primeras
> semanas y cada vez menos. La herramienta usa una curva decreciente.

---

## Cómo se proyecta cada peso

**Ingresos**
- Factura no vencida → entra en su fecha de vencimiento más el retraso promedio.
- Factura vencida → entra dentro del porcentaje de recuperación, repartido con
  la curva decreciente.
- Ventas nuevas → se facturan cada semana y entran al plazo de venta más el retraso.

**Egresos**
- Factura de proveedor → sale en su fecha de vencimiento.
- Factura ya vencida → sale esta semana (se asume que hay que pagarla).
- Proveedor con acuerdo → sale el día pactado.
- Proveedor excluido → no sale; entra su cuota real como costo fijo.
- Costos fijos → cada mes en su día, o en su fecha puntual.

---

## La tasa de pronto pago

La columna **Rinde (E.A.)** convierte el descuento en tasa efectiva anual, para
poder compararlo con lo que cuesta un crédito.

Un 45% significa que pagarle anticipado a ese proveedor equivale a una inversión
que renta 45% anual. Si eso es más de lo que cobra el banco, conviene pagar
anticipado **incluso con plata prestada**.

Detalles del cálculo:

- Los días que se anticipan se miden solo sobre el saldo que **aún no vence**.
- Hay un piso de 10 días: con plazos más cortos la tasa se dispara y deja de
  servir para comparar.
- Donde dice *ya vencido*, no se está anticipando nada. El descuento puede
  seguir sirviendo, pero hay que confirmarlo con el proveedor.

---

## Lo que la herramienta NO sabe

Hay que tenerlo presente al leer la proyección:

- **No conoce las compras futuras.** Proyecta los ingresos de las ventas nuevas,
  pero no los pagos a proveedores que esas ventas van a generar. La proyección
  es por eso más optimista en las últimas semanas.
- **No sabe si un cliente va a pagar.** Usa un promedio, no el comportamiento de
  cada cliente.
- **No conoce cupos de sobregiro ni créditos disponibles.** Un saldo negativo
  significa "falta plata", no necesariamente "la empresa se quiebra".

---

## Si los dos archivos son de fechas distintas

La herramienta arranca la proyección en el **corte más reciente** de los dos, y
muestra un aviso cuando la diferencia pasa de 5 días.

| Diferencia | Qué pasa |
|---|---|
| Mismo día | Ideal. Todo cuadra. |
| 1 a 5 días | Se puede usar sin problema. |
| Más de una semana | Sale el aviso. El archivo viejo trae facturas que quizá ya se pagaron, así que los ingresos salen inflados. |

Funciona igual si cargas uno solo:

- **Solo cuentas por pagar** → proyecta los egresos, y los ingresos solo con las
  ventas estimadas. Avisa que falta la cartera.
- **Solo cartera** → no arranca: sin los egresos no hay flujo que proyectar.
