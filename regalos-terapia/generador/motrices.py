"""Paquete: 100 actividades para la coordinación motora fina (fichas imprimibles)."""
import os
from common import C, e, base_css, pie, render_pdf, snapshot
from iconos import icono
import motor as M
import trazos as T

AC = C['naranja']; AC_S = '#FBE6D8'
MARCA = '100 actividades de motricidad fina'

AREAS = {
 'pinza': ('Pinza', C['naranja'], 'pinza', 'Fuerza y precisión de los dedos: pompones, pinzas de ropa, costura y punzado.'),
 'cortar': ('Cortar', C['rojo'], 'tijeras', 'Del primer corte recto a las espirales, figuras y rompecabezas.'),
 'apilar': ('Apilar', C['azul'], 'bloques', 'Copiar modelos con bloques, vasos y torres: planificación y control de la mano.'),
 'escribir': ('Escribir', C['verde'], 'lapiz', 'Trazos, figuras, letras y números para preparar la escritura.'),
}

def fichas():
    F = []
    def add(area, titulo, instr, mats, nivel, dibujo): F.append(dict(area=area, t=titulo, i=instr, m=mats, n=nivel, svg=dibujo))
    # ------------------------------------------------------------- PINZA (25)
    pom = 'Pon un pompón en cada círculo usando pinzas, tenacillas o solo pulgar e índice.'
    for t, tr, nv, col in [('Círculo de colores', M.f_circulo(), 1, True), ('La oruga', M.f_oruga(), 1, True), ('Corazón', M.f_corazon(), 1, True),
                            ('Estrella', M.f_estrella(), 2, True), ('Flor', M.f_flor(), 2, True), ('Caracol', M.f_espiral(), 2, False),
                            ('Casa', M.f_casa(), 2, True), ('Pez', M.f_pez(), 2, True), ('Árbol', M.f_arbol(), 3, True), ('Mariposa', M.f_mariposa(), 3, True)]:
        dib, n = M.pompones(tr, colores=col)
        add('pinza', f'Pompones: {t}', pom + (' Combina cada pompón con su color.' if col else ''), ['pompon', 'pinza'], nv, dib)
    for k, nums in enumerate([[1, 2, 3, 4], [3, 5, 6, 4], [7, 8, 9, 10]], 1):
        add('pinza', f'Cuenta y pon la pinza {k}', 'Cuenta las estrellas de cada tarjeta y pon una pinza de ropa en el número correcto. Puedes recortar las tarjetas.', ['pinza', 'tijeras'], k, M.pinzas_contar(nums, seed=k))
    for t, tr, nv in [('Corazón', M.f_corazon(s=14), 1), ('Estrella', M.f_estrella(), 2), ('Casa', M.f_casa(), 2), ('Pez', M.f_pez(), 3)]:
        add('pinza', f'Tarjeta de costura: {t}', 'Pega la hoja en cartón, perfora los agujeros con un lápiz y pasa un cordón por cada uno.', ['cordon', 'lapiz'], nv, M.costura(tr))
    for t, tr, nv in [('Círculo', M.f_circulo(r=200), 1), ('Flor', M.f_flor(), 2), ('Árbol', M.f_arbol(), 3)]:
        add('pinza', f'Punzado: {t}', 'Pon la hoja sobre una toalla doblada o foami y pica cada punto con un punzón o lápiz.', ['lapiz'], nv, M.punzar(tr))
    for ch in ['L', 'T', 'E', 'A', 'O']:
        dib, n = M.pompones(M.f_letra(ch), r=18, colores=False)
        add('pinza', f'Letra {ch} con bolitas', 'Haz bolitas de papel o plastilina con la punta de los dedos y pon una en cada círculo.', ['pompon'], 2, dib)
    # ------------------------------------------------------------ CORTAR (25)
    cr = 'Recorta siguiendo la línea punteada, empezando en las tijeras.'
    add('cortar', 'Flecos: el pasto', 'Corta cada línea de arriba hacia abajo sin pasar la línea verde.', ['tijeras'], 1, M.flecos_pasto())
    add('cortar', 'Flecos: la melena del león', 'Recorta el círculo grande y luego cada línea hasta la cara del león.', ['tijeras'], 2, M.flecos_leon())
    for t, f, nv, kw in [('Caminos anchos', M.l_recta, 1, dict(grueso=True)), ('Líneas rectas', M.l_recta, 1, {}), ('Rampas', M.l_diagonal, 1, dict(grueso=True)),
                         ('Montañas', M.l_zigzag, 2, dict(grueso=True, n=4, h=80)), ('Dientes', M.l_zigzag, 2, dict(n=8, h=46)), ('Olas grandes', M.l_onda, 2, dict(grueso=True, c=1, h=80)),
                         ('Olas pequeñas', M.l_onda, 2, dict(c=3, h=40)), ('Arcoíris', M.l_curva, 2, dict(h=80)), ('Escaleras', M.l_escalon, 3, dict(h=60)), ('Caminos mixtos', M.l_mixta, 3, dict(h=60))]:
        add('cortar', t, cr, ['tijeras'], nv, M.tiras(f, **kw))
    add('cortar', 'La serpiente', 'Recorta la espiral desde afuera hasta la cabeza. ¡Cuélgala de un hilo!', ['tijeras'], 3, M.espiral_corte())
    add('cortar', 'El laberinto', 'Corta por el camino sin salirte hasta llegar a la estrella.', ['tijeras'], 2, M.laberinto_corte())
    for t, fs, nv in [('Figuras básicas 1', ['circulo', 'cuadrado', 'triangulo', 'rectangulo'], 1), ('Figuras básicas 2', ['rombo', 'hexagono', 'circulo', 'cuadrado'], 2),
                      ('Estrellas y corazones', ['estrella', 'corazon', 'estrella', 'corazon'], 3), ('Cielo', ['nube', 'luna', 'estrella', 'circulo'], 3),
                      ('Figuras grandes', ['corazon', 'estrella'], 1), ('Collage de figuras', ['triangulo', 'circulo', 'rombo', 'cuadrado', 'hexagono', 'rectangulo'], 2)]:
        add('cortar', t, 'Recorta cada figura por la línea punteada. Después úsalas para armar un dibujo.', ['tijeras', 'pegamento'], nv, M.formas_recortar(fs))
    for t, ic, n, nv in [('Rompecabezas: la estrella', 'estrella', 2, 1), ('Rompecabezas: la camiseta', 'camiseta', 2, 2), ('Rompecabezas: el sol', 'sol', 3, 3)]:
        add('cortar', t, 'Recorta las piezas por la línea punteada y pégalas abajo en su número.', ['tijeras', 'pegamento'], nv, M.rompecabezas(ic, n))
    add('cortar', 'Recorta y clasifica: ropa y comida', 'Recorta las tarjetas y pega cada una en su grupo.', ['tijeras', 'pegamento'], 2, M.clasificar(['camiseta', 'pantalon', 'calcetin', 'zapato'], ['cuchara', 'plato', 'vaso', 'tenedor'], 'Ropa', 'Comida'))
    add('cortar', 'Recorta y clasifica: baño y cuarto', 'Recorta las tarjetas y pega cada una donde se usa.', ['tijeras', 'pegamento'], 3, M.clasificar(['jabon', 'cepillo', 'toalla', 'peine'], ['cama', 'mochila', 'reloj', 'luna'], 'Baño', 'Cuarto'))
    # ------------------------------------------------------------ APILAR (25)
    mods = M.modelos_bloques()
    for k in range(18):
        a, b = mods[2*k], mods[2*k + 1]
        add('apilar', f'Constructor {k + 1}', 'Construye cada modelo con bloques o legos. Después colorea la cuadrícula igual.', ['bloques'], 1 if k < 6 else 2 if k < 12 else 3, M.ficha_bloques(a, b))
    for t, f, alt, nv in [('Pirámide de vasos 1', [3, 2, 1], False, 1), ('Pirámide de vasos 2', [4, 3, 2, 1], False, 2), ('Vasos al revés', [4, 3, 2, 1], True, 3)]:
        add('apilar', t, 'Apila vasos de plástico como en el modelo. Al terminar, desármala de arriba hacia abajo.', ['vaso'], nv, M.vasos(f, alt))
    add('apilar', 'Recorta y apila: cuadrados', 'Recorta los cuadrados y pégalos apilados del más grande al más pequeño.', ['tijeras', 'pegamento'], 1, M.recortar_apilar('cuadrados'))
    add('apilar', 'Recorta y apila: aros', 'Recorta los aros y pégalos en el poste, del más grande al más pequeño.', ['tijeras', 'pegamento'], 2, M.recortar_apilar('aros'))
    add('apilar', 'Torre de números 1 al 5', 'Recorta los bloques y pégalos en orden: el 1 abajo y el 5 arriba.', ['tijeras', 'pegamento'], 2, M.torre_numeros(1))
    add('apilar', 'Torre de números 6 al 10', 'Recorta los bloques y pégalos en orden: el 6 abajo y el 10 arriba.', ['tijeras', 'pegamento'], 3, M.torre_numeros(6))
    # ---------------------------------------------------------- ESCRIBIR (25)
    a = C['verde']; rp = 'Repasa desde el punto verde. La primera fila es el modelo.'
    for t, svg_, nv in [('Lluvia', T.filas(T.p_vertical, a), 1), ('Caminos', T.filas(T.p_horizontal, a, n=6), 1), ('Toboganes', T.filas(T.p_diag, a), 1),
                        ('Cruces', T.filas(T.p_cruz, a), 1), ('Gusanos', T.filas(T.p_onda, a, ciclos=2), 1), ('Montañas', T.filas(T.p_zigzag, a, n=5, h=80), 2),
                        ('Puentes', T.filas(T.p_arcos, a, n=5, h=60), 2), ('Tazas', T.filas(T.p_arcos, a, n=5, h=60, abajo=True), 2), ('Burbujas', T.filas(T.p_circulos, a), 2),
                        ('Resortes', T.filas(T.p_bucles, a, n=5, h=80), 3), ('Caracoles', T.filas(T.p_espiral, a, n=3, h=150), 3), ('Cajas', T.filas(T.p_cuadrados, a), 3)]:
        add('escribir', t, rp, ['lapiz'], nv, svg_)
    add('escribir', 'Carretera ancha', 'Lleva el lápiz del punto verde a la estrella sin tocar los bordes.', ['lapiz'], 1, T.camino(a, ancho=86, ciclos=1, amp=120))
    add('escribir', 'Carretera estrecha', 'Llega a la estrella sin salirte del camino.', ['lapiz'], 2, T.camino(a, ancho=46, ciclos=1.5, amp=90))
    add('escribir', 'Une los puntos', 'Une los puntos del 1 al 10 y descubre la figura.', ['lapiz'], 2, T.unir_puntos(a))
    for t, f in [('Calca la casa', 'casa'), ('Calca el pez', 'pez'), ('Calca el sol', 'sol'), ('Calca el árbol', 'arbol')]:
        add('escribir', t, 'Repasa la figura desde el punto verde y luego coloréala.', ['lapiz'], 2, T.calco(a, f))
    add('escribir', 'Vocales minúsculas', 'Repasa por dentro de cada vocal.', ['lapiz'], 3, T.texto_trazo(a, ['*a e i o u', 'a e i o u', 'a e i o u', 'a e i o u']))
    add('escribir', 'Vocales mayúsculas', 'Repasa por dentro de cada vocal.', ['lapiz'], 3, T.texto_trazo(a, ['*A E I O U', 'A E I O U', 'A E I O U', 'A E I O U']))
    add('escribir', 'Números del 0 al 9', 'Repasa cada número empezando arriba.', ['lapiz'], 3, T.texto_trazo(a, ['*0 1 2 3 4', '0 1 2 3 4', '*5 6 7 8 9', '5 6 7 8 9']))
    add('escribir', 'Abecedario a – j', 'Repasa cada letra; se apoyan en la línea azul.', ['lapiz'], 3, T.texto_trazo(a, ['*a b c d e', 'a b c d e', '*f g h i j', 'f g h i j']))
    add('escribir', 'Abecedario k – t', 'Repasa cada letra; se apoyan en la línea azul.', ['lapiz'], 3, T.texto_trazo(a, ['*k l m n ñ', 'k l m n ñ', '*o p q r s t', 'o p q r s t']))
    add('escribir', 'Abecedario u – z', 'Repasa las letras y escribe tu nombre en la última línea.', ['lapiz'], 3, T.texto_trazo(a, ['*u v w x y z', 'u v w x y z', 'u v w x y z', ' ']))
    assert len(F) == 100, len(F)
    return F

NIVEL = {1: 'Inicial', 2: 'Intermedio', 3: 'Avanzado'}

def main():
    css = base_css(AC, AC_S) + f"""
.portada {{ background: {C['crema']}; padding: 30mm 22mm }}
.portada h1 {{ font-size: 46pt; margin: 8mm 0 6mm }}
.fhead {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 6mm }}
.fhead h2 {{ font-size: 21pt; margin-top: 1.4mm }}
.instr {{ margin-top: 1.6mm; font-size: 10.5pt }}
.mats {{ display: flex; gap: 2mm; align-items: center; flex: none }}
.mats span {{ width: 13mm; height: 13mm; background: {C['crema']}; border-radius: 3mm; padding: 1.4mm }}
.area {{ margin-top: 4mm; width: 174mm; height: 192mm; border: 1.6px solid {C['linea']}; border-radius: 5mm; padding: 2mm; display: flex; align-items: center; justify-content: center }}
.area svg {{ max-height: 100% }}
.nivel {{ display: inline-flex; gap: 1.2mm; margin-left: 2mm; vertical-align: middle }}
.nivel i {{ width: 2.6mm; height: 2.6mm; border-radius: 50%; background: {C['linea']} }}
.nivel i.on {{ background: currentColor }}
.nombre {{ display: flex; gap: 8mm; font-size: 9.5pt; color: {C['gris']}; margin-top: 4mm }}
.nombre span {{ flex: 1; border-bottom: 1.4px solid {C['linea']}; padding-bottom: 1mm }}
.divisor {{ position: absolute; left: 22mm; right: 22mm; top: 54mm }}
.divisor h2 {{ font-size: 44pt; margin: 6mm 0 }}
.div-ic {{ width: 46mm; height: 46mm; background: #fff; border-radius: 10mm; padding: 6mm; margin-top: 12mm }}
.grande {{ position: absolute; right: 16mm; bottom: 20mm; font-size: 200pt; font-weight: 900; color: rgba(255,255,255,.22); line-height: 1; letter-spacing: -6px }}
.areas4 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 5mm; margin-top: 8mm }}
.areas4 div {{ border-radius: 5mm; padding: 5mm 6mm; color: #fff }}
.areas4 .ic {{ width: 16mm; height: 16mm; background: #fff; border-radius: 4mm; padding: 2mm; margin-bottom: 3mm }}
.matlist {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 4mm; margin-top: 5mm }}
.matlist div {{ background: {C['crema']}; border-radius: 4mm; padding: 4mm; text-align: center; font-weight: 800; font-size: 9.6pt }}
.matlist .ic {{ width: 16mm; height: 16mm; margin: 0 auto 2mm }}
.cien {{ display: grid; grid-template-columns: repeat(10, 1fr); gap: 2.4mm; margin-top: 6mm }}
.cien span {{ aspect-ratio: 1; border-radius: 50%; border: 2px solid; display: grid; place-items: center; font-weight: 800; font-size: 10pt }}
.plan td {{ height: 18mm; font-size: 9.5pt }}
"""
    pags = []; num = [0]
    def pag(body, cls=''):
        num[0] += 1
        pags.append(f'<section class="pag {cls}">{body}{pie(MARCA, str(num[0])) if num[0] > 1 else ""}</section>')

    F = fichas()
    muestra = ''.join(f'<div style="width:36mm;height:36mm;background:{col};border-radius:8mm;padding:6mm"><div style="background:#fff;border-radius:5mm;padding:2.6mm;width:100%;height:100%">{icono(ic)}</div></div>' for _, (_, col, ic, _) in AREAS.items())
    pag(f'''<div class="kicker">Paquete imprimible · Material para casa y terapia</div>
<h1>100 actividades<br>de motricidad fina</h1>
<p class="lead" style="max-width:150mm">Fichas imprimibles con ejercicios de pinza, cortar, apilar y escribir. <b>Imprime y empieza.</b></p>
<div style="display:flex;gap:3mm;margin-top:9mm;flex-wrap:wrap">{''.join(f'<span class="chip" style="background:{col}">{n} · 25 fichas</span>' for n, col, _, _ in AREAS.values())}</div>
<div style="position:absolute;right:22mm;bottom:30mm;display:grid;grid-template-columns:repeat(2,36mm);gap:7mm;transform:rotate(-4deg)">{muestra}</div>
<div style="position:absolute;left:22mm;bottom:22mm;font-weight:900;font-size:14pt">Byignis</div>''', 'portada')

    pag(f'''<div class="kicker">Imprime y empieza</div><h2 style="margin:3mm 0 4mm">Cómo usar este paquete</h2>
<p class="lead">Cada página es una actividad lista: la imprimes, juntas el material de la esquina superior y empiezas. Sin preparación.</p>
<div class="areas4">{''.join(f'<div style="background:{col}"><div class="ic">{icono(ic)}</div><h3>{n}</h3><p style="margin-top:1.4mm;font-size:9.6pt">{d}</p></div>' for n, col, ic, d in AREAS.values())}</div>
<h3 style="margin-top:8mm">Material que vas a necesitar</h3>
<div class="matlist">{''.join(f'<div><div class="ic">{icono(i)}</div>{t}</div>' for i, t in [('tijeras', 'Tijeras de punta roma'), ('pinza', 'Pinzas de ropa'), ('pompon', 'Pompones o bolitas'), ('bloques', 'Bloques o legos'), ('vaso', 'Vasos de plástico'), ('pegamento', 'Pegamento en barra'), ('cordon', 'Cordón o lana'), ('lapiz', 'Lápices y crayones')])}</div>
<div class="grid2" style="margin-top:7mm">
<div class="caja"><h4>Consejos de impresión</h4><ul class="lista"><li>Tamaño A4 o carta, "ajustar a la página".</li><li>Las fichas de pinza y apilar duran más en cartulina o plastificadas.</li><li>Las fichas de escribir se reutilizan dentro de un folio con marcador borrable.</li></ul></div>
<div class="caja acento"><h4>Seguridad</h4><ul class="lista"><li>Pompones, bolitas y piezas pequeñas pueden causar asfixia: siempre con supervisión, especialmente en menores de 3 años.</li><li>Usa tijeras infantiles de punta roma.</li></ul></div></div>
<p class="nota" style="margin-top:6mm">Los niveles (● ● ●) indican dificultad: inicial, intermedio y avanzado. Este material es de apoyo y no sustituye la evaluación de un terapeuta ocupacional.</p>''')

    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
    plan_filas = ''.join(f'<tr><td style="font-weight:800">Semana {s}</td>' + ''.join(f'<td>{a} {s + k*5 if False else ""}</td>' for k, a in enumerate(['', '', '', '', ''])) + '</tr>' for s in range(1, 6))
    pag(f'''<div class="kicker">Plan sugerido</div><h2 style="margin:3mm 0 4mm">20 minutos al día, 5 semanas</h2>
<p class="lead">Una ficha de cada área por día: pinza, cortar, apilar y escribir. En 25 días hábiles completas las 100.</p>
<table class="reg plan" style="margin-top:7mm"><tr><th>Semana</th>{''.join(f'<th>{d}</th>' for d in dias)}</tr>{plan_filas}</table>
<div class="grid2" style="margin-top:7mm">
<div class="caja"><h4>Orden recomendado</h4><p><b>1.</b> Pinza (calienta los dedos) → <b>2.</b> Apilar → <b>3.</b> Cortar → <b>4.</b> Escribir (lo más exigente, al final cuando la mano ya trabajó).</p></div>
<div class="caja"><h4>Si una ficha cuesta mucho</h4><p>Vuelve a una de nivel ● inicial de la misma área. Terminar con éxito motiva más que forzar.</p></div></div>
<p class="nota" style="margin-top:5mm">Escribe en cada casilla los números de las fichas que hicieron ese día.</p>''')

    orden = ['pinza', 'cortar', 'apilar', 'escribir']
    num_ficha = 0
    for ia, area in enumerate(orden, 1):
        nombre, col, ic, desc = AREAS[area]
        pag(f'''<div class="divisor"><div class="kicker">Área {ia} · 25 fichas</div><h2>{nombre}</h2><p class="lead" style="max-width:140mm">{desc}</p><div class="div-ic">{icono(ic)}</div></div><div class="grande">{ia:02d}</div>''', f'color" style="background:{col}')
        for k, f in enumerate([x for x in F if x['area'] == area], 1):
            num_ficha += 1
            niv = ''.join(f'<i class="{"on" if j < f["n"] else ""}"></i>' for j in range(3))
            mats = ''.join(f'<span>{icono(m)}</span>' for m in f['m'])
            pag(f'''<div class="fhead"><div><div class="kicker" style="color:{col}">{nombre} · Ficha {k} de 25 · N.º {num_ficha} <span class="nivel" style="color:{col}">{niv}</span></div>
<h2>{e(f["t"])}</h2><p class="instr">{e(f["i"])}</p></div><div class="mats">{mats}</div></div>
<div class="area">{f["svg"]}</div>
<div class="nombre"><span>Nombre:</span><span>Fecha:</span><span>¿Cómo me fue? ☆ ☆ ☆</span></div>''')

    colores = [AREAS[a][1] for a in orden]
    circ = ''.join(f'<span style="border-color:{colores[(i-1)//25]};color:{colores[(i-1)//25]}">{i}</span>' for i in range(1, 101))
    pag(f'''<div class="kicker">Para imprimir</div><h2 style="margin:3mm 0 3mm">Mi camino de las 100</h2>
<p class="lead">Colorea un círculo cada vez que termines una ficha. ¿Llegarás a las 100?</p><div class="cien">{circ}</div>
<div style="display:flex;gap:6mm;margin-top:6mm;font-weight:800;font-size:9.6pt">{''.join(f'<span style="color:{AREAS[a][1]}">● {AREAS[a][0]} ({i*25 + 1}–{i*25 + 25})</span>' for i, a in enumerate(orden))}</div>''')

    pag(f'''<div style="border:3mm solid {AC};border-radius:6mm;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:14mm;background:{C['crema']}">
<div style="width:34mm">{icono("estrella")}</div><div class="kicker" style="margin-top:6mm">Diploma</div><h1 style="font-size:38pt;margin:4mm 0">¡100 actividades!</h1>
<p class="lead">Este diploma es para</p><div style="width:120mm;border-bottom:2px solid {C['tinta']};height:14mm"></div>
<p class="lead" style="margin-top:8mm">por completar las 100 actividades de motricidad fina con esfuerzo y paciencia.</p>
<div style="display:flex;gap:30mm;margin-top:18mm"><div style="width:50mm;border-top:1.6px solid {C['tinta']};padding-top:2mm" class="nota">Fecha</div><div style="width:50mm;border-top:1.6px solid {C['tinta']};padding-top:2mm" class="nota">Firma</div></div></div>''')

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out'); os.makedirs(out, exist_ok=True)
    hp = os.path.join(out, '100-actividades-motricidad-fina.html')
    open(hp, 'w').write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(pags)}</body></html>')
    print('paginas', len(pags), 'fichas', len(F))
    return hp

if __name__ == '__main__':
    import sys
    hp = main()
    if 'snap' in sys.argv:
        snapshot(hp, hp.replace('.html', ''), [int(x) for x in sys.argv[2:]])
    else:
        render_pdf(hp, hp.replace('.html', '.pdf'))
