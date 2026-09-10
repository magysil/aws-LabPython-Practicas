import os
import subprocess

#Ejercicio 1: Uso de os.system
os.system("ls")

#Ejercicio 2: Uso de subprocess.run
subprocess.run(["ls"])

#Ejercicio 3: Uso de subprocess.run con dos argumentos
subprocess.run(["ls","-l"])

#Ejercicio 4: Uso de subprocess.run con tres argumentos
subprocess.run(["ls","-l","Laboratorio2.py"])

#Ejercicio 5: Recuperación de información del sistema
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

#Ejercicio 6: Recuperación de información sobre el espacio en disco
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])