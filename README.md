 - Este sistema pretender usar el protocolo MIDI y enviar la señal a través de MQTT a WebSockets y hacer pruebas con REDIS para conseguir un control en tiempo real muy preciso


---------------------------------------------------------------------------------------------------------------------------------

 - USB
$ lsusb
$ lsusb -D /dev/bus/usb/002/005
002 & 005 must be find at $ lsusb


https://www.youtube.com/watch?v=xfhzbw93rzw


 - PROBLEMA:
$ pip3 install pyusb 
parece que ese comando no instala correctamente la librería
Para solucionarlo he tenido que descargar la última versión de la librería desde:

 - https://sourceforge.net/projects/pyusb/files/

Descomprimir, entrar con la termial y $ sudo python3 setup.py install



 - Para usar las librerías del código que nos ofrece
    - https://www.youtube.com/watch?v=w732EXqmfZU
 - Debemos instalar Cython::
    - https://www.youtube.com/watch?v=LsJH8b0E1Rs


Si rtmidi-python da problemas al instalar, instalar las siguientes librerías:
$ sudo apt-get install libjack-dev
$ sudo apt-get install libasound2-dev
