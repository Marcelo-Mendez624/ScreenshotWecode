# Proyecto de Capturas de Pantalla Programadas

Este proyecto toma capturas de pantalla basadas en un horario definido para diferentes escuelas. Las capturas se realizan según el día de la semana y la hora de inicio y fin especificada en un archivo de texto, y se guardan con un nombre que incluye la fecha actual y el nombre de la escuela.

## Requisitos

###Para ejecutar este proyecto, es necesario tener instaladas las siguientes dependencias de Python:

- **pyautogui**: Para realizar las capturas de pantalla.
- **datetime**: Para manejar fechas y horas.
- **os**: Para gestionar directorios y rutas de archivos.
- **re**: Para trabajar con expresiones regulares.

##El proyecto requiere un archivo de texto (por defecto escuelas.txt) que contiene la información sobre las escuelas y sus horarios. El formato de cada línea debe ser el siguiente:
<nombre_escuela> <día> de <hora_inicio> a <hora_fin>
escuela falsa2 Sábado de 20:00 a 22:00

##Notas:
Las horas deben estar en formato de 24 horas (HH:MM).

La línea debe contener el nombre de la escuela, el día de la semana, y las horas de inicio y fin de la clase.
Para instalar las dependencias, puedes usar el siguiente comando:

```bash
pip install pyautogui


