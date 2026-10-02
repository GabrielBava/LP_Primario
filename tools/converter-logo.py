"""
Converte o logo de uma administradora para o padrão da faixa "Administradoras parceiras":
uma única cor clara (Névoa #E0E1DD) com fundo transparente, recortado e com 160 px de altura.

Uso:
    pip install pillow
    python3 tools/converter-logo.py caminho/do/logo-original.png assets/img/adm/nome.png [limiar]

limiar (opcional, padrão 0.05): quanto um pixel precisa se afastar do fundo para virar logo.
Use 0.12 quando o arquivo traz um fundo cinza-claro ou o quadriculado de "transparência"
gravado na imagem (ex.: CNP, Mapfre).

Depois, adicione na faixa do index.html:
    <img class="adm-logo" src="assets/img/adm/nome.png" alt="Nome da Administradora"
         width="L" height="H" style="--h:Hpx" decoding="async">
(H entre 28 e 50 px: logos de uma linha só ficam menores; logos empilhados, maiores.)
"""
import sys
from PIL import Image

MIST = (224, 225, 221)  # Névoa (identidade visual)


def converter(entrada, saida, limiar=0.05, altura=160):
    im = Image.open(entrada).convert('RGBA')
    fundo = Image.new('RGBA', im.size, (255, 255, 255, 255))
    fundo.alpha_composite(im)
    px = fundo.convert('RGB').load()
    w, h = fundo.size
    # cor de fundo = média dos quatro cantos
    cantos = [px[2, 2], px[w - 3, 2], px[2, h - 3], px[w - 3, h - 3]]
    bg = [sum(c[i] for c in cantos) / 4 for i in range(3)]
    out = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    op = out.load()
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            d = max(abs(bg[0] - r), abs(bg[1] - g), abs(bg[2] - b)) / 255.0
            a = min(1.0, max(0.0, (d - limiar) / 0.25))  # tinta vira Névoa; fundo vira transparente
            if a > 0:
                op[x, y] = MIST + (round(a * 255),)
    out = out.crop(out.getbbox())
    largura = round(out.width * altura / out.height)
    out.resize((largura, altura), Image.LANCZOS).save(saida, optimize=True)
    print(f'{saida}: {largura}x{altura} (proporção {largura / altura:.2f})')


if __name__ == '__main__':
    if len(sys.argv) not in (3, 4):
        sys.exit(__doc__)
    converter(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) == 4 else 0.05)
