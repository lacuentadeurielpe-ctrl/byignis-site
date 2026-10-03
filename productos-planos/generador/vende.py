"""Libro 3: Vende los muebles que fabricas — guía visual para ganar dinero con tu taller."""
import os
from tienda_base import T, e, css_base, pie
from common import render_pdf, snapshot
from escenas import escena, META, DECO_BASE

HERE = os.path.dirname(os.path.abspath(__file__))
MARCA = 'Vende los muebles que fabricas'

def img(code, estilo=''):
    return f'<img src="file://{HERE}/iso/{code}.png" style="{estilo}">'

TOP20 = [
 ('SAL-01', 'Mueble de TV', 'Todos tienen TV: es el mueble más buscado en Marketplace.'),
 ('SAL-10', 'Mesa de centro', 'Fácil de fabricar, se vende rápido y se envía sin desarmar.'),
 ('SAL-19', 'Repisas flotantes', 'Bajo costo, alto margen. Ideal para empezar.'),
 ('SAL-17', 'Estante de cubos', 'Versátil: sala, cuarto, oficina. Se vende todo el año.'),
 ('COM-01', 'Mesa de comedor', 'Ticket alto. Muy pedida a medida.'),
 ('COM-09', 'Banca de comedor', 'Complemento perfecto para vender junto a la mesa.'),
 ('COM-14', 'Taburetes', 'Se venden de a 2 o 4: multiplicas la venta.'),
 ('COM-17', 'Aparador', 'Mueble de lucimiento, muy fotogénico.'),
 ('DOR-09', 'Mesas de noche', 'Se venden en pares. Producción en serie.'),
 ('DOR-12', 'Cómoda', 'Necesidad básica en cada dormitorio.'),
 ('DOR-16', 'Ropero', 'Ticket alto; muy pedido a medida en departamentos.'),
 ('DOR-20', 'Tocador', 'Regalo frecuente; gran demanda en fechas especiales.'),
 ('INF-11', 'Organizador de juguetes', 'Los padres compran organización todo el año.'),
 ('INF-13', 'Baúl juguetero', 'Regalo de cumpleaños y Navidad.'),
 ('COC-19', 'Carrito auxiliar', 'Práctico para cocinas pequeñas, se vende solo.'),
 ('REC-05', 'Banca zapatera', 'Resuelve el desorden de la entrada: vende por necesidad.'),
 ('REC-13', 'Perchero con repisa', 'Muy barato de fabricar, ideal para stock.'),
 ('EST-01', 'Escritorio', 'El trabajo y el estudio en casa disparan la demanda.'),
 ('EXT-12', 'Huerto elevado', 'Tendencia creciente: cultivar en casa.'),
 ('EXT-10', 'Maceteros', 'Se venden en sets; gran margen en primavera.'),
]

def main():
    css = css_base() + f"""
.cap {{ display: flex; align-items: center; gap: 4mm; margin-bottom: 3mm }}
.cap .n {{ font-family: 'Barlow Condensed'; font-weight: 700; font-size: 44pt; color: {T['ember']}; line-height: .9 }}
.costos {{ display: flex; height: 16mm; border-radius: 3mm; overflow: hidden; margin: 5mm 0 2mm }}
.costos div {{ display: grid; place-items: center; color: #fff; font-size: 10pt; font-weight: 700; text-align: center; line-height: 1.1; padding: 0 1mm }}
.leyenda {{ display: grid; grid-template-columns: 1fr 1fr; gap: 2mm 6mm; font-size: 9.6pt; margin-top: 3mm }}
.leyenda span i {{ display: inline-block; width: 3.4mm; height: 3.4mm; border-radius: 1mm; margin-right: 2mm; vertical-align: -.4mm }}
.formula {{ background: {T['ink']}; color: #fff; border-radius: 5mm; padding: 7mm; text-align: center; font-family: 'Barlow Condensed'; font-size: 22pt; margin: 6mm 0 }}
.formula b {{ color: {T['ember']} }}
.niveles {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4mm }}
.niveles div {{ border: 1.6px solid {T['line']}; border-radius: 4mm; padding: 5mm; text-align: center }}
.niveles div.on {{ border-color: {T['ember']}; background: {T['sand']} }}
.niveles b {{ display: block; font-family: 'Barlow Condensed'; font-size: 26pt; color: {T['ember']} }}
.top {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; margin-top: 5mm }}
.top > div {{ display: grid; grid-template-columns: 36mm 1fr; gap: 3.5mm; align-items: center; border: 1.4px solid {T['line']}; border-radius: 4mm; padding: 3mm 4mm 3mm 3mm; height: 41mm }}
.top .im {{ width: 36mm; height: 35mm; background: {T['sand']}; border-radius: 3mm; padding: 2.5mm; overflow: hidden }}
.top .im img {{ width: 100%; height: 100%; object-fit: contain; display: block }}
.top b {{ font-family: 'Barlow Condensed'; font-size: 13pt; display: block }}
.top p {{ font-size: 9.2pt; color: {T['muted']}; line-height: 1.3 }}
.top .rk {{ color: {T['ember']}; font-family: 'Barlow Condensed'; font-weight: 700 }}
.fotos {{ display: grid; grid-template-columns: 1fr 1fr; gap: 6mm; margin-top: 6mm }}
.foto {{ border-radius: 4mm; overflow: hidden; position: relative; height: 74mm; display: grid; place-items: center }}
.foto img {{ max-height: 80%; max-width: 80% }}
.foto .tag {{ position: absolute; top: 3mm; left: 3mm; color: #fff; font-weight: 700; font-size: 9pt; padding: 1mm 3mm; border-radius: 99px }}
.si {{ background: #F4F2EE }} .si .tag {{ background: #3E8E4E }}
.no {{ background: #6B6258 }} .no .tag {{ background: {T['ember']} }}
.no img {{ filter: brightness(.55) saturate(.6) blur(.6px); transform: rotate(-8deg) }}
.no::after {{ content: ''; position: absolute; inset: 0; background: radial-gradient(circle at 62% 38%, rgba(255,255,230,.75) 0 4mm, rgba(255,255,200,.18) 14mm, transparent 30mm), repeating-linear-gradient(45deg, rgba(0,0,0,.08) 0 6mm, rgba(255,255,255,.04) 6mm 12mm) }}
.angulos {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 3mm; margin-top: 5mm }}
.angulos > div {{ text-align: center; font-size: 8.8pt; font-weight: 600 }}
.angulos .f {{ height: 44mm; background: #F4F2EE; border-radius: 3mm; display: grid; place-items: center; overflow: hidden; margin-bottom: 1.4mm }}
.angulos .f img {{ max-width: 85%; max-height: 85% }}
.movil {{ width: 68mm; border: 3mm solid {T['ink']}; border-radius: 9mm; padding: 4mm 3mm; background: #fff; box-shadow: 0 4mm 10mm rgba(0,0,0,.15) }}
.movil .barra {{ font-size: 8pt; font-weight: 700; color: {T['muted']}; margin-bottom: 2mm }}
.anuncio .ph {{ height: 42mm; background: #F4F2EE; border-radius: 2mm; display: grid; place-items: center }}
.anuncio .ph img {{ max-width: 85%; max-height: 85% }}
.anuncio .pr {{ font-family: 'Barlow Condensed'; font-weight: 700; font-size: 17pt; margin-top: 2mm }}
.anuncio .ti {{ font-weight: 700; font-size: 9.4pt }}
.anuncio .de {{ font-size: 7.8pt; color: {T['muted']}; margin-top: 1mm; line-height: 1.35 }}
.ig {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1mm; margin-top: 2mm }}
.ig div {{ aspect-ratio: 1; background: #F4F2EE; display: grid; place-items: center; overflow: hidden }}
.ig img {{ max-width: 85%; max-height: 85% }}
.ig svg {{ height: 100%; width: auto }}
.chat {{ background: #EFE7DD; border-radius: 3mm; padding: 3mm; display: flex; flex-direction: column; gap: 2mm; font-size: 8.2pt; line-height: 1.35 }}
.b {{ max-width: 85%; padding: 2mm 3mm; border-radius: 3mm; background: #fff }}
.b.yo {{ align-self: flex-end; background: #D9FDD3 }}
.plantilla {{ border: 1.6px solid {T['line']}; border-radius: 4mm; padding: 7mm }}
.linea {{ border-bottom: 1.4px solid {T['line']}; height: 9mm }}
.semanas {{ display: grid; grid-template-columns: 1fr 1fr; gap: 5mm; margin-top: 6mm }}
.semanas > div {{ border: 1.4px solid {T['line']}; border-radius: 4mm; padding: 6mm; min-height: 62mm }}
.semanas h3 {{ color: {T['ember']} }}
.errores {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; margin-top: 5mm }}
.errores div {{ background: {T['sand']}; border-radius: 4mm; padding: 5.5mm 6mm; font-size: 10pt; min-height: 47mm }}
.errores b {{ display: block; font-family: 'Barlow Condensed'; font-size: 14pt }}
.errores span {{ color: {T['ember']}; font-family: 'Barlow Condensed'; font-weight: 700; font-size: 18pt; float: right; line-height: 1 }}
"""
    pags = []; num = [0]
    def pag(body, cls=''):
        num[0] += 1
        pags.append(f'<section class="pag {cls}">{body}{pie(MARCA, num[0]) if num[0] > 1 else ""}</section>')
    def capitulo(n, titulo, lead):
        return f'<div class="cap"><span class="n">{n:02d}</span><div><div class="kicker">Capítulo {n}</div><h2>{titulo}</h2></div></div><p class="lead">{lead}</p>'

    # Portada
    piezas = [('SAL-01', 20, 150, 92, -4, 'Vendido'), ('COM-01', 108, 140, 86, 5, '$$$'), ('DOR-12', 22, 214, 70, 3, 'Pedido'), ('EXT-12', 98, 212, 84, -5, 'Vendido')]
    tags = ''.join(f'<div style="position:absolute;left:{l}mm;top:{t}mm;width:{w}mm;height:{w*0.72:.0f}mm;background:#fff;border-radius:4mm;transform:rotate({r}deg);display:grid;place-items:center;box-shadow:0 5mm 12mm rgba(0,0,0,.35)">{img(c, "max-width:82%;max-height:78%")}<span style="position:absolute;top:3mm;right:3mm;background:{T["ember"]};color:#fff;font-weight:700;font-size:9pt;padding:1mm 3mm;border-radius:99px">{tg}</span></div>' for c, l, t, w, r, tg in piezas)
    pag(f'''<div class="kicker">Byignis · Guía de negocio</div><h1 style="margin:7mm 0 5mm">Vende los<br>muebles que<br>fabricas</h1>
<p class="lead" style="max-width:150mm">Calcula tus costos, pon el precio justo, toma fotos que venden y consigue clientes en Marketplace, Instagram y WhatsApp. Convierte tu taller en un ingreso.</p>{tags}''', 'oscura')

    pag(f'''<div class="kicker">Introducción</div><h2 style="margin:3mm 0 4mm">Tu taller puede ser un negocio</h2>
<p class="lead">Cada casa necesita muebles, y cada vez más personas prefieren muebles a medida, de madera real y hechos cerca. Con los planos correctos y un método simple, puedes vender desde tu casa.</p>
<h3 style="margin-top:8mm">Tres formas de vender</h3>
<div class="grid3" style="margin-top:4mm">
<div class="caja"><h4>A pedido</h4><p>El cliente elige el mueble, adelanta una parte y lo fabricas. Sin riesgo de stock. Ideal para empezar.</p></div>
<div class="caja"><h4>Stock</h4><p>Fabricas en serie los muebles que más salen (repisas, mesas de noche) y los vendes listos. Entregas rápidas.</p></div>
<div class="caja"><h4>Catálogo</h4><p>Muestras fotos de modelos y medidas. El cliente elige color y tamaño. Combina lo mejor de ambos.</p></div></div>
<div class="caja ember" style="margin-top:8mm"><h4 style="color:#fff">Importante: licencia de uso</h4><p style="font-size:11pt">Los planos byignis son para uso personal. Para fabricar y vender los muebles a terceros necesitas la <b>licencia comercial byignis</b>, que te autoriza a fabricar sin límite los 200 modelos y venderlos con tu marca.</p></div>
<h3 style="margin-top:8mm">Lo que vas a aprender</h3>
<ul class="lista" style="margin-top:3mm;font-size:11pt"><li>Calcular cuánto te cuesta de verdad cada mueble.</li><li>Poner un precio que te deje ganancia.</li><li>Los 20 muebles que más se venden.</li><li>Tomar fotos con tu celular que hacen vender.</li><li>Vender en Marketplace, Instagram y WhatsApp, con textos listos para copiar.</li><li>Cotizar, cobrar, entregar y dar garantía como un profesional.</li></ul>''')

    # Costos
    partes = [('Materiales', 45, T['ember']), ('Herrajes y cantos', 12, '#E07B3C'), ('Corte y transporte', 8, '#C9971B'), ('Tu tiempo', 25, T['ink']), ('Gastos del taller', 10, '#6B645C')]
    barra = ''.join(f'<div style="width:{p}%;background:{c}">{p}%</div>' for t, p, c in partes)
    leyenda = ''.join(f'<span><i style="background:{c}"></i>{t} · <b>{p}%</b></span>' for t, p, c in partes)
    filas = [('Tableros de melamina 18 mm', '2 planchas', '120'), ('Fondo HDF / MDF 3 mm', '1 plancha', '25'), ('Cubrecanto', '12 m', '15'), ('Bisagras, correderas, tiradores', '1 juego', '30'),
             ('Tornillos, confirmat, tarugos', '—', '8'), ('Servicio de corte', '—', '20'), ('Transporte de material', '—', '15'), ('Tu tiempo (4 h × 25)', '4 h', '100'), ('Gastos del taller (10 %)', '—', '33')]
    tabla = ''.join(f'<tr><td>{a}</td><td>{b}</td><td style="text-align:right">$ {c}</td></tr>' for a, b, c in filas)
    pag(f'''{capitulo(1, 'Calcula tu costo real', 'El error más común es cobrar solo los materiales. Tu tiempo, la luz, las brocas y el transporte también cuestan.')}
<div class="costos">{barra}</div><div class="leyenda" style="grid-template-columns:1fr 1fr 1fr">{leyenda}</div><p class="nota" style="margin-top:2mm">Ejemplo de cómo se reparte el costo de un mueble de melamina.</p>
<h3 style="margin-top:7mm">Ejemplo: Mueble de TV nórdico 120 (SAL-01)</h3>
<table class="t" style="margin-top:3mm"><tr><th>Concepto</th><th>Cantidad</th><th style="text-align:right">Costo</th></tr>{tabla}
<tr><td colspan="2"><b>Costo total</b></td><td style="text-align:right;font-weight:700;font-size:12pt">$ 366</td></tr></table>
<p class="nota" style="margin-top:3mm">Los montos son un ejemplo en unidades de tu moneda: reemplázalos con los precios de tu ciudad. Cada plano byignis trae la lista exacta de materiales y herrajes, así que solo tienes que cotizarla.</p>
<div class="caja" style="margin-top:5mm"><h4>No olvides tu tiempo</h4><p>Define cuánto vale tu hora (por ejemplo, lo que ganarías en un trabajo similar) y multiplícalo por las horas que indica el plano. Si no cobras tu tiempo, estás trabajando gratis.</p></div>''')

    pag(f'''{capitulo(2, 'Pon el precio justo', 'El precio no es el costo: es el costo más la ganancia que te permite crecer.')}
<div class="formula">Precio = Costo total × <b>1,5 a 2</b></div>
<p>Un margen de 50 % a 100 % sobre el costo es lo habitual en muebles hechos a mano. Con el ejemplo anterior (costo $ 366):</p>
<div class="niveles" style="margin-top:5mm"><div>{img('SAL-01', 'width:100%;height:30mm;object-fit:contain;filter:grayscale(.5)')}<span class="nota">Mínimo</span><b>$ 550</b><p>× 1,5 · competir por precio</p><p class="nota">Herrajes simples, sin extras.</p></div><div class="on">{img('SAL-01', 'width:100%;height:30mm;object-fit:contain')}<span class="nota">Recomendado</span><b>$ 650</b><p>× 1,8 · buen margen</p><p class="nota">Cierre suave y cantos gruesos.</p></div><div>{img('SAL-01', 'width:100%;height:30mm;object-fit:contain;filter:sepia(.35) saturate(1.4) brightness(.9)')}<span class="nota">Premium</span><b>$ 730</b><p>× 2 · acabado especial</p><p class="nota">Madera o laca, tiradores premium.</p></div></div>
<h3 style="margin-top:8mm">Cómo saber si tu precio está bien</h3>
<ul class="lista" style="margin-top:3mm"><li><b>Mira la competencia:</b> busca el mismo mueble en Marketplace y anota 5 precios. Ubícate en el medio.</li>
<li><b>Compara con tiendas:</b> un mueble hecho a medida y de madera real puede costar igual o más que uno de tienda.</li>
<li><b>Ofrece 3 opciones:</b> básico, estándar y premium (por ejemplo, con mejor acabado o herrajes de cierre suave). La mayoría elige el del medio.</li>
<li><b>Precios redondos y claros:</b> $ 650 se entiende mejor que $ 647.</li></ul>
<div class="caja ember" style="margin-top:6mm"><p style="font-size:11pt"><b>Nunca bajes el precio sin quitar algo.</b> Si el cliente pide descuento, ofrécele una versión más simple (menos cajones, otro herraje) en lugar de regalar tu ganancia.</p></div>''')

    # Top 20
    for k in (0, 10):
        items = ''.join(f'<div><div class="im">{img(c)}</div><div><span class="rk">#{k + i + 1}</span> <b style="display:inline">{n}</b><p>{e(d)}</p><p style="color:{T["ink"]};font-weight:600">Plano {c} · {META[c]["level"]}</p></div></div>' for i, (c, n, d) in enumerate(TOP20[k:k+10]))
        cab = capitulo(3, 'Los 20 muebles que más se venden', 'Empieza por estos: tienen demanda todo el año y están en tu catálogo de 200 planos.') if k == 0 else '<div class="kicker">Capítulo 3 · continuación</div><h2 style="margin:2mm 0 2mm">Los 20 muebles que más se venden</h2>'
        pag(f'{cab}<div class="top">{items}</div>')

    # Fotos
    c = 'SAL-05'
    pag(f'''{capitulo(4, 'Fotos que venden', 'En internet, la foto es tu vitrina. Con tu celular y luz natural puedes lograr fotos profesionales.')}
<div class="fotos"><div class="foto si"><span class="tag">ASÍ SÍ</span>{img(c)}</div><div class="foto no"><span class="tag">ASÍ NO</span>{img(c)}</div></div>
<div class="grid2" style="margin-top:5mm"><div><h4>Así sí</h4><ul class="lista"><li>Luz natural de día, cerca de una ventana.</li><li>Fondo limpio: pared lisa y piso despejado.</li><li>Cámara a la altura del mueble, recta.</li><li>Mueble limpio, sin polvo ni virutas.</li></ul></div>
<div><h4>Así no</h4><ul class="lista"><li>De noche o con flash directo.</li><li>Taller desordenado de fondo.</li><li>Foto torcida o desde muy arriba.</li><li>Foto borrosa o muy lejos.</li></ul></div></div>
<h3 style="margin-top:7mm">Las 4 fotos que no pueden faltar</h3>
<div class="angulos"><div><div class="f">{img('SAL-05')}</div>1. Vista 3/4 (la principal)</div><div><div class="f">{img('SAL-05', 'transform:scaleX(-1)')}</div>2. El otro lado</div>
<div><div class="f" style="background:#E9E3D9">{img('SAL-05', 'max-width:180%;max-height:180%;transform:translate(10%,8%)')}</div>3. Detalle de acabado</div><div><div class="f">{escena('SAL-05', 'nordico', DECO_BASE['nordico'], x_centro=500)}</div>4. En un ambiente</div></div>
<div class="caja" style="margin-top:7mm;display:grid;grid-template-columns:1fr 1fr 1fr;gap:5mm;font-size:9.6pt"><div><h4>Hora</h4>Entre 10 y 16 h, con luz de ventana de lado. Apaga las luces del cuarto.</div><div><h4>Celular</h4>Limpia el lente, usa la cámara principal (1×) y no uses zoom digital.</div><div><h4>Edición</h4>Solo endereza y sube un poco el brillo. Nada de filtros fuertes.</div></div>''')

    # Marketplace / Instagram / WhatsApp
    pag(f'''{capitulo(5, 'Dónde vender', 'Tres canales gratuitos que funcionan muy bien para muebles. Empieza por Marketplace y WhatsApp.')}
<div style="display:grid;grid-template-columns:72mm 1fr;gap:8mm;margin-top:6mm;align-items:start">
<div class="movil anuncio"><div class="barra">Marketplace</div><div class="ph">{img('COM-01')}</div><div class="pr">$ 1.250</div><div class="ti">Mesa de comedor 4 personas en madera de pino · 120 × 80 cm</div><div class="de">Hecha a mano en madera maciza. Acabado natural con aceite protector. Entrega en 7 días. También a medida. ¡Escríbeme!</div></div>
<div><h3>Facebook Marketplace</h3><ul class="lista" style="margin-top:2mm"><li><b>Título con lo que la gente busca:</b> tipo de mueble + material + medida.</li><li><b>Precio visible</b> siempre. Los anuncios sin precio reciben menos mensajes.</li><li><b>4 a 6 fotos</b> como las del capítulo anterior.</li><li><b>Publica en grupos</b> de compra y venta de tu ciudad.</li><li><b>Renueva el anuncio</b> cada semana para que vuelva a aparecer arriba.</li></ul>
<div class="caja" style="margin-top:4mm"><h4>Texto modelo para copiar</h4><p style="font-size:9.6pt">[Mueble] en [material] · [medidas]<br>Hecho a mano, nuevo, listo para entregar en [X] días.<br>Disponible en [colores]. Hago medidas especiales.<br>Precio: $ ___ · Entrega en [zona].<br>¡Escríbeme para más fotos!</p></div></div></div>
<h3 style="margin-top:9mm">Títulos que venden</h3>
<div class="grid2" style="margin-top:3mm"><div class="caja borde"><h4 style="color:#A33">Así no</h4><ul class="lista"><li>"Vendo mueble"</li><li>"Mesa linda barata!!!"</li><li>"Mueble de madera, consultar"</li></ul></div>
<div class="caja borde" style="border-color:#3E8E4E"><h4 style="color:#3E8E4E">Así sí</h4><ul class="lista"><li>"Mueble de TV 120 cm melamina roble"</li><li>"Mesa de centro pino macizo 90 × 50"</li><li>"Repisas flotantes set x3 · a medida"</li></ul></div></div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;margin-top:7mm;text-align:center">{''.join(f'<div class="caja" style="padding:4mm 3mm"><b style="font-family:Barlow Condensed;font-size:22pt;color:{T["ember"]}">{a}</b><p style="font-size:9pt">{b}</p></div>' for a, b in [('1', 'Publica con precio y 4+ fotos'), ('2', 'Comparte en 5 grupos locales'), ('3', 'Responde en menos de 1 hora'), ('4', 'Pasa la charla a WhatsApp')])}</div>''')

    grid = ''.join(f'<div>{img(c)}</div>' if i % 3 != 1 else f'<div>{escena(c, st, DECO_BASE[st], x_centro=500)}</div>' for i, (c, st) in enumerate([('SAL-17', 'costero'), ('DOR-14', 'nordico'), ('EST-03', 'moderno'), ('INF-11', 'infantil'), ('SAL-15', 'tropical'), ('REC-08', 'nordico'), ('COM-17', 'clasico'), ('EXT-02', 'tropical'), ('SAL-19', 'boho')]))
    pag(f'''<div class="kicker">Capítulo 5 · continuación</div><h2 style="margin:2mm 0 5mm">Instagram y WhatsApp</h2>
<div style="display:grid;grid-template-columns:72mm 1fr;gap:8mm;align-items:start">
<div class="movil"><div class="barra">@tutaller.muebles</div><div style="display:flex;gap:2mm;align-items:baseline;font-size:7pt;white-space:nowrap"><b style="font-family:Barlow Condensed;font-size:14pt">24</b> publicaciones <b style="font-family:Barlow Condensed;font-size:14pt;margin-left:2mm">1,2k</b> seguidores</div><div class="ig">{grid}</div></div>
<div><h3>Instagram y Facebook</h3><ul class="lista" style="margin-top:2mm"><li><b>Alterna</b> fotos del mueble solo y del mueble en un ambiente decorado.</li><li><b>Muestra el proceso:</b> videos cortos cortando, armando y entregando. Generan confianza.</li><li><b>Antes y después:</b> el espacio vacío y luego con tu mueble.</li><li><b>Testimonios:</b> pide a cada cliente una foto con su mueble.</li><li><b>Link a WhatsApp</b> en la biografía para cotizar.</li></ul></div></div>
<div style="display:grid;grid-template-columns:72mm 1fr;gap:8mm;align-items:start;margin-top:8mm">
<div class="movil"><div class="barra">WhatsApp Business</div><div class="chat"><div class="b">Hola, vi la mesa de comedor en Marketplace. ¿Sigue disponible?</div><div class="b yo">¡Hola! Sí, está disponible. ¿Para cuántas personas la necesitas? La hago en 120 o 160 cm 😊</div><div class="b">Para 6 personas</div><div class="b yo">Te recomiendo la de 160 × 90 cm. Cuesta $ 1.650 e incluye acabado con aceite protector. Te envío fotos 📷</div><div class="b">¡Me encanta! ¿Cómo pago?</div><div class="b yo">Con el 50 % de adelanto la empiezo hoy y te la entrego en 7 días. ✅</div></div></div>
<div><h3>WhatsApp Business</h3><ul class="lista" style="margin-top:2mm"><li><b>Catálogo:</b> sube tus muebles con foto, precio y medidas.</li><li><b>Respuestas rápidas</b> para precios, medidas y formas de pago.</li><li><b>Responde en menos de 1 hora:</b> el que responde primero, vende.</li><li><b>Pregunta para recomendar:</b> "¿para cuántas personas?", "¿qué medida tiene tu espacio?".</li><li><b>Cierra con un paso claro:</b> adelanto, fecha de entrega y dirección.</li></ul></div></div>''')

    # Cotizar, entregar, garantía
    pag(f'''{capitulo(6, 'Cotiza, cobra y entrega como profesional', 'La forma en que cotizas y entregas define si el cliente vuelve y te recomienda.')}
<div style="display:flex;align-items:flex-start;margin-top:6mm">{''.join(f'<div style="flex:1;text-align:center;position:relative"><div style="width:13mm;height:13mm;margin:0 auto;border-radius:50%;background:{T["ember"] if i % 2 == 0 else T["ink"]};color:#fff;display:grid;place-items:center;font-family:Barlow Condensed;font-weight:700;font-size:15pt;position:relative;z-index:1">{i + 1}</div>' + (f'<div style="position:absolute;top:6.5mm;left:50%;width:100%;border-top:1.6px dashed {T["line"]}"></div>' if i < 5 else '') + f'<p style="font-size:8.8pt;font-weight:600;margin-top:2mm;line-height:1.25">{t}</p></div>' for i, t in enumerate(['Cotización por escrito', 'Adelanto 50 %', 'Fabricación con fotos de avance', 'Entrega e instalación', 'Cobro del saldo', 'Reseña y recomendación']))}</div>
<div class="grid2" style="margin-top:6mm"><div><h4>Al cotizar</h4><ol class="pasos"><li>Pide medidas del espacio y una foto del lugar.</li><li>Recomienda el modelo y el color adecuados.</li><li>Envía la cotización por escrito (usa la plantilla de este libro).</li><li>Indica tiempo de entrega y forma de pago.</li><li>Haz seguimiento a los 2 días si no responde.</li></ol></div>
<div><h4>Al cobrar</h4><ol class="pasos"><li>Pide un adelanto del 50 % para comprar materiales.</li><li>El saldo, contra entrega.</li><li>Acepta transferencia y billeteras digitales.</li><li>Entrega siempre un comprobante.</li></ol></div></div>
<div class="grid2" style="margin-top:6mm"><div><h4>Al entregar</h4><ul class="lista"><li>Protege el mueble con cartón o mantas.</li><li>Lleva herramientas para ajustes y nivelado.</li><li>Fija a la pared los muebles altos.</li><li>Explica el cuidado del acabado.</li><li>Pide una foto y una reseña.</li></ul></div>
<div><h4>Garantía</h4><ul class="lista"><li>Ofrece 3 a 6 meses en herrajes y armado.</li><li>Ponla por escrito en la cotización.</li><li>Atiende rápido cualquier reclamo: una buena solución genera más clientes que un mueble perfecto.</li></ul></div></div>
<div class="caja ember" style="margin-top:6mm"><p style="font-size:11pt"><b>Recomendación:</b> un cliente feliz te trae, en promedio, más clientes. Regala un detalle (un posavasos con tu logo, un aceite de mantenimiento) y pide que te recomiende.</p></div>''')

    errores = [('Cobrar solo los materiales', 'Tu tiempo y los gastos del taller también se cobran.'), ('No pedir adelanto', 'Sin adelanto, el riesgo es todo tuyo.'), ('Fotos de noche y en el taller', 'Una mala foto espanta compradores.'), ('Responder tarde', 'Si no respondes rápido, compran a otro.'),
               ('Prometer plazos imposibles', 'Mejor entregar antes de lo prometido que tarde.'), ('No medir en el lugar', 'Un mueble que no entra es una pérdida doble.'), ('Bajar el precio sin quitar nada', 'Ofrece una versión más simple, no menos ganancia.'), ('No pedir reseñas', 'Las recomendaciones son tu mejor publicidad gratis.')]
    sol = ['Usa la hoja de costos de este libro en cada mueble.', 'Pide 50 % antes de comprar materiales.', 'Fotografía de día, junto a la ventana.', 'Activa respuestas rápidas en WhatsApp Business.', 'Calcula las horas del plano y suma 2 días de margen.', 'Pide medidas y una foto del espacio antes de cotizar.', 'Ten siempre una versión básica lista para ofrecer.', 'Pide la reseña el mismo día de la entrega.']
    er = ''.join(f'<div><span>{i:02d}</span><b>{t}</b>{d}<p style="margin-top:2.4mm;padding-top:2.4mm;border-top:1.2px solid {T["line"]};color:#2F7A3F;font-weight:600">✓ {sol[i - 1]}</p></div>' for i, (t, d) in enumerate(errores, 1))
    pag(f'{capitulo(7, "8 errores que te hacen perder dinero", "Evítalos desde el primer día y tu negocio crecerá más rápido.")}<div class="errores">{er}</div>')

    semanas = [('Semana 1 · Prepara', ['Elige 3 muebles del top 20.', 'Cotiza materiales en tu ciudad.', 'Calcula costos y precios con este libro.', 'Crea tu WhatsApp Business y tu página.']),
               ('Semana 2 · Fabrica tu muestra', ['Fabrica 1 o 2 muebles de muestra.', 'Toma las 4 fotos de cada uno.', 'Decora y fotografía uno en ambiente.', 'Sube el catálogo a WhatsApp.']),
               ('Semana 3 · Publica', ['Publica en Marketplace y 5 grupos locales.', 'Publica 3 veces en Instagram.', 'Cuéntale a familiares y amigos.', 'Responde todo en menos de 1 hora.']),
               ('Semana 4 · Vende y mejora', ['Cierra tus primeras ventas con adelanto.', 'Entrega y pide reseñas con foto.', 'Anota qué preguntan más los clientes.', 'Ajusta precios y elige el siguiente mueble.'])]
    sm = ''.join(f'<div><h3>{t}</h3><ul class="lista" style="margin-top:2mm">{"".join(f"<li>{x}</li>" for x in xs)}</ul></div>' for t, xs in semanas)
    cols = ['#F3D9CE', '#E9A98C', T['ember'], T['ink']]
    cal = ''.join(f'<div style="height:11mm;border-radius:2mm;background:{cols[min((d - 1) // 7, 3)]};color:{"#fff" if d > 14 else T["ink"]};display:grid;place-items:center;font-weight:700;font-size:9.6pt">{d}</div>' for d in range(1, 31))
    pag(f'{capitulo(8, "Tu plan de 30 días", "Un paso por semana. En un mes puedes tener tus primeras ventas.")}<div style="display:grid;grid-template-columns:repeat(10,1fr);gap:1.6mm;margin-top:6mm">{cal}</div><div class="semanas">{sm}</div><div class="caja" style="margin-top:7mm"><h4>Meta del primer mes</h4><p>3 ventas, 3 reseñas con foto y una lista de los 5 muebles que más te piden. Con eso ya tienes un negocio.</p></div>')

    # Plantillas
    pag(f'''<div class="kicker">Plantilla para imprimir</div><h2 style="margin:2mm 0 4mm">Cotización</h2>
<div class="plantilla"><div style="display:flex;justify-content:space-between"><div><b style="font-family:Barlow Condensed;font-size:20pt">Tu taller</b><p class="nota">WhatsApp: ____________ · Instagram: ____________</p></div><div style="text-align:right"><b>Cotización N.° ____</b><p class="nota">Fecha: ____ / ____ / ______</p></div></div>
<p style="margin-top:5mm"><b>Cliente:</b> ________________________________ <b style="margin-left:4mm">Teléfono:</b> ____________________</p>
<table class="t" style="margin-top:5mm"><tr><th>Mueble / descripción</th><th style="width:22mm">Cant.</th><th style="width:30mm">Precio unit.</th><th style="width:30mm">Total</th></tr>{''.join('<tr><td style="height:12.5mm"></td><td></td><td></td><td></td></tr>' for _ in range(8))}
<tr><td colspan="3" style="text-align:right"><b>Total</b></td><td></td></tr><tr><td colspan="3" style="text-align:right">Adelanto (50 %)</td><td></td></tr><tr><td colspan="3" style="text-align:right">Saldo contra entrega</td><td></td></tr></table>
<div class="grid2" style="margin-top:5mm;font-size:9.6pt"><p><b>Color / acabado:</b> ____________________<br><b>Medidas especiales:</b> ________________<br><b>Tiempo de entrega:</b> ______ días hábiles</p><p><b>Garantía:</b> ____ meses en armado y herrajes.<br><b>Validez de la cotización:</b> 15 días.<br><b>Forma de pago:</b> ____________________</p></div>
<div style="display:flex;gap:30mm;margin-top:14mm"><div style="flex:1;border-top:1.4px solid {T['ink']};padding-top:1.4mm" class="nota">Firma del taller</div><div style="flex:1;border-top:1.4px solid {T['ink']};padding-top:1.4mm" class="nota">Firma del cliente</div></div></div>''')

    pag(f'''<div class="kicker">Plantilla para imprimir</div><h2 style="margin:2mm 0 4mm">Hoja de costos por mueble</h2>
<p><b>Mueble:</b> ______________________________ <b style="margin-left:4mm">Plano:</b> ________</p>
<table class="t" style="margin-top:4mm"><tr><th>Concepto</th><th style="width:30mm">Cantidad</th><th style="width:30mm">Precio unit.</th><th style="width:30mm">Subtotal</th></tr>{''.join(f'<tr><td style="height:13.6mm">{x}</td><td></td><td></td><td></td></tr>' for x in ['Tableros / madera', 'Fondo', 'Cubrecanto', 'Bisagras', 'Correderas', 'Tiradores', 'Tornillería', 'Acabado (aceite, barniz, pintura)', 'Corte', 'Transporte', 'Mi tiempo (horas × valor hora)', 'Gastos del taller (10 %)'])}
<tr><td colspan="3" style="text-align:right"><b>Costo total</b></td><td></td></tr><tr><td colspan="3" style="text-align:right">× Margen (1,5 a 2)</td><td></td></tr><tr><td colspan="3" style="text-align:right"><b>Precio de venta</b></td><td></td></tr></table>''')

    pag(f'''<div style="height:100%;display:flex;flex-direction:column;justify-content:center"><div class="kicker">Ahora te toca</div><h1 style="margin:5mm 0">Tu primer<br>mueble vendido</h1>
<p class="lead" style="max-width:140mm">Empieza con un mueble, una buena foto y un precio justo. Cada venta te enseña algo y cada cliente feliz te trae el siguiente.</p>
<div style="margin-top:12mm;font-family:'Barlow Condensed';font-weight:700;font-size:22pt">byignis</div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:4mm;margin-top:16mm">{''.join(f'<div style="background:#2E2B27;border-radius:4mm;height:34mm;padding:3mm">{img(c, "width:100%;height:100%;object-fit:contain")}</div>' for c in ['SAL-10', 'DOR-09', 'COM-14', 'REC-05'])}</div></div>''', 'oscura')

    out = os.path.join(HERE, 'out'); os.makedirs(out, exist_ok=True)
    hp = os.path.join(out, 'vende-tus-muebles.html')
    open(hp, 'w').write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(pags)}</body></html>')
    print('paginas', len(pags))
    return hp

if __name__ == '__main__':
    import sys
    hp = main()
    if 'snap' in sys.argv:
        snapshot(hp, hp.replace('.html', ''), [int(x) for x in sys.argv[2:]])
    else:
        render_pdf(hp, hp.replace('.html', '.pdf'))
