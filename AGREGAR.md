# Cómo agregar páginas y posts


## Posts

En la carpeta `_posts`. El nombre del archivo tiene que empezar con algo que sea una fecha, YYYY-MM-DD (año, mes, día). Ejemplo de configuración:

```
---
layout: post
title: Sobre este trabajo 
navigation: Qué es esto? 
---
```

"navigation" es lo que aparece en la navegación al márgen. Sin esa línea, el post no es mencionado en la navegación.





## Pages

En la misma carpeta que este archivo. Ejemplo de configuración:

Para una página:
```
---
layout: page
title: Sobre este trabajo 
navigation: Qué es esto? 
position: bottom
---
```

"Position: bottom" ubica el enlace a la página por debajo de los posts en la navegación. 

Para un enlace:
```
---
layout: page
navigation: Google 
link: https://www.google.com
title: "El buscador más grande del mundo."
target: _blank
position: bottom
---
```
