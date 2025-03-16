# Proyecto final de ciencia de datos aplicada
Resumen ejecutivo
En este proyecto final, predeciremos si la primera etapa del Falcon 9 de SpaceX aterrizará con éxito mediante varios algoritmos de clasificación de aprendizaje automático. Los pasos principales de este proyecto incluyen:

# Recopilación, gestión y formato de datos
Análisis exploratorio de datos
Visualización interactiva de datos
Predicción de aprendizaje automático
Nuestros gráficos muestran que algunas características de los lanzamientos de cohetes se correlacionan con su resultado, es decir, su éxito o fracaso. También se concluye que el árbol de decisión podría ser el mejor algoritmo de aprendizaje automático para predecir si la primera etapa del Falcon 9 aterrizará con éxito.

# Introducción
En este proyecto final, predeciremos si la primera etapa del Falcon 9 aterrizará con éxito. SpaceX anuncia lanzamientos de cohetes Falcon 9 en su sitio web con un costo de 62 millones de dólares; otros proveedores cuestan más de 165 millones de dólares cada uno. Gran parte del ahorro se debe a que SpaceX puede reutilizar la primera etapa. Por lo tanto, si podemos determinar si la primera etapa aterrizará, podemos determinar el costo del lanzamiento. Esta información puede utilizarse si otra empresa desea pujar contra SpaceX por el lanzamiento de un cohete.

La mayoría de los aterrizajes fallidos son planificados. En ocasiones, SpaceX realizará un aterrizaje controlado en el océano. La pregunta principal que intentamos responder es: dadas las características del lanzamiento del cohete Falcon 9, como la masa de la carga útil, el tipo de órbita, el lugar de lanzamiento, etc., ¿aterrizará con éxito la primera etapa del cohete?

Metodología
La metodología general incluye:

Recopilación, organización y formato de datos mediante:
API de SpaceX
Raspado web
Análisis exploratorio de datos (EDA), utilizando:
Pandas y NumPy
SQL
Visualización de datos, utilizando:
Matplotlib y Seaborn
Folio
Estrellarse
Predicción de aprendizaje automático, utilizando
Regresión logística
Máquina de vectores de soporte (SVM)
Árbol de decisiones
K vecinos más cercanos (KNN)
