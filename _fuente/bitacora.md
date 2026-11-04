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
