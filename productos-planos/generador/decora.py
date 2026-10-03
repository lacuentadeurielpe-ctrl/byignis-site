"""Libro 4: Decora tu casa con muebles hechos por ti — 35 ambientes decorados."""
import os
from tienda_base import T, e, css_base, pie
from common import render_pdf, snapshot
from escenas import escena, ESTILOS, META, DECO_BASE, ALTERNO
from decora_data import A, PALETA_NOMBRES, ZONAS

MARCA = 'Decora tu casa con muebles hechos por ti'

def esc(a):
    zona, code, estilo, titulo, deco, cx, tips, truco = a
    return escena(code, estilo, deco, x_centro=cx)

def mm(v):
    return f'{v/10:.0f} cm' if v >= 100 else f'{v} mm'

def main():
    css = css_base() + f"""
.scene {{ width: 174mm; height: 111.4mm; border-radius: 5mm; overflow: hidden }}
.swatches {{ display: flex; gap: 2.4mm }}
.sw {{ flex: 1; text-align: center; font-size: 7.6pt; font-weight: 600; color: {T['muted']} }}
.sw i {{ display: block; height: 8mm; border-radius: 2.4mm; border: 1px solid rgba(0,0,0,.08); margin-bottom: 1.2mm }}
.pal {{ display: grid; grid-template-columns: 22mm 1fr; align-items: center; gap: 4mm; margin-top: 4mm }}
.pal h4 {{ margin: 0 }}
.ficha {{ display: grid; grid-template-columns: 1.35fr 1fr; gap: 7mm; margin-top: 4mm; font-size: 10pt }}
.ficha ul.lista li {{ margin: 1mm 0 }}
.mueble {{ font-size: 9.2pt; background: {T['sand']}; border-radius: 4mm; padding: 4mm }}
.mueble b {{ font-family: 'Barlow Condensed'; font-size: 13pt }}
.mueble table td {{ padding: .8mm 0; border-bottom: 1px dashed {T['line']} }}
.mueble table td:first-child {{ color: {T['muted']}; width: 22mm }}
.extra {{ position: absolute; left: 18mm; right: 18mm; bottom: 16mm; display: grid; grid-template-columns: 74mm 1fr; gap: 6mm; align-items: center }}
.alt {{ width: 74mm; height: 47.4mm; border-radius: 3mm; overflow: hidden }}
.truco2 {{ background: {T['ink']}; color: #fff; border-radius: 4mm; padding: 5mm 6mm; font-size: 10.6pt; line-height: 1.45 }}
.truco2 b {{ display: block; font-family: 'Barlow Condensed'; font-size: 15pt; color: {T['ember']}; margin-bottom: 1mm }}
.truco {{ position: absolute; left: 18mm; right: 18mm; bottom: 17mm; background: {T['ink']}; color: #fff; border-radius: 4mm; padding: 4mm 6mm 4mm 22mm; font-size: 10.4pt }}
.truco::before {{ content: 'TRUCO'; position: absolute; left: 5mm; top: 50%; transform: translateY(-50%); font-family: 'Barlow Condensed'; font-weight: 700; color: {T['ember']}; letter-spacing: 1px }}
.mini {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 2.4mm 3mm; margin-top: 4mm }}
.mini div {{ font-size: 7.4pt; font-weight: 600; line-height: 1.2 }}
.mini .im {{ aspect-ratio: 1000/640; border-radius: 2mm; overflow: hidden; margin-bottom: 1mm }}
.estilos {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; margin-top: 5mm }}
.estilo {{ border: 1.4px solid {T['line']}; border-radius: 4mm; padding: 3.6mm 4.4mm }}
.estilo h3 {{ font-size: 15pt }}
.estilo .bar {{ display: flex; height: 7mm; border-radius: 2mm; overflow: hidden; margin: 2mm 0 }}
.estilo .bar i {{ flex: 1 }}
.estilo p {{ font-size: 9.2pt; color: {T['muted']}; line-height: 1.35 }}
.combo {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 5mm; margin-top: 6mm }}
.combo > div {{ border-radius: 4mm; overflow: hidden; border: 1.4px solid {T['line']} }}
.combo .c {{ display: flex; height: 26mm }}
.combo .c i {{ flex: 1 }}
.combo p {{ padding: 3mm 4mm; font-size: 9.4pt; line-height: 1.35 }}
.combo p b {{ display: block; font-family: 'Barlow Condensed'; font-size: 13pt }}
.trucos {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; margin-top: 6mm }}
.trucos div {{ background: {T['sand']}; border-radius: 4mm; padding: 4mm 5mm; font-size: 10pt }}
.trucos b {{ display: block; font-family: 'Barlow Condensed'; font-size: 14pt; margin-bottom: 1mm }}
.trucos span {{ font-family: 'Barlow Condensed'; font-weight: 700; color: {T['ember']}; font-size: 20pt; float: right; line-height: 1 }}
"""
    pags = []; num = [0]
    def pag(body, cls=''):
        num[0] += 1
        pags.append(f'<section class="pag {cls}">{body}{pie(MARCA, num[0]) if num[0] > 1 else ""}</section>')

    # Portada
    col = [A[0], A[3], A[17], A[22]]
    tarjetas = ''.join(f'<div style="position:absolute;width:112mm;height:72mm;border-radius:4mm;overflow:hidden;box-shadow:0 5mm 12mm rgba(0,0,0,.35);left:{l}mm;top:{t}mm;transform:rotate({r}deg)">{esc(a)}</div>' for a, (l, t, r) in zip(col, [(6, 150, -6), (92, 140, 5), (14, 212, 4), (88, 206, -4)]))
    pag(f'''<div class="kicker">Byignis · Guía visual</div>
<h1 style="margin:7mm 0 5mm">Decora tu casa<br>con muebles<br>hechos por ti</h1>
<p class="lead" style="max-width:150mm">35 ambientes decorados, 10 estilos, colores que combinan y las medidas que necesitas para que cada mueble luzca como de revista.</p>
{tarjetas}''', 'oscura')

    pag(f'''<div class="kicker">Antes de empezar</div><h2 style="margin:3mm 0 4mm">Un mueble hecho por ti merece lucir</h2>
<p class="lead">Fabricar el mueble es la mitad del trabajo. La otra mitad es elegir el color, el lugar y los detalles que lo acompañan. Esta guía te muestra cómo, con ejemplos reales de los planos byignis.</p>
<div class="grid3" style="margin-top:8mm">
<div class="caja"><h4>1. Elige un estilo</h4><p>Revisa los 10 estilos y quédate con el que más se parece a ti o a tu casa.</p></div>
<div class="caja"><h4>2. Busca tu ambiente</h4><p>Cada página muestra un mueble decorado, con su paleta de colores y el plano exacto que usa.</p></div>
<div class="caja"><h4>3. Copia y adapta</h4><p>Usa las ideas tal cual o cambia colores y objetos. Las medidas y trucos te evitan errores.</p></div></div>
<h3 style="margin-top:9mm">Lo que vas a encontrar</h3>
<ul class="lista" style="margin-top:3mm;font-size:11pt">
<li><b>10 estilos de decoración</b> con su paleta de colores.</li><li><b>Medidas que funcionan:</b> alturas, distancias y espacios de paso.</li>
<li><b>Combinaciones de melamina y madera</b> que nunca fallan.</li><li><b>Trucos para espacios pequeños.</b></li>
<li><b>35 ambientes decorados</b> en sala, comedor, dormitorio, cuarto infantil, cocina, baño, recibidor, estudio y exterior.</li></ul>
<div class="caja ember" style="margin-top:8mm"><p style="font-size:11.5pt">Cada ambiente indica el código del plano (por ejemplo, <b>SAL-01</b>) para que lo encuentres en tu catálogo de 200 planos.</p></div>''')

    # 10 estilos
    desc = {
        'nordico': 'Luz, blancos y madera clara. Pocos objetos, plantas y textiles suaves.',
        'industrial': 'Ladrillo, metal negro y madera oscura. Lámparas de foco visible.',
        'rustico': 'Madera con veta y nudos, tonos tierra, lino y barro.',
        'moderno': 'Líneas rectas, grises y un color de acento intenso.',
        'boho': 'Tonos tierra, fibras naturales, plantas y mucha textura.',
        'minimal': 'Lo justo: superficies despejadas, neutros y orden.',
        'infantil': 'Pasteles alegres, formas divertidas y todo a su altura.',
        'tropical': 'Verdes intensos, plantas grandes y colores frutales.',
        'costero': 'Blanco y azul, rayas, fibras y luz de playa.',
        'clasico': 'Simetría, molduras, tonos profundos y detalles dorados.',
    }
    cards = ''.join(f'''<div class="estilo"><h3>{ESTILOS[k]["nombre"]}</h3><div class="bar"><i style="background:{ESTILOS[k]["pared"]}"></i>{''.join(f'<i style="background:{c}"></i>' for c in ESTILOS[k]["acentos"])}<i style="background:{ESTILOS[k]["piso"]}"></i></div><p>{desc[k]}</p></div>''' for k in ESTILOS)
    pag(f'<div class="kicker">Estilos</div><h2 style="margin:3mm 0 2mm">10 estilos para tu casa</h2><p class="lead">Cada estilo tiene su paleta: pared, acentos y piso.</p><div class="estilos">{cards}</div>')

    # Medidas
    filas = [('Mesa de comedor', '75 – 76 cm de alto', '60 cm de ancho por persona'), ('Silla de comedor', '45 cm de asiento', '30 cm entre asiento y mesa'),
             ('Escritorio', '72 – 75 cm de alto', '60 cm de fondo mínimo'), ('Encimera de cocina', '85 – 90 cm de alto', '60 cm de fondo'),
             ('Barra / mesa alta', '100 – 110 cm de alto', 'Taburete de 75 cm'), ('Mesa de centro', '40 – 45 cm de alto', '40 – 45 cm del sofá'),
             ('Mesa de noche', 'A la altura del colchón', '±5 cm'), ('Mueble de TV', 'Centro de la TV a 100 – 110 cm', 'Distancia: 2,5 × la diagonal'),
             ('Repisas', 'A 40 cm sobre un escritorio', 'Entre repisas: 30 – 35 cm'), ('Espacio de paso', '60 cm mínimo', '90 cm ideal'),
             ('Alrededor de la mesa', '90 cm para pasar detrás de las sillas', ''), ('Lámpara sobre mesa', '70 – 80 cm sobre la superficie', '')]
    tabla = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>' for a, b, c in filas)
    pag(f'''<div class="kicker">Medidas que funcionan</div><h2 style="margin:3mm 0 3mm">Las medidas de una casa cómoda</h2>
<p class="lead">Un mueble bonito pero mal ubicado se vuelve incómodo. Estas medidas son las que usan los diseñadores de interiores.</p>
<table class="t" style="margin-top:6mm"><tr><th>Mueble</th><th>Altura recomendada</th><th>Espacio / distancia</th></tr>{tabla}</table>
<div class="caja" style="margin-top:6mm"><h4>Regla de oro</h4><p>Antes de fabricar, marca el tamaño del mueble en el piso con cinta de papel y vive con ella unos días: sabrás si el tamaño es el correcto.</p></div>''')

    # Combinaciones
    combos = [('Blanco + Roble natural', ['#F4F2EE', '#C9A57A'], 'La combinación más vendida: luminosa y cálida. Va con todo.'),
              ('Grafito + Nogal', ['#3B3B3D', '#7A5236'], 'Elegante y moderna. Ideal para salas y estudios.'),
              ('Gris humo + Roble', ['#9A9894', '#C9A57A'], 'Neutra y actual. Perfecta para dormitorios.'),
              ('Blanco + Grafito', ['#F4F2EE', '#3B3B3D'], 'Contraste limpio para cocinas modernas.'),
              ('Pino natural + Blanco', ['#E3C79A', '#F4F2EE'], 'Fresca y nórdica. Ideal para cuartos infantiles.'),
              ('Nogal + Verde salvia', ['#7A5236', '#8FA58C'], 'Cálida con un toque de color en paredes o textiles.')]
    cb = ''.join(f'<div><div class="c">{"".join(f"<i style=background:{c}></i>" for c in cs)}</div><p><b>{t}</b>{d}</p></div>' for t, cs, d in combos)
    pag(f'''<div class="kicker">Colores</div><h2 style="margin:3mm 0 3mm">Combinaciones que nunca fallan</h2>
<p class="lead">Melamina y madera en dúos probados. El primer color es la estructura; el segundo, los frentes o la cubierta.</p><div class="combo">{cb}</div>
<div class="grid2" style="margin-top:7mm"><div class="caja"><h4>Regla 60 – 30 – 10</h4><p>60 % de un color base (paredes), 30 % de un color secundario (muebles) y 10 % de acento (cojines, cuadros, plantas).</p></div>
<div class="caja"><h4>Repite el acento</h4><p>Si eliges un color de acento, repítelo al menos 3 veces en el ambiente: un cojín, un cuadro y un jarrón.</p></div></div>''')

    trucos = [('Muebles flotantes', 'Dejar el piso a la vista agranda visualmente cualquier ambiente.'), ('Espejos grandes', 'Duplican la luz y la sensación de espacio.'),
              ('Colores claros', 'Paredes y muebles claros hacen que el ambiente respire.'), ('Muebles con doble función', 'Banco con baúl, mesa de centro con cajones, cama con cajones.'),
              ('Almacenamiento en altura', 'Repisas y armarios hasta el techo aprovechan la pared.'), ('Patas delgadas', 'Muebles con patas se ven más livianos que los que llegan al piso.'),
              ('Menos es más', 'Pocos objetos grandes lucen mejor que muchos pequeños.'), ('Luz en capas', 'Combina luz general, lámpara de pie y luz cálida de ambiente.')]
    tr = ''.join(f'<div><span>{i:02d}</span><b>{t}</b>{d}</div>' for i, (t, d) in enumerate(trucos, 1))
    pag(f'<div class="kicker">Espacios pequeños</div><h2 style="margin:3mm 0 3mm">8 trucos para que tu casa se vea más grande</h2><div class="trucos">{tr}</div>')

    # Índice visual
    mini = ''.join(f'<div><div class="im">{esc(a)}</div>{i:02d} · {e(a[3])}</div>' for i, a in enumerate(A, 1))
    pag(f'<div class="kicker">Índice visual</div><h2 style="margin:3mm 0 1mm">Los 35 ambientes</h2><div class="mini">{mini}</div>')

    for i, a in enumerate(A, 1):
        zona, code, estilo, titulo, deco, cx, tips, truco = a
        m = META[code]; est = ESTILOS[estilo]; alt = ALTERNO[estilo]
        nombres = PALETA_NOMBRES[estilo]
        colores = [est['pared']] + est['acentos'][:2] + [est['piso'], est['acentos'][3]]
        sw = ''.join(f'<div class="sw"><i style="background:{c}"></i>{n}</div>' for c, n in zip(colores, nombres))
        pag(f'''<div class="kicker">Ambiente {i:02d} · {zona}</div>
<div style="display:flex;justify-content:space-between;align-items:flex-end;margin:2mm 0 4mm"><h2>{e(titulo)}</h2><div><span class="chip on">{est["nombre"]}</span> <span class="chip">Plano {code}</span></div></div>
<div class="scene">{esc(a)}</div>
<div class="pal"><h4>Paleta</h4><div class="swatches">{sw}</div></div>
<div class="ficha"><div><h4>Cómo decorarlo</h4><ul class="lista">{''.join(f"<li>{e(t)}</li>" for t in tips)}</ul></div>
<div class="mueble"><h4>El mueble</h4><b>{e(m["name"])}</b><table style="width:100%;border-collapse:collapse;margin-top:1mm"><tr><td>Código</td><td>{code}</td></tr><tr><td>Medidas</td><td>{m["w"]} × {m["d"]} × {m["h"]} mm</td></tr><tr><td>Acabado</td><td>{e(m["finish"])}</td></tr><tr><td>Nivel</td><td>{m["level"]} · {m["hours"]:g} h aprox.</td></tr></table></div></div>
<div class="extra"><div><div class="alt">{escena(code, alt, DECO_BASE[alt], x_centro=500)}</div><p class="nota" style="margin-top:1.4mm"><b>El mismo mueble en estilo {ESTILOS[alt]["nombre"].lower()}</b></p></div>
<div class="truco2"><b>Truco</b>{e(truco)}</div></div>''')

    pag(f'''<div style="height:100%;display:flex;flex-direction:column;justify-content:center"><div class="kicker">Tu turno</div><h1 style="margin:5mm 0">Hazlo tuyo</h1>
<p class="lead" style="max-width:140mm">Elige un plano, elige un estilo y empieza. Un mueble hecho con tus manos tiene algo que ninguna tienda puede vender: tu historia.</p>
<div style="margin-top:12mm;font-family:'Barlow Condensed';font-weight:700;font-size:22pt">byignis</div></div>''', 'oscura')

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out'); os.makedirs(out, exist_ok=True)
    hp = os.path.join(out, 'decora-tu-casa.html')
    open(hp, 'w').write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(pags)}</body></html>')
    print('paginas', len(pags), 'ambientes', len(A))
    return hp

if __name__ == '__main__':
    import sys
    hp = main()
    if 'snap' in sys.argv:
        snapshot(hp, hp.replace('.html', ''), [int(x) for x in sys.argv[2:]])
    else:
        render_pdf(hp, hp.replace('.html', '.pdf'))
