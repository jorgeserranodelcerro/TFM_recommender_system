# TFM: Choose&Eat
## Jorge Serrano del Cerro

### Introducción
Este Trabajo de Fin de Máster de Data Science de KSCHOOL y es un sistema recomendador de restaurantes. Para ello hemos realizado tres fases:
- **Carga y codificación de los datos**
- **Creación de método recomendador**
- **Creación de aplicacion web con Flask**

### Tecnología
- **Python:** Para la parte de back-end. Hemos usado las bibliotecas Numpy, Pandas, Matplotlib y scipy.spatial.
- **Flask:** Para la creación de la aplicación web y unir el front-end y el back-end.
- **Html:** Para desarrollar la parte de front-end.

### Resultados
Como resultado del sistema de recomendación hemos creado una aplicación Web con Flask para la visualización de los resultados. Para ello hemos creado:
- **recommender.py:** Donde tenemos los métodos para realizar el proceso de recomendador.
- **Init.py:** Se encuentra como puente entre el front-end y el back-end.
- **main.html:** Donde vamos a volcar los datos para el usuario.

### Manual de usuario
Una vez que nos hemos descargado el repositorio nos situamos en la carpeta web y ejecutamos el fichero init.py (usamos el comando “Python init.py”). Si no se abre el navegador automáticamente, abrimos un navegador y en la barra de direcciones escribimos http://127.0.0.1:5000

