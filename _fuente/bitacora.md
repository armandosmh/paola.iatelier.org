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

## 2026-11-04 — Ediciones de Armando al PDF y descripción de T-Site
- **Tipo:** espontáneo
- **Qué se hizo:** aplicadas las notas y tachones de Armando sobre el PDF: portada "Una tarde en Daikanyama (y el río Meguro)" y "paseo opcional"; fuera frases de relleno en las rutas (Yoyogi/Harajuku, sótano 5, "transbordo confuso", "unos 15 minutos", intro de Ueno, "Mismo aviso", "Bonito", "desvío"); río Meguro reescrito; mapa sin los círculos de árboles ni las rutas a pie (y sin su leyenda); nota del mapa fuera, se dejó solo "© OpenStreetMap" dentro del mapa por la licencia ODbL. Sitio: nueva descripción de T-Site con la "pequeña Brooklyn".
- **Quedó a medias:** otros lugares del mapa; prueba en iPhone real.
- **Commit:** este mismo commit, "Sesión: ediciones de Armando al PDF y nueva descripción de T-Site"

## 2026-11-04 — Lugares opcionales en el mapa
- **Tipo:** espontáneo
- **Qué se hizo:** cuatro lugares que dio Armando, numerados en orden de caminata en los mapas (círculos naranja, posición indicativa): 1 Kyu Asakura House, 2 Sato Sakura Museum, 3 Traveler's Factory, 4 Naka-Meguro Park. Coordenadas de Nominatim salvo Traveler's Factory (ubicada por su dirección, 3-13-10 Kamimeguro). Nueva página 6 "Otros lugares lindos" con mapa ampliado y descripción de 3–4 líneas por lugar, con datos verificados en fuentes (horario de Traveler's Factory del sitio oficial; año de la casa Asakura y del parque de fuentes secundarias/ofic. del distrito). Etiqueta de Naka-meguro movida para no tapar el 3.
- **Quedó a medias:** prueba en iPhone real.
- **Commit:** este mismo commit, "Sesión: lugares opcionales en el mapa y página 6 del PDF"

## 2026-11-04 — Hilo rojo guía y contraseña nueva
- **Tipo:** espontáneo
- **Qué se hizo:** un hilo rojo ondulado nace bajo la firma y se dibuja con el scroll hasta "Tu misión"; su punta queda justo bajo el borde de la pantalla para indicar que la página sigue. Si Paola se detiene más de ~2 s con el hilo en pantalla, el hilo da un tirón hacia abajo (desactivado con reduced-motion). Contraseña cambiada a pedido de Armando (solo cambia el hash; se normaliza sin acentos ni tilde). Probado en 375×812 y 1440×900; sin errores en consola.
- **Quedó a medias:** prueba en iPhone real. Los navegadores que ya entraron con la contraseña anterior no la vuelven a pedir (localStorage).
- **Commit:** este mismo commit, "Sesión: hilo rojo guía y contraseña nueva"

## 2026-11-04 — Hilo guía como trazo de acuarela
- **Tipo:** espontáneo
- **Qué se hizo:** el hilo rojo guía pasó de línea lisa a trazo de acuarela (opción C de tres maquetadas en `_borrador/hilos.html`): lavado ancho rosa diluido + línea fina de pigmento, con filtro SVG de ondulación, desenfoque y poros de papel, en multiply. Mismo dibujado con scroll y tirón. El trazo solo se repinta cuando cambia (el filtro es costoso). Probado en 375×812 y 1440×900; ~60 fps en escritorio; sin errores en consola.
- **Quedó a medias:** prueba en iPhone real (rendimiento del filtro en celular).
- **Commit:** este mismo commit, "Sesión: hilo guía como trazo de acuarela"

## 2026-11-04 — Arreglo: pantalla negra en iPhone
- **Tipo:** espontáneo (corrección)
- **Qué se hizo:** en el iPhone de Armando la página se quedaba negra tras el despliegue del hilo de acuarela. Causa probable (no reproducida: esta Mac no tiene Xcode ni simulador): el filtro SVG (feTurbulence + desplazamiento + desenfoque + mezcla multiply) sobre un SVG de ~3 000 px de alto agota la memoria de la GPU del iPhone. El hilo anterior, sin filtro, sí se había visto bien en su celular. Ahora el hilo son tres trazos vectoriales (dos lavados y una línea de pigmento cortada) sin filtros ni blend; el SVG solo cubre el trazo, no toda la página, y se descubre con un rectángulo recortado. Además, la contraseña se normaliza a solo letras y dígitos (acepta mayúsculas, espacios y signos) y el SHA-256 tiene respaldo en JS puro para navegadores sin `crypto.subtle` (comprobado contra node en 11 casos).
- **Quedó a medias:** confirmar en el iPhone de Armando que ya entra; sigue sin probarse en un iOS real.
- **Commit:** este mismo commit, "Sesión: arreglo de pantalla negra en iPhone (hilo sin filtros)"

## 2026-11-04 — Velocidad de carga
- Grano: la capa SVG feTurbulence 200% con mix-blend-mode se cambió por un mosaico PNG estático (`img/grano.png`), sin blend.
- Escena: `escena.webp` de 2000 a 1600 px (443 → 240 KB); WebGL a 1× en teléfono; el respaldo CSS solo carga si no hay WebGL; precarga de la imagen.
- Fuentes de Google ya no bloquean el primer dibujo (media=print + onload).
- Pendiente: si aún se traba al scroll, aligerar blur/text-shadow animados de la carta. No medido en iPhone real.
