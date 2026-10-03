"""Íconos tipo pictograma (SVG, viewBox 0 0 100 100), estilo plano con contorno de la marca."""
from common import C

T = C['tinta']
S = f'stroke="{T}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"'

def svg(inner, size='100%'):
    return f'<svg viewBox="0 0 100 100" width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'

FLECHAS = {
    'arriba': f'<path d="M82 40 V14 M74 22 L82 13 L90 22" fill="none" {S} stroke="{C["rojo"]}"/>',
    'abajo': f'<path d="M82 14 V40 M74 32 L82 41 L90 32" fill="none" {S} stroke="{C["rojo"]}"/>',
    'giro': f'<path d="M72 20 a10 10 0 1 1 10 12" fill="none" {S} stroke="{C["rojo"]}"/><path d="M78 28 L82 33 L87 29" fill="none" {S} stroke="{C["rojo"]}"/>',
    'ok': f'<circle cx="82" cy="20" r="12" fill="{C["verde"]}"/><path d="M76 20 l4 4 l8 -9" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
}

I = {
 'calcetin': f'<path d="M38 12 h24 v40 l14 14 a10 10 0 0 1 -6 18 h-26 a10 10 0 0 1 -6 -6 z" fill="{C["azul"]}" {S}/><path d="M38 24 h24" {S}/>',
 'camiseta': f'<path d="M34 16 l-20 12 l8 16 l10 -5 v45 h36 v-45 l10 5 l8 -16 l-20 -12 a16 10 0 0 1 -32 0 z" fill="{C["naranja"]}" {S}/>',
 'pantalon': f'<path d="M28 12 h44 l6 76 h-18 l-10 -50 l-10 50 h-18 z" fill="{C["azul"]}" {S}/><path d="M28 22 h44" {S}/>',
 'zapato': f'<path d="M12 58 c0 -14 8 -20 14 -22 l14 -4 l10 14 c12 2 30 6 36 14 c2 4 2 12 -4 14 h-62 c-6 0 -8 -6 -8 -16 z" fill="{C["rojo"]}" {S}/><path d="M38 44 l14 0 M42 52 l16 0" stroke="#fff" stroke-width="5" stroke-linecap="round"/><path d="M12 72 h74" {S}/>',
 'boton': f'<rect x="18" y="16" width="64" height="70" rx="8" fill="{C["turquesa"]}" {S}/><path d="M50 16 v70" {S}/><circle cx="50" cy="38" r="9" fill="#fff" {S}/><circle cx="50" cy="64" r="9" fill="#fff" {S}/><circle cx="47" cy="38" r="1.6" fill="{T}"/><circle cx="53" cy="38" r="1.6" fill="{T}"/><circle cx="47" cy="64" r="1.6" fill="{T}"/><circle cx="53" cy="64" r="1.6" fill="{T}"/>',
 'cierre': f'<path d="M22 14 h56 v74 h-56 z" fill="{C["morado"]}" {S}/><path d="M50 14 v74" stroke="#fff" stroke-width="3" stroke-dasharray="4 4"/><rect x="42" y="40" width="16" height="14" rx="3" fill="{C["mostaza"]}" {S}/><path d="M50 54 v12" {S}/>',
 'cordones': f'<path d="M10 64 c0 -12 8 -18 14 -20 l20 -6 c14 2 34 8 44 18 c3 6 0 14 -6 14 h-64 c-6 0 -8 -2 -8 -6 z" fill="{C["azul"]}" {S}/><path d="M40 40 c-14 -18 -26 -4 -12 4 c10 4 16 -2 12 -4 c4 -2 22 -16 22 0 c-2 8 -14 6 -22 4" fill="none" {S} stroke="#fff" stroke-width="3.4"/><path d="M40 40 c-14 -18 -26 -4 -12 4 c10 4 16 -2 12 -4 c4 -2 22 -16 22 0 c-2 8 -14 6 -22 4" fill="none" {S}/>',
 'cuchara': f'<ellipse cx="50" cy="28" rx="14" ry="18" fill="{C["linea"]}" {S}/><path d="M50 46 v42" {S} stroke-width="7"/>',
 'tenedor': f'<path d="M36 12 v22 a14 14 0 0 0 28 0 v-22 M50 12 v22 M43 12 v20 M57 12 v20" fill="none" {S}/><path d="M50 48 v40" {S} stroke-width="7"/>',
 'cuchillo': f'<path d="M14 56 h40 c14 0 22 -6 24 -12 h-64 z" fill="{C["linea"]}" {S}/><rect x="54" y="52" width="34" height="10" rx="5" fill="{C["mostaza"]}" {S}/><path d="M18 74 c0 -10 10 -12 16 -8 c6 -6 18 -6 22 2 c6 0 10 4 10 10 h-48 z" fill="#E9C27A" {S}/>',
 'vaso': f'<path d="M28 18 h44 l-6 68 h-32 z" fill="#CFE3F5" {S}/><path d="M31 42 h38" stroke="{C["azul"]}" stroke-width="4"/>',
 'jarra': f'<path d="M26 22 h38 l-4 64 h-30 z" fill="#CFE3F5" {S}/><path d="M64 34 c14 0 14 26 -2 26" fill="none" {S}/><path d="M26 22 l-8 -6" {S}/>',
 'plato': f'<ellipse cx="50" cy="56" rx="40" ry="18" fill="#fff" {S}/><ellipse cx="50" cy="54" rx="24" ry="9" fill="{C["mostaza"]}" {S}/>',
 'grifo': f'<path d="M22 30 h40 a12 12 0 0 1 12 12 v6 h-12 v-4 h-40 z" fill="{C["linea"]}" {S}/><path d="M38 30 v-12 h-10 M38 18 h12" {S}/><path d="M68 58 v8 M64 72 v6 M72 72 v6" stroke="{C["azul"]}" stroke-width="4" stroke-linecap="round"/>',
 'jabon': f'<rect x="20" y="44" width="60" height="36" rx="12" fill="{C["rosa"]}" {S}/><circle cx="34" cy="30" r="7" fill="#fff" {S}/><circle cx="52" cy="22" r="5" fill="#fff" {S}/><circle cx="64" cy="32" r="6" fill="#fff" {S}/>',
 'manos': f'<path d="M30 86 v-30 l-10 -16 c-2 -6 6 -8 8 -4 l8 10 v-30 c0 -6 8 -6 8 0 v22 v-28 c0 -6 8 -6 8 0 v28 v-24 c0 -6 8 -6 8 0 v26 v-18 c0 -6 8 -6 8 0 v32 c0 14 -6 22 -12 32 z" fill="#F2C9A0" {S}/>',
 'toalla': f'<rect x="20" y="16" width="60" height="70" rx="6" fill="{C["turquesa"]}" {S}/><path d="M20 70 h60 M20 76 h60" stroke="#fff" stroke-width="3"/><path d="M14 16 h72" {S}/>',
 'cepillo': f'<g transform="rotate(-35 50 50)"><rect x="8" y="44" width="62" height="12" rx="6" fill="{C["azul"]}" {S}/><rect x="66" y="40" width="24" height="12" rx="3" fill="#fff" {S}/><path d="M70 40 v-10 M76 40 v-10 M82 40 v-10 M88 40 v-10" {S} stroke-width="3.4"/></g>',
 'pasta': f'<path d="M16 40 h56 l12 10 l-12 10 h-56 a8 8 0 0 1 0 -20 z" fill="#fff" {S}/><path d="M24 40 v20" stroke="{C["azul"]}" stroke-width="5"/><path d="M84 50 h6" {S}/>',
 'inodoro': f'<path d="M24 16 h24 v30 h-24 z" fill="#fff" {S}/><path d="M16 46 h64 c0 18 -12 26 -24 28 l4 14 h-28 l2 -14 c-12 -4 -18 -12 -18 -28 z" fill="#fff" {S}/>',
 'papel': f'<rect x="20" y="30" width="44" height="40" rx="20" fill="#fff" {S}/><ellipse cx="42" cy="50" rx="8" ry="8" fill="{C["linea"]}" {S}/><path d="M64 50 h20 v28 h-34" fill="#fff" {S}/>',
 'panuelo': f'<path d="M22 30 l56 0 l-4 50 l-48 0 z" fill="{C["linea"]}" {S}/><path d="M36 30 c4 -16 24 -16 28 0" fill="#fff" {S}/>',
 'cara': f'<circle cx="50" cy="50" r="34" fill="#F2C9A0" {S}/><circle cx="38" cy="44" r="3" fill="{T}"/><circle cx="62" cy="44" r="3" fill="{T}"/><path d="M38 62 c6 6 18 6 24 0" fill="none" {S}/><path d="M80 18 v8 M86 30 v6" stroke="{C["azul"]}" stroke-width="4" stroke-linecap="round"/>',
 'peine': f'<rect x="14" y="30" width="72" height="16" rx="4" fill="{C["morado"]}" {S}/><path d="M22 46 v24 M30 46 v24 M38 46 v24 M46 46 v24 M54 46 v24 M62 46 v24 M70 46 v24 M78 46 v24" {S}/>',
 'tina': f'<path d="M10 46 h80 v8 c0 16 -12 26 -26 26 h-28 c-14 0 -26 -10 -26 -26 z" fill="#fff" {S}/><path d="M22 46 v-26 a8 8 0 0 1 16 0" fill="none" {S}/><circle cx="58" cy="36" r="5" fill="#CFE3F5" {S}/><circle cx="72" cy="30" r="4" fill="#CFE3F5" {S}/><path d="M30 86 l-4 6 M70 86 l4 6" {S}/>',
 'silla': f'<path d="M30 12 v76 M30 50 h40 v38 M30 50 h40" fill="none" {S} stroke-width="6"/><path d="M30 14 h10 v36" fill="none" {S}/>',
 'sol': f'<circle cx="50" cy="50" r="18" fill="{C["mostaza"]}" {S}/><path d="M50 12 v10 M50 78 v10 M12 50 h10 M78 50 h10 M23 23 l7 7 M70 70 l7 7 M77 23 l-7 7 M30 70 l-7 7" {S}/>',
 'luna': f'<path d="M62 14 a36 36 0 1 0 22 54 a28 28 0 1 1 -22 -54 z" fill="{C["morado"]}" {S}/>',
 'cama': f'<path d="M12 76 v-46 M12 56 h76 v20 M88 56 v20" fill="none" {S} stroke-width="5"/><rect x="18" y="44" width="20" height="12" rx="4" fill="#fff" {S}/><path d="M38 56 v-10 h50 v10" fill="{C["azul"]}" {S}/>',
 'estrella': f'<path d="M50 10 l12 26 l28 3 l-21 19 l6 28 l-25 -14 l-25 14 l6 -28 l-21 -19 l28 -3 z" fill="{C["mostaza"]}" {S}/>',
 'reloj': f'<circle cx="50" cy="50" r="36" fill="#fff" {S}/><path d="M50 26 v24 l14 10" fill="none" {S}/>',
 'lapiz': f'<path d="M20 80 l8 -22 l40 -40 l14 14 l-40 40 z" fill="{C["mostaza"]}" {S}/><path d="M20 80 l8 -22 l14 14 z" fill="#F2C9A0" {S}/><path d="M64 22 l14 14" {S}/>',
 'mochila': f'<rect x="22" y="26" width="56" height="62" rx="12" fill="{C["verde"]}" {S}/><path d="M38 26 v-6 a12 12 0 0 1 24 0 v6" fill="none" {S}/><rect x="32" y="56" width="36" height="20" rx="4" fill="#fff" {S}/>',
}

def icono(nombre, flecha=None, size='100%'):
    extra = FLECHAS.get(flecha, '') if flecha else ''
    return svg(I[nombre] + extra, size)
