"""Generadores de fichas de trazo (SVG). Área de trabajo: viewBox 0 0 600 600."""
import math
from common import C

W, H = 600, 600
GUIA = '#A4AAB6'

def _dot(x, y, color=None):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{color or C["verde"]}"/>'

def _path(d, modelo, acento):
    if modelo:
        return f'<path d="{d}" fill="none" stroke="{acento}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    return f'<path d="{d}" fill="none" stroke="{GUIA}" stroke-width="3.6" stroke-dasharray="0.1 9" stroke-linecap="round" stroke-linejoin="round"/>'

def svg(inner):
    return f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">{inner}</svg>'

def pts(p):
    return 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in p)

# --- Patrones por fila: f(x0, x1, ymid, h) -> (d, start(x,y)) -----------------
def p_vertical(x0, x1, y, h, n=9):
    step = (x1 - x0) / (n - 1)
    d = ' '.join(f'M{x0 + i*step:.1f} {y - h/2:.1f} V{y + h/2:.1f}' for i in range(n))
    return d, [(x0 + i*step, y - h/2) for i in range(n)]

def p_horizontal(x0, x1, y, h):
    return f'M{x0} {y} H{x1}', [(x0, y)]

def p_diag(x0, x1, y, h, sube=False, n=8):
    step = (x1 - x0) / n
    segs, st = [], []
    for i in range(n):
        xa = x0 + i*step + 6
        ya, yb = (y + h/2, y - h/2) if sube else (y - h/2, y + h/2)
        segs.append(f'M{xa:.1f} {ya:.1f} L{xa + step*0.6:.1f} {yb:.1f}'); st.append((xa, ya))
    return ' '.join(segs), st

def p_cruz(x0, x1, y, h, aspa=False, n=6):
    step = (x1 - x0) / n
    segs, st = [], []
    for i in range(n):
        cx = x0 + step*(i + .5); r = h/2
        if aspa:
            segs.append(f'M{cx-r:.1f} {y-r:.1f} L{cx+r:.1f} {y+r:.1f} M{cx+r:.1f} {y-r:.1f} L{cx-r:.1f} {y+r:.1f}'); st += [(cx-r, y-r), (cx+r, y-r)]
        else:
            segs.append(f'M{cx:.1f} {y-r:.1f} V{y+r:.1f} M{cx-r:.1f} {y:.1f} H{cx+r:.1f}'); st += [(cx, y-r), (cx-r, y)]
    return ' '.join(segs), st

def p_onda(x0, x1, y, h, ciclos=3):
    p = [(x0 + (x1-x0)*t/200, y - h/2*math.sin(2*math.pi*ciclos*t/200)) for t in range(201)]
    return pts(p), [p[0]]

def p_zigzag(x0, x1, y, h, n=6):
    p = [(x0 + (x1-x0)*i/(2*n), y + (h/2 if i % 2 == 0 else -h/2)) for i in range(2*n + 1)]
    return pts(p), [p[0]]

def p_arcos(x0, x1, y, h, n=5, abajo=False):
    w = (x1 - x0) / n
    d = f'M{x0} {y + (-h/2 if abajo else h/2)}'
    for i in range(n):
        xe = x0 + w*(i+1)
        d += f' A{w/2:.1f} {h:.1f} 0 0 {0 if abajo else 1} {xe:.1f} {y + (-h/2 if abajo else h/2):.1f}'
    return d, [(x0, y + (-h/2 if abajo else h/2))]

def p_bucles(x0, x1, y, h, n=6):
    # cicloide alargada: forma bucles tipo "eeee"
    a = (x1 - x0) / (n * 2*math.pi); b = h * 0.55
    p = []
    for k in range(400):
        t = 2*math.pi*n * k/399
        p.append((x0 + a*t - b*0.55*math.sin(t) + b*0.55*0, y + h*0.35 - b*(1 - math.cos(t))*0.65))
    return pts(p), [p[0]]

def p_circulos(x0, x1, y, h, n=5):
    step = (x1 - x0) / n; r = min(h/2, step/2 - 6)
    d = ' '.join(f'M{x0 + step*(i+.5):.1f} {y - r:.1f} a{r:.1f} {r:.1f} 0 1 0 0.1 0' for i in range(n))
    return d, [(x0 + step*(i+.5), y - r) for i in range(n)]

def p_cuadrados(x0, x1, y, h, n=5):
    step = (x1 - x0) / n; s = min(h, step - 14)
    d = ' '.join(f'M{x0 + step*i + 7:.1f} {y - s/2:.1f} h{s:.1f} v{s:.1f} h{-s:.1f} Z' for i in range(n))
    return d, [(x0 + step*i + 7, y - s/2) for i in range(n)]

def p_triangulos(x0, x1, y, h, n=5):
    step = (x1 - x0) / n; s = min(h, step - 14)
    d = ' '.join(f'M{x0 + step*i + 7 + s/2:.1f} {y - s/2:.1f} L{x0 + step*i + 7 + s:.1f} {y + s/2:.1f} H{x0 + step*i + 7:.1f} Z' for i in range(n))
    return d, [(x0 + step*i + 7 + s/2, y - s/2) for i in range(n)]

def p_escalera(x0, x1, y, h, n=6):
    step = (x1 - x0) / n; dy = h / n
    p = [(x0, y + h/2)]
    for i in range(n):
        p.append((x0 + step*i, y + h/2 - dy*(i+1))); p.append((x0 + step*(i+1), y + h/2 - dy*(i+1)))
    return pts(p), [p[0]]

def p_almenas(x0, x1, y, h, n=6):
    step = (x1 - x0) / (2*n); p = [(x0, y + h/2)]
    for i in range(2*n):
        yy = y - h/2 if i % 2 == 0 else y + h/2
        p.append((p[-1][0], yy)); p.append((x0 + step*(i+1), yy))
    return pts(p), [p[0]]

def p_espiral(x0, x1, y, h, n=3):
    step = (x1 - x0) / n; r = min(h/2, step/2 - 6); d, st = [], []
    for i in range(n):
        cx = x0 + step*(i+.5); p = []
        for k in range(160):
            t = 3*2*math.pi*k/159; rr = r*k/159
            p.append((cx + rr*math.cos(t), y + rr*math.sin(t)))
        d.append(pts(p)); st.append(p[0])
    return ' '.join(d), st

def p_combinado(x0, x1, y, h):
    a, _ = p_onda(x0, (x0+x1)/2, y, h, 2); b, _ = p_zigzag((x0+x1)/2, x1, y, h, 3)
    return a + ' ' + b.replace('M', 'L', 1), [(x0, y)]

def filas(patron, acento, n=5, h=60, x0=40, x1=560, **kw):
    """Primera fila modelo (color), el resto punteadas para repasar."""
    out = []; gap = (H - 40) / n
    for i in range(n):
        y = 20 + gap*(i + .5)
        d, starts = patron(x0, x1, y, h, **kw)
        out.append(_path(d, i == 0, acento))
        if i > 0:
            out += [_dot(sx, sy) for sx, sy in starts[:12]]
        out.append(f'<path d="M20 {20 + gap*(i+1):.1f} H580" stroke="{C["linea"]}" stroke-width="1.5"/>' if i < n-1 else '')
    return svg(''.join(out))

def _estrella(cx, cy, r):
    p = [(cx + (r if i % 2 == 0 else r*.45)*math.cos(-math.pi/2 + i*math.pi/5), cy + (r if i % 2 == 0 else r*.45)*math.sin(-math.pi/2 + i*math.pi/5)) for i in range(10)]
    return f'<path d="{pts(p)} Z" fill="{C["mostaza"]}" stroke="{C["tinta"]}" stroke-width="3" stroke-linejoin="round"/>'

# --- Fichas especiales -------------------------------------------------------
def camino(acento, ancho=70, ciclos=1, amp=120):
    p = [(60 + 480*t/200, 300 - amp*math.sin(2*math.pi*ciclos*t/200)) for t in range(201)]
    def offset(sig):
        out = []
        for i in range(len(p)):
            a = p[max(i-1, 0)]; b = p[min(i+1, len(p)-1)]
            dx, dy = b[0]-a[0], b[1]-a[1]; L = math.hypot(dx, dy) or 1
            out.append((p[i][0] - sig*dy/L*ancho/2, p[i][1] + sig*dx/L*ancho/2))
        return out
    road = offset(1) + offset(-1)[::-1]
    body = f'<path d="{pts(road)} Z" fill="{acento}" fill-opacity=".16" stroke="{acento}" stroke-width="4"/>'
    body += f'<path d="{pts(p)}" fill="none" stroke="{GUIA}" stroke-width="3" stroke-dasharray="0.1 10" stroke-linecap="round"/>'
    body += _dot(*p[0]) + _estrella(p[-1][0] - 10, p[-1][1], 26)
    return svg(body)

def unir_puntos(acento):
    # estrella de 10 puntos numerados
    puntos = []
    for i in range(10):
        r = 230 if i % 2 == 0 else 100; t = -math.pi/2 + i*math.pi/5
        puntos.append((300 + r*math.cos(t), 310 + r*math.sin(t)))
    body = ''
    for i, (x, y) in enumerate(puntos):
        body += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="{C["tinta"]}"/><text x="{x + (18 if x >= 300 else -18):.0f}" y="{y + 7:.0f}" font-size="26" font-weight="800" font-family="NS" text-anchor="middle" fill="{acento}">{i+1}</text>'
    return svg(body)

def cuadricula(acento, mitad=True):
    n = 10; s = 44; ox = 80; oy = 70
    body = ''.join(f'<path d="M{ox + i*s} {oy} V{oy + n*s} M{ox} {oy + i*s} H{ox + n*s}" stroke="{C["linea"]}" stroke-width="2"/>' for i in range(n+1))
    for i in range(n+1):
        for j in range(n+1):
            body += f'<circle cx="{ox + i*s}" cy="{oy + j*s}" r="2.6" fill="{GUIA}"/>'
    # mitad izquierda de un corazón/casa en la cuadrícula
    casa = [(5,1),(1,4),(1,9),(5,9)] if mitad else []
    if mitad:
        body += f'<path d="{pts([(ox + x*s, oy + y*s) for x, y in casa])}" fill="none" stroke="{acento}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>'
        body += f'<path d="{pts([(ox + x*s, oy + y*s) for x, y in [(2,6),(4,6),(4,9)]])}" fill="none" stroke="{acento}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>'
        body += f'<path d="M{ox + 5*s} {oy - 20} V{oy + n*s + 20}" stroke="{C["rojo"]}" stroke-width="3" stroke-dasharray="10 8"/>'
    return svg(body)

def copiar_figura(acento):
    n = 6; s = 40
    def grid(ox, oy):
        g = ''.join(f'<path d="M{ox + i*s} {oy} V{oy + n*s} M{ox} {oy + i*s} H{ox + n*s}" stroke="{C["linea"]}" stroke-width="2"/>' for i in range(n+1))
        return g + ''.join(f'<circle cx="{ox + i*s}" cy="{oy + j*s}" r="3" fill="{GUIA}"/>' for i in range(n+1) for j in range(n+1))
    fig = [(1,5),(1,2),(3,0),(5,2),(5,5),(1,5)]
    body = grid(40, 60) + grid(320, 60) + grid(40, 340) + grid(320, 340)
    body += f'<path d="{pts([(40 + x*s, 60 + y*s) for x, y in fig])}" fill="none" stroke="{acento}" stroke-width="6" stroke-linejoin="round"/>'
    fig2 = [(0,3),(3,0),(6,3),(3,6),(0,3)]
    body += f'<path d="{pts([(40 + x*s, 340 + y*s) for x, y in fig2])}" fill="none" stroke="{acento}" stroke-width="6" stroke-linejoin="round"/>'
    body += f'<text x="300" y="44" font-size="22" font-family="NS" font-weight="800" text-anchor="middle" fill="{C["gris"]}">Modelo  →  Tu copia</text>'
    return svg(body)

def calco(acento, figura):
    figs = {
        'casa': 'M150 300 L300 160 L450 300 V500 H150 Z M250 500 V390 H350 V500 M180 330 H240 V380 H180 Z',
        'pez': 'M120 300 C200 180 360 180 440 300 C360 420 200 420 120 300 Z M440 300 L520 230 V370 Z M200 290 a8 8 0 1 0 0.1 0',
        'arbol': 'M300 110 C200 120 160 220 200 270 C130 300 160 400 240 390 H360 C440 400 470 300 400 270 C440 220 400 120 300 110 Z M270 390 V520 H330 V390',
        'sol': 'M300 220 a80 80 0 1 0 0.1 0 M300 110 V170 M300 440 V500 M110 300 H170 M430 300 H490 M165 165 L205 205 M395 395 L435 435 M435 165 L395 205 M205 395 L165 435',
    }
    d = figs[figura]
    return svg(f'<path d="{d}" fill="none" stroke="{GUIA}" stroke-width="4" stroke-dasharray="0.1 10" stroke-linecap="round" stroke-linejoin="round"/>' + _dot(*{'casa': (150, 300), 'pez': (120, 300), 'arbol': (300, 110), 'sol': (300, 220)}[figura]))

def texto_trazo(acento, lineas):
    body = ''; gap = (H - 40) / len(lineas)
    for i, t in enumerate(lineas):
        y = 20 + gap*(i + .78)
        base = 20 + gap*(i + .78)
        body += f'<path d="M30 {base:.0f} H570" stroke="{C["azul"]}" stroke-width="2" opacity=".5"/><path d="M30 {base - gap*0.36:.0f} H570" stroke="{C["rojo"]}" stroke-width="1.5" stroke-dasharray="6 6" opacity=".5"/>'
        modelo = t.startswith('*'); t = t.lstrip('*')
        estilo = f'fill="{acento}"' if modelo else f'fill="none" stroke="{GUIA}" stroke-width="2.4" stroke-dasharray="0.1 6" stroke-linecap="round"'
        body += f'<text x="300" y="{y:.0f}" font-family="NS" font-weight="700" font-size="{gap*0.62:.0f}" text-anchor="middle" letter-spacing="14" {estilo}>{t}</text>'
    return svg(body)

def pauta(acento, n=6):
    body = ''; gap = (H - 40) / n
    for i in range(n):
        b = 20 + gap*(i + .8); m = b - gap*0.32; t = b - gap*0.62
        body += f'<path d="M30 {t:.0f} H570" stroke="{C["azul"]}" stroke-width="1.6" opacity=".45"/><path d="M30 {m:.0f} H570" stroke="{C["rojo"]}" stroke-width="1.6" stroke-dasharray="6 6" opacity=".55"/><path d="M30 {b:.0f} H570" stroke="{C["azul"]}" stroke-width="2.4" opacity=".7"/>'
    return svg(body)
