"""Ambientes decorados: mueble real (render del plano) + decoración vectorial. SVG 1000×640."""
import json, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
META = json.load(open(os.path.join(HERE, 'iso/meta.json')))
W, H, PISO = 1000, 640, 440
INK = '#2B2724'

ESTILOS = {
 'nordico':    dict(nombre='Nórdico', pared='#ECE7DF', piso='#D8BE98', tabla='#C9AC83', acentos=['#8FA58C', '#E3B04B', '#F4F1EB', '#3E4A3D', '#C98B6B']),
 'industrial': dict(nombre='Industrial', pared='#B9AFA6', piso='#6E5644', tabla='#5E4838', acentos=['#2F2F2F', '#B5653A', '#D9D3C7', '#7C8B7A', '#E3B04B'], textura='ladrillo'),
 'rustico':    dict(nombre='Rústico', pared='#E9D8BF', piso='#9C6B43', tabla='#8A5C38', acentos=['#7A8B5C', '#B5653A', '#F3E9D8', '#5A3E2B', '#D9A441'], textura='madera'),
 'moderno':    dict(nombre='Moderno', pared='#DCE2E6', piso='#CFC8BE', tabla='#BEB6AB', acentos=['#2F3B4C', '#E07B3C', '#FFFFFF', '#6B8AA6', '#D9D3C7']),
 'boho':       dict(nombre='Boho', pared='#F1E0CC', piso='#C79A6E', tabla='#B5875D', acentos=['#C0623A', '#7A8B5C', '#E8C07D', '#F7EEE2', '#8C4A32']),
 'minimal':    dict(nombre='Minimalista', pared='#F5F4F1', piso='#DEDBD5', tabla='#D1CDC6', acentos=['#1F1F1F', '#BDB6AB', '#FFFFFF', '#8E9AA0', '#D8CFC1']),
 'infantil':   dict(nombre='Infantil', pared='#DCEBF2', piso='#E7D3B5', tabla='#D9C29E', acentos=['#F2A7A0', '#7CC1C4', '#F6D365', '#A8C686', '#FFFFFF'], textura='lunares'),
 'tropical':   dict(nombre='Tropical', pared='#D9E6D2', piso='#D2B48C', tabla='#C3A47B', acentos=['#3E7B4F', '#E8A33D', '#F4EFE6', '#C0623A', '#2E5E4E']),
 'costero':    dict(nombre='Costero', pared='#E3EEF3', piso='#E2D3BB', tabla='#D3C2A6', acentos=['#2F6690', '#F4F1EB', '#9CC5D9', '#E3B04B', '#C9B79C'], textura='rayas'),
 'clasico':    dict(nombre='Clásico', pared='#E8E1D6', piso='#8E6A4E', tabla='#7E5C42', acentos=['#5B3A4A', '#C9A15A', '#F4EFE6', '#3E4A3D', '#A65E4E'], textura='zocalo'),
}

def _fondo(e):
    s = f'<rect width="{W}" height="{PISO}" fill="{e["pared"]}"/>'
    t = e.get('textura')
    if t == 'ladrillo':
        for r in range(0, PISO, 28):
            off = 0 if (r // 28) % 2 == 0 else 40
            for c in range(-40 + off, W, 80):
                s += f'<rect x="{c + 2}" y="{r + 2}" width="76" height="24" rx="2" fill="#A9573C" opacity=".22"/>'
    elif t == 'madera':
        for c in range(0, W, 70):
            s += f'<path d="M{c} 0 V{PISO}" stroke="#B9946B" stroke-width="2" opacity=".35"/>'
    elif t == 'lunares':
        for r in range(30, PISO, 60):
            for c in range(30 + (r // 60 % 2)*30, W, 60):
                s += f'<circle cx="{c}" cy="{r}" r="5" fill="#FFFFFF" opacity=".7"/>'
    elif t == 'rayas':
        for c in range(0, W, 60):
            s += f'<rect x="{c}" y="0" width="28" height="{PISO}" fill="#FFFFFF" opacity=".45"/>'
    elif t == 'zocalo':
        s += f'<rect y="{PISO - 150}" width="{W}" height="150" fill="#FFFFFF" opacity=".35"/><path d="M0 {PISO - 150} H{W}" stroke="#FFFFFF" stroke-width="6" opacity=".7"/>'
        for c in range(40, W, 160):
            s += f'<rect x="{c}" y="{PISO - 125}" width="120" height="100" fill="none" stroke="#FFFFFF" stroke-width="3" opacity=".6"/>'
    s += f'<rect y="{PISO}" width="{W}" height="{H - PISO}" fill="{e["piso"]}"/>'
    for k in range(1, 6):
        y = PISO + (H - PISO) * (k / 6) ** 1.3
        s += f'<path d="M0 {y:.0f} H{W}" stroke="{e["tabla"]}" stroke-width="2"/>'
    s += f'<rect y="{PISO - 10}" width="{W}" height="12" fill="#FFFFFF" opacity=".6"/>'
    return s

# --------------------------------------------------------------- decoración --
def planta_alta(x, y, a, h=230):
    pot = f'<path d="M{x-34} {y-70} h68 l-10 70 h-48 z" fill="{a[1]}" stroke="{INK}" stroke-width="3"/>'
    hojas = ''
    for i, (dx, dy, r) in enumerate([(-40, -150, -30), (35, -170, 25), (-10, -210, -5), (-55, -105, -50), (50, -120, 45), (5, -260, 0)]):
        if -dy > h: continue
        hojas += f'<ellipse cx="{x+dx}" cy="{y+dy}" rx="20" ry="46" transform="rotate({r} {x+dx} {y+dy})" fill="{a[0]}" stroke="{INK}" stroke-width="3"/>'
    tallo = f'<path d="M{x} {y-70} V{y-h+40}" stroke="{INK}" stroke-width="3"/>'
    return tallo + hojas + pot

def planta_peq(x, y, a):
    return (f'<ellipse cx="{x-14}" cy="{y-58}" rx="12" ry="26" transform="rotate(-25 {x-14} {y-58})" fill="{a[0]}" stroke="{INK}" stroke-width="2.6"/>'
            f'<ellipse cx="{x+14}" cy="{y-60}" rx="12" ry="26" transform="rotate(25 {x+14} {y-60})" fill="{a[0]}" stroke="{INK}" stroke-width="2.6"/>'
            f'<ellipse cx="{x}" cy="{y-70}" rx="11" ry="28" fill="{a[0]}" stroke="{INK}" stroke-width="2.6"/>'
            f'<path d="M{x-24} {y-40} h48 l-6 40 h-36 z" fill="{a[2]}" stroke="{INK}" stroke-width="2.6"/>')

def cactus(x, y, a):
    return (f'<rect x="{x-14}" y="{y-120}" width="28" height="80" rx="14" fill="{a[0]}" stroke="{INK}" stroke-width="2.6"/>'
            f'<path d="M{x-14} {y-80} h-12 a8 8 0 0 1 -8 -8 v-18" fill="none" stroke="{INK}" stroke-width="2.6"/>'
            f'<path d="M{x-26} {y-30} h52 l-6 30 h-40 z" fill="{a[1]}" stroke="{INK}" stroke-width="2.6"/>')

def cuadro(x, y, w, h, a, motivo=0):
    m = [f'<circle cx="{x+w*.4}" cy="{y+h*.45}" r="{min(w, h)*.22}" fill="{a[1]}"/><rect x="{x+w*.5}" y="{y+h*.35}" width="{w*.3}" height="{h*.4}" fill="{a[0]}"/>',
         f'<path d="M{x+8} {y+h-8} L{x+w*.4} {y+h*.35} L{x+w*.6} {y+h*.6} L{x+w*.75} {y+h*.45} L{x+w-8} {y+h-8} Z" fill="{a[0]}"/><circle cx="{x+w*.75}" cy="{y+h*.25}" r="{w*.08}" fill="{a[1]}"/>',
         f'<path d="M{x+w*.2} {y+h*.8} C{x+w*.2} {y+h*.2} {x+w*.8} {y+h*.2} {x+w*.8} {y+h*.8}" fill="none" stroke="{a[0]}" stroke-width="6"/><circle cx="{x+w*.5}" cy="{y+h*.6}" r="{w*.1}" fill="{a[1]}"/>',
         f'<rect x="{x+w*.15}" y="{y+h*.15}" width="{w*.35}" height="{h*.7}" fill="{a[1]}"/><rect x="{x+w*.5}" y="{y+h*.45}" width="{w*.35}" height="{h*.4}" fill="{a[0]}"/>'][motivo % 4]
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{a[2] if a[2] != "#FFFFFF" else "#F7F5F1"}" stroke="{INK}" stroke-width="5"/>' + m

def espejo(x, y, r, a):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#DDE8EE" stroke="{a[1]}" stroke-width="10"/><path d="M{x-r*.4} {y-r*.2} l{r*.3} {-r*.3}" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'

def repisa(x, y, w, a):
    libros = ''; cx = x + 10
    for i in range(6):
        hh = 40 + (i * 7) % 18; ww = 12 + (i * 5) % 8
        libros += f'<rect x="{cx}" y="{y-hh}" width="{ww}" height="{hh}" fill="{a[i % 5]}" stroke="{INK}" stroke-width="2"/>'; cx += ww + 2
    return libros + f'<rect x="{x}" y="{y}" width="{w}" height="10" fill="{a[3] if len(a) > 3 else INK}" stroke="{INK}" stroke-width="2.4"/>' + planta_peq(x + w - 30, y, a).replace(f'{y}', f'{y}', 1)

def lampara_pie(x, y, a, h=300):
    return (f'<path d="M{x} {y} V{y-h+60}" stroke="{INK}" stroke-width="5"/><ellipse cx="{x}" cy="{y}" rx="30" ry="8" fill="{INK}"/>'
            f'<path d="M{x-45} {y-h+60} L{x-28} {y-h} H{x+28} L{x+45} {y-h+60} Z" fill="{a[2]}" stroke="{INK}" stroke-width="3"/>'
            f'<ellipse cx="{x}" cy="{y-h+80}" rx="70" ry="18" fill="#FFF3C4" opacity=".35"/>')

def colgante(x, a, largo=110):
    return (f'<path d="M{x} 0 V{largo}" stroke="{INK}" stroke-width="3"/><path d="M{x-40} {largo+40} Q{x} {largo-20} {x+40} {largo+40} Z" fill="{a[1]}" stroke="{INK}" stroke-width="3"/>'
            f'<ellipse cx="{x}" cy="{largo+48}" rx="60" ry="14" fill="#FFF3C4" opacity=".5"/>')

def alfombra(cx, y, w, a):
    return (f'<ellipse cx="{cx}" cy="{y}" rx="{w/2}" ry="{w*.11}" fill="{a[2] if a[2] != "#FFFFFF" else "#EFEAE2"}" stroke="{INK}" stroke-width="2.6"/>'
            f'<ellipse cx="{cx}" cy="{y}" rx="{w/2 - 22}" ry="{w*.11 - 9}" fill="none" stroke="{a[0]}" stroke-width="5" stroke-dasharray="14 8"/>')

def ventana(x, y, a, w=180, h=210):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#CFE7F3" stroke="#FFFFFF" stroke-width="12"/><path d="M{x+w/2} {y} V{y+h} M{x} {y+h/2} H{x+w}" stroke="#FFFFFF" stroke-width="8"/>'
            f'<path d="M{x-24} {y-16} q12 {h*.6} 0 {h+30} h28 q-10 {-h*.6} 0 {-h-30} z" fill="{a[0]}" opacity=".85"/><path d="M{x+w+24} {y-16} q-12 {h*.6} 0 {h+30} h-28 q10 {-h*.6} 0 {-h-30} z" fill="{a[0]}" opacity=".85"/>'
            f'<path d="M{x-40} {y-18} H{x+w+40}" stroke="{INK}" stroke-width="5"/>')

def guirnalda(x1, x2, y, a):
    d = f'M{x1} {y} Q{(x1+x2)/2} {y+70} {x2} {y}'
    luces = ''.join(f'<circle cx="{x1 + (x2-x1)*t:.0f}" cy="{y + 70*2*t*(1-t)*0.98 + 10:.0f}" r="7" fill="#FFE08A" stroke="{INK}" stroke-width="1.6"/>' for t in [i/9 for i in range(1, 9)])
    return f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="2"/>' + luces

def banderines(x1, x2, y, a):
    n = 9; out = f'<path d="M{x1} {y} Q{(x1+x2)/2} {y+50} {x2} {y}" fill="none" stroke="{INK}" stroke-width="2"/>'
    for i in range(n):
        t = (i + .5) / n; cx = x1 + (x2-x1)*t; cy = y + 50*2*t*(1-t)
        out += f'<path d="M{cx-18:.0f} {cy:.0f} h36 l-18 34 z" fill="{a[i % 4]}" stroke="{INK}" stroke-width="2"/>'
    return out

def estrellas(x, y, a):
    out = ''
    for i, (dx, dy, r) in enumerate([(0, 0, 18), (60, 40, 12), (120, -10, 16), (40, 90, 10), (150, 70, 14)]):
        cx, cy = x+dx, y+dy
        p = ' '.join(f'{cx + (r if k % 2 == 0 else r*.45)*math.cos(-math.pi/2 + k*math.pi/5):.0f},{cy + (r if k % 2 == 0 else r*.45)*math.sin(-math.pi/2 + k*math.pi/5):.0f}' for k in range(10))
        out += f'<polygon points="{p}" fill="{a[2]}" stroke="{INK}" stroke-width="2"/>'
    return out

def nube(x, y, a):
    return f'<path d="M{x} {y} a26 26 0 0 1 30 -32 a34 34 0 0 1 62 6 a24 24 0 0 1 24 26 z" fill="#FFFFFF" stroke="{INK}" stroke-width="2.6"/>'

def reloj(x, y, a):
    return f'<circle cx="{x}" cy="{y}" r="38" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/><path d="M{x} {y-24} V{y} L{x+16} {y+10}" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'

def cesto(x, y, a):
    return (f'<path d="M{x-40} {y-70} h80 l-8 70 h-64 z" fill="#D9B98C" stroke="{INK}" stroke-width="3"/>'
            + ''.join(f'<path d="M{x-38} {y-70 + k*14} h76" stroke="#B48B5A" stroke-width="3"/>' for k in range(1, 5))
            + f'<path d="M{x-30} {y-70} q-6 -24 16 -26 q16 -10 30 6" fill="{a[2]}" stroke="{INK}" stroke-width="2.4"/>')

def utensilios(x, y, w, a):
    out = f'<path d="M{x} {y} H{x+w}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
    for i in range(5):
        cx = x + 20 + i*(w-40)/4
        out += f'<path d="M{cx} {y} v10" stroke="{INK}" stroke-width="2"/>'
        if i % 2 == 0: out += f'<path d="M{cx} {y+10} v40" stroke="{INK}" stroke-width="4"/><ellipse cx="{cx}" cy="{y+60}" rx="9" ry="13" fill="{a[1]}" stroke="{INK}" stroke-width="2.4"/>'
        else: out += f'<rect x="{cx-12}" y="{y+10}" width="24" height="34" rx="4" fill="{a[0]}" stroke="{INK}" stroke-width="2.4"/>'
    return out

def macetas_colgantes(x, a):
    out = ''
    for i, (dx, l) in enumerate([(0, 120), (90, 170), (180, 110)]):
        cx = x + dx
        out += f'<path d="M{cx} 0 L{cx-18} {l} M{cx} 0 L{cx+18} {l}" stroke="{INK}" stroke-width="1.6"/><path d="M{cx-22} {l} h44 l-6 30 h-32 z" fill="{a[2]}" stroke="{INK}" stroke-width="2.4"/>'
        out += ''.join(f'<path d="M{cx + j*10} {l+20} q{j*6} 40 {j*14} 70" fill="none" stroke="{a[0]}" stroke-width="7" stroke-linecap="round"/>' for j in (-1, 0, 1))
    return out

def farol(x, y, a):
    return (f'<rect x="{x-22}" y="{y-80}" width="44" height="64" rx="4" fill="#FFF3C4" stroke="{INK}" stroke-width="3"/><path d="M{x-28} {y-80} h56 l-10 -16 h-36 z M{x-26} {y-16} h52 v16 h-52 z" fill="{INK}"/>'
            f'<path d="M{x} {y-96} v-12" stroke="{INK}" stroke-width="3"/><circle cx="{x}" cy="{y-48}" r="10" fill="#FFC94A"/>')

def cojines(x, y, a):
    return (f'<rect x="{x}" y="{y-44}" width="56" height="44" rx="12" fill="{a[0]}" stroke="{INK}" stroke-width="2.6"/>'
            f'<rect x="{x+40}" y="{y-40}" width="52" height="40" rx="12" fill="{a[1]}" stroke="{INK}" stroke-width="2.6"/>')

DECOR = dict(planta_alta=planta_alta, planta_peq=planta_peq, cactus=cactus, lampara_pie=lampara_pie, cesto=cesto, farol=farol, cojines=cojines)

def escena(code, estilo, deco, escala=0.245, ancho_max=700, x_centro=None):
    e = ESTILOS[estilo]; a = e['acentos']; m = META[code]
    fw = min((m['w'] + m['d']) * escala, ancho_max)
    if m['w'] + m['d'] < 900: fw = max(fw, 170)
    fh = fw * m['ih'] / m['iw']
    if fh > 520: fh = 520; fw = fh * m['iw'] / m['ih']
    cx = x_centro or 520
    fx = cx - fw/2; fb = 600; fy = fb - fh
    capas_fondo, capas_frente = '', ''
    for d in deco:
        n = d[0]; p = d[1:] if len(d) > 1 else ()
        if n == 'ventana': capas_fondo += ventana(p[0] if p else 70, 90, a)
        elif n == 'cuadro':
            w_, h_ = (p[0], p[1]) if p else (160, 120)
            capas_fondo += cuadro(cx - w_/2 + (p[2] if len(p) > 2 else 0), max(40, fy - h_ - 50), w_, h_, a, p[3] if len(p) > 3 else 0)
        elif n == 'cuadros_trio':
            y0 = max(40, fy - 170)
            for i, (dx, w_, h_) in enumerate([(-170, 100, 130), (-50, 100, 100), (70, 100, 130)]):
                capas_fondo += cuadro(cx + dx, y0 + (130 - h_)/2, w_, h_, a, i)
        elif n == 'espejo': capas_fondo += espejo(cx + (p[0] if p else 0), max(110, fy - 120), 80, a)
        elif n == 'repisa': capas_fondo += repisa(p[0], p[1], p[2] if len(p) > 2 else 200, a)
        elif n == 'reloj': capas_fondo += reloj(p[0], p[1], a)
        elif n == 'colgante': capas_fondo += colgante(p[0] if p else cx, a, p[1] if len(p) > 1 else 110)
        elif n == 'guirnalda': capas_fondo += guirnalda(p[0], p[1], p[2] if len(p) > 2 else 40, a)
        elif n == 'banderines': capas_fondo += banderines(p[0], p[1], p[2] if len(p) > 2 else 40, a)
        elif n == 'estrellas': capas_fondo += estrellas(p[0], p[1], a)
        elif n == 'nube': capas_fondo += nube(p[0], p[1], a)
        elif n == 'utensilios': capas_fondo += utensilios(p[0], p[1], p[2], a)
        elif n == 'macetas_colgantes': capas_fondo += macetas_colgantes(p[0], a)
        elif n == 'alfombra': capas_fondo += alfombra(cx, fb + 4, fw * (p[0] if p else 1.25), a)
        elif n in ('izq', 'der'):
            item = p[0]; gap = p[1] if len(p) > 1 else 30
            x = fx - gap - 50 if n == 'izq' else fx + fw + gap + 50
            capas_frente += DECOR[item](x, fb + (p[2] if len(p) > 2 else 0), a)
        elif n == 'piso': capas_frente += DECOR[p[0]](p[1], fb + 10, a)
    sombra = f'<ellipse cx="{cx}" cy="{fb - 2}" rx="{fw*.48}" ry="{max(10, fw*.05)}" fill="#000" opacity=".12"/>'
    img = f'<image href="file://{HERE}/iso/{code}.png" x="{fx:.0f}" y="{fy:.0f}" width="{fw:.0f}" height="{fh:.0f}"/>'
    return f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><defs><clipPath id="cl"><rect width="{W}" height="{H}" rx="28"/></clipPath></defs><g clip-path="url(#cl)">{_fondo(e)}{capas_fondo}{sombra}{img}{capas_frente}</g></svg>'

DECO_BASE = {
 'nordico': [('alfombra',), ('cuadros_trio',), ('izq', 'planta_alta')],
 'industrial': [('reloj', 840, 130), ('der', 'planta_alta'), ('colgante', 200, 80)],
 'rustico': [('ventana', 40), ('der', 'cesto')],
 'moderno': [('cuadro', 220, 140, 0, 3), ('izq', 'planta_alta')],
 'boho': [('guirnalda', 120, 880, 30), ('espejo',), ('der', 'planta_alta')],
 'minimal': [('cuadro', 240, 150, 0, 1)],
 'infantil': [('banderines', 60, 560, 30), ('estrellas', 700, 80), ('der', 'cesto')],
 'tropical': [('macetas_colgantes', 40), ('der', 'planta_alta')],
 'costero': [('ventana', 720), ('izq', 'cesto')],
 'clasico': [('espejo',), ('izq', 'lampara_pie')],
}
ALTERNO = {'nordico': 'boho', 'industrial': 'nordico', 'rustico': 'moderno', 'moderno': 'rustico', 'boho': 'minimal', 'minimal': 'tropical',
           'infantil': 'costero', 'tropical': 'industrial', 'costero': 'clasico', 'clasico': 'nordico'}
