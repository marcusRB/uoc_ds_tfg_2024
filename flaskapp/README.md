## Predicción de Enfermedades Cardíacas 

### Descripción General

Una aplicación web simple que utiliza un algoritmo de aprendizaje automático para predecir el estado cardíaco de una persona proporcionando algunos datos de salud como edad, género, presión arterial, nivel de colesterol, entre otros. Construida con `Flask` y desplegada en `Heroku`.

### Motivación 

Como entusiasta de los datos y el aprendizaje automático, he trabajado en diferentes proyectos relacionados con el tema, pero lo que he descubierto es que desplegar tu modelo de aprendizaje automático es un aspecto clave en cada proyecto de ML y ciencia de datos. Todo lo que he estudiado o me han enseñado en mi recorrido en ciencia de datos y ML se ha enfocado principalmente en definir el problema, seguido de la recopilación y preparación de datos, la construcción del modelo y su evaluación. Por supuesto, estos pasos son importantes, pero ¿cómo hago que otras personas interactúen con mis modelos? No puedo enviarles notebooks de Jupyter, ¿cierto? Por eso quise realizar un proyecto de aprendizaje automático de extremo a extremo.

- Para ver la aplicación desplegada, haga clic en el siguiente enlace:  
  **Heart Disease Predictor Web App -** *[https://heart-disease-predictor-flask.herokuapp.com/](https://heart-disease-predictor-flask.herokuapp.com/)*

- Para obtener el código de análisis exploratorio de datos/visualizaciones, los diferentes algoritmos utilizados y la evaluación del modelo, haga clic en el siguiente enlace:  
  **Enlace del notebook de Jupyter -** *[https://github.com/asthasharma98/Data-Science/blob/main/Heart%20Disease%20Prediction/heart_disease_prediction.ipynb](https://github.com/asthasharma98/Data-Science/blob/main/Heart%20Disease%20Prediction/heart_disease_prediction.ipynb)*

**Demostración de la aplicación web:**

![Heart_disease](https://github.com/asthasharma98/Heart-Disease-Prediction-Deployment/blob/master/Readme_resources/heart_disease.gif)
 
### Aspectos Técnicos
 
Este proyecto se divide principalmente en dos partes:
 
1. Explorar el conjunto de datos y entrenar el modelo utilizando `Sklearn`.
2. Construir y alojar una aplicación web `Flask` en `Heroku`.

**Acerca de la estructura del repositorio:**

- El proyecto incluye el script `app.py`, que se utiliza para ejecutar la aplicación y es el motor de esta. Contiene la API que recibe datos de entrada del usuario y calcula un valor predicho basado en el modelo.
- `prediction.py` contiene el código para construir y entrenar un modelo de aprendizaje automático.
- La carpeta *templates* contiene los archivos `main.html` y `result.html`, que describen la estructura de la aplicación y cómo funciona. Estos archivos están conectados con Python a través del marco Flask.
- La carpeta *static* contiene el archivo `style.css`, que agrega estilos y mejora la apariencia de la aplicación.

### Instalación

El código está escrito en Python 3.8. Si no tienes Python instalado, puedes descargarlo [aquí](https://www.python.org/downloads/). Si usas una versión inferior, puedes actualizarla usando el paquete pip, asegurándote de tener la última versión. Para instalar las bibliotecas requeridas, ejecuta este comando en el directorio del proyecto después de clonar el repositorio:

```bash
pip install -r requirements.txt 
````

*To clone the repository*

```
git clone https://github.com/asthasharma98/Heart-Disease-Prediction-Deployment.git
```

### Run

*To Run the Application*

```
python app.py
```

### Deployement on Heroku

Install Heroku CLI as this makes it easy to create and manage your Heroku apps directly from the terminal. 
You can download it from [here](https://devcenter.heroku.com/articles/heroku-cli).

next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

### Technologies used

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  

[![Heroku](https://github.com/jalbertsr/logo-badge-images/blob/master/img/rsz_heroku.png?raw=true)](https://www.heroku.com/)

[![Flask](https://github.com/jalbertsr/logo-badge-images/blob/master/img/rsz_flask.png?raw=true)](http://flask.pocoo.org/)  

### Future work

- improve model performance.
- Add more better styling to the user interface.

### credit

- A big thanks to [Anuj vyas](https://github.com/anujvyas/Diabetes-Prediction-Deployment) as I got the desinging idea of web app from his projects on github.

**Some Useful Resources**

- **Flask Quickstart Documentation** : [https://flask.palletsprojects.com/en/1.1.x/quickstart/](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
- FlaskApplication based by: https://github.com/asthasharma98/Data-Science/