#!/bin/sh
# Genera el archivo autonomo que se abre directamente en el navegador.
# La fuente (src/*.body.html) es el cuerpo de la pagina; aqui se le agrega
# el esqueleto HTML que el navegador necesita al abrirla desde el disco.
set -e
OUT=herramientas/analizador-cartera.html
mkdir -p herramientas
{
  printf '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
  printf '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
  printf '<style>html{color-scheme:light dark}body{margin:0}img{max-width:100%%}[hidden]{display:none!important}</style>\n'
  printf '</head>\n<body>\n'
  cat src/analizador-cartera.body.html
  printf '\n</body>\n</html>\n'
} > "$OUT"
echo "generado: $OUT  ($(wc -c < "$OUT") bytes)"
