#!/bin/sh
# Construye las herramientas a partir de los fuentes en src/.
#
#   src/app.core.html   -> Analizador de Cartera
#   src/flujo.core.html -> Flujo de Caja 13 Semanas
#
# De cada uno salen dos versiones: la publicable (cuerpo de la página, que se
# sube como enlace) y la autónoma (con el esqueleto HTML, para abrir desde el
# disco). El Analizador lleva además una copia de su propio código en base64,
# que es lo que le permite publicarse con los datos del corte dentro.
set -e
mkdir -p herramientas src

esqueleto() {
  printf '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
  printf '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
  printf '<style>html{color-scheme:light dark}body{margin:0}img{max-width:100%%}[hidden]{display:none!important}</style>\n'
  printf '</head>\n<body>\n'
  cat "$1"
  printf '\n</body>\n</html>\n'
}

# --- Analizador de Cartera (se autopublica: necesita su fuente incrustada) ---
B64=$(base64 -w0 < src/app.core.html)
{ cat src/app.core.html; printf '\n<script type="text/plain" id="fuente">%s</script>\n' "$B64"; } \
  > src/analizador-cartera.body.html
esqueleto src/analizador-cartera.body.html > herramientas/analizador-cartera.html

# --- Flujo de Caja ---
cp src/flujo.core.html src/flujo-de-caja.body.html
esqueleto src/flujo-de-caja.body.html > herramientas/flujo-de-caja.html

for f in herramientas/analizador-cartera.html herramientas/flujo-de-caja.html; do
  echo "$f  ($(wc -c < "$f") bytes)"
done
