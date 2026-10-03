"""Estilo de marca de la tienda de planos (byignis.shop): Barlow, tinta, arena y ladrillo."""
import os, re, html

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS_CSS = os.path.join(HERE, '..', 'fonts.css')
T = dict(ink='#211F1C', ember='#D1542A', ember_dark='#B54420', sand='#F7F3EE', line='#E3DCD2', muted='#6B645C', line_dark='#3B3732', muted_dark='#C9C2B8')

def e(s):
    return html.escape(str(s))

def fuentes():
    css = open(FONTS_CSS).read()
    base = 'file://' + os.path.abspath(os.path.join(HERE, '..'))
    return re.sub(r'url\(f/', f'url({base}/f/', css)

def css_base():
    return fuentes() + f"""
@page {{ size: A4; margin: 0 }}
* {{ box-sizing: border-box; margin: 0; padding: 0 }}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact }}
body {{ font-family: Barlow, sans-serif; color: {T['ink']}; font-size: 10.8pt; line-height: 1.5 }}
h1, h2, h3, .cond {{ font-family: 'Barlow Condensed', sans-serif; font-weight: 700; line-height: 1.02; letter-spacing: -.2px }}
h1 {{ font-size: 54pt }} h2 {{ font-size: 30pt }} h3 {{ font-size: 17pt }}
h4 {{ font-size: 10.5pt; font-weight: 700; text-transform: uppercase; letter-spacing: 1.4px; color: {T['ember']}; margin-bottom: 2mm }}
.pag {{ width: 210mm; height: 297mm; position: relative; overflow: hidden; page-break-after: always; background: #fff; padding: 18mm 18mm 18mm }}
.pag.oscura {{ background: {T['ink']}; color: #fff }}
.pag.arena {{ background: {T['sand']} }}
.kicker {{ font-size: 9pt; font-weight: 700; letter-spacing: 2.4px; text-transform: uppercase; color: {T['ember']} }}
.pag.oscura .kicker {{ color: {T['ember']} }}
.lead {{ font-size: 13pt; color: {T['muted']}; line-height: 1.45 }}
.pag.oscura .lead {{ color: {T['muted_dark']} }}
.chip {{ display: inline-block; border: 1.4px solid {T['line']}; border-radius: 99px; padding: 1mm 3.4mm; font-size: 8.8pt; font-weight: 600 }}
.chip.on {{ background: {T['ember']}; border-color: {T['ember']}; color: #fff }}
.pag.oscura .chip {{ border-color: {T['line_dark']} }}
.caja {{ background: {T['sand']}; border-radius: 4mm; padding: 5mm 6mm }}
.caja.borde {{ background: #fff; border: 1.4px solid {T['line']} }}
.caja.ember {{ background: {T['ember']}; color: #fff }}
ul.lista {{ list-style: none }}
ul.lista li {{ position: relative; padding-left: 6mm; margin: 1.6mm 0 }}
ul.lista li::before {{ content: ''; position: absolute; left: 0; top: 2.2mm; width: 2.6mm; height: 2.6mm; background: {T['ember']}; transform: rotate(45deg) }}
ol.pasos {{ list-style: none; counter-reset: p }}
ol.pasos li {{ counter-increment: p; position: relative; padding-left: 9mm; margin: 2mm 0 }}
ol.pasos li::before {{ content: counter(p); position: absolute; left: 0; top: 0; width: 6mm; height: 6mm; background: {T['ember']}; color: #fff; font-weight: 700; font-size: 9pt; display: grid; place-items: center; border-radius: 1.4mm }}
.grid2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 6mm }}
.grid3 {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 5mm }}
.pie {{ position: absolute; bottom: 8mm; left: 18mm; right: 18mm; display: flex; justify-content: space-between; font-size: 8pt; color: {T['muted']}; font-weight: 600; letter-spacing: .4px }}
.pag.oscura .pie {{ color: {T['muted_dark']} }}
.nota {{ font-size: 8.8pt; color: {T['muted']} }}
table.t {{ width: 100%; border-collapse: collapse; font-size: 9.8pt }}
table.t th {{ background: {T['ink']}; color: #fff; text-align: left; padding: 2.2mm 3mm; font-weight: 600 }}
table.t td {{ border-bottom: 1px solid {T['line']}; padding: 2.4mm 3mm }}
"""

def pie(marca, n):
    return f'<div class="pie"><span>byignis · {e(marca)}</span><span>{n}</span></div>'
