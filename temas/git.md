# Flujos de trabajo con Git y GitHub


## Planteamiento

Git es una herramienta para gestionar flujos de trabajo y equipos, y
en combinación con GitHub/GitLab es imprescindible para gestionar los
procesos de calidad del software que vamos a ver en este
curso. 

## Al final de esta sesión

Conocerán las órdenes esenciales de git, y como usar la herramienta de
línea de órdenes de GitHub para realizar algunas tareas fundamentales;
también sabrán cómo organizar flujos de desarrollo usando pull
requests y el concepto del mismo.

## Criterio de aceptación

Cada equipo habrá creado una descripción del mismo, con los
componentes del mismo en un README.md, todos los usuarios añadidos al
repositorio, y tendrán que haber añadido sus nombre con un PR (que
habrá aprobado algún otro miembro del equipo).

## 


## Actividad

Esencialmente, en esta primera fase se llevarán a cabo las actividades
de diseño para el resto del curso.

1. Elegir un equipo para trabajar en el proyecto, y crear un
   repositorio 
   [usando esta plantilla](https://github.com/JJ/curso-qa-template),
   que contiene ya algunos tests y el diseño general, así como la
   licencia libre.

## Entrega

Esta entrega se llevará a cabo, como el resto de las mismas, como un
pull request al fichero de [proyectos](../proyectos.md), tras añadir
en el *fork* propio el nombre del proyecto y un enlace al repo, así
como la versión.

Usaremos
[versionado semántico para las entregas](https://semver.org/), donde
el primer número será siempre el hito (comenzando por el hito
0). Diferentes versiones cambiarán el *minor* (el segundo) o el
tercero, si son algunos cambios que no alteran el API ni la
funcionalidad. Cada entrega corresponderá a un *release*, y por tanto
el repositorio tendrá que tener un tag 

> Los tags se hacen con `git tag`, y para hacer push de los mismos se
> tendrá que hacer, adicionalmente al normal, `git push --tags`

que deberá corresponder exactamente a la versión que se haya enviado.