"""Regalo 2: Manual de Autonomía — Actividades de la vida diaria en pediatría."""
import os
from common import C, e, base_css, pie, render_pdf, snapshot
from iconos import icono

AC = C['verde']; AC_S = '#E3F0DF'
MARCA = 'Manual de Autonomía'

def R(t, edad, meta, pasos, entorno, ensenar, tea, tdah, rgd):
    return dict(t=t, edad=edad, meta=meta, pasos=pasos, entorno=entorno, ensenar=ensenar, tea=tea, tdah=tdah, rgd=rgd)

VESTIR = [
 R('Quitarse los calcetines', '1½ – 2 años', 'Es el primer logro de vestido y da mucha confianza.',
   [('calcetin', None, 'Sentado en el suelo'), ('manos', None, 'Pulgar dentro del calcetín'), ('calcetin', 'abajo', 'Empuja hacia el talón'), ('calcetin', 'abajo', 'Jala desde la punta'), ('calcetin', 'ok', '¡Fuera!')],
   ['Siéntalo en el suelo con la espalda apoyada en la pared.', 'Usa calcetines un poco grandes al principio.'],
   ['Bájale tú el calcetín hasta el talón y deja que termine él (encadenamiento hacia atrás).', 'Conviértelo en juego: "¡a sacar el calcetín del monstruo!".'],
   'Anticipa con el pictograma antes de empezar y usa siempre la misma frase.', 'Hazlo como reto rápido: "¿puedes antes de que cuente 5?".', 'Calcetines amplios y de tela suave; guía su mano con la tuya.'),
 R('Ponerse los calcetines', '3 – 4 años', 'Coordina las dos manos y el equilibrio sentado.',
   [('calcetin', None, 'Talón hacia abajo'), ('manos', None, 'Abre con los pulgares'), ('calcetin', None, 'Mete los dedos del pie'), ('calcetin', 'arriba', 'Jala hasta el talón'), ('calcetin', 'arriba', 'Sube hasta arriba'), ('calcetin', 'ok', '¡Listo!')],
   ['Sentado en el suelo o en una silla baja con los pies apoyados.', 'Calcetines cortos y con el talón de otro color.'],
   ['Empieza poniéndole el calcetín hasta el talón: él solo lo sube.', 'Después él mete los dedos y tú ayudas con el talón.'],
   'El talón de color ayuda a entender cómo orientarlo. Evita texturas que le molesten.', 'Un paso a la vez, con el pictograma frente a él.', 'Practica primero en el antebrazo o en un peluche grande.'),
 R('Quitarse la camiseta', '2 – 3 años', 'Primero se aprende a quitar y luego a poner.',
   [('camiseta', None, 'Cruza los brazos'), ('manos', None, 'Toma la parte de abajo'), ('camiseta', 'arriba', 'Sube por la panza'), ('camiseta', 'arriba', 'Saca la cabeza'), ('camiseta', 'ok', 'Saca los brazos')],
   ['De pie, frente a un espejo si le ayuda.', 'Camisetas holgadas de cuello ancho.'],
   ['Súbele la camiseta hasta la cabeza y deja que él la saque.', 'Luego deja que la suba desde el pecho.'],
   'Avisa antes de que la tela tape la cara; algunos niños se angustian.', 'Músicas cortas o cuenta regresiva para mantener la atención.', 'Prenda grande y de tela que se estire.'),
 R('Ponerse la camiseta', '3 – 4 años', 'Reconocer adelante y atrás y coordinar brazos.',
   [('camiseta', None, 'Etiqueta abajo, en la mesa'), ('camiseta', None, 'Mete la cabeza'), ('manos', None, 'Mete un brazo'), ('manos', None, 'Mete el otro brazo'), ('camiseta', 'abajo', 'Jala hacia abajo'), ('camiseta', 'ok', '¡Listo!')],
   ['Coloca la camiseta sobre la mesa boca abajo con la etiqueta o un dibujo como referencia.', 'Elige cuello ancho y mangas cortas para empezar.'],
   ['Ponle tú la cabeza y los brazos; él solo jala hacia abajo.', 'Ve quitando tu ayuda de atrás hacia adelante.'],
   'Quita etiquetas que molesten y usa siempre la misma prenda para practicar.', 'Deja la camiseta preparada antes de llamarlo.', 'Mangas cortas y holgadas; más tiempo para cada paso.'),
 R('Ponerse el pantalón', '3 – 4 años', 'Equilibrio, orientación y fuerza para jalar.',
   [('silla', None, 'Siéntate'), ('pantalon', None, 'Etiqueta atrás'), ('pantalon', None, 'Mete una pierna'), ('pantalon', None, 'Mete la otra pierna'), ('pantalon', 'arriba', 'Ponte de pie y sube'), ('pantalon', 'ok', '¡Listo!')],
   ['Siempre sentado al empezar: en una silla baja o en el suelo.', 'Pantalón con elástico, sin botones.'],
   ['Hazlo tú hasta las rodillas y que él se pare y suba.', 'Marca la parte de adelante con un dibujo o cinta.'],
   'Usa la misma secuencia todos los días; el orden da seguridad.', 'Ropa preparada en el orden en que se pone.', 'Pantalones un poco grandes y de elástico suave.'),
 R('Zapatos de velcro', '3 – 4 años', 'Diferenciar pie derecho e izquierdo y cerrar.',
   [('zapato', None, 'Zapatos juntos: "se miran"'), ('manos', None, 'Abre bien el velcro'), ('zapato', None, 'Mete la punta del pie'), ('zapato', 'abajo', 'Empuja el talón'), ('zapato', None, 'Cierra el velcro'), ('zapato', 'ok', '¡Listo!')],
   ['Sentado, con el pie apoyado en el suelo.', 'Pega pegatinas: dos mitades de un dibujo que se unen cuando están bien.'],
   ['Ponle tú el pie y deja que él cierre el velcro.', 'Luego que meta el pie y tú ayudes con el talón.'],
   'Las mitades de dibujo ayudan mucho a orientarse sin palabras.', 'Zapatos siempre en el mismo lugar de la entrada.', 'Calzador largo o zapatos un número más holgados para practicar.'),
 R('Abrochar botones', '3½ – 5 años', 'Pinza fina y coordinación de las dos manos.',
   [('boton', None, 'Busca el botón y el ojal'), ('manos', None, 'Pellizca el botón'), ('boton', None, 'Mételo en el ojal'), ('manos', None, 'La otra mano jala'), ('boton', 'ok', '¡Abrochado!')],
   ['Empieza con botones grandes en una prenda sobre la mesa, no puesta.', 'Abrochar de abajo hacia arriba evita desfases.'],
   ['Practica en un "tablero de botones" (fieltro con botones grandes).', 'Pasa a la prenda puesta cuando lo logre en la mesa.'],
   'Pocos botones y del mismo color al inicio.', 'Un botón cada día y celebra; no toda la camisa.', 'Botones grandes y ojales holgados; puedes agrandar el ojal.'),
 R('Subir el cierre', '4 – 5½ años', 'El paso difícil es enganchar; subirlo es fácil.',
   [('cierre', None, 'Junta los dos lados'), ('manos', None, 'Mete la punta hasta abajo'), ('manos', None, 'Sujeta abajo con una mano'), ('cierre', 'arriba', 'Sube con la otra'), ('cierre', 'ok', '¡Cerrado!')],
   ['Pon un llavero o argolla en el tirador para agarrarlo mejor.', 'Practica con la chamarra sobre la mesa.'],
   ['Engánchalo tú y deja que él lo suba.', 'Después él engancha con tu mano guiando.'],
   'Usa siempre la misma prenda al practicar.', 'Pocos pasos y refuerzo inmediato al terminar.', 'Tirador grande y cierre de dientes gruesos.'),
 R('Atar los cordones', '5½ – 7 años', 'Una de las tareas más complejas: necesita paciencia.',
   [('cordones', None, 'Cruza los cordones'), ('cordones', None, 'Mete uno por abajo y jala'), ('cordones', None, 'Haz una oreja de conejo'), ('cordones', None, 'Haz la otra oreja'), ('cordones', None, 'Cruza las orejas'), ('cordones', 'ok', 'Jala fuerte')],
   ['Practica en una caja de zapatos con cordones de dos colores.', 'Cordones planos y gruesos, no redondos.'],
   ['Haz todo y deja que él jale el último paso; ve sumando pasos hacia atrás.', 'Usa la técnica de las dos orejas de conejo, que es la más fácil de enseñar.'],
   'Video o fotos de cada paso, siempre en el mismo orden.', 'Sesiones de 5 minutos; usa colores llamativos.', 'Mientras aprende, usa cordones elásticos o velcro para su autonomía diaria.'),
]

COMER = [
 R('Comer con cuchara', '1½ – 2½ años', 'Llevar la comida a la boca sin derramar.',
   [('silla', None, 'Sentado, pies apoyados'), ('cuchara', None, 'Toma la cuchara'), ('plato', None, 'Recoge la comida'), ('cuchara', 'arriba', 'Llévala a la boca'), ('plato', 'ok', '¡Bien hecho!')],
   ['Silla a su altura con los pies apoyados y mesa a la altura del pecho.', 'Plato hondo o con borde y comida espesa (puré, arroz con salsa).'],
   ['Guía su mano desde el codo, no desde la mano.', 'Carga tú la cuchara y deja que él la lleve a la boca.'],
   'Ofrece los mismos utensilios cada día y anticipa cuándo termina la comida.', 'Pocas cosas en la mesa: solo plato, cuchara y vaso.', 'Cuchara de mango grueso y plato con ventosa.'),
 R('Beber de un vaso abierto', '2 – 3 años', 'Controlar la inclinación y la cantidad.',
   [('vaso', None, 'Poca agua en el vaso'), ('manos', None, 'Dos manos al vaso'), ('vaso', 'arriba', 'Inclina despacio'), ('vaso', None, 'Pequeño sorbo'), ('vaso', 'abajo', 'Deja el vaso en la mesa'), ('vaso', 'ok', '¡Bien!')],
   ['Vaso pequeño y transparente para que vea el líquido.', 'Llena solo un dedo de agua al principio.'],
   ['Practica en el baño o al aire libre, donde derramar no importa.', 'Agrega agua poco a poco a medida que lo controle.'],
   'Si le molesta una textura o temperatura, empieza con su bebida favorita.', 'Que se sirva él mismo con una jarrita: mantiene la atención.', 'Vaso con asas o con borde recortado para la nariz.'),
 R('Usar el tenedor', '2½ – 3½ años', 'Pinchar y llevar la comida a la boca.',
   [('tenedor', None, 'Toma el tenedor'), ('plato', None, 'Elige un trozo'), ('tenedor', 'abajo', 'Pincha firme'), ('tenedor', 'arriba', 'A la boca'), ('plato', 'ok', '¡Muy bien!')],
   ['Trozos medianos y firmes: fruta, salchicha, queso.', 'Tenedor infantil de puntas redondeadas.'],
   ['Pincha tú y deja que él lo lleve a la boca.', 'Juego de "pinchar" plastilina o fruta antes de comer.'],
   'Presenta un alimento a la vez para no saturar.', 'Pinchar es divertido: úsalo como juego de puntería.', 'Mango grueso o forrado; trozos más grandes.'),
 R('Untar con cuchillo', '4 – 5 años', 'Usar las dos manos: una sujeta y la otra unta.',
   [('cuchillo', None, 'Toma el cuchillo de untar'), ('cuchillo', None, 'Recoge un poco'), ('manos', None, 'La otra mano sujeta el pan'), ('cuchillo', None, 'Unta de lado a lado'), ('cuchillo', 'ok', '¡A comer!')],
   ['Cuchillo de mesa sin filo, de punta redonda.', 'Untables blandos: queso crema, mantequilla a temperatura ambiente.'],
   ['Practica untando con plastilina sobre cartón.', 'Pan firme o galletas grandes para empezar.'],
   'Si le molesta ensuciarse, ten una servilleta a mano y anticípalo.', 'Tarea corta y con resultado inmediato: ¡su merienda!', 'Pan tostado (no se rompe) y untable muy blando.'),
 R('Servirse agua', '4 – 5 años', 'Autonomía en la mesa y control de la fuerza.',
   [('jarra', None, 'Jarra pequeña'), ('vaso', None, 'Vaso firme en la mesa'), ('manos', None, 'Una mano sujeta el vaso'), ('jarra', None, 'Inclina despacio'), ('vaso', 'ok', 'Para a la mitad')],
   ['Jarra pequeña con poca agua y vaso pesado.', 'Marca con una línea hasta dónde llenar.'],
   ['Practica con arroz o legumbres antes que con agua.', 'Ten una toalla cerca: derramar es parte de aprender.'],
   'La línea de "hasta aquí" da una regla clara.', 'Dale este rol en cada comida: "el que sirve el agua".', 'Jarra con asa grande y vaso con base ancha.'),
]

HIGIENE = [
 R('Lavarse las manos', '3 – 4 años (con supervisión)', 'La rutina de higiene más importante del día.',
   [('grifo', None, 'Abre el agua'), ('manos', None, 'Moja las manos'), ('jabon', None, 'Pon jabón'), ('manos', 'giro', 'Frota 20 segundos'), ('grifo', None, 'Enjuaga y cierra'), ('toalla', 'ok', 'Seca las manos')],
   ['Escalón seguro para llegar al lavabo.', 'Jabón de dosificador fácil y toalla a su alcance.'],
   ['Canta una canción corta mientras frota (unos 20 segundos).', 'Pega la secuencia en pictogramas junto al espejo.'],
   'Prueba la temperatura y el tipo de jabón: algunos niños rechazan el olor o la espuma.', 'Temporizador de arena o canción para no saltarse el frotado.', 'Grifo de palanca y jabón en espuma, más fácil de usar.'),
 R('Cepillarse los dientes', 'desde 2–3 años, con ayuda', 'Hábito diario, mañana y noche. Un adulto supervisa y repasa hasta los 7–8 años.',
   [('pasta', None, 'Pon poca pasta'), ('cepillo', None, 'Cepilla arriba'), ('cepillo', None, 'Cepilla abajo'), ('cepillo', 'giro', 'Haz círculos pequeños'), ('vaso', None, 'Escupe'), ('cepillo', 'ok', 'Enjuaga el cepillo')],
   ['Cantidad de pasta: como un grano de arroz antes de los 3 años; como un guisante de 3 a 6 años.', 'Espejo a su altura.'],
   ['Él cepilla primero y tú repasas al final.', 'Cuenta hasta 10 en cada zona de la boca.'],
   'Prueba cepillos suaves y pastas de sabor neutro si rechaza la textura o el sabor.', 'Cepillo eléctrico infantil o temporizador de 2 minutos.', 'Mango grueso o forrado con espuma para agarrarlo mejor.'),
 R('Ir al baño', '2½ – 4 años (de día)', 'Reconocer la necesidad y completar la secuencia.',
   [('inodoro', None, 'Baja la ropa'), ('inodoro', None, 'Siéntate'), ('papel', None, 'Límpiate'), ('inodoro', None, 'Jala la cadena'), ('pantalon', 'arriba', 'Sube la ropa'), ('jabon', 'ok', 'Lava tus manos')],
   ['Reductor de asiento y escalón para apoyar los pies.', 'Ropa fácil de bajar: pantalón de elástico.'],
   ['Llévalo en horarios fijos: al despertar, después de comer y antes de dormir.', 'Celebra cada intento, aunque no haya resultado.'],
   'El ruido de la cadena o el secador puede asustar: anticipa y deja que él la jale cuando esté listo.', 'Un libro o juego corto en el baño ayuda a esperar sentado.', 'Asiento estable con apoyo para los pies; más tiempo y paciencia.'),
 R('Sonarse la nariz', '3 – 4½ años', 'Aprender a soplar por la nariz.',
   [('panuelo', None, 'Toma un pañuelo'), ('cara', None, 'Tápate un lado'), ('cara', None, 'Sopla por la nariz'), ('panuelo', None, 'Limpia'), ('jabon', 'ok', 'Tira y lávate')],
   ['Pañuelos a su alcance y papelera cerca.', 'Practica cuando no esté resfriado.'],
   ['Juego: soplar por la nariz una bolita de papel sobre la mesa (boca cerrada).', 'Frente al espejo para que vea el vapor.'],
   'Usa pañuelos suaves; el contacto en la cara puede molestar.', 'Hazlo competencia: ¿quién mueve más lejos la bolita?', 'Practica primero soplar con la boca y luego con la nariz.'),
 R('Lavarse la cara', '3 – 4 años', 'Rutina de la mañana y después de comer.',
   [('grifo', None, 'Abre el agua tibia'), ('manos', None, 'Haz una copa con las manos'), ('cara', None, 'Moja la cara'), ('toalla', None, 'Seca con suavidad'), ('cara', 'ok', '¡Carita limpia!')],
   ['Toalla pequeña a su alcance y espejo.', 'Agua tibia, nunca muy fría ni caliente.'],
   ['Empieza con una toallita húmeda en lugar del chorro de agua.', 'Señala en el espejo: frente, mejillas, barbilla.'],
   'Muchos niños rechazan el agua en la cara: empieza con toallita y avanza poco a poco.', 'Hazlo parte de la rutina fija de la mañana.', 'Toallita húmeda y guía con tu mano.'),
 R('Peinarse', '4 – 5 años', 'Cuidado personal y movimiento de los brazos.',
   [('peine', None, 'Toma el peine'), ('cara', None, 'Mírate al espejo'), ('peine', 'abajo', 'Peina de arriba hacia abajo'), ('peine', None, 'Un lado y el otro'), ('cara', 'ok', '¡Qué bien te ves!')],
   ['Espejo a su altura y cepillo de cerdas suaves.', 'Desenreda tú antes, si el pelo es largo.'],
   ['Practica peinando una muñeca o un peluche.', 'Divide la cabeza en zonas: arriba, lado, lado, atrás.'],
   'Cepillo suave; presión firme suele tolerarse mejor que roces ligeros.', 'Que se peine mientras canta una canción corta.', 'Cepillo de mango grueso y largo.'),
 R('La hora del baño', '5 – 8 años (siempre con supervisión)', 'Lavarse el cuerpo por partes.',
   [('tina', None, 'Prueba el agua con el codo'), ('jabon', None, 'Jabón en la esponja'), ('manos', None, 'Brazos y panza'), ('manos', None, 'Piernas y pies'), ('tina', None, 'Enjuaga'), ('toalla', 'ok', 'Sécate')],
   ['Nunca dejes a un niño solo en la bañera, ni un momento.', 'Alfombrilla antideslizante y todo preparado antes de empezar.'],
   ['Lista de partes del cuerpo en pictogramas pegada en la pared del baño.', 'Esponja con forma de guante para que sea más fácil.'],
   'Mantén temperatura, luz y orden iguales cada día; avisa antes de mojar la cabeza.', 'Juguetes de baño solo después de lavarse: es la recompensa.', 'Asiento de baño y esponja con mango largo.'),
]

def guion(pasos):
    t = [p[2].rstrip('!¡').strip() for p in pasos]
    t = [x[0].lower() + x[1:] for x in t]
    if len(t) <= 2: return 'Primero ' + ', luego '.join(t) + '.'
    medio = ', luego '.join(t[1:-1])
    return f'"Primero {t[0]}, luego {medio}… ¡y {t[-1]}!" Usa siempre las mismas palabras y señala cada pictograma al decirlo.'

def rutina(cat, i, r, color):
    pasos = ''.join(f'''<div class="paso"><div class="pn">{k}</div><div class="pic">{icono(ic, fl)}</div><div class="pt">{e(txt)}</div></div>''' for k, (ic, fl, txt) in enumerate(r['pasos'], 1))
    cols = len(r['pasos'])
    return f'''<div class="kicker">{cat} · Rutina {i}</div>
<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:6mm;margin-top:2mm"><h2>{e(r["t"])}</h2><span class="chip suave" style="white-space:nowrap">Edad orientativa: {e(r["edad"])}</span></div>
<p class="lead" style="margin-top:2mm">{e(r["meta"])}</p>
<div class="tira" style="grid-template-columns:repeat({cols},1fr)">{pasos}</div>
<div class="grid2" style="margin-top:6mm">
 <div class="caja"><h4>Prepara el entorno</h4><ul class="lista">{''.join(f"<li>{e(x)}</li>" for x in r["entorno"])}</ul></div>
 <div class="caja"><h4>Cómo enseñarlo</h4><ul class="lista">{''.join(f"<li>{e(x)}</li>" for x in r["ensenar"])}</ul></div>
</div>
<div class="perfiles">
 <div><span class="tag" style="background:{C['morado']}">TEA</span>{e(r["tea"])}</div>
 <div><span class="tag" style="background:{C['naranja']}">TDAH</span>{e(r["tdah"])}</div>
 <div><span class="tag" style="background:{C['azul']}">Retraso global</span>{e(r["rgd"])}</div>
</div>
<div class="guion"><b>Guion para acompañar</b>{guion(r["pasos"])}</div>
<div class="progreso"><b>Mi progreso — marca la ayuda que necesitó esta semana:</b>
<div class="niveles">{''.join(f'<span><i class="check"></i>{x}</span>' for x in ['Física total', 'Física parcial', 'Le mostré', 'Le señalé', 'Se lo dije', '¡Solo!'])}</div></div>'''

def main():
    css = base_css(AC, AC_S) + f"""
.portada {{ background: {C['crema']}; padding: 30mm 22mm }}
.portada h1 {{ font-size: 44pt; margin: 8mm 0 6mm }}
.tira {{ display: grid; gap: 3mm; margin-top: 7mm }}
.paso {{ min-width: 0; background: #fff; border: 1.6px solid {C['linea']}; border-radius: 4mm; padding: 4mm 2.4mm 5mm; text-align: center; position: relative }}
.paso .pn {{ position: absolute; top: -3mm; left: -2mm; width: 7mm; height: 7mm; border-radius: 50%; background: {AC}; color: #fff; font-weight: 900; font-size: 9pt; display: grid; place-items: center }}
.paso .pic {{ width: 100%; max-width: 25mm; aspect-ratio: 1; margin: 2mm auto 3mm }}
.paso .pt {{ font-size: 9.6pt; font-weight: 700; line-height: 1.25 }}
.perfiles {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4mm; margin-top: 6mm }}
.perfiles > div {{ border: 1.4px solid {C['linea']}; border-radius: 4mm; padding: 4.6mm; font-size: 10pt; line-height: 1.4 }}
.tag {{ display: block; width: max-content; color: #fff; font-weight: 800; font-size: 8pt; border-radius: 99px; padding: .6mm 2.8mm; margin-bottom: 2mm }}
.guion {{ margin-top: 6mm; border-left: 2.4mm solid {AC}; background: {C['crema']}; border-radius: 0 4mm 4mm 0; padding: 4.4mm 6mm; font-size: 11pt }}
.guion b {{ display: block; color: {AC}; font-size: 8.6pt; letter-spacing: 1.6px; text-transform: uppercase; margin-bottom: 1mm }}
.progreso {{ position: absolute; left: 18mm; right: 18mm; bottom: 20mm; background: {AC_S}; border-radius: 4mm; padding: 4mm 6mm; font-size: 9.4pt }}
.niveles {{ display: flex; justify-content: space-between; margin-top: 2.4mm; font-weight: 700 }}
.niveles .check {{ display: inline-block }}
.escalera {{ display: flex; align-items: flex-end; gap: 2.4mm; margin-top: 5mm; height: 52mm }}
.escalera div {{ flex: 1; background: {AC}; color: #fff; border-radius: 3mm 3mm 0 0; padding: 2.4mm; font-size: 8.6pt; font-weight: 800; line-height: 1.2 }}
.herr {{ display: grid; grid-template-columns: 14mm 1fr; gap: 4mm; padding: 4mm 0; border-bottom: 1px solid {C['linea']} }}
.herr .n {{ width: 12mm; height: 12mm; border-radius: 3mm; background: {AC_S}; color: {AC}; font-weight: 900; font-size: 14pt; display: grid; place-items: center }}
.divisor {{ position: absolute; left: 22mm; right: 22mm; top: 50mm }}
.divisor h2 {{ font-size: 38pt; margin: 6mm 0 }}
.grande {{ position: absolute; right: 16mm; bottom: 20mm; font-size: 220pt; font-weight: 900; color: rgba(255,255,255,.22); line-height: 1; letter-spacing: -6px }}
.div-iconos {{ display: flex; gap: 5mm; margin-top: 12mm }}
.div-iconos span {{ width: 24mm; height: 24mm; background: #fff; border-radius: 5mm; padding: 3mm }}
.perfil {{ border-radius: 5mm; padding: 6mm 7mm; color: #fff; margin-bottom: 5mm }}
.perfil h3 {{ margin-bottom: 2mm }}
.perfil ul {{ list-style: none }}
.perfil li {{ margin: 1.4mm 0; padding-left: 5mm; position: relative }}
.perfil li::before {{ content: '•'; position: absolute; left: 0; font-weight: 900 }}
.tarjetas {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 5mm; margin-top: 6mm }}
.tarjeta {{ border: 1.6px dashed {C['gris']}; border-radius: 4mm; padding: 4mm; text-align: center; font-weight: 800; font-size: 12pt }}
.tarjeta .pic {{ width: 36mm; height: 36mm; margin: 0 auto 2mm }}
.rutina-v {{ display: flex; flex-direction: column; gap: 3mm; margin-top: 5mm }}
.rutina-v .fila {{ display: grid; grid-template-columns: 9mm 20mm 1fr 14mm; align-items: center; gap: 4mm; border: 1.4px solid {C['linea']}; border-radius: 4mm; padding: 2.4mm 4mm; font-weight: 800; font-size: 12pt }}
.rutina-v .num {{ width: 8mm; height: 8mm; border-radius: 50%; background: {AC}; color: #fff; display: grid; place-items: center; font-size: 10pt }}
.rutina-v .box {{ width: 11mm; height: 11mm; border: 2px solid {C['tinta']}; border-radius: 2.4mm; justify-self: end }}
table.estrellas td {{ text-align: center; height: 16mm }}
"""
    pags = []; num = [0]
    def pag(body, cls=''):
        num[0] += 1
        pags.append(f'<section class="pag {cls}">{body}{pie(MARCA, str(num[0])) if num[0] > 1 else ""}</section>')

    total = len(VESTIR) + len(COMER) + len(HIGIENE)
    muestra = ''.join(f'<div style="width:38mm;height:38mm;background:#fff;border-radius:7mm;padding:5mm;box-shadow:0 3mm 8mm rgba(31,36,51,.08)">{icono(x)}</div>' for x in ['camiseta', 'cuchara', 'cepillo', 'zapato', 'vaso', 'jabon'])
    pag(f'''<div class="kicker">Regalo exclusivo · Material para casa y terapia</div>
<h1>Manual de<br>Autonomía</h1>
<p class="lead" style="max-width:150mm">Estrategias ilustradas para enseñar a vestirse, comer y la higiene personal. Ideal para niños con TEA, TDAH y retraso global del desarrollo.</p>
<div style="display:flex;gap:3mm;margin-top:9mm;flex-wrap:wrap"><span class="chip">{total} rutinas paso a paso</span><span class="chip">Pictogramas</span><span class="chip">Adaptaciones por perfil</span><span class="chip">Imprimibles</span></div>
<div style="position:absolute;right:22mm;bottom:28mm;display:grid;grid-template-columns:repeat(3,38mm);gap:7mm">{muestra}</div>
<div style="position:absolute;left:22mm;bottom:22mm;font-weight:900;font-size:14pt">Byignis</div>''', 'portada')

    pag(f'''<div class="kicker">Antes de empezar</div><h2 style="margin:3mm 0 5mm">Cómo usar este manual</h2>
<p class="lead">Vestirse, comer y asearse son las primeras actividades que dan independencia a un niño. Cada logro, por pequeño que parezca, le da confianza y alivia la rutina de toda la familia.</p>
<div class="grid2" style="margin-top:8mm">
<div class="caja"><h4>1. Elige una sola rutina</h4><p>Empieza por la que más se repite en su día o la que más le motive. Practicar todo a la vez agota a todos.</p></div>
<div class="caja"><h4>2. Pega la tira de pictogramas</h4><p>Cada rutina tiene su secuencia en imágenes. Imprímela y pégala donde se hace la actividad: baño, cuarto, comedor.</p></div>
<div class="caja"><h4>3. Practica en el momento real</h4><p>La mejor práctica es en la vida diaria: vestirse al despertar, lavarse las manos antes de comer.</p></div>
<div class="caja"><h4>4. Retira la ayuda poco a poco</h4><p>Marca cada semana cuánta ayuda necesitó. Ver cómo baja la ayuda es la mejor señal de progreso.</p></div>
</div>
<div class="caja acento" style="margin-top:7mm"><h4>Sobre las edades</h4><p>Las edades de cada rutina son orientativas, basadas en el desarrollo típico. Muchos niños con TEA, TDAH o retraso global aprenden estas habilidades más tarde y por otro camino: lo importante es su propio avance, no la comparación.</p></div>
<p class="nota" style="margin-top:8mm">Este material es de apoyo y no sustituye la evaluación ni el tratamiento de un terapeuta ocupacional u otro profesional de la salud. Ante dificultades para comer, tragar o con el control de esfínteres, consulta con un especialista.</p>''')

    pag(f'''<div class="kicker">La caja de herramientas</div><h2 style="margin:3mm 0 4mm">4 estrategias que usan los terapeutas</h2>
<p class="lead">Estas cuatro ideas funcionan para cualquier rutina de este manual.</p>
<div class="herr"><span class="n">1</span><div><h3>Divide la tarea en pasos</h3><p>Lo que para un adulto es "vestirse", para un niño son muchos pasos. Las tiras de pictogramas ya vienen divididas: enseña paso por paso.</p></div></div>
<div class="herr"><span class="n">2</span><div><h3>Empieza por el final</h3><p>Haz tú todos los pasos menos el último y deja que él lo termine. Cuando lo domine, deja los dos últimos, y así hacia atrás. Así el niño <b>siempre termina con éxito</b>.</p></div></div>
<div class="herr"><span class="n">3</span><div><h3>Ayuda de más a menos</h3><p>Da solo la ayuda necesaria y ve retirándola. Este es el orden, de más ayuda a menos:</p>
<div class="escalera">{''.join(f'<div style="height:{h}%;opacity:{o}">{t}</div>' for t, h, o in [('Física total: guías su mano', 100, 1), ('Física parcial: tocas el codo', 84, .92), ('Le muestras cómo', 68, .84), ('Le señalas', 52, .76), ('Se lo dices', 36, .68), ('¡Lo hace solo!', 22, .6)])}</div></div></div>
<div class="herr" style="border:none"><span class="n">4</span><div><h3>Imágenes y celebración</h3><p>Los pictogramas le dicen qué viene después sin necesidad de muchas palabras. Celebra el esfuerzo inmediatamente: un choque de manos, una estrella en el tablero.</p></div></div>
<div class="caja acento" style="margin-top:4mm"><h4>Ejemplo: ponerse los calcetines</h4><p><b>Semana 1:</b> tú haces todo y él solo sube el calcetín desde el tobillo. <b>Semana 2:</b> tú lo pones hasta el talón y él termina. <b>Semana 3:</b> tú metes los dedos y él hace el resto. <b>Semana 4:</b> ¡lo hace solo! En cada paso, la ayuda pasa de física a solo palabras.</p></div>''')

    pag(f'''<div class="kicker">Cada niño es distinto</div><h2 style="margin:3mm 0 5mm">Adaptaciones según su perfil</h2>
<div class="perfil" style="background:{C['morado']}"><h3>Trastorno del espectro autista (TEA)</h3><ul>
<li>Anticipa: muestra la secuencia antes de empezar y usa siempre las mismas palabras.</li>
<li>Cuida lo sensorial: texturas de ropa, temperatura del agua, olores y ruidos pueden ser el verdadero obstáculo.</li>
<li>Mantén el mismo orden, lugar y horario: la rutina da seguridad.</li></ul></div>
<div class="perfil" style="background:{C['naranja']}"><h3>TDAH</h3><ul>
<li>Pasos cortos, de uno en uno, con la tira de pictogramas a la vista.</li>
<li>Usa retos y temporizadores: "¿lo logras antes de que acabe la canción?".</li>
<li>Reduce las distracciones: pocos objetos y sin pantallas encendidas.</li></ul></div>
<div class="perfil" style="background:{C['azul']}"><h3>Retraso global del desarrollo</h3><ul>
<li>Da más tiempo y más repeticiones; avanza un paso cuando el anterior sea fácil.</li>
<li>Adapta los materiales: mangos gruesos, ropa holgada, velcro en lugar de botones.</li>
<li>Celebra cada pequeño avance: es un gran logro.</li></ul></div>
<p class="nota">En cada rutina encontrarás una sugerencia específica para cada perfil.</p>''')

    def divisor(n, titulo, texto, iconos):
        ic = ''.join(f'<span>{icono(x)}</span>' for x in iconos)
        pag(f'''<div class="divisor"><div class="kicker">Parte {n}</div><h2>{titulo}</h2><p class="lead" style="max-width:140mm">{texto}</p><div class="div-iconos">{ic}</div></div><div class="grande">0{n}</div>''', 'color')

    divisor(1, 'Vestirse', f'{len(VESTIR)} rutinas: de quitarse los calcetines a atar los cordones.', ['calcetin', 'camiseta', 'pantalon', 'zapato', 'boton'])
    for i, r in enumerate(VESTIR, 1): pag(rutina('Vestirse', i, r, AC))
    divisor(2, 'Alimentación', f'{len(COMER)} rutinas para comer con más autonomía, además de la postura en la mesa.', ['cuchara', 'tenedor', 'vaso', 'plato', 'jarra'])
    pag(f'''<div class="kicker">Alimentación · Antes de empezar</div><h2 style="margin:3mm 0 5mm">La mesa y la postura</h2>
<p class="lead">Un niño que se sienta estable come mejor, se cansa menos y derrama menos.</p>
<div style="display:grid;grid-template-columns:60mm 1fr;gap:8mm;margin-top:8mm;align-items:center"><div style="background:{C['crema']};border-radius:6mm;padding:8mm">{icono('silla')}</div>
<ul class="lista" style="font-size:11pt"><li><b>Pies apoyados</b> en el suelo o en un escalón: nunca colgando.</li><li><b>Mesa a la altura del pecho</b>, con los codos sobre ella.</li><li><b>Espalda apoyada</b> y cadera al fondo de la silla.</li><li><b>Pocos objetos</b> en la mesa: plato, cubierto y vaso.</li><li><b>Comidas en familia</b>: el niño aprende imitando.</li></ul></div>
<div class="caja acento" style="margin-top:10mm"><h4>Cuando comer es difícil</h4><p>Es común que los niños rechacen algunos alimentos. Consulta con un profesional (pediatra, terapeuta ocupacional o especialista en alimentación) si tu hijo:</p>
<ul class="lista"><li>Acepta muy pocos alimentos (menos de 15 a 20) o deja de comer los que antes comía.</li><li>Tiene arcadas, tose o se atraganta con frecuencia al comer o beber.</li><li>No aumenta de peso o las comidas son siempre una batalla.</li></ul></div>''')
    for i, r in enumerate(COMER, 1): pag(rutina('Alimentación', i, r, AC))
    divisor(3, 'Higiene personal', f'{len(HIGIENE)} rutinas de cuidado personal, del lavado de manos a la hora del baño.', ['jabon', 'cepillo', 'inodoro', 'toalla', 'peine'])
    for i, r in enumerate(HIGIENE, 1): pag(rutina('Higiene', i, r, AC))

    divisor(4, 'Recursos imprimibles', 'Rutinas visuales, tarjetas de pictogramas, registro de ayudas y tablero de logros.', ['sol', 'luna', 'estrella', 'reloj', 'mochila'])
    def rutina_visual(titulo, ic, items):
        filas = ''.join(f'<div class="fila"><span class="num">{k}</span><span style="width:18mm;height:18mm">{icono(i)}</span><span>{e(t)}</span><span class="box"></span></div>' for k, (i, t) in enumerate(items, 1))
        pag(f'''<div style="display:flex;align-items:center;gap:5mm"><div style="width:22mm">{icono(ic)}</div><div><div class="kicker">Para imprimir y pegar</div><h2>{titulo}</h2></div></div>
<p class="nota" style="margin-top:2mm">Recorta o deja completa. El niño marca cada casilla al terminar el paso.</p><div class="rutina-v">{filas}</div>''')
    rutina_visual('Mi rutina de la mañana', 'sol', [('cama', 'Me levanto'), ('inodoro', 'Voy al baño'), ('jabon', 'Me lavo las manos'), ('cara', 'Me lavo la cara'), ('camiseta', 'Me visto'), ('cuchara', 'Desayuno'), ('cepillo', 'Me cepillo los dientes'), ('mochila', '¡Listo para salir!')])
    rutina_visual('Mi rutina de la noche', 'luna', [('plato', 'Ceno'), ('tina', 'Me baño'), ('camiseta', 'Me pongo el pijama'), ('cepillo', 'Me cepillo los dientes'), ('inodoro', 'Voy al baño'), ('jabon', 'Me lavo las manos'), ('estrella', 'Cuento o canción'), ('cama', 'A dormir')])

    nombres = [('camiseta', 'Camiseta'), ('pantalon', 'Pantalón'), ('calcetin', 'Calcetines'), ('zapato', 'Zapatos'), ('boton', 'Botones'), ('cierre', 'Cierre'), ('cuchara', 'Cuchara'), ('tenedor', 'Tenedor'), ('vaso', 'Vaso'), ('plato', 'Comer'), ('grifo', 'Agua'), ('jabon', 'Jabón'),
               ('toalla', 'Toalla'), ('cepillo', 'Cepillo'), ('pasta', 'Pasta'), ('inodoro', 'Baño'), ('papel', 'Papel'), ('panuelo', 'Pañuelo'), ('peine', 'Peine'), ('tina', 'Bañera'), ('cama', 'Dormir'), ('mochila', 'Mochila'), ('estrella', '¡Bien hecho!'), ('reloj', 'Esperar')]
    for parte in (nombres[:12], nombres[12:]):
        tj = ''.join(f'<div class="tarjeta"><div class="pic">{icono(i)}</div>{e(t)}</div>' for i, t in parte)
        pag(f'''<div class="kicker">Para imprimir y recortar</div><h2 style="margin:3mm 0 2mm">Tarjetas de pictogramas</h2>
<p class="nota">Recorta por la línea punteada. Plastifícalas o cúbrelas con cinta ancha para que duren; con velcro puedes armar rutinas propias.</p><div class="tarjetas">{tj}</div>''')

    filas = ''.join(f'<tr><td>{d}</td>' + '<td></td>'*5 + '</tr>' for d in ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
    pag(f'''<div class="kicker">Para imprimir</div><h2 style="margin:3mm 0 3mm">Registro semanal de ayudas</h2>
<p class="lead">Escribe la rutina que están practicando y anota cada día la ayuda que necesitó.</p>
<p style="margin-top:5mm"><b>Rutina:</b> ______________________________ <b style="margin-left:6mm">Semana del:</b> ____________</p>
<table class="reg" style="margin-top:5mm"><tr><th>Día</th><th>Física total</th><th>Física parcial</th><th>Le mostré / señalé</th><th>Se lo dije</th><th>¡Solo!</th></tr>{filas}</table>
<div class="caja acento" style="margin-top:7mm"><h4>Cómo leer el registro</h4><p>Si las marcas se mueven hacia la derecha con las semanas, ¡está aprendiendo! Cuando haga la rutina solo durante una semana completa, celebra y elige la siguiente.</p></div>''')

    est = ''.join(f'<tr><td style="text-align:left;font-weight:800">{d}</td>' + '<td></td>'*4 + '</tr>' for d in ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
    pag(f'''<div style="display:flex;align-items:center;gap:5mm"><div style="width:24mm">{icono('estrella')}</div><div><div class="kicker">Para imprimir</div><h2>Mi tablero de logros</h2></div></div>
<p class="lead" style="margin-top:3mm">Cada vez que lo logre, dibuja o pega una estrella. Al completar la fila, ¡una recompensa elegida juntos!</p>
<p style="margin-top:6mm;font-weight:800">Estoy aprendiendo a: _________________________________</p>
<table class="reg estrellas" style="margin-top:5mm"><tr><th>Día</th><th>Mañana</th><th>Mediodía</th><th>Tarde</th><th>Noche</th></tr>{est}</table>
<p style="margin-top:7mm;font-weight:800">Mi recompensa: _________________________________</p>''')

    pag(f'''<div style="height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">
<div style="width:40mm">{icono('estrella')}</div><h2 style="margin:6mm 0 4mm">Paso a paso, con paciencia</h2>
<p class="lead" style="max-width:140mm">Cada niño tiene su propio ritmo. Lo importante no es la velocidad, sino que cada día pueda hacer un poquito más por sí mismo.</p>
<div style="margin-top:12mm;font-weight:900;font-size:16pt">Byignis</div><p class="nota">Material complementario de "300 Actividades de Terapia Ocupacional Infantil".</p></div>''', 'crema')

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out'); os.makedirs(out, exist_ok=True)
    hp = os.path.join(out, 'manual-autonomia.html')
    open(hp, 'w').write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(pags)}</body></html>')
    print('paginas', len(pags), 'rutinas', total)
    return hp

if __name__ == '__main__':
    import sys
    hp = main()
    if 'snap' in sys.argv:
        snapshot(hp, hp.replace('.html', ''), [int(x) for x in sys.argv[2:]])
    else:
        render_pdf(hp, hp.replace('.html', '.pdf'))
