"""
Gera as LPs em arquivo único, com as imagens embutidas no próprio arquivo. Útil para enviar,
publicar ou abrir as páginas sem a pasta assets/.

  index.html               -> dist/lp-completa.html     (Vero Consórcios)
  planejamento/index.html  -> dist/lp-planejamento.html (Vero Planejamento)

No arquivo único de consórcios, o menu Ecossistema passa a abrir dist/lp-planejamento.html.
O vídeo de fundo da LP de planejamento (planejamento/assets/video/familia.mp4) é embutido
quando existe e tem até 8 MB; acima disso, publique o vídeo junto com o arquivo.

Uso:
    python3 tools/gerar-html-completo.py
"""
import base64
import pathlib
import re

RAIZ = pathlib.Path(__file__).resolve().parent.parent
TIPOS = {'.webp': 'image/webp', '.png': 'image/png', '.jpg': 'image/jpeg', '.mp4': 'video/mp4'}
LIMITE_VIDEO = 8 * 1024 * 1024


def gerar(origem, destino, trocas=()):
    base = origem.parent
    html = origem.read_text(encoding='utf-8')
    avisos = []

    def embutir(m):
        caminho = base / m.group(2)
        if not caminho.exists():  # exemplos citados em comentários do HTML, ou vídeo ainda não enviado
            if caminho.suffix == '.mp4':
                avisos.append(f'vídeo não encontrado: {caminho.relative_to(RAIZ)}')
            return m.group(0)
        if caminho.suffix == '.mp4' and caminho.stat().st_size > LIMITE_VIDEO:
            avisos.append(f'vídeo com mais de 8 MB: publique {m.group(2)} junto com o arquivo')
            return m.group(0)
        dados = base64.b64encode(caminho.read_bytes()).decode('ascii')
        return f'{m.group(1)}="data:{TIPOS[caminho.suffix]};base64,{dados}"'

    html, n = re.subn(r'(src|href|poster)="(assets/(?:img|video)/(?:[a-z0-9-]+/)?[a-z0-9-]+\.(?:png|webp|jpg|mp4))"', embutir, html)
    # a fonte Famels só é usada se estiver instalada no computador
    html = html.replace(',url("assets/fonts/Famels-Regular.woff2") format("woff2")', '')
    html = html.replace(',url("assets/fonts/Famels-Italic.woff2") format("woff2")', '')
    for a, b in trocas:
        html = html.replace(a, b)

    destino.parent.mkdir(exist_ok=True)
    destino.write_text(html, encoding='utf-8')
    print(f'{destino.relative_to(RAIZ)}: {n} arquivos embutidos, {destino.stat().st_size / 1024:.0f} KB')
    for a in avisos:
        print('  aviso:', a)


gerar(RAIZ / 'index.html', RAIZ / 'dist' / 'lp-completa.html',
      trocas=[('href="planejamento/index.html"', 'href="lp-planejamento.html"')])
gerar(RAIZ / 'planejamento' / 'index.html', RAIZ / 'dist' / 'lp-planejamento.html')
