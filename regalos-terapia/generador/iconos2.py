"""Pictogramas para historias sociales (viewBox 0 0 100 100)."""
from common import C
from iconos import I, S, T

PIEL = '#F2C9A0'

def cara(boca, ojos='normal', extra='', cx=50, cy=50, r=34):
    o = {
        'normal': f'<circle cx="{cx-12}" cy="{cy-6}" r="3.4" fill="{T}"/><circle cx="{cx+12}" cy="{cy-6}" r="3.4" fill="{T}"/>',
        'cerrados': f'<path d="M{cx-17} {cy-6} q5 4 10 0 M{cx+7} {cy-6} q5 4 10 0" fill="none" {S}/>',
        'grandes': f'<circle cx="{cx-12}" cy="{cy-7}" r="5.5" fill="#fff" {S}/><circle cx="{cx+12}" cy="{cy-7}" r="5.5" fill="#fff" {S}/><circle cx="{cx-12}" cy="{cy-7}" r="2" fill="{T}"/><circle cx="{cx+12}" cy="{cy-7}" r="2" fill="{T}"/>',
        'enojado': f'<path d="M{cx-19} {cy-15} l11 5 M{cx+19} {cy-15} l-11 5" {S}/><circle cx="{cx-12}" cy="{cy-5}" r="3.4" fill="{T}"/><circle cx="{cx+12}" cy="{cy-5}" r="3.4" fill="{T}"/>',
    }[ojos]
    b = {
        'feliz': f'<path d="M{cx-13} {cy+9} q13 13 26 0" fill="none" {S}/>',
        'triste': f'<path d="M{cx-12} {cy+16} q12 -10 24 0" fill="none" {S}/>',
        'neutra': f'<path d="M{cx-10} {cy+12} h20" {S}/>',
        'abierta': f'<ellipse cx="{cx}" cy="{cy+13}" rx="7" ry="6" fill="{T}"/>',
        'ondulada': f'<path d="M{cx-14} {cy+13} q4 -5 7 0 q4 5 7 0 q4 -5 7 0 q4 5 7 0" fill="none" {S}/>',
    }[boca]
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{PIEL}" {S}/>{o}{b}{extra}'

def persona(x=50, color=None, s=1.0, pelo=None):
    color = color or C['azul']
    hx, hy = x, 30*s + (1-s)*60
    return (f'<rect x="{x - 20*s:.1f}" y="{hy + 16*s:.1f}" width="{40*s:.1f}" height="{46*s:.1f}" rx="{14*s:.1f}" fill="{color}" {S}/>'
            f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="{15*s:.1f}" fill="{PIEL}" {S}/>'
            + (f'<path d="M{hx - 15*s:.1f} {hy - 2*s:.1f} a{15*s:.1f} {15*s:.1f} 0 0 1 {30*s:.1f} 0 q-15 -8 -30 0" fill="{pelo}" {S}/>' if pelo else ''))

LAG = f'<path d="M30 26 q-3 6 0 9" stroke="{C["azul"]}" stroke-width="4" fill="none" stroke-linecap="round"/>'

N = {
 'feliz': cara('feliz'), 'triste': cara('triste', extra=f'<path d="M36 52 q-3 7 0 10" stroke="{C["azul"]}" stroke-width="4" fill="none" stroke-linecap="round"/>'),
 'enojado': cara('neutra', 'enojado', extra=f'<path d="M80 14 l6 -6 M86 22 l8 -2" stroke="{C["rojo"]}" stroke-width="4" stroke-linecap="round"/>'),
 'miedo': cara('ondulada', 'grandes'), 'calma': cara('feliz', 'cerrados'), 'sorpresa': cara('abierta', 'grandes'),
 'nervioso': cara('ondulada', 'normal', extra=f'<path d="M82 30 q4 6 0 10" stroke="{C["azul"]}" stroke-width="4" fill="none" stroke-linecap="round"/>'),
 'yo': persona(50, C['naranja'], pelo='#6B4A2B'),
 'adulto': persona(50, C['verde'], pelo='#3A2A1E'),
 'doctor': persona(50, '#FFFFFF', pelo='#3A2A1E') + f'<path d="M50 60 v12 M44 66 h12" stroke="{C["rojo"]}" stroke-width="5" stroke-linecap="round"/>',
 'maestra': persona(40, C['morado'], pelo='#6B4A2B') + f'<rect x="64" y="20" width="30" height="24" rx="3" fill="{C["verde"]}" {S}/><path d="M70 34 h14" stroke="#fff" stroke-width="3"/>',
 'amigos': persona(30, C['naranja'], .8, '#6B4A2B') + persona(70, C['azul'], .8, '#2B1E14'),
 'familia': persona(24, C['verde'], .9, '#3A2A1E') + persona(76, C['morado'], .9, '#6B4A2B') + persona(50, C['naranja'], .62, '#6B4A2B'),
 'bebe': f'<ellipse cx="50" cy="66" rx="30" ry="20" fill="#CFE3F5" {S}/>' + cara('feliz', 'cerrados', cx=50, cy=38, r=22),
 'fila': persona(22, C['azul'], .7) + persona(50, C['naranja'], .7) + persona(78, C['verde'], .7) + f'<path d="M8 92 h84" {S}/>',
 'mano_arriba': f'<path d="M40 92 v-40 l-8 -22 c-2 -6 6 -9 8 -3 l6 14 v-34 c0 -7 9 -7 9 0 v28 v-32 c0 -7 9 -7 9 0 v32 v-26 c0 -7 9 -7 9 0 v40 c0 18 -8 28 -16 43 z" fill="{PIEL}" {S}/>',
 'abrazo': f'<path d="M50 84 c-30 -18 -40 -34 -34 -48 c6 -14 26 -14 34 2 c8 -16 28 -16 34 -2 c6 14 -4 30 -34 48 z" fill="{C["rosa"]}" {S}/>',
 'escuela': f'<path d="M14 44 l36 -22 l36 22" fill="none" {S}/><rect x="20" y="44" width="60" height="44" fill="{C["mostaza"]}" {S}/><rect x="42" y="62" width="16" height="26" fill="#fff" {S}/><rect x="26" y="52" width="12" height="10" fill="#fff" {S}/><rect x="62" y="52" width="12" height="10" fill="#fff" {S}/><path d="M50 22 v-14 h14 l-4 5 l4 5 h-14" fill="{C["rojo"]}" {S}/>',
 'casa': f'<path d="M12 48 l38 -32 l38 32" fill="{C["rojo"]}" {S}/><rect x="22" y="46" width="56" height="42" fill="{C["crema"]}" {S}/><rect x="42" y="62" width="16" height="26" fill="{C["naranja"]}" {S}/>',
 'hospital': f'<rect x="18" y="24" width="64" height="64" fill="#fff" {S}/><rect x="40" y="34" width="20" height="20" fill="{C["rojo"]}"/><path d="M50 36 v16 M42 44 h16" stroke="#fff" stroke-width="5"/><rect x="42" y="66" width="16" height="22" fill="{C["azul"]}" {S}/>',
 'bus': f'<rect x="14" y="20" width="72" height="56" rx="10" fill="{C["mostaza"]}" {S}/><rect x="22" y="28" width="56" height="20" rx="3" fill="#CFE3F5" {S}/><circle cx="30" cy="80" r="8" fill="{T}"/><circle cx="70" cy="80" r="8" fill="{T}"/>',
 'auto': f'<path d="M12 64 v-12 l12 -18 h40 l14 18 h10 v12 z" fill="{C["azul"]}" {S}/><path d="M30 36 l-6 14 h22 v-14 z M52 36 v14 h22 l-10 -14 z" fill="#CFE3F5" {S}/><circle cx="30" cy="68" r="9" fill="{T}"/><circle cx="72" cy="68" r="9" fill="{T}"/>',
 'avion': f'<path d="M8 54 l84 -20 c4 -1 6 4 2 6 l-30 14 l-10 26 h-8 l4 -22 l-20 8 l-6 10 h-6 l2 -14 z" fill="#fff" {S}/><path d="M40 46 l-10 -20 h8 l18 16" fill="{C["azul"]}" {S}/>',
 'maleta': f'<rect x="18" y="32" width="64" height="52" rx="8" fill="{C["morado"]}" {S}/><path d="M38 32 v-10 h24 v10" fill="none" {S}/><path d="M18 52 h64" stroke="#fff" stroke-width="4"/>',
 'carrito': f'<path d="M8 20 h14 l10 40 h48 l8 -28 h-60" fill="none" {S}/><rect x="28" y="34" width="54" height="22" fill="{C["verde"]}" opacity=".6"/><circle cx="38" cy="76" r="7" fill="{T}"/><circle cx="72" cy="76" r="7" fill="{T}"/>',
 'pastel': f'<rect x="18" y="50" width="64" height="36" rx="6" fill="{C["rosa"]}" {S}/><path d="M18 62 q8 8 16 0 q8 8 16 0 q8 8 16 0 q8 8 16 0" fill="none" stroke="#fff" stroke-width="4"/><path d="M50 50 v-16" {S}/><path d="M50 30 c-6 -6 0 -14 0 -18 c0 4 6 12 0 18" fill="{C["mostaza"]}" {S}/>',
 'regalo': f'<rect x="16" y="40" width="68" height="46" rx="4" fill="{C["turquesa"]}" {S}/><rect x="12" y="30" width="76" height="14" rx="3" fill="{C["turquesa"]}" {S}/><path d="M50 30 v56" stroke="{C["rojo"]}" stroke-width="8"/><path d="M50 30 c-14 -20 -28 -2 0 0 c14 -20 28 -2 0 0" fill="none" {S} stroke="{C["rojo"]}"/>',
 'globo': f'<ellipse cx="50" cy="38" rx="24" ry="28" fill="{C["rojo"]}" {S}/><path d="M50 66 c-6 10 6 16 0 28" fill="none" {S}/>',
 'diente': f'<path d="M26 22 c10 -8 18 0 24 0 c6 0 14 -8 24 0 c10 10 2 34 -4 60 c-2 8 -10 8 -12 0 l-8 -22 l-8 22 c-2 8 -10 8 -12 0 c-6 -26 -14 -50 -4 -60 z" fill="#fff" {S}/>',
 'curita': f'<rect x="10" y="38" width="80" height="26" rx="13" fill="#F2C9A0" {S} transform="rotate(-30 50 51)"/><rect x="38" y="40" width="24" height="22" fill="#E8B48A" transform="rotate(-30 50 51)"/>',
 'medicina': f'<rect x="30" y="30" width="40" height="58" rx="8" fill="{C["naranja"]}" {S}/><rect x="34" y="14" width="32" height="16" rx="3" fill="#fff" {S}/><rect x="36" y="48" width="28" height="20" fill="#fff" {S}/>',
 'termometro': f'<rect x="42" y="10" width="16" height="60" rx="8" fill="#fff" {S}/><circle cx="50" cy="76" r="14" fill="{C["rojo"]}" {S}/><path d="M50 30 v40" stroke="{C["rojo"]}" stroke-width="6"/>',
 'jeringa': f'<g transform="rotate(-40 50 50)"><rect x="20" y="40" width="50" height="20" rx="3" fill="#CFE3F5" {S}/><path d="M70 50 h22 M8 40 v20 M8 50 h12" {S}/></g>',
 'ruido': f'<path d="M16 40 h14 l20 -18 v56 l-20 -18 h-14 z" fill="{C["morado"]}" {S}/><path d="M62 36 q8 14 0 28 M72 28 q14 22 0 44 M82 20 q20 30 0 60" fill="none" {S}/>',
 'auriculares': f'<path d="M20 60 v-10 a30 30 0 0 1 60 0 v10" fill="none" {S}/><rect x="12" y="54" width="18" height="28" rx="6" fill="{C["azul"]}" {S}/><rect x="70" y="54" width="18" height="28" rx="6" fill="{C["azul"]}" {S}/>',
 'tablet': f'<rect x="20" y="12" width="60" height="78" rx="8" fill="{T}" {S}/><rect x="26" y="20" width="48" height="60" rx="2" fill="#CFE3F5"/><circle cx="50" cy="85" r="2.5" fill="#fff"/>',
 'pelota': f'<circle cx="50" cy="52" r="34" fill="{C["rojo"]}" {S}/><path d="M18 46 c20 10 44 10 64 0 M34 22 c10 20 10 44 0 62 M66 22 c-10 20 -10 44 0 62" fill="none" stroke="#fff" stroke-width="4"/>',
 'libro': f'<path d="M50 26 c-12 -8 -28 -8 -38 -4 v58 c10 -4 26 -4 38 4 c12 -8 28 -8 38 -4 v-58 c-10 -4 -26 -4 -38 4 z" fill="#fff" {S}/><path d="M50 26 v58" {S}/>',
 'puerta': f'<rect x="26" y="10" width="48" height="80" rx="3" fill="{C["naranja"]}" {S}/><circle cx="64" cy="52" r="4" fill="{T}"/>',
 'alarma': f'<path d="M30 70 v-22 a20 20 0 0 1 40 0 v22 l8 8 h-56 z" fill="{C["mostaza"]}" {S}/><circle cx="50" cy="84" r="6" fill="{T}"/><path d="M16 30 l8 6 M84 30 l-8 6 M50 10 v10" {S} stroke="{C["rojo"]}"/>',
 'lonchera': f'<rect x="16" y="38" width="68" height="46" rx="8" fill="{C["verde"]}" {S}/><path d="M38 38 v-10 h24 v10" fill="none" {S}/><rect x="30" y="52" width="40" height="16" rx="3" fill="#fff" {S}/>',
 'no': f'<circle cx="50" cy="50" r="36" fill="#fff" stroke="{C["rojo"]}" stroke-width="8"/><path d="M26 74 l48 -48" stroke="{C["rojo"]}" stroke-width="8"/>',
 'si': f'<circle cx="50" cy="50" r="36" fill="{C["verde"]}" {S}/><path d="M32 52 l12 12 l24 -26" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>',
 'pregunta': f'<circle cx="50" cy="50" r="36" fill="{C["azul"]}" {S}/><path d="M38 40 a12 12 0 1 1 18 10 c-6 4 -6 6 -6 12" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/><circle cx="50" cy="74" r="4.5" fill="#fff"/>',
 'respirar': f'<path d="M14 40 h48 a10 10 0 1 0 -10 -10 M14 56 h64 a10 10 0 1 1 -10 10 M14 72 h30" fill="none" {S} stroke="{C["turquesa"]}" stroke-width="6"/>',
 'corazon': f'<path d="M50 84 c-30 -18 -40 -34 -34 -48 c6 -14 26 -14 34 2 c8 -16 28 -16 34 -2 c6 14 -4 30 -34 48 z" fill="{C["rojo"]}" {S}/>',
 'parque': f'<rect x="26" y="56" width="8" height="32" fill="#8B5E3C" {S}/><circle cx="30" cy="42" r="22" fill="{C["verde"]}" {S}/><path d="M52 88 v-40 h14 l26 40" fill="none" {S}/><path d="M66 48 l26 40" stroke="{C["rojo"]}" stroke-width="7" stroke-linecap="round"/><path d="M52 62 h14 M52 76 h14" {S}/><path d="M6 90 h90" {S}/>',
 'restaurante': f'<ellipse cx="50" cy="62" rx="38" ry="16" fill="#fff" {S}/><path d="M22 14 v22 a8 8 0 0 0 16 0 v-22 M30 14 v58" fill="none" {S}/><path d="M70 14 c-10 10 -10 24 0 26 v32" fill="none" {S}/>',
 'tijeras_pelo': persona(50, C['turquesa'], pelo='#6B4A2B') + f'<g transform="translate(58 4) scale(.4)">{I["tijeras"]}</g>',
 'cama_dormir': I['cama'] + f'<text x="64" y="30" font-family="NS" font-weight="900" font-size="18" fill="{C["morado"]}">z z</text>',
 'juguetes': I['bloques'],
 'reloj_espera': I['reloj'],
 'sismo': I['casa'] if False else f'<path d="M12 48 l38 -32 l38 32" fill="{C["rojo"]}" {S}/><rect x="22" y="46" width="56" height="42" fill="{C["crema"]}" {S}/><path d="M6 62 l6 -6 M6 76 l6 -6 M94 62 l-6 -6 M94 76 l-6 -6" {S}/>',
 'ordenar': f'<rect x="16" y="46" width="68" height="40" rx="4" fill="{C["mostaza"]}" {S}/><path d="M16 46 l8 -12 h52 l8 12" fill="#E9C27A" {S}/>' + f'<circle cx="40" cy="30" r="10" fill="{C["rojo"]}" {S}/><rect x="54" y="18" width="18" height="18" fill="{C["azul"]}" {S}/>',
 'bano_pelo': I['tina'],
 'unas': I['manos'] + f'<g transform="translate(56 50) scale(.42)">{I["tijeras"]}</g>',
 'zapatos': I['zapato'],
}

def ic(nombre):
    inner = N.get(nombre) or I[nombre]
    return f'<svg viewBox="0 0 100 100" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'
