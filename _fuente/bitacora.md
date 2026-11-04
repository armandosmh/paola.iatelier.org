# Bitácora — regalo-paola

> Documento **append-only**: registro cronológico de sesiones. Lo escribe la skill
> `cerrar-sesion` al final de cada sesión con cambios; nunca se edita lo ya escrito.
> Vive en `_fuente/` y no en `docs/` porque el repo es público y GitHub Pages
> serviría `docs/*.md`; Jekyll ignora las carpetas con guion bajo.

## 2026-11-04 — PDF "Cómo llegar a T-Site"
- **Tipo:** espontáneo
- **Qué se hizo:** maqueta y luego PDF A5 de 5 páginas (`pdf/como-llegar.pdf`): portada, T-Site con mapa, rutas desde Shinjuku y Ueno, desvío por el río Meguro en otoño. Fuente en `_fuente/pdf/` (WeasyPrint; mapa en acuarela con geometrías de OSM cacheadas en `osm.json`). Decisiones de Armando: WeasyPrint, mapa híbrido, A5, repo abierto sin cifrar, sin páginas extra.
- **Quedó a medias:** mensaje de Ana y Armando y sección T-Site en la landing; enlace al PDF; otros lugares del mapa (los da Armando); tiempos de viaje y salida de la estación Daikanyama sin verificar (el PDF remite a Google Maps). No se hizo push.
- **Commit:** este mismo commit, "Sesión: PDF de cómo llegar a T-Site (rutas y mapa)"

## 2026-11-04 — Mensaje de cumpleaños y T-Site en la landing
- **Tipo:** espontáneo
- **Qué se hizo:** "Próximamente" sustituido por la carta de Ana y Armando (texto corregido, opción B) en pantalla de papel; al hacer scroll cada párrafo se lava como tinta, luego el papel, y la escena hace paneo hasta la fachada de la librería (`LIBRERIA = 0.7`). Abajo: T-Site con descarga del PDF y enlaces a Google Maps (T-Site y río Meguro). Firma "Ana y Armando" agregada. PDF: página 5 ahora "Quest +". Probado en 375×812 y 1440×900 en el navegador integrado; sin errores en consola.
- **Quedó a medias:** otros lugares del mapa (los da Armando); no se hizo push. No probado en un iPhone real.
- **Commit:** este mismo commit, "Sesión: carta de cumpleaños y T-Site en la landing"
- **Push (2026-11-04):** publicado en paola.iatelier.org (`7d24c1f`); verificado con curl que sirve la carta y `pdf/como-llegar.pdf` (200). También subieron los commits pendientes del QR.

## 2026-11-04 — Enlaces de mapa bajo el botón
- **Tipo:** espontáneo
- **Qué se hizo:** "T-Site en el mapa" y "Río Meguro" pasaron a su propia línea, debajo de "Cómo llegar (PDF)", también en escritorio. Revisado en 375×812 y 1440×900. Publicado con push.
- **Quedó a medias:** nada nuevo.
- **Commit:** este mismo commit, "Sesión: enlaces de mapa debajo del botón del PDF"

## 2026-11-04 — Cursiva, Quest+ y postal revelada durante la lectura
- **Tipo:** espontáneo
- **Qué se hizo:** la carta pasó a Cormorant Garamond itálica (el resto del sitio sigue en Shippori Mincho); "QUEST +" → "QUEST+"; nueva línea "Misión extra: tómate una foto en un puente del río" en la carta y en la página 5 del PDF (también "Quest+"). Mientras se lee, el papel se vuelve translúcido (40% de escena en celular, 55% en escritorio) con halo de papel en el texto y la escena se mueve del árbol al centro; al terminar, se lava el papel y paneo final a la librería. Probado en 375×812 y 1440×900; sin errores en consola.
- **Quedó a medias:** otros lugares del mapa; prueba en iPhone real.
- **Commit:** este mismo commit, "Sesión: carta en cursiva, misión extra y postal revelada al leer"
