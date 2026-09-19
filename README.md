# Herramientas de Cartera, Tesorería y Compras

Repositorio de herramientas internas para automatizar el trabajo diario de las áreas
de **Cartera**, **Tesorería** y **Compras**.

---

## Contexto

| Punto | Situación |
|---|---|
| Software contable | **Oceanic** — en la nube, se usa por navegador |
| Exportaciones disponibles | Excel, PDF, TXT |
| API / base de datos | **No disponible.** Toda entrada de datos es por export manual |
| Correo corporativo | Google Workspace (Gmail) |
| Entrega de cartera | Semanal, cada inicio de semana. Dos destinatarios: vendedores y gerencia |
| Áreas a cargo | Cartera, Tesorería y Compras (las tres en la misma persona) |

**Consecuencia de diseño:** las herramientas NO se conectan a Oceanic. Reciben el
archivo exportado y trabajan sobre él. El único paso manual es el export (~2 min).

---

## Decisión de arquitectura

Las herramientas se construyen como **aplicaciones HTML autónomas** (un solo archivo `.html`).

Motivo:
- No requieren instalar nada en el PC de la empresa
- No requieren permisos de TI
- Se abren en Chrome, funcionan sin internet
- Se pueden compartir por correo o por enlace

Se descarta Python como formato principal: requiere instalación y autorización de TI.
Se usa solo si en algún momento hay un PC donde sí se pueda.

---

## Flujo de trabajo previsto

```
1. Oceanic  ──► exportar a Excel                 (manual, ~2 min)
2. Abrir la herramienta HTML en Chrome
3. Arrastrar el archivo                          (automático)
4. Revisar reporte / gráficas / alertas
5. Exportar resultado a Excel o PDF
```

---

## Roadmap

### Fase 1 — Base
- [x] **Lector del formato Oceanic** — interpreta el informe jerárquico (sucursal →
      cliente → facturas → subtotal) sin librerías externas. Validado contra el total
      del propio archivo.

### Fase 2 — Alto impacto
- [x] **Analizador de Cartera** → `herramientas/analizador-cartera.html`
      ([guía de uso](docs/USO-ANALIZADOR-CARTERA.md)) — tramos por vencer / 1-15 /
      16-30 / 31-60 / 61-90 / +90, panel de decisiones, concentración de riesgo,
      hojas de cobro por vendedor, comparativo semanal e impresión a PDF.
- [ ] **Flujo de Caja a 13 semanas** — cruza cartera por cobrar + cuentas por pagar +
      costos fijos. Marca la semana de déficit. Incluye simulador de escenarios.
- [ ] **Generador de cartas de cobro** — textos personalizados en tres tonos
      (recordatorio / requerimiento / prejurídico), listos para pegar en Gmail o bajar en PDF.

### Fase 3 — Complementarias
- [ ] **Conciliador bancario** — cruza extracto vs. libro auxiliar por monto, fecha y
      referencia; deja solo las partidas que no cuadran.
- [ ] **Comparador de cotizaciones** — homologa precio unitario, flete, IVA, plazo de pago
      y tiempo de entrega entre proveedores.
- [ ] **Analizador de gasto de compras** — Pareto de proveedores, variación de precios
      por artículo, alertas de alza no detectada.
- [ ] **Scorecard de proveedores** — cumplimiento de entregas, calidad, precio vs. histórico.
- [ ] **Control de vencimientos** — obligaciones financieras, pólizas, contratos.

### Fase 4 — Integración
- [ ] **Centro de Control** — tablero único con los indicadores de las tres áreas
      y generación del informe mensual para gerencia.

---

## División de herramientas

| Dónde | Para qué |
|---|---|
| **Claude Code** (este repositorio) | Construir y mantener las herramientas |
| **Claude / Cowork** (chat) | Uso diario: subir exports, pedir análisis, redactar correos |

---

## Pendientes administrativos

- [ ] Solicitar a TI la autorización de los conectores de **Gmail** y **Google Drive**
      para Claude en el Workspace corporativo.
- [ ] Definir si se conecta el buzón personal o el buzón compartido del área.
      **Recomendación: el personal**, para no exponer correspondencia de terceros.
