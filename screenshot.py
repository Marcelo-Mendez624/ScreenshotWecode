import pyautogui
import datetime
import os
import re  # Importar re para manejo avanzado de expresiones regulares

# Diccionario para traducir los días de inglés a español
dias_semana = {
    'Monday': 'Lunes',
    'Tuesday': 'Martes',
    'Wednesday': 'Miércoles',
    'Thursday': 'Jueves',
    'Friday': 'Viernes',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}

# Función para limpiar y convertir la hora de texto a formato adecuado
def limpiar_hora(hora):
    # Eliminar espacios no estándar y caracteres extraños (como "a. m." o "p. m.")
    hora_limpia = re.sub(r'[^\d:]', '', hora.strip())  # Elimina todo lo que no sea dígito o ":"
    return hora_limpia

# Ruta del archivo de texto
txt_path = 'escuelas.txt'

# Carpeta donde se guardarán las capturas
carpeta_destino = 'ceibal'
os.makedirs(carpeta_destino, exist_ok=True)  # Crea la carpeta si no existe

# Obtener la fecha y hora actuales
ahora = datetime.datetime.now()

# Leer el archivo y verificar las horas
with open(txt_path, 'r', encoding='utf-8') as file:
    for linea in file.readlines():
        # Usamos una expresión regular para extraer las partes relevantes (escuela, día, horas)
        match = re.match(r'(\S+ \S+) (\S+) de (\d{1,2}:\d{2}) a (\d{1,2}:\d{2})', linea.strip())
        
        if match:
            nombre_escuela = match.group(1)
            dia = match.group(2).capitalize()  # Capitalizamos para asegurarnos de que el día coincida
            hora_inicio = limpiar_hora(match.group(3))  # "10:10"
            hora_fin = limpiar_hora(match.group(4))  # "11:00"
            
            # Verificar que las horas se hayan limpiado correctamente
            print(f"Hora de inicio limpia: {hora_inicio}, Hora de fin limpia: {hora_fin}")

            # Convertir el día actual a español
            dia_actual = dias_semana[ahora.strftime('%A')]

            # Verificar si el día actual es el mismo que el del archivo
            if dia == dia_actual:
                try:
                    # Convertir hora de inicio y fin a objetos datetime para compararlos
                    hora_inicio_obj = datetime.datetime.strptime(hora_inicio, '%H:%M')
                    hora_fin_obj = datetime.datetime.strptime(hora_fin, '%H:%M')
                    hora_actual_obj = datetime.datetime.strptime(ahora.strftime('%H:%M'), '%H:%M')

                    # Verificar si la hora actual está dentro del rango de la clase
                    if hora_inicio_obj <= hora_actual_obj <= hora_fin_obj:
                        # Crear el nombre del archivo con la fecha y nombre de la escuela
                        fecha = ahora.strftime('%d-%m-%y')
                        nombre_archivo = f"{fecha} {nombre_escuela}.png"
                        ruta_completa = os.path.join(carpeta_destino, nombre_archivo)

                        # Tomar y guardar la captura de pantalla
                        screenshot = pyautogui.screenshot()
                        screenshot.save(ruta_completa)

                        print(f"Captura guardada en: {ruta_completa}")
                    else:
                        print("La hora actual no está dentro del horario especificado.")
                except ValueError as e:
                    print(f"Error al procesar la hora: {e}")
            else:
                print(f"Hoy no es {dia}, no se toma captura para esta escuela.")
        else:
            print(f"No se pudo procesar la línea: {linea.strip()}")
