# Hangman/ahorcado

Proyecto programado utilizado como recurso adicional
para el curso Introducción a la programación 
disponible en el aula virtual 
[projecto](https://github.com/LuisPadillaM/proyecto_introduccion_a_la_programacion)


Instalacion 

MAC/Windows/Linux 
installar virtual env 

´´´ ´pip install virtualenv ´´´ 

MAC 

´´´ make runlocal ´´´ 

Windows 

Instalar [Chocolatey](http://chocolatey.org/install) 

posteriormente correr
´´´ make -f WMakefile runlocal ´´´

Otra opcie

Otra opción es correr manualmente los siguientes comandos 

virtualenv venv
venv/Scripts/pip install -r requirements/local.txt
venv/Scripts/activate 
python Proyecto.py