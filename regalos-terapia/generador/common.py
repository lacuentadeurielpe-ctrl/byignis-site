"""Base compartida de los ebooks Byignis: estilos de marca, íconos SVG y render a PDF."""
import html, os, subprocess, json

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, 'node_modules/@fontsource/nunito-sans/files')

# Paleta de la marca (tomada del ebook "300 Actividades de Terapia Ocupacional Infantil")
C = {
    'crema': '#FAF6F0', 'tinta': '#1F2433', 'gris': '#5A6070', 'linea': '#E7E0D6',
    'morado': '#7B5EA7', 'azul': '#3F7CC4', 'naranja': '#E07B3C', 'verde': '#4A9A3D',
    'rosa': '#D9517A', 'turquesa': '#2A9D8F', 'mostaza': '#C9971B', 'rojo': '#E05A47',
}

def e(s):
    return html.escape(str(s))

def font_face():
    out = []
    for w in (400, 600, 700, 800, 900):
        out.append(f"@font-face{{font-family:'NS';font-weight:{w};src:url('file://{FONTS}/nunito-sans-latin-{w}-normal.woff2') format('woff2')}}")
    return '\n'.join(out)

def base_css(acento, acento_suave):
    return font_face() + f"""
@page {{ size: A4; margin: 0 }}
* {{ box-sizing: border-box; margin: 0; padding: 0 }}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact }}
body {{ font-family: 'NS', sans-serif; color: {C['tinta']}; font-size: 10.5pt; line-height: 1.5 }}
.pag {{ width: 210mm; height: 297mm; position: relative; overflow: hidden; page-break-after: always; background: #fff; padding: 20mm 18mm 18mm }}
.pag.crema {{ background: {C['crema']} }}
.pag.color {{ background: {acento}; color: #fff }}
.pie {{ position: absolute; bottom: 9mm; left: 18mm; right: 18mm; display: flex; justify-content: space-between; font-size: 8pt; color: {C['gris']}; font-weight: 700; letter-spacing: .4px }}
.pag.color .pie {{ color: rgba(255,255,255,.75) }}
.kicker {{ font-size: 9pt; font-weight: 800; letter-spacing: 2.4px; text-transform: uppercase; color: {acento} }}
.pag.color .kicker {{ color: rgba(255,255,255,.85) }}
h1 {{ font-size: 40pt; line-height: 1.04; font-weight: 900; letter-spacing: -.5px }}
h2 {{ font-size: 24pt; line-height: 1.1; font-weight: 900; letter-spacing: -.3px }}
h3 {{ font-size: 14pt; line-height: 1.2; font-weight: 800 }}
h4 {{ font-size: 10.5pt; font-weight: 800; margin-bottom: 2mm }}
p + p {{ margin-top: 2.5mm }}
.lead {{ font-size: 13pt; color: {C['gris']}; line-height: 1.45 }}
.pag.color .lead {{ color: rgba(255,255,255,.9) }}
.chip {{ display: inline-block; background: {acento}; color: #fff; font-weight: 800; font-size: 8.5pt; padding: 1.2mm 3.6mm; border-radius: 99px }}
.chip.suave {{ background: {acento_suave}; color: {acento} }}
.caja {{ background: {C['crema']}; border-radius: 4mm; padding: 5mm 6mm }}
.caja.borde {{ background: #fff; border: 1.4px solid {C['linea']} }}
.caja.acento {{ background: {acento_suave} }}
ul.lista {{ list-style: none }}
ul.lista li {{ position: relative; padding-left: 6mm; margin: 1.2mm 0 }}
ul.lista li::before {{ content: ''; position: absolute; left: 0; top: 2.1mm; width: 2.4mm; height: 2.4mm; border-radius: 50%; background: {acento} }}
ol.pasos {{ list-style: none; counter-reset: p }}
ol.pasos li {{ counter-increment: p; position: relative; padding-left: 8mm; margin: 1.6mm 0 }}
ol.pasos li::before {{ content: counter(p); position: absolute; left: 0; top: .2mm; width: 5.4mm; height: 5.4mm; border-radius: 50%; background: {acento}; color: #fff; font-weight: 800; font-size: 8pt; display: grid; place-items: center }}
.grid2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 5mm }}
.grid3 {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4mm }}
.check {{ display: inline-block; width: 4.2mm; height: 4.2mm; border: 1.6px solid {C['tinta']}; border-radius: 1mm; vertical-align: -0.8mm; margin-right: 1.6mm }}
.nota {{ font-size: 8.5pt; color: {C['gris']} }}
table.reg {{ width: 100%; border-collapse: collapse; font-size: 9pt }}
table.reg th {{ background: {acento}; color: #fff; font-weight: 800; padding: 2mm; text-align: left }}
table.reg td {{ border: 1px solid {C['linea']}; padding: 2.4mm 2mm; height: 10mm }}
"""

def pie(marca, pagina_txt):
    return f'<div class="pie"><span>Byignis · {e(marca)}</span><span>{e(pagina_txt)}</span></div>'

def render_pdf(html_path, pdf_path):
    js = f"""
import {{ chromium }} from '/opt/node-tools/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://{html_path}', {{ waitUntil: 'load' }});
await p.evaluate(() => document.fonts.ready);
await p.pdf({{ path: '{pdf_path}', format: 'A4', printBackground: true, preferCSSPageSize: true }});
await b.close();
"""
    tmp = os.path.join(HERE, '_render.mjs')
    open(tmp, 'w').write(js)
    subprocess.run(['node', tmp], check=True)

def snapshot(html_path, png_prefix, paginas):
    """Captura PNG de algunas páginas para revisar el diseño."""
    js = f"""
import {{ chromium }} from '/opt/node-tools/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage({{ viewport: {{ width: 794, height: 1123 }} }});
await p.goto('file://{html_path}', {{ waitUntil: 'load' }});
await p.evaluate(() => document.fonts.ready);
const pags = await p.$$('.pag');
for (const i of {json.dumps(paginas)}) {{ if (pags[i]) await pags[i].screenshot({{ path: '{png_prefix}-' + i + '.png' }}); }}
console.log('paginas', pags.length);
await b.close();
"""
    tmp = os.path.join(HERE, '_snap.mjs')
    open(tmp, 'w').write(js)
    subprocess.run(['node', tmp], check=True)
