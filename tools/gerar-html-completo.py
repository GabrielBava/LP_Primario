"""
Gera um HTML completo em arquivo único (dist/lp-completa.html), com os logos das
administradoras embutidos no próprio arquivo. Útil para enviar, publicar ou abrir a
página sem a pasta assets/.

Uso:
    python3 tools/gerar-html-completo.py
"""
import base64
import pathlib
import re

RAIZ = pathlib.Path(__file__).resolve().parent.parent
html = (RAIZ / 'index.html').read_text(encoding='utf-8')


def embutir(m):
    caminho = RAIZ / m.group(1)
    dados = base64.b64encode(caminho.read_bytes()).decode('ascii')
    return f'src="data:image/png;base64,{dados}"'


html, n = re.subn(r'src="(assets/img/adm/[a-z0-9-]+\.png)"', embutir, html)
# a fonte Famels só é usada se estiver instalada no computador
html = html.replace(',url("assets/fonts/Famels-Regular.woff2") format("woff2")', '')
html = html.replace(',url("assets/fonts/Famels-Italic.woff2") format("woff2")', '')

saida = RAIZ / 'dist' / 'lp-completa.html'
saida.parent.mkdir(exist_ok=True)
saida.write_text(html, encoding='utf-8')
print(f'{saida.relative_to(RAIZ)}: {n} logos embutidos, {saida.stat().st_size / 1024:.0f} KB')
