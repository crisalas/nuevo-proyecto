#!/bin/sh
# Construye las dos salidas a partir de src/app.core.html:
#
#   src/analizador-cartera.body.html  -> lo que se publica como enlace compartible
#   herramientas/analizador-cartera.html -> el archivo autónomo para el disco
#
# Ambas llevan incrustada una copia del propio código en base64. Eso es lo que
# le permite a la página volver a publicarse con los datos del corte dentro,
# para que quien abra el enlace vea el informe completo y pueda navegarlo.
set -e
CORE=src/app.core.html
mkdir -p herramientas src

B64=$(base64 -w0 < "$CORE")
FUENTE="<script type=\"text/plain\" id=\"fuente\">$B64</script>"

{ cat "$CORE"; printf '\n%s\n' "$FUENTE"; } > src/analizador-cartera.body.html

{
  printf '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
  printf '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
  printf '<style>html{color-scheme:light dark}body{margin:0}img{max-width:100%%}[hidden]{display:none!important}</style>\n'
  printf '</head>\n<body>\n'
  cat src/analizador-cartera.body.html
  printf '\n</body>\n</html>\n'
} > herramientas/analizador-cartera.html

echo "publicable: src/analizador-cartera.body.html ($(wc -c < src/analizador-cartera.body.html) bytes)"
echo "autónomo:   herramientas/analizador-cartera.html ($(wc -c < herramientas/analizador-cartera.html) bytes)"
