#!/usr/bin/env python3
"""Cifra el tablero de cobro con una clave y arma la página de acceso.

Uso:  python3 -I herramientas/cifrar_tablero.py tablero.html docs/index.html "clave"

El repositorio es público: aquí solo se guarda el tablero CIFRADO (AES-256-GCM,
clave derivada con PBKDF2-SHA256). La página pide la clave y descifra en el
navegador; sin la clave solo se ve la pantalla de acceso. Nunca subir al
repositorio el tablero sin cifrar ni la clave.
"""
import base64, os, sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

ITER = 600000

PAGINA = r'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<title>Tablero de Cobro Campofértil</title>
<style>
:root{--bg:#f4f6f5;--card:#fff;--tx:#1d2b26;--mut:#5d6b66;--ac:#1f6f50;--bd:#d5ddd9;--er:#b3261e}
@media(prefers-color-scheme:dark){:root{--bg:#121917;--card:#1b2420;--tx:#e8efec;--mut:#9fb0a9;--ac:#4fbf92;--bd:#2e3b36;--er:#ff8a80}}
*{box-sizing:border-box}
body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;background:var(--bg);color:var(--tx);font:16px/1.4 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;padding:16px}
.c{background:var(--card);border:1px solid var(--bd);border-radius:14px;padding:28px 24px;width:100%;max-width:380px}
h1{font-size:20px;margin:0 0 4px}
p{margin:0 0 18px;color:var(--mut);font-size:14px}
input[type=password],input[type=text]{width:100%;padding:12px;border:1px solid var(--bd);border-radius:10px;font-size:16px;background:var(--bg);color:var(--tx)}
button{width:100%;margin-top:12px;padding:12px;border:0;border-radius:10px;background:var(--ac);color:#fff;font-size:16px;font-weight:600;cursor:pointer}
button:disabled{opacity:.6}
label{display:flex;gap:8px;align-items:center;margin-top:12px;font-size:14px;color:var(--mut)}
#e{color:var(--er);font-size:14px;margin-top:10px;min-height:1.2em}
</style>
</head>
<body>
<form class="c" id="f" autocomplete="on">
<h1>Tablero de Cobro</h1>
<p>Comercializadora Campofértil S.A.S. Escriba la clave de acceso.</p>
<input type="password" id="k" placeholder="Clave" autocomplete="current-password" autocapitalize="none" autocorrect="off" spellcheck="false" autofocus>
<label><input type="checkbox" id="r" checked> Recordar en este dispositivo</label>
<button id="b" type="submit">Entrar</button>
<div id="e" role="alert"></div>
</form>
<script>
var BLOB="__BLOB__",ITER=__ITER__,LS="tablero_clave";
function b64(s){var b=atob(s),u=new Uint8Array(b.length);for(var i=0;i<b.length;i++)u[i]=b.charCodeAt(i);return u}
async function abrir(clave){
  var d=b64(BLOB),salt=d.slice(0,16),iv=d.slice(16,28),ct=d.slice(28);
  var m=await crypto.subtle.importKey("raw",new TextEncoder().encode(clave),"PBKDF2",false,["deriveKey"]);
  var k=await crypto.subtle.deriveKey({name:"PBKDF2",salt:salt,iterations:ITER,hash:"SHA-256"},m,{name:"AES-GCM",length:256},false,["decrypt"]);
  var pt=await crypto.subtle.decrypt({name:"AES-GCM",iv:iv},k,ct);
  return new TextDecoder().decode(pt);
}
function mostrar(html){document.open();document.write(html);document.close()}
async function entrar(clave,recordar,auto){
  var e=document.getElementById("e"),b=document.getElementById("b");
  e.textContent="";b.disabled=true;b.textContent="Abriendo...";
  try{
    var html=await abrir(clave);
    if(recordar){try{localStorage.setItem(LS,clave)}catch(x){}}
    mostrar(html);
  }catch(x){
    b.disabled=false;b.textContent="Entrar";
    if(auto){try{localStorage.removeItem(LS)}catch(y){}}
    else e.textContent=window.crypto&&crypto.subtle?"Clave incorrecta. Revise e intente de nuevo.":"Este navegador no permite abrirlo. Use Chrome o Safari.";
  }
}
document.getElementById("f").addEventListener("submit",function(ev){
  ev.preventDefault();
  var v=document.getElementById("k").value.trim();
  if(v)entrar(v,document.getElementById("r").checked,false);
});
(function(){var g=null;try{g=localStorage.getItem(LS)}catch(x){}if(g)entrar(g,true,true)})();
</script>
</body>
</html>
'''


def main():
    ent, sal, clave = sys.argv[1], sys.argv[2], sys.argv[3]
    datos = open(ent, 'rb').read()
    salt, iv = os.urandom(16), os.urandom(12)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITER)
    llave = kdf.derive(clave.encode('utf-8'))
    ct = AESGCM(llave).encrypt(iv, datos, None)
    blob = base64.b64encode(salt + iv + ct).decode()
    open(sal, 'w', encoding='utf-8').write(
        PAGINA.replace('__BLOB__', blob).replace('__ITER__', str(ITER)))
    print('listo', sal, len(blob), 'bytes cifrados (base64)')


if __name__ == '__main__':
    main()
