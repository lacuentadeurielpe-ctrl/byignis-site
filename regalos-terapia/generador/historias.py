"""50 Historias sociales ilustradas — Byignis."""
import os
from common import C, e, base_css, pie, render_pdf, snapshot
from iconos2 import ic
from historias_data import H, CATS

AC = C['morado']; AC_S = '#ECE5F5'
MARCA = '50 Historias sociales'
COLCAT = {'salud': C['turquesa'], 'colegio': C['mostaza'], 'emociones': C['rosa'], 'amigos': C['azul'], 'casa': C['verde'], 'salidas': C['naranja']}

def main():
    css = base_css(AC, AC_S) + f"""
.portada {{ background: {C['crema']}; padding: 30mm 22mm }}
.portada h1 {{ font-size: 48pt; margin: 8mm 0 6mm }}
.hist-head {{ display: flex; justify-content: space-between; align-items: flex-end; gap: 6mm }}
.hist-head h2 {{ font-size: 26pt; margin-top: 2mm }}
.duenio {{ font-size: 9pt; color: {C['gris']}; white-space: nowrap; border-bottom: 1.4px solid {C['linea']}; padding-bottom: 1mm; min-width: 52mm }}
.vinetas {{ display: grid; grid-template-columns: 1fr 1fr; grid-auto-rows: 1fr; gap: 5mm; margin-top: 7mm; height: 202mm }}
.cuento {{ display: grid; grid-template-columns: 1fr; grid-auto-rows: 1fr; gap: 3mm; margin-top: 6mm; height: 204mm }}
.cuento .vin {{ grid-template-columns: 19mm 1fr; min-height: 0; padding: 0 6mm 0 2.4mm; gap: 5mm; border-radius: 4mm }}
.cuento .vin .pic {{ width: 19mm; height: 19mm; padding: 1.6mm }}
.cuento .vin .tx {{ font-size: 13pt; font-weight: 600; line-height: 1.38 }}
.vin {{ display: grid; grid-template-columns: 34mm 1fr; gap: 4mm; align-items: center; border: 1.6px solid {C['linea']}; border-radius: 5mm; padding: 4mm 5mm 4mm 4mm; min-height: 46mm; position: relative; background: #fff }}
.vin .pic {{ width: 34mm; height: 34mm; background: {C['crema']}; border-radius: 4mm; padding: 2.6mm }}
.vin .tx {{ font-size: 12.5pt; font-weight: 700; line-height: 1.35 }}
.vin .n {{ position: absolute; top: -2.6mm; left: -2.2mm; width: 7mm; height: 7mm; border-radius: 50%; color: #fff; font-weight: 900; font-size: 9pt; display: grid; place-items: center }}
.vin.fin {{ grid-column: 1 / -1 }}
.nota-adulto {{ position: absolute; left: 18mm; right: 18mm; bottom: 20mm; background: {C['crema']}; border-radius: 4mm; padding: 4mm 6mm; font-size: 9.6pt; border-left: 2.4mm solid }}
.nota-adulto b {{ display: block; font-size: 8.4pt; letter-spacing: 1.6px; text-transform: uppercase; margin-bottom: .8mm }}
.divisor {{ position: absolute; left: 22mm; right: 22mm; top: 50mm }}
.divisor h2 {{ font-size: 40pt; margin: 6mm 0 }}
.div-ic {{ width: 48mm; height: 48mm; background: #fff; border-radius: 10mm; padding: 6mm; margin-top: 10mm }}
.div-lista {{ margin-top: 9mm; columns: 2; column-gap: 8mm; font-weight: 700; font-size: 11.5pt }}
.div-lista div {{ break-inside: avoid; padding: 1.4mm 0; border-bottom: 1px solid rgba(255,255,255,.3) }}
.grande {{ position: absolute; right: 16mm; bottom: 20mm; font-size: 200pt; font-weight: 900; color: rgba(255,255,255,.2); line-height: 1; letter-spacing: -6px }}
.indice {{ columns: 2; column-gap: 10mm; margin-top: 6mm }}
.indice h4 {{ break-after: avoid; margin-top: 4mm; padding: 1.4mm 3mm; border-radius: 2mm; color: #fff; font-size: 9.6pt }}
.indice div {{ display: flex; justify-content: space-between; font-size: 10pt; padding: 1mm 0; border-bottom: 1px dotted {C['linea']}; break-inside: avoid }}
.blanco .pic {{ background: #fff; border: 1.6px dashed {C['linea']} }}
.blanco .tx {{ border-bottom: 1.4px solid {C['linea']}; height: 24mm }}
"""
    pags = []; num = [0]
    def pag(body, cls=''):
        num[0] += 1
        pags.append(f'<section class="pag {cls}">{body}{pie(MARCA, str(num[0])) if num[0] > 1 else ""}</section>')

    orden = list(CATS)
    historias = sorted(H, key=lambda h: orden.index(h[0]))
    n_hist = {id(h): i for i, h in enumerate(historias, 1)}

    portada_ic = ''.join(f'<div style="width:34mm;height:34mm;background:#fff;border-radius:8mm;padding:4mm;box-shadow:0 3mm 8mm rgba(31,36,51,.08)">{ic(x)}</div>' for x in ['escuela', 'feliz', 'doctor', 'amigos', 'avion', 'pastel'])
    pag(f'''<div class="kicker">Material para casa, aula y terapia</div>
<h1>50 Historias<br>sociales</h1>
<p class="lead" style="max-width:150mm">Cuentos ilustrados que preparan al niño para situaciones nuevas o difíciles: el médico, el colegio, las emociones, los amigos y las salidas. Ideal para niños con TEA, TDAH y dificultades de comunicación.</p>
<div style="display:flex;gap:3mm;margin-top:8mm;flex-wrap:wrap">{''.join(f'<span class="chip" style="background:{COLCAT[k]}">{v[0]}</span>' for k, v in CATS.items())}</div>
<div style="position:absolute;right:22mm;bottom:28mm;display:grid;grid-template-columns:repeat(3,34mm);gap:6mm">{portada_ic}</div>
<div style="position:absolute;left:22mm;bottom:22mm;font-weight:900;font-size:14pt">Byignis</div>''', 'portada')

    pag(f'''<div class="kicker">Antes de empezar</div><h2 style="margin:3mm 0 4mm">Qué son las historias sociales</h2>
<p class="lead">Una historia social es un cuento corto, contado por el propio niño, que narra una situación de principio a fin: qué pasa, qué siente, qué sienten los demás y cómo lo resuelve. Así, cuando llega el momento real, ya lo vivió en el cuento.</p>
<div class="grid2" style="margin-top:7mm">
<div class="caja"><h4>¿Para quién son?</h4><p>Para niños a los que les cuesta anticipar, tolerar cambios o entender situaciones sociales: niños con TEA, TDAH, ansiedad o dificultades de lenguaje. También para cualquier niño ante algo nuevo.</p></div>
<div class="caja"><h4>¿Por qué funcionan?</h4><p>Saber qué va a pasar reduce la ansiedad. Las imágenes ayudan a entender sin muchas palabras, y la repetición convierte lo desconocido en algo familiar.</p></div></div>
<h3 style="margin-top:8mm">Cómo usarlas</h3>
<ol class="pasos" style="margin-top:3mm;font-size:11pt">
<li><b>Lee la historia varios días antes</b> de la situación (por ejemplo, una semana antes del dentista), en un momento tranquilo.</li>
<li><b>Léela despacio</b>, señalando cada imagen. Deja que el niño pase las páginas o lea contigo.</li>
<li><b>Repítela</b> todos los días que haga falta. La repetición es la clave.</li>
<li><b>Personalízala:</b> escribe su nombre arriba, cambia "mamá o papá" por quien lo acompañe y pega fotos reales del lugar si puedes.</li>
<li><b>Llévala contigo</b> el día de la situación y léela antes de entrar.</li>
<li><b>Nunca la uses como castigo</b> ni en medio de una crisis: primero calma, después la historia.</li>
</ol>
<p class="nota" style="margin-top:6mm">Cada historia trae una nota para el adulto con un consejo práctico. Al final encontrarás plantillas en blanco para crear tus propias historias. Este material es de apoyo y no sustituye la orientación de un profesional.</p>''')

    # Índice
    filas = ''
    for k in orden:
        filas += f'<h4 style="background:{COLCAT[k]}">{CATS[k][0]}</h4>'
        filas += ''.join(f'<div><span>{n_hist[id(h)]:02d}. {e(h[1])}</span></div>' for h in historias if h[0] == k)
    pag(f'<div class="kicker">Índice</div><h2 style="margin:3mm 0 2mm">Las 50 historias</h2><div class="indice">{filas}</div>')

    for ci, k in enumerate(orden, 1):
        nombre, icono = CATS[k]; col = COLCAT[k]
        lista = ''.join(f'<div>{n_hist[id(h)]:02d} · {e(h[1])}</div>' for h in historias if h[0] == k)
        pag(f'''<div class="divisor"><div class="kicker">Parte {ci}</div><h2>{nombre}</h2><div class="div-ic">{ic(icono)}</div><div class="div-lista">{lista}</div></div><div class="grande">0{ci}</div>''', f'color" style="background:{col}')
        for h in [x for x in historias if x[0] == k]:
            cat, titulo, vinetas, nota = h
            nv = len(vinetas)
            celdas = ''.join(f'<div class="vin"><div class="pic">{ic(p)}</div><div class="tx">{e(t)}</div></div>' for p, t in vinetas)
            pag(f'''<div class="hist-head"><div><div class="kicker" style="color:{col}">Historia {n_hist[id(h)]:02d} · {nombre}</div><h2>{e(titulo)}</h2></div><div class="duenio">Esta historia es de: </div></div>
<div class="cuento">{celdas}</div>
<div class="nota-adulto" style="border-color:{col}"><b style="color:{col}">Nota para el adulto</b>{e(nota)}</div>''')

    for t, nb in [('Crea tu propia historia', 6), ('Crea tu propia historia', 8)]:
        blanco = ''.join(f'<div class="vin blanco"><span class="n" style="background:{AC}">{j}</span><div class="pic"></div><div class="tx"></div></div>' for j in range(1, nb + 1))
        pag(f'''<div class="hist-head"><div><div class="kicker">Plantilla en blanco</div><h2>{t}</h2></div><div class="duenio">Título: </div></div>
<p class="nota" style="margin-top:2mm">Dibuja o pega una foto en cada recuadro y escribe una frase corta en primera persona. Usa frases positivas: "puedo…", "está bien sentir…".</p>
<div class="vinetas">{blanco}</div>''')

    pag(f'''<div style="height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">
<div style="width:42mm">{ic('abrazo')}</div><h2 style="margin:6mm 0 4mm">Cada historia, un paso más</h2>
<p class="lead" style="max-width:140mm">Entender el mundo da seguridad. Con paciencia y repetición, las situaciones difíciles se vuelven conocidas, y lo conocido se vive con calma.</p>
<div style="margin-top:12mm;font-weight:900;font-size:16pt">Byignis</div></div>''', 'crema')

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out'); os.makedirs(out, exist_ok=True)
    hp = os.path.join(out, '50-historias-sociales.html')
    open(hp, 'w').write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(pags)}</body></html>')
    print('paginas', len(pags), 'historias', len(historias))
    return hp

if __name__ == '__main__':
    import sys
    hp = main()
    if 'snap' in sys.argv:
        snapshot(hp, hp.replace('.html', ''), [int(x) for x in sys.argv[2:]])
    else:
        render_pdf(hp, hp.replace('.html', '.pdf'))
