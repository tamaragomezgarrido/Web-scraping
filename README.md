# Web-scraping
Ejemplo de web scraping.


Es necesario tener instaladas las librerías: pandas, requests, BeautifulSoup, datetime:  
pip install pandas  
pip install requests  
pip install beautifulsoup4 as bs4  
pip install datetime

### Contexto:
La información se ha recogido del sitio web surf-forecast.com, un sitio web de referencia para consultar previsiones de olas y reportes de surf para las mejores playas del mundo.  
Puesto que se pretenden almacenar datos de las condiciones del mar en la playa de Pantin para futuros estudios y detección de eventos, esta web proporciona la información necesaria para conseguirlo.

### Descripción del dataset y contenido:
El dataset recoge datos relevantes para la previsión de las condiciones en la playa de Pantin para la práctica de surf y otros deportes y actividades acuáticas.  
La información se almacena en las siguientes variables:  
**mes** : mes en el que se recoge la información.  
**dia**: día para el que se recoge la información.  
**tramo**: hora/tramo del día para la que se recoge la información.  
**olas**: Altura de las olas y dirección.  
**periodo**: Periodo de las olas (duración en segundos entre crestas de olas sucesivas).  
**energia**: Energia de la ola (se calcula en función del tamaño y el periodo).  
**viento(velocidad/direccion)**: Viento (km/h y dirección).  
**viento(direccion costa)**: direccón del viento con respecto a la costa.  
**marea alta**: hora de pleamar.  
**marea baja**: hora de bajamar.  
**temperatura mar**: temperatura del mar.  
  
Se proporciona esta información para los siguientes 7 días desde la fecha de descarga de la información, en diferentes tramos horarios para cada día.
Puesto que las previsiones tanto meteorológicas como de oleaje son muy cambiantes, se recomienda recoger la información cada día a las 00:00, sustituyendo los valores de cada celda por su nuevo valor, de forma que los datos se almacenen con los valores más fiables posibles para su posterior análisis.

Gráfica del dataset:

### Agradecimientos:  
El propietario de los datos es surf-forecast.com, registrado en la dirección Meteo365.com Unit 1 Link Trade Park, Llandough, CF11 8TQ. No se han encontrado estudios similares al propuesto.  

Se han encontrado algunos estudios sobre los condicionantes para la formación de una ola, o  los efectos del nivel del oleaje y la velocidad del viento en la atenuación de la señal en las comunicaciones.  

Se ha verificado si el useragent tiene permiso para buscar y acceder a la url consultando el archivo robots.txt de la web mediante el siguiente código:  

import urllib.robotparser  
rp = urllib.robotparser.RobotFileParser()  
rp.set_url("http://surf-forecast.com/robots.txt")  
rp.read()  
rp.can_fetch('*','https://es.surf-forecast.com/breaks/Pantin/forecasts/latest/six_day')   

Además, la información rastreada es pública, es decir, no se han tenido que aceptar ningunos términos ni condiciones para acceder a ella, por lo que el uso moderado del web scraping sería adecuado en este caso.

### Inspiración:  
El surf es un deporte que está en auge. Puede ser un reclamo para atraer turismo a ciertas zonas, en este caso la zona de Ferrol en Galicia, por lo que estudiando los datos sobre previsiones se puede determinar cuales son las mejores condiciones para la práctica de surf en esta playa, las épocas del año que tienen unas mejores condiciones de forma histórica, y además, estudiar cómo afectan los cambios del entorno geográfico a las mareas y olas.  

Este estudio se puede extrapolar a cualquier spot de interés.  Es interesante el estudio de los cambios en las mareas y tipología de las olas tras cambios por la actuación del hombre en emplazamientos cercanos, para tenerlo en cuenta como un indicador del impacto ambiental que provocan ciertas acciones, y cruzarlo con otros estudios para tener una visión más general sobre el impacto ambiental.    

### Licencia:  
Released Under CC BY-SA 4.0 License.  
Todas las licencias Creative Commons tienen la obligación de reconocimiento del autor.  
Según se indica en creativecommons.org, el tipo de licencia elegido permite el uso comercial de la obra y de las posibles obras derivadas, siempre y cuando las nuevas creaciones se distribuyan bajo los mismos términos, con lo que todos los trabajos basados en este permitirían también un uso comercial.  

Esta licencia está recomendada para materiales que se beneficiarían de la incorporación de contenidos.  
Para el objetivo que se plantea, esta licencia es la adecuada, ya que se busca tener los mejores datos posibles para realizar predicciones, utilizando datos cambiantes, de cara a poder tomar decisiones para mejorar la promoción, actividades y estudio ambiental de spots de surf.  
Se autoriza el uso comercial ya que este, al final, será en beneficio del lugar. Además, los datos recopilados son datos meteorológicos.
