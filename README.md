# TFM: Choose&Eat
## Jorge Serrano del Cerro

### Introducción
Este Trabajo Fin de Máster de Data Science en KSCHOOL son dos sistemas recomendadores de restaurantes. Para ello hemos realizado tres fases:
- **Carga y codificación de los datos.**
- **Creación de los métodos recomendadores.**
- **Creación de aplicacion web con Flask.**

### Tecnología
- **Python:** para la parte de back-end. Hemos usado las bibliotecas Numpy, Pandas, Matplotlib y Scipy.Spatial.
- **Flask:** para la creación de la aplicación web y la unión el front-end y el back-end.
- **Html:** para desarrollar la parte de front-end.

### Resultados
Como resultado del sistema de recomendación hemos creado una aplicación Web con Flask para la visualización de los resultados. Para ello hemos desarrollado:
- **Recommender.py:** donde tenemos los métodos para realizar el proceso de recomendador.
- **Init.py:** se encuentra como puente entre el front-end y el back-end.
- **Main.html:** página principal de la Web con dos botones que redireccionan a cada método.
- **MyRs.html:** donde se muestran los datos para el método de k-vecinos.
- **RSBC.html:** donde se muestran los datos para el método basado en contenido.


### Manual de usuario
Una vez que nos hemos descargado el repositorio nos situamos en la carpeta web y ejecutamos el fichero init.py (usamos el comando “Python init.py”). Si no se abre el navegador automáticamente, abrimos un navegador y en la barra de direcciones escribimos http://127.0.0.1:5000
Nos aparece la web donde podemos elegir los distintos recomendadores, basado en contenido o en filtrado colaborativo. Si pulsamos el botón “My Recommender System” nos llega a la página donde elegimos en los menús despegables nuestras preferencias y, pulsando el botón de “Submit”, la aplicación nos devuelve los 5 restaurantes recomendados. Sin embargo, si pulsamos el botón “Content-based recommenders” vemos los restaurantes que hemos comentado anteriormente.


