"""Generadores de fichas de motricidad fina (SVG, viewBox 0 0 600 660)."""
import math, random
from common import C
from iconos import I

W, H = 600, 660
GUIA = '#A4AAB6'
PAL = [C['rojo'], C['azul'], C['mostaza'], C['verde'], C['morado'], C['rosa'], C['turquesa'], C['naranja']]

def svg(inner, vb=f'0 0 {W} {H}'):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">{inner}</svg>'

def pts(p, cerrar=False):
    return 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in p) + (' Z' if cerrar else '')

def icon_g(nombre, x, y, s):
    return f'<g transform="translate({x:.1f} {y:.1f}) scale({s/100:.3f})">{I[nombre]}</g>'

# ---------------------------------------------------------------- formas ----
def f_circulo(cx=300, cy=330, r=220, n=240):
    return [[(cx + r*math.cos(2*math.pi*k/n - math.pi/2), cy + r*math.sin(2*math.pi*k/n - math.pi/2)) for k in range(n+1)]]

def f_corazon(cx=300, cy=320, s=15):
    p = []
    for k in range(361):
        t = 2*math.pi*k/360
        p.append((cx + s*16*math.sin(t)**3, cy - s*(13*math.cos(t) - 5*math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t))))
    return [p]

def f_estrella(cx=300, cy=340, R=250, r=105):
    p = [(cx + (R if i % 2 == 0 else r)*math.cos(-math.pi/2 + i*math.pi/5), cy + (R if i % 2 == 0 else r)*math.sin(-math.pi/2 + i*math.pi/5)) for i in range(11)]
    return [p]

def f_flor(cx=300, cy=330):
    return [[(cx + (170 + 70*math.cos(5*t))*math.cos(t), cy + (170 + 70*math.cos(5*t))*math.sin(t)) for t in [2*math.pi*k/400 for k in range(401)]]]

def f_espiral(cx=300, cy=330):
    return [[(cx + 240*k/300*math.cos(3*2*math.pi*k/300), cy + 240*k/300*math.sin(3*2*math.pi*k/300)) for k in range(301)]]

def f_oruga():
    return [[(60 + 480*t/200, 330 + 120*math.sin(2*math.pi*1.5*t/200)) for t in range(201)]]

def f_casa():
    return [[(130, 300), (300, 120), (470, 300), (470, 560), (130, 560), (130, 300)]]

def f_pez():
    p = []
    for k in range(201):
        t = math.pi*k/200
        p.append((110 + 330*k/200, 330 - 150*math.sin(t)))
    for k in range(201):
        t = math.pi*k/200
        p.append((440 - 330*k/200, 330 + 150*math.sin(t)))
    return [p, [(440, 330), (530, 240), (530, 420), (440, 330)]]

def f_arbol():
    copa = [(300 + 190*math.cos(t), 260 + 170*math.sin(t)) for t in [2*math.pi*k/200 for k in range(201)]]
    return [copa, [(260, 430), (260, 590), (340, 590), (340, 430)]]

def f_mariposa():
    p = []
    for k in range(401):
        t = 2*math.pi*k/400
        r = 120*(math.exp(math.sin(t)) - 2*math.cos(4*t)) / 2.4 + 60
        p.append((300 + r*math.cos(t) * 1.2, 340 - r*math.sin(t)))
    return [p]

LETRAS = {
    'L': [[(0, 0), (0, 1), (.7, 1)]], 'T': [[(0, 0), (1, 0)], [(.5, 0), (.5, 1)]],
    'E': [[(.8, 0), (0, 0), (0, 1), (.8, 1)], [(0, .5), (.65, .5)]],
    'A': [[(0, 1), (.5, 0), (1, 1)], [(.22, .58), (.78, .58)]],
    'M': [[(0, 1), (0, 0), (.5, .55), (1, 0), (1, 1)]],
    'O': [[(.5 + .5*math.cos(2*math.pi*k/80), .5 + .5*math.sin(2*math.pi*k/80)) for k in range(81)]],
    'S': [[(.5 + .45*math.cos(math.pi*(0.1 + 1.4*k/40)), .25 - .25*math.sin(math.pi*(0.1 + 1.4*k/40))) for k in range(41)] +
          [(.5 - .45*math.cos(math.pi*(-0.5 + 1.4*k/40)), .75 + .25*math.sin(math.pi*(-0.5 + 1.4*k/40))) for k in range(41)]],
    '1': [[(.25, .2), (.55, 0), (.55, 1)]], '2': [[(.05, .25)] + [(.5 + .45*math.cos(math.pi*(1 - k/20)), .27 - .27*math.sin(math.pi*(1 - k/20))) for k in range(21)][1:] + [(.05, 1), (.95, 1)]],
}

def f_letra(ch, x=150, y=110, w=300, h=470):
    return [[(x + px*w, y + py*h) for px, py in s] for s in LETRAS[ch]]

def muestrear(trazos, paso):
    out = []
    for s in trazos:
        acc = paso
        for (x1, y1), (x2, y2) in zip(s, s[1:]):
            L = math.hypot(x2-x1, y2-y1)
            if L == 0: continue
            d = 0
            while acc <= L - d:
                d += acc
                if d > L: break
                t = d / L; out.append((x1 + (x2-x1)*t, y1 + (y2-y1)*t)); acc = paso
            acc -= (L - d)
        out.append(s[-1])
    # quitar duplicados cercanos
    res = []
    for p in out:
        if all(math.hypot(p[0]-q[0], p[1]-q[1]) > paso*0.92 for q in res):
            res.append(p)
    return res

# --------------------------------------------------------------- PINZA ------
def pompones(trazos, r=24, colores=True, guia=True):
    puntos = muestrear(trazos, r*2.3)
    body = ''
    if guia:
        body += ''.join(f'<path d="{pts(s)}" fill="none" stroke="{C["linea"]}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>' for s in trazos)
    for i, (x, y) in enumerate(puntos):
        col = PAL[i % 6] if colores else C['naranja']
        body += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#fff" stroke="{col}" stroke-width="5"/><circle cx="{x:.1f}" cy="{y:.1f}" r="{r*0.35:.1f}" fill="{col}" opacity=".25"/>'
    return svg(body), len(puntos)

def pinzas_contar(numeros, seed=1):
    rnd = random.Random(seed)
    body = ''
    for i, n in enumerate(numeros):
        ox = 20 + (i % 2)*290; oy = 20 + (i // 2)*320
        body += f'<rect x="{ox}" y="{oy}" width="270" height="300" rx="22" fill="#fff" stroke="{C["linea"]}" stroke-width="4"/>'
        cols = 4 if n > 6 else 3
        for k in range(n):
            cx = ox + 50 + (k % cols)*(170/(cols-1) if cols > 1 else 0); cy = oy + 50 + (k // cols)*52
            body += icon_g('estrella', cx - 22, cy - 22, 44)
        opciones = sorted({n, max(1, n - rnd.choice([1, 2])), n + rnd.choice([1, 2])})
        while len(opciones) < 3: opciones = sorted(set(opciones) | {opciones[-1] + 1})
        for j, o in enumerate(opciones):
            x = ox + 55 + j*80; y = oy + 255
            body += f'<circle cx="{x}" cy="{y}" r="30" fill="{C["crema"]}" stroke="{C["naranja"]}" stroke-width="4"/><text x="{x}" y="{y + 12}" font-family="NS" font-weight="900" font-size="34" text-anchor="middle" fill="{C["tinta"]}">{o}</text>'
    return svg(body)

def costura(trazos, paso=42):
    body = ''.join(f'<path d="{pts(s)}" fill="{C["naranja"]}" fill-opacity=".12" stroke="{C["naranja"]}" stroke-width="6" stroke-linejoin="round"/>' for s in trazos)
    for x, y in muestrear(trazos, paso):
        body += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="10" fill="#fff" stroke="{C["tinta"]}" stroke-width="3.4"/>'
    return svg(body)

def punzar(trazos):
    body = ''.join(f'<path d="{pts(s)}" fill="none" stroke="{C["tinta"]}" stroke-width="5" stroke-dasharray="0.1 14" stroke-linecap="round"/>' for s in trazos)
    body += ''.join(f'<path d="{pts(s)}" fill="none" stroke="{C["naranja"]}" stroke-width="18" stroke-opacity=".12" stroke-linejoin="round"/>' for s in trazos)
    return svg(body)

# --------------------------------------------------------------- CORTAR -----
def _tijera(x, y):
    return icon_g('tijeras', x - 30, y - 30, 44)

def linea_corte(d, grueso=False):
    banda = f'<path d="{d}" fill="none" stroke="{C["naranja"]}" stroke-opacity=".14" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/>' if grueso else ''
    return banda + f'<path d="{d}" fill="none" stroke="{C["tinta"]}" stroke-width="3.4" stroke-dasharray="14 9" stroke-linejoin="round"/>'

def tiras(patron, n=5, grueso=False, h=50, **kw):
    """Hoja con n líneas de corte; patrón(x0,x1,y,h) -> lista de puntos."""
    body = ''; gap = (H - 40) / n
    for i in range(n):
        y = 20 + gap*(i + .5)
        p = patron(80, 570, y, h, **kw)
        body += linea_corte(pts(p), grueso) + _tijera(p[0][0] - 28, p[0][1])
        if i < n - 1:
            body += f'<path d="M20 {20 + gap*(i+1):.0f} H580" stroke="{C["linea"]}" stroke-width="1.5"/>'
    return svg(body)

def l_recta(x0, x1, y, h): return [(x0, y), (x1, y)]
def l_diagonal(x0, x1, y, h): return [(x0, y - h/2), (x1, y + h/2)]
def l_zigzag(x0, x1, y, h, n=6): return [(x0 + (x1-x0)*i/(2*n), y + (h/2 if i % 2 == 0 else -h/2)) for i in range(2*n + 1)]
def l_onda(x0, x1, y, h, c=2): return [(x0 + (x1-x0)*t/120, y - h/2*math.sin(2*math.pi*c*t/120)) for t in range(121)]
def l_escalon(x0, x1, y, h, n=5):
    p = [(x0, y + h/2)]; s = (x1 - x0) / n
    for i in range(n):
        yy = y - h/2 if i % 2 == 0 else y + h/2
        p.append((x0 + s*i, yy)); p.append((x0 + s*(i+1), yy))
    return p
def l_curva(x0, x1, y, h): return [(x0 + (x1-x0)*t/120, y - h/2*math.sin(math.pi*t/120)) for t in range(121)]
def l_mixta(x0, x1, y, h):
    a = l_onda(x0, (x0+x1)/2, y, h, 1); b = l_zigzag((x0+x1)/2, x1, y, h, 3)
    return a + b[1:]

def flecos_leon():
    cx, cy = 300, 330; body = ''
    for k in range(28):
        t = 2*math.pi*k/28
        body += linea_corte(f'M{cx + 250*math.cos(t):.1f} {cy + 250*math.sin(t):.1f} L{cx + 140*math.cos(t):.1f} {cy + 140*math.sin(t):.1f}')
    body += f'<circle cx="{cx}" cy="{cy}" r="250" fill="{C["mostaza"]}" fill-opacity=".18" stroke="{C["tinta"]}" stroke-width="3.4" stroke-dasharray="14 9"/>'
    body += f'<circle cx="{cx}" cy="{cy}" r="130" fill="#F2C9A0" stroke="{C["tinta"]}" stroke-width="5"/><circle cx="{cx-45}" cy="{cy-20}" r="10" fill="{C["tinta"]}"/><circle cx="{cx+45}" cy="{cy-20}" r="10" fill="{C["tinta"]}"/><path d="M{cx-20} {cy+25} q20 18 40 0" fill="none" stroke="{C["tinta"]}" stroke-width="5" stroke-linecap="round"/><path d="M{cx-12} {cy+8} h24 l-12 12 z" fill="{C["tinta"]}"/>'
    return svg(body)

def flecos_pasto():
    body = f'<rect x="40" y="120" width="520" height="420" rx="16" fill="{C["verde"]}" fill-opacity=".16" stroke="{C["tinta"]}" stroke-width="3.4" stroke-dasharray="14 9"/>'
    for k in range(13):
        x = 70 + k*38
        body += linea_corte(f'M{x} 120 V430')
    body += f'<path d="M40 430 H560" stroke="{C["verde"]}" stroke-width="6"/>' + ''.join(icon_g('sol', 470, 20, 90) for _ in [0])
    return svg(body)

def espiral_corte():
    p = [(300 + (40 + 230*k/400)*math.cos(3*2*math.pi*k/400), 330 + (40 + 230*k/400)*math.sin(3*2*math.pi*k/400)) for k in range(401)][::-1]
    return svg(linea_corte(pts(p)) + _tijera(p[0][0] + 30, p[0][1]) + f'<circle cx="300" cy="330" r="22" fill="{C["verde"]}"/><circle cx="292" cy="324" r="4" fill="#fff"/>')

def formas_recortar(cuales):
    body = ''; n = len(cuales); cols = 2; rows = (n + 1) // 2
    cw, ch = 290, (H - 20) / rows
    for i, f in enumerate(cuales):
        cx = 20 + (i % cols)*cw + cw/2; cy = 10 + (i // cols)*ch + ch/2; s = min(cw, ch)*0.36
        if f == 'circulo': d = f'M{cx} {cy - s} a{s} {s} 0 1 0 0.1 0'
        elif f == 'cuadrado': d = f'M{cx - s} {cy - s} h{2*s} v{2*s} h{-2*s} Z'
        elif f == 'triangulo': d = f'M{cx} {cy - s} L{cx + s*1.1} {cy + s*.9} H{cx - s*1.1} Z'
        elif f == 'rectangulo': d = f'M{cx - s*1.2} {cy - s*.65} h{2.4*s} v{1.3*s} h{-2.4*s} Z'
        elif f == 'estrella': d = pts([(cx + (s if k % 2 == 0 else s*.45)*math.cos(-math.pi/2 + k*math.pi/5), cy + (s if k % 2 == 0 else s*.45)*math.sin(-math.pi/2 + k*math.pi/5)) for k in range(10)], True)
        elif f == 'corazon': d = pts([(cx + s/17*16*math.sin(t)**3, cy - s/17*(13*math.cos(t) - 5*math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t))) for t in [2*math.pi*k/120 for k in range(121)]], True)
        elif f == 'rombo': d = f'M{cx} {cy - s} L{cx + s*.8} {cy} L{cx} {cy + s} L{cx - s*.8} {cy} Z'
        elif f == 'hexagono': d = pts([(cx + s*math.cos(math.pi/3*k), cy + s*math.sin(math.pi/3*k)) for k in range(6)], True)
        elif f == 'luna': d = f'M{cx + s*.3} {cy - s} a{s} {s} 0 1 0 0.1 {2*s} a{s*.75} {s*.8} 0 1 1 0 {-2*s} Z'
        elif f == 'nube': d = f'M{cx - s} {cy + s*.5} a{s*.45} {s*.45} 0 0 1 {s*.2} {-s*.85} a{s*.6} {s*.6} 0 0 1 {s*1.1} {-s*.3} a{s*.5} {s*.5} 0 0 1 {s*.7} {s*.6} a{s*.4} {s*.4} 0 0 1 0 {s*.55} Z'
        col = PAL[i % 8]
        body += f'<path d="{d}" fill="{col}" fill-opacity=".22" stroke="{C["tinta"]}" stroke-width="3.4" stroke-dasharray="14 9" stroke-linejoin="round"/>'
    return svg(body)

def rompecabezas(icono_nombre, n):
    """Arriba: figura dividida en n×n piezas numeradas para recortar. Abajo: base para pegar."""
    s = 260; ox = 170; oy = 20; c = s / n
    body = f'<rect x="{ox}" y="{oy}" width="{s}" height="{s}" fill="{C["crema"]}"/>' + icon_g(icono_nombre, ox + 10, oy + 10, s - 20)
    for i in range(1, n):
        body += f'<path d="M{ox + i*c} {oy} V{oy + s} M{ox} {oy + i*c} H{ox + s}" stroke="{C["tinta"]}" stroke-width="3" stroke-dasharray="12 8"/>'
    body += f'<rect x="{ox}" y="{oy}" width="{s}" height="{s}" fill="none" stroke="{C["tinta"]}" stroke-width="3" stroke-dasharray="12 8"/>'
    k = 1
    for r in range(n):
        for q in range(n):
            body += f'<circle cx="{ox + q*c + 16}" cy="{oy + r*c + 16}" r="12" fill="#fff" stroke="{C["naranja"]}" stroke-width="2.4"/><text x="{ox + q*c + 16}" y="{oy + r*c + 21}" font-family="NS" font-size="15" font-weight="900" text-anchor="middle">{k}</text>'
            k += 1
    oy2 = 360; body += f'<text x="300" y="{oy2 - 14}" font-family="NS" font-size="20" font-weight="800" text-anchor="middle" fill="{C["gris"]}">Pega aquí cada pieza en su número</text>'
    k = 1
    for r in range(n):
        for q in range(n):
            body += f'<rect x="{ox + q*c}" y="{oy2 + r*c}" width="{c}" height="{c}" fill="#fff" stroke="{C["linea"]}" stroke-width="3"/><text x="{ox + q*c + c/2}" y="{oy2 + r*c + c/2 + 12}" font-family="NS" font-size="32" font-weight="900" text-anchor="middle" fill="{C["linea"]}">{k}</text>'
            k += 1
    return svg(body)

def clasificar(grupo_a, grupo_b, titulo_a, titulo_b):
    body = ''; items = grupo_a + grupo_b
    rnd = random.Random(len(titulo_a)); rnd.shuffle(items)
    for i, it in enumerate(items):
        x = 30 + (i % 4)*140; y = 20 + (i // 4)*140
        body += f'<rect x="{x}" y="{y}" width="120" height="120" rx="10" fill="#fff" stroke="{C["tinta"]}" stroke-width="3" stroke-dasharray="12 8"/>' + icon_g(it, x + 15, y + 15, 90)
    for j, t in enumerate([titulo_a, titulo_b]):
        x = 30 + j*280
        body += f'<rect x="{x}" y="330" width="260" height="310" rx="18" fill="{PAL[j+1]}" fill-opacity=".1" stroke="{PAL[j+1]}" stroke-width="4"/><text x="{x + 130}" y="375" font-family="NS" font-size="28" font-weight="900" text-anchor="middle" fill="{PAL[j+1]}">{t}</text>'
    return svg(body)

def laberinto_corte():
    p = [(70, 80)]
    for i, y in enumerate([80, 210, 340, 470, 600]):
        a, b = (70, 530) if i % 2 == 0 else (530, 70)
        if i: p.append((a, y))
        p.append((b, y))
    return svg(linea_corte(pts(p), grueso=True) + _tijera(40, 80) + icon_g('estrella', p[-1][0] - 30, p[-1][1] - 40, 60))

# --------------------------------------------------------------- APILAR -----
def _bloques(model, ox, oy, cel=40, vacio=False, cols=6, rows=7):
    body = ''
    for r in range(rows):
        for c in range(cols):
            body += f'<rect x="{ox + c*cel}" y="{oy + r*cel}" width="{cel}" height="{cel}" fill="none" stroke="{C["linea"]}" stroke-width="1.6"/>'
    if not vacio:
        for c, r, col in model:
            y = oy + (rows - 1 - r)*cel
            body += f'<rect x="{ox + c*cel + 2}" y="{y + 2}" width="{cel - 4}" height="{cel - 4}" rx="5" fill="{col}" stroke="{C["tinta"]}" stroke-width="3"/>'
    body += f'<path d="M{ox - 8} {oy + rows*cel} H{ox + cols*cel + 8}" stroke="{C["tinta"]}" stroke-width="5" stroke-linecap="round"/>'
    return body

def ficha_bloques(m1, m2):
    body = ''
    for i, m in enumerate([m1, m2]):
        oy = 14 + i*336
        body += _bloques(m, 30, oy) + _bloques(m, 330, oy, vacio=True)
        body += f'<text x="150" y="{oy + 310}" font-family="NS" font-size="18" font-weight="800" text-anchor="middle" fill="{C["gris"]}">Modelo · {len(m)} bloques</text><text x="450" y="{oy + 310}" font-family="NS" font-size="18" font-weight="800" text-anchor="middle" fill="{C["gris"]}">Colorea tu torre</text>'
    return svg(body, f'0 0 {W} 680')

def modelos_bloques():
    rnd = random.Random(7)
    def col(): return rnd.choice(PAL[:6])
    M = []
    def torre(c, n, cols=None): return [(c, r, (cols[r % len(cols)] if cols else col())) for r in range(n)]
    M.append(torre(2, 3, [C['rojo']])); M.append(torre(2, 3, [C['azul'], C['mostaza']]))
    M.append(torre(2, 4, [C['verde']])); M.append(torre(2, 5, [C['rojo'], C['azul']]))
    M.append(torre(1, 2) + torre(3, 3)); M.append(torre(1, 3) + torre(4, 1))
    M.append(torre(0, 1) + torre(1, 2) + torre(2, 3)); M.append(torre(1, 1) + torre(2, 2) + torre(3, 3) + torre(4, 4))
    M.append([(1, 0, C['azul']), (2, 0, C['azul']), (3, 0, C['azul']), (2, 1, C['rojo'])])
    M.append([(c, 0, C['verde']) for c in range(1, 5)] + [(c, 1, C['mostaza']) for c in range(2, 4)])
    M.append([(c, 0, col()) for c in range(5)] + [(c, 1, col()) for c in range(1, 4)] + [(2, 2, col())])
    M.append([(c, 0, C['morado']) for c in range(6)] + [(c, 1, C['rosa']) for c in range(1, 5)] + [(c, 2, C['turquesa']) for c in range(2, 4)])
    M.append(torre(1, 2, [C['azul']]) + torre(3, 2, [C['azul']]) + [(1, 2, C['rojo']), (2, 2, C['rojo']), (3, 2, C['rojo'])])
    M.append(torre(0, 3, [C['verde']]) + torre(4, 3, [C['verde']]) + [(c, 3, C['mostaza']) for c in range(5)])
    M.append(torre(1, 4, [C['rojo']]) + [(2, 0, C['rojo']), (3, 0, C['rojo'])])
    M.append([(c, 3, C['azul']) for c in range(1, 4)] + torre(2, 3, [C['azul']]))
    M.append([(c, r, C['mostaza'] if (c + r) % 2 == 0 else C['azul']) for c in range(1, 4) for r in range(2)])
    M.append([(c, r, C['rojo'] if (c + r) % 2 == 0 else C['verde']) for c in range(1, 5) for r in range(2)])
    M.append([(c, r, C['morado'] if r != 1 else C['rosa']) for c in range(1, 5) for r in range(3)])
    M.append([(c, 0, col()) for c in range(6)] + [(0, 1, col()), (2, 1, col()), (3, 1, col()), (5, 1, col())] + [(0, 2, col()), (5, 2, col())])
    M.append(torre(0, 4, [C['azul']]) + torre(5, 4, [C['azul']]) + [(c, 0, C['mostaza']) for c in range(1, 5)] + [(0, 4, C['rojo']), (5, 4, C['rojo'])])
    M.append(torre(0, 2) + torre(1, 4) + torre(2, 6) + torre(3, 4) + torre(4, 2))
    M.append([(c, 0, C['verde']) for c in range(6)] + torre(0, 3, [C['verde']])[1:] + [(c, 1, C['mostaza']) for c in range(2, 4)] + [(c, 2, C['rojo']) for c in range(2, 4)])
    M.append([(1, r, C['azul']) for r in range(5)] + [(2, 4, C['azul']), (3, 4, C['azul'])] + [(4, r, C['azul']) for r in range(5)])
    M.append([(c, r, PAL[(c + r) % 6]) for c in range(6) for r in range(2)])
    M.append([(c, r, PAL[r % 6]) for r in range(5) for c in range(r, 6 - r) if r < 3])
    M.append(torre(2, 7, [C['rojo'], C['mostaza'], C['azul']]) + torre(3, 7, [C['azul'], C['rojo'], C['mostaza']]))
    M.append([(c, 0, C['tinta'] if False else C['morado']) for c in range(6)] + [(c, 1, C['rosa']) for c in (0, 2, 3, 5)] + [(c, 2, C['turquesa']) for c in (0, 1, 2, 3, 4, 5)] + [(c, 3, C['mostaza']) for c in (0, 2, 3, 5)] + [(c, 4, C['rojo']) for c in (0, 5)])
    M.append(torre(0, 1) + torre(1, 3) + torre(2, 5) + torre(3, 7) + torre(4, 5) + torre(5, 3))
    M.append([(c, r, col()) for c in range(6) for r in range(3) if not (r == 0 and c in (2, 3))])
    M.append(torre(0, 5) + torre(1, 3) + torre(2, 1) + torre(3, 1) + torre(4, 3) + torre(5, 5))
    M.append([(c, r, PAL[c % 6]) for c in range(6) for r in range(c + 1)])
    M.append([(c, r, PAL[(5 - c) % 6]) for c in range(6) for r in range(6 - c)])
    M.append([(c, r, col()) for c in range(6) for r in range(6) if r <= min(c, 5 - c) * 2 + 1])
    M.append([(c, r, col()) for c in range(6) for r in range(7) if c in (0, 5) or r in (0, 6) or (c in (2, 3) and r in (2, 3, 4))])
    M.append([(c, r, PAL[r % 6]) for c in range(6) for r in range(7) if r < 2 or c in (0, 1, 4, 5) and r < 5 or (c in (0, 5) and r < 7)])
    return M

def vasos(filas, alterna=False):
    body = ''; w = 74; h = 82
    total = len(filas)
    for i, n in enumerate(filas):
        y = 560 - i*h
        x0 = 300 - n*w/2
        for k in range(n):
            x = x0 + k*w
            boca_arriba = (alterna and (i + k) % 2 == 1)
            if boca_arriba:
                d = f'M{x + 4} {y - h} L{x + w - 4} {y - h} L{x + w - 14} {y} L{x + 14} {y} Z'
            else:
                d = f'M{x + 14} {y - h} L{x + w - 14} {y - h} L{x + w - 4} {y} L{x + 4} {y} Z'
            body += f'<path d="{d}" fill="{PAL[i % 6]}" stroke="{C["tinta"]}" stroke-width="3.4" stroke-linejoin="round"/>'
    body += f'<path d="M60 562 H540" stroke="{C["tinta"]}" stroke-width="6" stroke-linecap="round"/>'
    body += f'<text x="300" y="630" font-family="NS" font-size="24" font-weight="800" text-anchor="middle" fill="{C["gris"]}">¿Cuántos vasos usaste? ______</text>'
    return svg(body)

def recortar_apilar(tipo):
    body = ''
    tams = [130, 108, 86, 64, 44]
    xs = [20, 170, 300, 410, 500]
    for i, (s, x) in enumerate(zip(tams, xs)):
        y = 30 + (130 - s)/2
        if tipo == 'cuadrados':
            body += f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="6" fill="{PAL[i]}" stroke="{C["tinta"]}" stroke-width="3.4" stroke-dasharray="12 8"/>'
        else:
            cx = x + s/2; cy = y + s/2
            body += f'<circle cx="{cx}" cy="{cy}" r="{s/2}" fill="{PAL[i]}" stroke="{C["tinta"]}" stroke-width="3.4" stroke-dasharray="12 8"/><circle cx="{cx}" cy="{cy}" r="{s*0.14}" fill="#fff" stroke="{C["tinta"]}" stroke-width="3" stroke-dasharray="6 5"/>'
    if tipo == 'aros':
        body += f'<rect x="290" y="260" width="20" height="330" rx="8" fill="{C["mostaza"]}" stroke="{C["tinta"]}" stroke-width="3.4"/>'
    body += f'<path d="M140 600 H460" stroke="{C["tinta"]}" stroke-width="6" stroke-linecap="round"/><text x="300" y="640" font-family="NS" font-size="20" font-weight="800" text-anchor="middle" fill="{C["gris"]}">Pega aquí: el más grande abajo, el más pequeño arriba</text>'
    body += f'<path d="M20 220 H580" stroke="{C["linea"]}" stroke-width="2"/>'
    return svg(body)

def torre_numeros(desde):
    body = ''
    for i in range(5):
        n = desde + i; x = 30 + (i % 3)*190; y = 20 + (i // 3)*130
        body += f'<rect x="{x}" y="{y}" width="170" height="100" rx="10" fill="{PAL[i]}" fill-opacity=".9" stroke="{C["tinta"]}" stroke-width="3.4" stroke-dasharray="12 8"/><text x="{x + 85}" y="{y + 70}" font-family="NS" font-size="58" font-weight="900" text-anchor="middle" fill="#fff">{n}</text>'
    for k in range(5):
        y = 600 - (k + 1)*72
        body += f'<rect x="215" y="{y}" width="170" height="70" rx="8" fill="none" stroke="{C["linea"]}" stroke-width="3"/><text x="400" y="{y + 45}" font-family="NS" font-size="22" font-weight="800" fill="{C["linea"]}">{desde + k}</text>'
    body += f'<path d="M180 602 H420" stroke="{C["tinta"]}" stroke-width="6" stroke-linecap="round"/>'
    return svg(body)
