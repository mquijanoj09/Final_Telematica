# Final_Telematica
Este proyecto mide el nivel de altura del agua en cada una de las cuencas en el área metropolitana, tomando los datos de SIATA Medellín.
Los notifico para una aplicación movil, aplicación web y base de datos.

# Importante:
Para poder correr el programa se debe: 
1. Modificar el archivo web.py y cambiar la dirección localhost a su dirección IP pública
2. En la linea 68: return redirect('http://localhost:5600/?password=040405') (se modifica localhost)

En el aws modificar el security group habilitando el puerto 80 y el puerto 5600

# Ejecutar la pagina:
Es necesario actualizar el repositorio de paquetes e instalar el docker-compose junto con dos imágenes, mysql y ubuntu, finalmente, ejecutará el archivo docker-compose.yml, que creará tres contenedores.

# Para terminar:
Ingresar la IP publica con el puerto :80 y le aparecerá la pagina, cuando ingrese un usuario lo redireccionara a la pagina de https://siata.gov.co/siata_nuevo/ de lo contrario lo redireccionara a la pagina de la upb.
