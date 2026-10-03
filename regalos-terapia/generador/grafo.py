"""Regalo 1: Biblioteca Grafomotora — 57 actividades para la escritura a mano."""
import os
from common import C, e, base_css, pie, render_pdf, snapshot
from iconos import icono
import trazos as T

AC = C['mostaza']; AC_S = '#F6ECD2'
MARCA = 'Biblioteca Grafomotora'

# ---------------------------------------------------------------------------
# PARTE 1 · Antes del lápiz (preparación, postura y fuerza)
P1 = [
 dict(t='Mi rincón de escritura', para='Una buena postura libera el brazo y la mano para escribir con control y sin cansarse.',
      mat='Silla y mesa a su altura, cojín o caja como reposapiés.',
      pasos=['Comprueba la regla 90-90-90: cadera, rodillas y tobillos doblados en ángulo recto.', 'Los pies deben apoyarse completos en el suelo o en una caja.', 'La mesa queda a la altura del codo doblado, con los antebrazos apoyados.', 'La mano que no escribe sujeta el papel.'],
      facil='Usa un cojín firme en la silla y una caja bajo los pies.', dificil='Pídele que revise solo su postura antes de cada tarea.',
      logro='Se sienta solo en la postura correcta y la mantiene 10 minutos.'),
 dict(t='La carretilla', para='Fortalece hombros y brazos: un hombro estable da precisión a la mano.',
      mat='Espacio libre y alfombra.',
      pasos=['El niño apoya las manos en el suelo; tú lo sostienes de los muslos.', 'Camina con las manos hacia adelante, mirando el suelo.', 'Empieza con 2 metros y descansa.', 'Repite 3 veces.'],
      facil='Sostenlo más cerca de la cadera.', dificil='Sostenlo de los tobillos o hazlo recoger fichas por el camino.',
      logro='Recorre 4 metros sin apoyar la panza.'),
 dict(t='Dibujo en la pared', para='Trabajar en superficie vertical lleva la muñeca hacia atrás, la posición ideal para escribir.',
      mat='Papel pegado en la pared o pizarra, crayones.',
      pasos=['Pega el papel a la altura de sus ojos.', 'Que dibuje círculos, caminos y soles grandes.', 'Recuérdale mantener el codo abajo y la muñeca doblada hacia atrás.', '5 a 10 minutos por sesión.'],
      facil='Trazos grandes y libres con tiza o marcador grueso.', dificil='Copiar figuras pequeñas o laberintos en la pared.',
      logro='Dibuja 5 minutos sin apoyar el antebrazo en la pared.'),
 dict(t='Bolitas con la punta de los dedos', para='Fortalece los músculos pequeños de la mano que controlan el lápiz.',
      mat='Plastilina o masa casera.',
      pasos=['Toma un trocito del tamaño de un garbanzo.', 'Haz una bolita usando solo pulgar, índice y medio, sin la palma.', 'Haz 10 bolitas y forma una oruga.', 'Cambia de mano en cada ronda.'],
      facil='Masa más blanda y bolitas más grandes.', dificil='Bolitas del tamaño de una lenteja, o con los ojos cerrados.',
      logro='Hace 10 bolitas pequeñas solo con la punta de los dedos.'),
 dict(t='Pinzas de ropa', para='Desarrolla la fuerza de la pinza (pulgar con índice) para sujetar el lápiz.',
      mat='Pinzas de ropa y el borde de una caja de cartón.',
      pasos=['Coloca la caja frente al niño.', 'Que abra cada pinza con pulgar e índice y la cuelgue del borde.', 'Puedes pintar colores en el borde para hacer parejas.', 'Al terminar, que las quite una por una.'],
      facil='Pinzas suaves, de plástico.', dificil='Pinzas de madera duras o usar solo pulgar y dedo medio.',
      logro='Coloca 10 pinzas sin cambiar de agarre.'),
 dict(t='Rasgar y arrugar', para='Ambas manos trabajan juntas: una sujeta y la otra rasga, como al escribir.',
      mat='Papel de revista o seda, pegamento, un dibujo para rellenar.',
      pasos=['Rasga tiras de papel sujetando con las puntas de los dedos.', 'Corta las tiras en cuadritos.', 'Haz bolitas arrugando con una sola mano.', 'Pégalas sobre un dibujo para rellenarlo.'],
      facil='Papel de seda, que se rasga fácil.', dificil='Rasgar siguiendo una línea marcada.',
      logro='Rasga una tira siguiendo una línea recta.'),
 dict(t='Rescate con tenacillas', para='Prepara la mano para movimientos de abrir y cerrar controlados.',
      mat='Pinzas de cocina o de ensalada, pompones o bolitas, dos recipientes.',
      pasos=['Pon los pompones en un recipiente.', 'Que los traslade uno por uno al otro recipiente.', 'Cuenten juntos en voz alta.', 'Repite con la otra mano.'],
      facil='Pinzas grandes y objetos grandes.', dificil='Pinzas pequeñas y objetos pequeños, o clasificar por color.',
      logro='Traslada 15 objetos sin que se le caigan.'),
 dict(t='Tesoros en la masa', para='Fuerza de los dedos y separación de movimientos dentro de la mano.',
      mat='Plastilina firme y monedas o cuentas.',
      pasos=['Esconde 5 objetos dentro de una bola de plastilina.', 'El niño los busca jalando y pellizcando la masa.', 'Luego los vuelve a esconder para ti.', 'Celebra cada tesoro encontrado.'],
      facil='Masa blanda y objetos grandes.', dificil='Masa dura y cuentas pequeñas.',
      logro='Encuentra los 5 tesoros en menos de 2 minutos.'),
 dict(t='Camino de pegatinas', para='Pinza fina precisa: despegar con la uña y colocar en un punto exacto.',
      mat='Hoja de pegatinas pequeñas, papel con un camino dibujado.',
      pasos=['Dibuja un camino o una letra grande.', 'Que despegue cada pegatina usando la punta de los dedos.', 'La pega encima de la línea, una tras otra.', 'Al final repasa el camino con el dedo.'],
      facil='Pegatinas grandes, ya levantadas en una esquina.', dificil='Pegatinas pequeñas sobre letras.',
      logro='Despega y coloca 10 pegatinas sobre la línea.'),
 dict(t='Rociador de plantas', para='Fortalece la mano completa y la separación de los dedos.',
      mat='Atomizador con agua, plantas o una pizarra con tiza.',
      pasos=['Que apriete el gatillo con índice y medio.', 'Riega las plantas o borra dibujos de tiza.', 'Cuenta cuántas veces apretó.', 'Cambia de mano.'],
      facil='Atomizador pequeño y suave.', dificil='Apuntar a dibujos pequeños.',
      logro='Aprieta 20 veces seguidas con la misma mano.'),
]

# PARTE 2 · El agarre del lápiz
P2 = [
 dict(t='Crayones cortitos', para='Un crayón de 2–3 cm no deja espacio para la mano entera, así que los dedos toman la posición de pinza.',
      mat='Crayones partidos en trozos pequeños.',
      pasos=['Parte los crayones en trozos de 2 a 3 cm.', 'Dale solo trozos cortos para colorear y dibujar.', 'Observa: los dedos se acomodan solos en la punta.', 'Úsalos en sesiones cortas, a diario.'],
      facil='Trozos de 4 cm al principio.', dificil='Tiza o lápiz corto de golf.',
      logro='Colorea un dibujo usando pulgar, índice y medio.'),
 dict(t='Pellizca y voltea', para='Un truco para que el niño coloque solo el lápiz en la posición correcta.',
      mat='Lápiz y mesa.',
      pasos=['Pon el lápiz sobre la mesa, con la punta hacia el niño.', 'Que lo pellizque con pulgar e índice justo encima de la parte pintada.', 'Que lo voltee hacia sí mismo, por encima de la mano.', 'El lápiz cae apoyado en el dedo medio: ¡listo!'],
      facil='Marca con cinta dónde pellizcar.', dificil='Que lo haga solo antes de cada tarea.',
      logro='Coloca el lápiz correctamente sin ayuda.'),
 dict(t='El tesoro escondido', para='Separa los dos lados de la mano: el lado que maneja el lápiz y el que estabiliza.',
      mat='Un pompón o goma de borrar pequeña.',
      pasos=['Pon el pompón bajo el anular y el meñique.', 'Que lo sostenga escondido mientras dibuja.', 'Si se cae, se recoge y se sigue.', 'Empieza con 2 minutos.'],
      facil='Pompón más grande.', dificil='Escribir una palabra completa sin soltarlo.',
      logro='Dibuja 3 minutos sin soltar el tesoro.'),
 dict(t='Escribir en plano inclinado', para='La superficie inclinada pone la muñeca en extensión y mejora el control.',
      mat='Archivador de anillas grueso o atril.',
      pasos=['Coloca el archivador con el lomo hacia arriba, lejos del niño.', 'Fija la hoja con una pinza.', 'Que dibuje o escriba sobre la inclinación.', 'Compara con la mesa plana.'],
      facil='Inclinación pequeña.', dificil='Escribir frases completas.',
      logro='Mantiene la muñeca hacia atrás durante toda la tarea.'),
 dict(t='El lápiz adecuado', para='El grosor y la forma del lápiz cambian mucho el agarre.',
      mat='Lápiz triangular, grueso, normal y adaptadores si tienes.',
      pasos=['Prueba cada lápiz en la misma ficha de trazos.', 'Observa cuál le deja usar la punta de los dedos.', 'Para manos pequeñas, el triangular suele ayudar.', 'Usa el adaptador solo si el agarre no mejora.'],
      facil='Lápiz triangular grueso.', dificil='Pasar poco a poco al lápiz normal.',
      logro='Elige su lápiz y lo sostiene en pinza trípode.'),
 dict(t='Tiza en la acera', para='La tiza corta y la superficie rugosa dan información a los dedos y fortalecen la pinza.',
      mat='Tizas cortas, suelo o pizarra.',
      pasos=['Dibuja caminos y figuras grandes en el suelo.', 'El niño los repasa con tiza corta, de rodillas.', 'Apoyar el peso en el otro brazo fortalece el hombro.', 'Termina borrando con un trapo.'],
      facil='Tiza gruesa.', dificil='Tiza cortita de 2 cm y figuras pequeñas.',
      logro='Repasa un camino largo sin cambiar de agarre.'),
 dict(t='La presión justa', para='Algunos niños aprietan tanto que rompen la punta; otros escriben tan suave que no se ve.',
      mat='Lámina de foami (goma eva) bajo la hoja.',
      pasos=['Pon el foami bajo el papel.', 'Si aprieta mucho, el lápiz rompe el papel: debe ser más suave.', 'Si aprieta poco, la línea casi no se ve: un poco más fuerte.', 'Jueguen a "suave como pluma" y "fuerte como roca".'],
      facil='Lápiz blando (2B) que marca con poca presión.', dificil='Escribir sin romper el papel durante una ficha completa.',
      logro='Termina una ficha sin romper el papel ni dejar líneas débiles.'),
 dict(t='Los dedos saludan', para='Mejora la independencia de cada dedo, clave para mover el lápiz con precisión.',
      mat='Ninguno, o caritas dibujadas en las yemas.',
      pasos=['Que toque con el pulgar la punta de cada dedo, uno por uno.', 'Ida y vuelta: índice, medio, anular, meñique y de regreso.', 'Hazlo lento y luego más rápido.', 'Con una mano y luego con la otra.'],
      facil='Solo índice y medio.', dificil='Con los ojos cerrados o con las dos manos a la vez.',
      logro='Toca los 4 dedos ida y vuelta sin saltarse ninguno.'),
]

# PARTE 4 · Escritura multisensorial y juegos
P4 = [
 dict(t='Bandeja de sal', para='Practicar letras y trazos sin miedo a equivocarse: se borra agitando la bandeja.',
      mat='Bandeja, sal o arena, tarjetas con modelos.',
      pasos=['Cubre el fondo de la bandeja con sal.', 'Muestra una tarjeta con un trazo o letra.', 'El niño la traza con el dedo índice.', 'Agita para borrar y repite.'],
      facil='Trazos simples: líneas y círculos.', dificil='Letras y su nombre.',
      logro='Escribe su nombre en la sal sin ver el modelo.'),
 dict(t='Letras de plastilina', para='Construir la letra ayuda a entender su forma y sus partes.',
      mat='Plastilina, tarjetas de letras grandes.',
      pasos=['Haz churritos de plastilina rodando con las palmas.', 'Colócalos encima de la letra modelo.', 'Repasa la letra de plastilina con el dedo.', 'Dila en voz alta.'],
      facil='Letras de una sola pieza: c, o, l.', dificil='Letras con varias partes: k, f, x.',
      logro='Forma 5 letras sin modelo.'),
 dict(t='¿Qué letra escribí?', para='Trabaja la percepción del trazo con el tacto, sin la vista.',
      mat='Ninguno.',
      pasos=['Escribe con el dedo un trazo o letra grande en su espalda.', 'El niño adivina cuál es.', 'Luego cambian de rol.', 'Empieza con formas: círculo, línea, cruz.'],
      facil='Solo formas básicas.', dificil='Letras y números.',
      logro='Adivina 5 de 6 trazos.'),
 dict(t='Del aire al papel', para='Aprende primero el movimiento grande y luego lo hace pequeño.',
      mat='Ninguno, luego papel y lápiz.',
      pasos=['Dibuja el trazo en el aire con el brazo estirado.', 'Repítelo más pequeño, con el codo doblado.', 'Ahora con el dedo sobre la mesa.', 'Por último, con lápiz en el papel.'],
      facil='Trazos de una dirección.', dificil='Letras con cambio de dirección.',
      logro='Hace el mismo trazo en los cuatro tamaños.'),
 dict(t='Agua mágica', para='Practica trazos verticales en pizarra: la muñeca trabaja en la posición correcta.',
      mat='Pincel, vaso con agua, pizarra o pared exterior.',
      pasos=['Moja el pincel en agua.', 'Repasa letras o figuras dibujadas con tiza.', 'La tiza "desaparece" donde pasa el agua.', 'Celebra cuando el dibujo se borra completo.'],
      facil='Figuras grandes.', dificil='Letras pequeñas.',
      logro='Borra una letra siguiendo su trazo exacto.'),
 dict(t='Bolsa sensorial', para='Ideal para niños que evitan el lápiz: trazar se vuelve juego.',
      mat='Bolsa con cierre hermético, gel para el cabello o pintura, cinta adhesiva.',
      pasos=['Llena la bolsa con gel y ciérrala bien con cinta.', 'Pégala sobre una hoja con trazos.', 'El niño sigue los trazos presionando con el dedo.', 'Alisa la bolsa para borrar.'],
      facil='Trazos rectos.', dificil='Laberintos y letras.',
      logro='Recorre un laberinto sin salirse.'),
 dict(t='Carreteras para carritos', para='Antes del lápiz, el niño planifica el recorrido con un juguete.',
      mat='Carrito pequeño, papel grande, marcador.',
      pasos=['Dibuja una carretera con curvas.', 'El niño pasea el carrito sin salirse.', 'Luego la recorre con el dedo.', 'Por último, con lápiz por el centro.'],
      facil='Carretera ancha.', dificil='Carretera estrecha con muchas curvas.',
      logro='Traza la carretera con lápiz sin tocar los bordes.'),
 dict(t='Dibujo dictado', para='Une la escucha, la orientación en el papel y el trazo.',
      mat='Papel y lápiz.',
      pasos=['Da instrucciones: "dibuja un círculo arriba".', 'Luego: "una línea abajo del círculo".', 'Sigue hasta formar una figura sorpresa.', 'Comparen el resultado.'],
      facil='2 o 3 instrucciones.', dificil='Instrucciones con derecha e izquierda.',
      logro='Sigue 5 instrucciones seguidas.'),
]

# PARTE 3 · Fichas imprimibles de trazo (nivel, título, objetivo, cómo, consejo, svg)
def F():
    a = AC
    return [
 (1, 'Lluvia que cae', 'Trazos verticales de arriba hacia abajo.', 'Repasa cada gota desde el punto verde hacia abajo.', 'Siempre de arriba hacia abajo: así se escriben las letras.', T.filas(T.p_vertical, a)),
 (1, 'Caminos rectos', 'Trazos horizontales de izquierda a derecha.', 'Lleva el lápiz por el camino sin levantarlo.', 'Que la otra mano sujete la hoja.', T.filas(T.p_horizontal, a, n=6)),
 (1, 'Gusanos ondulados', 'Curvas suaves y continuas.', 'Sigue la onda sin levantar el lápiz.', 'Antes, haz la onda en el aire con todo el brazo.', T.filas(T.p_onda, a, ciclos=2)),
 (1, 'Burbujas', 'El círculo, base de letras como a, o, d.', 'Empieza en el punto verde y gira hacia la izquierda.', 'El sentido antihorario es el de las letras redondas.', T.filas(T.p_circulos, a)),
 (2, 'Toboganes', 'Diagonales hacia abajo.', 'Baja por cada tobogán desde el punto verde.', 'Dile "arriba… y abajo" mientras traza.', T.filas(T.p_diag, a)),
 (2, 'Cohetes', 'Diagonales hacia arriba.', 'Sube cada cohete desde abajo.', 'Las diagonales llegan cerca de los 4–5 años: ten paciencia.', T.filas(T.p_diag, a, sube=True)),
 (2, 'Cruces', 'Combinar vertical y horizontal.', 'Primero la línea de arriba abajo, luego la de lado.', 'Fíjate en que las líneas se crucen en el centro.', T.filas(T.p_cruz, a)),
 (2, 'Aspas', 'Cruzar dos diagonales.', 'Traza cada línea desde su punto verde.', 'Es la base de letras como x, k, v.', T.filas(T.p_cruz, a, aspa=True)),
 (2, 'Montañas', 'Zigzag grande: cambio de dirección.', 'Sube y baja sin levantar el lápiz.', 'Haz una pausa pequeña en cada pico.', T.filas(T.p_zigzag, a, n=5, h=80)),
 (2, 'Dientes de tiburón', 'Zigzag pequeño y preciso.', 'Traza los dientes, todos del mismo tamaño.', 'Si se deforma, vuelve a la ficha de Montañas.', T.filas(T.p_zigzag, a, n=10, h=36)),
 (3, 'Olas del mar', 'Ondas pequeñas y seguidas.', 'Sigue las olas de izquierda a derecha.', 'Ritmo: "sube, baja, sube, baja".', T.filas(T.p_onda, a, ciclos=5, h=40)),
 (3, 'Puentes', 'Arcos hacia arriba (como la n y la m).', 'Sube, curva y baja en cada puente.', 'Mantén todos los puentes de la misma altura.', T.filas(T.p_arcos, a, n=5, h=60)),
 (3, 'Tazas', 'Arcos hacia abajo (como la u).', 'Baja, curva y sube en cada taza.', 'Es el movimiento inverso a los puentes.', T.filas(T.p_arcos, a, n=5, h=60, abajo=True)),
 (3, 'Caracoles', 'Espiral de afuera hacia adentro.', 'Empieza en el punto verde y gira hasta el centro.', 'Luego prueba al revés: del centro hacia afuera.', T.filas(T.p_espiral, a, n=3, h=150)),
 (3, 'La carretera ancha', 'Controlar el trazo dentro de un límite.', 'Lleva el lápiz del punto verde a la estrella sin tocar los bordes.', 'Antes, recórrela con un carrito o con el dedo.', T.camino(a, ancho=86, ciclos=1, amp=120)),
 (3, 'La carretera estrecha', 'Más control y precisión.', 'Llega a la estrella sin salirte del camino.', 'Ve lento: aquí gana el que no se sale, no el más rápido.', T.camino(a, ancho=46, ciclos=1.5, amp=90)),
 (4, 'Resortes', 'Bucles grandes (base de la letra cursiva).', 'Traza los bucles sin levantar el lápiz.', 'Haz primero los resortes en el aire.', T.filas(T.p_bucles, a, n=5, h=80)),
 (4, 'Ruedas de bicicleta', 'Bucles pequeños y seguidos.', 'Sigue cada rueda de izquierda a derecha.', 'Si se aplastan, vuelve a Resortes.', T.filas(T.p_bucles, a, n=8, h=46)),
 (4, 'Escaleras', 'Ángulos rectos y cambio de dirección.', 'Sube la escalera escalón por escalón.', 'Haz una pausa en cada esquina.', T.filas(T.p_escalera, a, n=7, h=70, x0=60, x1=540)),
 (4, 'Castillos', 'Arriba, lado, abajo, lado.', 'Traza las almenas del castillo sin levantar el lápiz.', 'Cuenta en voz alta cada cambio.', T.filas(T.p_almenas, a, n=6, h=46)),
 (4, 'Cajas', 'El cuadrado: cuatro lados y cuatro esquinas.', 'Empieza arriba a la izquierda y cierra la caja.', 'El cuadrado se logra cerca de los 4 años.', T.filas(T.p_cuadrados, a)),
 (4, 'Techos', 'El triángulo, con dos diagonales.', 'Empieza en la punta de arriba.', 'El triángulo suele lograrse cerca de los 5 años.', T.filas(T.p_triangulos, a)),
 (4, 'Olas y montañas', 'Combinar curvas y ángulos en un solo trazo.', 'Traza sin levantar el lápiz, cambiando de curva a pico.', 'Di en voz alta: "curva, curva, pico, pico".', T.filas(T.p_combinado, a)),
 (4, 'Une los puntos', 'Planificar el trazo siguiendo un orden.', 'Une los puntos del 1 al 10 y descubre la figura.', 'Que diga el número antes de unir cada punto.', T.unir_puntos(a)),
 (5, 'Calco: la casa', 'Reproducir una figura completa.', 'Repasa la casa desde el punto verde.', 'Al terminar, ¡a colorearla!', T.calco(a, 'casa')),
 (5, 'Calco: el pez', 'Curvas cerradas y detalles.', 'Repasa el pez y su ojo.', 'Gira la hoja si le resulta más cómodo.', T.calco(a, 'pez')),
 (5, 'Calco: el árbol', 'Curvas irregulares.', 'Repasa la copa y luego el tronco.', 'Puede terminarlo dibujando frutas.', T.calco(a, 'arbol')),
 (5, 'Calco: el sol', 'Círculo y rayos en todas las direcciones.', 'Primero el círculo, luego cada rayo hacia afuera.', 'Los rayos combinan vertical, horizontal y diagonal.', T.calco(a, 'sol')),
 (5, 'Espejo', 'Simetría y orientación en el espacio.', 'Completa la otra mitad de la casa al otro lado de la línea roja.', 'Cuenta los cuadritos para no perderte.', T.cuadricula(a)),
 (5, 'Copia en cuadrícula', 'Copiar un modelo: planificación visual.', 'Copia cada figura en la cuadrícula de la derecha.', 'Empieza por un punto de esquina y cuenta.', T.copiar_figura(a)),
 (5, 'Números', 'Trazo correcto de los números.', 'Repasa por dentro de cada número, empezando arriba.', 'Repasa con el dedo antes que con el lápiz.', T.texto_trazo(a, ['*0 1 2 3 4', '0 1 2 3 4', '*5 6 7 8 9', '5 6 7 8 9'])),
 (5, 'Vocales', 'Las primeras letras.', 'Repasa por dentro de cada vocal; se apoyan en la línea azul.', 'Las letras se apoyan en la línea azul.', T.texto_trazo(a, ['*a e i o u', 'a e i o u', '*A E I O U', 'A E I O U'])),
 (5, 'Mi pauta de escritura', 'Escribir respetando el tamaño de las letras.', 'Escribe tu nombre y palabras favoritas entre las líneas.', 'Las letras pequeñas llegan a la línea roja; las altas, a la azul de arriba.', T.pauta(a)),
    ]

# ---------------------------------------------------------------------------
TIPS = [
 'Calienta las manos antes de escribir: frotarlas, abrir y cerrar los puños 10 veces y "tocar el piano" en la mesa.',
 'Si el niño se frustra, baja un nivel. Terminar con éxito es más importante que terminar la tarea.',
 'Las manos fuertes nacen del juego: trepar, colgarse, empujar y jalar también preparan para escribir.',
 'Felicita el esfuerzo, no solo el resultado: "te esforzaste mucho en hacer la curva lenta".',
 'Pocos minutos y todos los días: la constancia es lo que construye la habilidad.',
 'Observa el codo y el hombro: si el brazo "flota" o se tensa, vuelve a las actividades de estabilidad.',
 'Los niños aprenden imitando. Haz tú la actividad primero y luego túrnense.',
 'Si aprieta mucho el lápiz, revisa la postura: un cuerpo inestable compensa apretando la mano.',
 'Cambia el material para mantener la motivación: marcadores, tizas, pinceles o crayones gruesos.',
 'Antes de una ficha, haz el mismo trazo en el aire o con el dedo: el cuerpo aprende el movimiento primero.',
 'Deja que el niño elija el orden de las actividades: sentir control aumenta la cooperación.',
 'Una pausa de movimiento (saltar, empujar la pared) ayuda a los niños inquietos a volver a concentrarse.',
 'Guarda sus trabajos con fecha: comparar el mes 1 con el mes 3 es la mejor motivación.',
]
tip_i = [0]
def tip():
    t = TIPS[tip_i[0] % len(TIPS)]; tip_i[0] += 1
    return f'<div class="tip"><b>Consejo de terapia</b>{e(t)}</div>'

def actividad(n, a, color):
    return f'''<div class="act">
  <div class="act-top"><span class="num" style="background:{color}">{n:02d}</span><h3>{e(a["t"])}</h3></div>
  <p class="para">{e(a["para"])}</p>
  <div class="act-grid">
    <div><h4>Paso a paso</h4><ol class="pasos">{''.join(f"<li>{e(x)}</li>" for x in a["pasos"])}</ol></div>
    <div>
      <div class="mini"><b>Materiales</b>{e(a["mat"])}</div>
      <div class="mini"><b>↓ Más fácil</b>{e(a["facil"])}</div>
      <div class="mini"><b>↑ Más reto</b>{e(a["dificil"])}</div>
    </div>
  </div>
  <div class="logro"><span class="check"></span><b>Logrado:</b> {e(a["logro"])}</div>
</div>'''

NIVELES = {1: 'Trazos básicos', 2: 'Diagonales y cruces', 3: 'Curvas y control', 4: 'Bucles y figuras', 5: 'Hacia la escritura'}

def main():
    css = base_css(AC, AC_S) + f"""
.portada {{ background: {C['crema']}; padding: 30mm 22mm }}
.portada h1 {{ font-size: 46pt; margin: 8mm 0 6mm }}
.portada .deco {{ position: absolute; right: 22mm; bottom: 24mm; width: 112mm; height: 128mm; background: #fff; border-radius: 6mm; padding: 6mm 6mm 10mm; box-shadow: 0 6mm 14mm rgba(31,36,51,.10); transform: rotate(-3deg) }}
.indice-item {{ display: flex; align-items: center; gap: 4mm; padding: 3.2mm 0; border-bottom: 1px solid {C['linea']}; font-weight: 700 }}
.indice-item .n {{ width: 9mm; height: 9mm; border-radius: 50%; background: {AC}; color: #fff; display: grid; place-items: center; font-weight: 900 }}
.indice-item small {{ color: {C['gris']}; font-weight: 600; margin-left: auto }}
.acts {{ height: 252mm; display: flex; flex-direction: column; gap: 6mm }}
.acts .act {{ margin: 0; display: flex; flex-direction: column; padding: 7mm 8mm; font-size: 11pt }}
.tip {{ margin-top: auto; background: {AC_S}; border-radius: 4mm; padding: 5mm 7mm; font-size: 11pt; border-left: 2.4mm solid {AC} }}
.tip b {{ display: block; color: {AC}; font-size: 8.6pt; letter-spacing: 1.6px; text-transform: uppercase; margin-bottom: 1mm }}
.acts .act h3 {{ font-size: 16pt }}
.acts ol.pasos li {{ margin: 2.6mm 0 }}
.act {{ border: 1.4px solid {C['linea']}; border-radius: 4mm; padding: 5mm 6mm; margin-bottom: 6mm; background: #fff }}
.act-top {{ display: flex; align-items: center; gap: 3.5mm; margin-bottom: 2mm }}
.num {{ color: #fff; font-weight: 900; border-radius: 2.4mm; padding: 1mm 2.6mm; font-size: 11pt }}
.para {{ color: {C['gris']}; margin-bottom: 3mm }}
.act-grid {{ display: grid; grid-template-columns: 1.35fr 1fr; gap: 5mm }}
.mini {{ background: {C['crema']}; border-radius: 2.6mm; padding: 2.4mm 3.4mm; margin-bottom: 2.2mm; font-size: 9.2pt; line-height: 1.4 }}
.mini b {{ display: block; font-size: 8.4pt; color: {AC}; letter-spacing: .4px; text-transform: uppercase }}
.logro {{ margin-top: 2.4mm; padding-top: 2.6mm; border-top: 1.4px dashed {C['linea']}; font-size: 9.4pt }}
.ficha-head {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 6mm }}
.ficha-area {{ margin-top: 5mm; width: 174mm; height: 186mm; border: 1.6px solid {C['linea']}; border-radius: 5mm; padding: 2mm }}
.nombre {{ display: flex; gap: 8mm; font-size: 9.5pt; color: {C['gris']}; margin-top: 5mm }}
.nombre span {{ flex: 1; border-bottom: 1.4px solid {C['linea']}; padding-bottom: 1mm }}
.divisor h2 {{ font-size: 38pt; margin: 6mm 0 }}
.divisor {{ position: absolute; left: 22mm; right: 22mm; top: 50mm }}
.grande {{ position: absolute; right: 16mm; bottom: 20mm; font-size: 220pt; font-weight: 900; color: rgba(255,255,255,.22); line-height: 1; letter-spacing: -6px }}
.div-lista {{ margin-top: 12mm; display: flex; flex-direction: column; gap: 2.6mm; font-weight: 700; font-size: 12pt }}
.div-lista span {{ background: rgba(255,255,255,.16); border-radius: 3mm; padding: 2.4mm 4.4mm; width: max-content }}
.etapa {{ display: grid; grid-template-columns: 14mm 1fr 30mm; gap: 4mm; align-items: center; padding: 3.6mm 0; border-bottom: 1px solid {C['linea']} }}
.etapa .n {{ width: 12mm; height: 12mm; border-radius: 50%; background: {AC_S}; color: {AC}; font-weight: 900; display: grid; place-items: center; font-size: 13pt }}
.etapa .edad {{ text-align: right; font-weight: 800; color: {AC} }}
.diploma {{ border: 3mm solid {AC}; border-radius: 6mm; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 14mm; background: {C['crema']} }}
"""
    pags = []; num = [0]
    def pag(body, cls='', pie_txt=None):
        num[0] += 1
        pags.append(f'<section class="pag {cls}">{body}{pie(MARCA, pie_txt or str(num[0])) if num[0] > 1 else ""}</section>')

    fichas = F()
    total = len(P1) + len(P2) + len(fichas) + len(P4)

    # Portada
    pag(f'''<div class="kicker">Regalo exclusivo · Material para casa y terapia</div>
<h1>Biblioteca<br>Grafomotora</h1>
<p class="lead" style="max-width:150mm">{total} actividades y fichas imprimibles para preparar la mano, mejorar el agarre del lápiz y avanzar paso a paso hacia la escritura.</p>
<div style="display:flex;gap:3mm;margin-top:9mm;flex-wrap:wrap">
<span class="chip">Antes del lápiz · {len(P1)}</span><span class="chip">El agarre · {len(P2)}</span><span class="chip">Fichas de trazo · {len(fichas)}</span><span class="chip">Juegos multisensoriales · {len(P4)}</span></div>
<div style="position:absolute;left:22mm;bottom:22mm;font-weight:900;font-size:14pt">Byignis</div>
<div class="deco"><div style="font-weight:800;font-size:9pt;letter-spacing:2px;color:{AC};margin-bottom:3mm">EJEMPLO DE FICHA</div>{T.filas(T.p_onda, AC, n=4, h=70, ciclos=2)}</div>''', 'portada')

    # Cómo usar
    pag(f'''<div class="kicker">Antes de empezar</div><h2 style="margin:3mm 0 6mm">Cómo usar esta biblioteca</h2>
<p class="lead">La escritura no empieza con el lápiz: empieza con un cuerpo estable, una mano fuerte y dedos que saben moverse por separado. Por eso este material avanza en cuatro partes.</p>
<div style="margin-top:7mm">
{''.join(f'<div class="indice-item"><span class="n">{i}</span>{t}<small>{s}</small></div>' for i, t, s in [
 (1, 'Antes del lápiz: postura, hombro y fuerza de la mano', f'{len(P1)} actividades'),
 (2, 'El agarre: cómo sostener el lápiz', f'{len(P2)} actividades'),
 (3, 'Fichas de trazo imprimibles, en 5 niveles', f'{len(fichas)} fichas'),
 (4, 'Escritura multisensorial y juegos', f'{len(P4)} actividades')])}
</div>
<div class="grid2" style="margin-top:9mm">
<div class="caja"><h4>Sesiones cortas, todos los días</h4><p>10 a 15 minutos diarios dan más resultado que una hora a la semana. Termina siempre con algo que le salga bien.</p></div>
<div class="caja"><h4>Combina las partes</h4><p>Una buena sesión: 1 actividad de la parte 1 o 2 como calentamiento, 1 ficha de trazo y 1 juego de la parte 4.</p></div>
<div class="caja"><h4>Imprime las fichas</h4><p>Imprime solo las fichas que necesites, o mételas en un folio plástico y usa marcador borrable para reutilizarlas.</p></div>
<div class="caja"><h4>Respeta su ritmo</h4><p>Las edades son orientativas. Si una ficha cuesta mucho, vuelve a la anterior: avanzar con éxito motiva más que forzar.</p></div>
</div>
<p class="nota" style="margin-top:8mm">Este material es de apoyo y no sustituye la evaluación ni el tratamiento de un terapeuta ocupacional. Si tienes dudas sobre el desarrollo de tu hijo, consulta con un profesional.</p>''')

    # Etapas del agarre
    etapas = [
        ('Agarre palmar', 'Sostiene el crayón con el puño cerrado y mueve todo el brazo.', '1 – 1½ años'),
        ('Agarre digital', 'La palma mira hacia abajo y los dedos rodean el crayón; el movimiento sale del hombro y el codo.', '2 – 3 años'),
        ('Trípode estático o de 4 dedos', 'Usa la punta de los dedos, pero mueve la muñeca y el brazo en bloque.', '3½ – 4 años'),
        ('Trípode dinámico', 'Pulgar, índice y medio sostienen el lápiz y lo mueven; la muñeca y el brazo quedan quietos.', '4½ – 6 años'),
    ]
    pag(f'''<div class="kicker">Guía rápida</div><h2 style="margin:3mm 0 4mm">Cómo evoluciona el agarre del lápiz</h2>
<p class="lead">El agarre madura con la edad. Identifica en qué etapa está tu hijo para elegir las actividades adecuadas.</p>
<div style="margin-top:6mm">{''.join(f'<div class="etapa"><span class="n">{i+1}</span><div><h4 style="margin:0">{t}</h4><span class="nota" style="font-size:9.5pt">{d}</span></div><span class="edad">{a}</span></div>' for i, (t, d, a) in enumerate(etapas))}</div>
<div class="grid2" style="margin-top:9mm">
<div class="caja acento"><h4>Señales para consultar a un profesional</h4><ul class="lista">
<li>Después de los 5 años sigue tomando el lápiz con el puño.</li><li>Se cansa o se queja de dolor en la mano al escribir.</li>
<li>Cambia de mano constantemente después de los 5 años.</li><li>Evita dibujar y colorear de forma persistente.</li></ul></div>
<div class="caja"><h4>Recuerda</h4><p>Las edades son aproximadas y cada niño tiene su ritmo. Un agarre diferente que es cómodo, legible y no cansa puede ser funcional.</p></div>
</div>''')

    def divisor(n, titulo, texto, items=()):
        lista = ''.join(f'<span>{e(x)}</span>' for x in items[:9])
        pag(f'''<div class="divisor"><div class="kicker">Parte {n}</div><h2>{titulo}</h2><p class="lead" style="max-width:140mm">{texto}</p><div class="div-lista">{lista}</div></div><div class="grande">0{n}</div>''', 'color')

    n_act = [0]
    def bloque(lista):
        for i in range(0, len(lista), 2):
            html_ = ''
            for a in lista[i:i+2]:
                n_act[0] += 1; html_ += actividad(n_act[0], a, AC)
            pag(f'<div class="acts">{html_}{tip()}</div>')

    divisor(1, 'Antes del lápiz', 'Postura, estabilidad del hombro y fuerza de la mano: la base invisible de una buena letra.', [a['t'] for a in P1])
    bloque(P1)
    divisor(2, 'El agarre', 'Estrategias y trucos para que el niño sostenga el lápiz con comodidad y control.', [a['t'] for a in P2])
    bloque(P2)
    divisor(3, 'Fichas de trazo', f'{len(fichas)} fichas imprimibles en 5 niveles: de las líneas simples a las primeras letras. La primera fila siempre es el modelo en color.', [f'Nivel {k} · {v}' for k, v in NIVELES.items()])
    for k, (nivel, titulo, obj, como, consejo, dibujo) in enumerate(fichas, 1):
        n_act[0] += 1
        pag(f'''<div class="ficha-head"><div><div class="kicker">Ficha {k} de {len(fichas)} · Nivel {nivel} · {NIVELES[nivel]}</div><h2 style="margin-top:2mm">{e(titulo)}</h2>
<p style="margin-top:2mm"><b>Objetivo:</b> {e(obj)} <b>Cómo:</b> {e(como)}</p></div>
<div style="width:20mm;flex:none">{icono("lapiz")}</div></div>
<div class="ficha-area">{dibujo}</div>
<div class="nombre"><span>Nombre:</span><span>Fecha:</span><span>¿Cómo me fue? ☆ ☆ ☆</span></div>
<p class="nota" style="margin-top:3mm"><b style="color:{AC}">CONSEJO ·</b> {e(consejo)}</p>''')
    divisor(4, 'Escritura multisensorial', 'Juegos con arena, plastilina, agua y movimiento para practicar trazos y letras sin presión.', [a['t'] for a in P4])
    bloque(P4)

    # Seguimiento
    filas = ''.join(f'<tr><td>{s}</td><td></td><td></td><td></td><td></td></tr>' for s in ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4', 'Semana 5', 'Semana 6', 'Semana 7', 'Semana 8'])
    pag(f'''<div class="kicker">Para imprimir</div><h2 style="margin:3mm 0 4mm">Registro de progreso</h2>
<p class="lead">Anota cada semana lo que practicaron y cómo fue. Ver el avance motiva a todos.</p>
<table class="reg" style="margin-top:6mm"><tr><th style="width:20%">Semana</th><th>Actividades / fichas</th><th style="width:16%">Agarre (1–4)</th><th style="width:16%">¿Le gustó?</th><th>Notas</th></tr>{filas}</table>
<p class="nota" style="margin-top:4mm">Agarre: 1 palmar · 2 digital · 3 trípode estático · 4 trípode dinámico (ver la guía de etapas).</p>''')

    pag(f'''<div class="diploma"><div style="width:34mm">{icono("estrella")}</div>
<div class="kicker" style="margin-top:6mm">Diploma</div><h1 style="font-size:38pt;margin:4mm 0">¡Lo logré!</h1>
<p class="lead">Este diploma es para</p><div style="width:120mm;border-bottom:2px solid {C['tinta']};height:14mm"></div>
<p class="lead" style="margin-top:8mm">por completar la Biblioteca Grafomotora con esfuerzo y paciencia.</p>
<div style="display:flex;gap:30mm;margin-top:18mm"><div style="width:50mm;border-top:1.6px solid {C['tinta']};padding-top:2mm" class="nota">Fecha</div><div style="width:50mm;border-top:1.6px solid {C['tinta']};padding-top:2mm" class="nota">Firma</div></div></div>''')

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out'); os.makedirs(out, exist_ok=True)
    hp = os.path.join(out, 'biblioteca-grafomotora.html')
    open(hp, 'w').write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(pags)}</body></html>')
    print('paginas', len(pags), 'actividades', total)
    return hp

if __name__ == '__main__':
    import sys
    hp = main()
    if 'snap' in sys.argv:
        snapshot(hp, hp.replace('.html', ''), [int(x) for x in sys.argv[2:]])
    else:
        render_pdf(hp, hp.replace('.html', '.pdf'))
