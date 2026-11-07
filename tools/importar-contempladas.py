"""
Importa o estoque de cartas contempladas do parceiro (planilha .xlsx ou .csv) para a LP de consórcios.

Uso:
    python3 tools/importar-contempladas.py estoque.xlsx        (precisa de: pip install openpyxl)
    python3 tools/importar-contempladas.py estoque.csv

A planilha precisa ter uma linha de cabeçalho com estas colunas (a ordem não importa e os nomes
aceitam variações comuns, com ou sem acento):
    Segmento   Imóvel / Veículo / Pesados (também aceita Imovel, Auto, Carro, Moto, Caminhão...)
    ADM        nome da administradora (também aceita "Administradora")
    Crédito    valor da carta (também aceita "Valor do crédito", "Carta")
    Entrada    valor de entrada
    Parcela    valor da parcela
    Prazo      parcelas restantes (também aceita "Parcelas", "Meses", "Prazo restante")
Valores podem vir como número ou texto ("R$ 300.000,00"). Linhas incompletas são ignoradas.

O script reescreve o trecho entre CONTEMPLADAS:INICIO e CONTEMPLADAS:FIM no index.html,
marca o estoque como real (exemplo: false) e mostra um resumo. Depois, gere os arquivos
únicos com:  python3 tools/gerar-html-completo.py
"""
import csv
import json
import pathlib
import re
import sys
import unicodedata

RAIZ = pathlib.Path(__file__).resolve().parent.parent
INDEX = RAIZ / 'index.html'


def norm(t):
    t = unicodedata.normalize('NFKD', str(t or '')).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9%]+', ' ', t).strip()


COLUNAS = {
    'segmento': ['segmento', 'tipo', 'categoria', 'bem', 'tipo de bem'],
    'adm': ['adm', 'administradora', 'admin', 'administradora do grupo'],
    'credito': ['credito', 'valor do credito', 'valor credito', 'carta', 'valor da carta', 'credito r'],
    'entrada': ['entrada', 'valor de entrada', 'valor entrada', 'agio', 'entrada r'],
    'parcela': ['parcela', 'valor da parcela', 'valor parcela', 'parcela r'],
    'prazo': ['prazo', 'parcelas', 'meses', 'prazo restante', 'parcelas restantes', 'qtd parcelas', 'n parcelas'],
}
SEGMENTOS = {
    'imovel': ['imovel', 'imoveis', 'imobiliario', 'casa', 'apartamento'],
    'veiculo': ['veiculo', 'veiculos', 'auto', 'automovel', 'automoveis', 'carro', 'carros', 'moto', 'motos', 'leves'],
    'pesados': ['pesado', 'pesados', 'caminhao', 'caminhoes', 'maquina', 'maquinas', 'agricola', 'onibus'],
}


def numero(v):
    if v is None or v == '':
        return None
    if isinstance(v, (int, float)):
        return float(v)
    t = re.sub(r'[^0-9,.\-]', '', str(v))
    if not t:
        return None
    if ',' in t:                       # padrão brasileiro: 300.000,00
        t = t.replace('.', '').replace(',', '.')
    elif t.count('.') > 1 or re.search(r'\.\d{3}$', t):
        t = t.replace('.', '')         # 300.000 sem centavos
    try:
        return float(t)
    except ValueError:
        return None


def segmento(v):
    n = norm(v)
    for chave, nomes in SEGMENTOS.items():
        if any(n == x or n.startswith(x) for x in nomes):
            return chave
    return None


def ler(caminho):
    if caminho.suffix.lower() in ('.xlsx', '.xlsm'):
        try:
            import openpyxl
        except ImportError:
            sys.exit('Para ler .xlsx, instale o openpyxl:  pip install openpyxl   (ou salve a planilha como .csv)')
        wb = openpyxl.load_workbook(caminho, data_only=True, read_only=True)
        linhas = []
        for ws in wb.worksheets:
            linhas += [list(r) for r in ws.iter_rows(values_only=True)]
        return linhas
    texto = caminho.read_text(encoding='utf-8-sig', errors='replace')
    dialeto = csv.Sniffer().sniff(texto[:4096], delimiters=';,\t')
    return [r for r in csv.reader(texto.splitlines(), dialeto)]


def mapear(cab):
    idx = {}
    for i, c in enumerate(cab):
        n = norm(c)
        for chave, nomes in COLUNAS.items():
            if chave not in idx and n in nomes:
                idx[chave] = i
    return idx


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    linhas = ler(pathlib.Path(sys.argv[1]))
    estoque, idx, ignoradas, seg_atual = [], None, 0, None
    for r in linhas:
        if not r or all(v in (None, '') for v in r):
            continue
        m = mapear(r)
        if len(m) >= 4 and 'credito' in m:          # linha de cabeçalho (pode haver uma por aba ou por bloco)
            idx = m
            continue
        if idx is None:
            # título de bloco com o segmento (ex.: "IMÓVEIS") antes do cabeçalho
            s = segmento(next((v for v in r if v not in (None, '')), ''))
            seg_atual = s or seg_atual
            continue
        g = lambda k: r[idx[k]] if k in idx and idx[k] < len(r) else None
        seg = segmento(g('segmento')) if 'segmento' in idx else seg_atual
        if seg is None and len([v for v in r if v not in (None, '')]) == 1:
            seg_atual = segmento(next(v for v in r if v not in (None, ''))) or seg_atual
            continue
        item = {'segmento': seg, 'adm': str(g('adm') or '').strip(), 'credito': numero(g('credito')),
                'entrada': numero(g('entrada')), 'parcela': numero(g('parcela')), 'prazo': numero(g('prazo'))}
        if not item['segmento'] or not item['adm'] or not all(item[k] for k in ('credito', 'entrada', 'parcela', 'prazo')):
            ignoradas += 1
            continue
        for k in ('credito', 'entrada', 'parcela', 'prazo'):
            item[k] = int(round(item[k]))
        estoque.append(item)

    if not estoque:
        sys.exit('Nenhuma carta encontrada. Confira se a planilha tem as colunas Segmento, ADM, Crédito, Entrada, Parcela e Prazo.')

    corpo = ',\n'.join('    { segmento: %s, adm: %s, credito: %d, entrada: %d, parcela: %d, prazo: %d }' % (
        json.dumps(c['segmento']), json.dumps(c['adm'], ensure_ascii=False), c['credito'], c['entrada'], c['parcela'], c['prazo'])
        for c in estoque)
    html = INDEX.read_text(encoding='utf-8')
    ini, fim = '/* CONTEMPLADAS:INICIO */', '/* CONTEMPLADAS:FIM */'
    a, b = html.index(ini) + len(ini), html.index(fim)
    por_seg = re.search(r'porSegmento:\s*(\d+)', html[a:b])
    bloco = '''
  contempladas: {
    exemplo: false,  // estoque importado de %s
    porSegmento: %s,
    estoque: [
%s
    ]
  },
  ''' % (pathlib.Path(sys.argv[1]).name, por_seg.group(1) if por_seg else '8', corpo)
    INDEX.write_text(html[:a] + bloco + html[b:], encoding='utf-8')

    print(f'{len(estoque)} cartas importadas para o index.html ({ignoradas} linhas ignoradas).')
    for s in SEGMENTOS:
        n = sum(1 for c in estoque if c['segmento'] == s)
        if n:
            print(f'  {s}: {n} cartas' + (' (rodízio diário de 8 em 8)' if n > 8 else ''))
    print('Agora rode:  python3 tools/gerar-html-completo.py')


if __name__ == '__main__':
    main()
