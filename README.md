# Calculadora-Investigacion
Calculadora realizada con Python y la biblioteca TKinter. Fue realizada para facilitar muchos de los cálculos realizados en un proyecto de investigación científica que estoy realizando. Si bien no reemplaza a las aplicaciones oficiales ya que algunos cálculos no son del todo exactos, ayudó bastante en varios casos.

*1) Unit:* Permite realizar un pasaje de unidad de mmol/L a ng/mL a niveles séricos de Vitamina D (25[OH]D)

*2) IC95%:* Utiliza la fórmula de proporciones para poblaciones infinitas y finitas con un IC95% para calcular el tamaño de una muestra en base a un valor de prevalencia (%). Por default, el valor de población es de 2.000 y valor de Precisión de 2 (este valor se usa en la fórmula prevalencia/valor que se eligio, generalmente se utiliza 2 o 3). Da el siguiente formato de resultado "Muestra con población infinita | Muestra para población finita". Si se quiere solamente obtener el tamaño muestral en base a una población infinita, colocar 0 en el apartado de población. 

*3) DEC:* Permite calcular la desviación estandar combinada con los valores de n y desviación estandar de casos y controles. Si bien esto fue utilizado para niveles de vitamina D, es util para cualquier variable cuantitativa, ya sea continua o discreta.

*4) D de Cohen:* Permite calcular la D de Cohen al utilizar la media de casos y controles, y el valor de desviación estandar combinada.

*5) Potencia Priori:* Permite calcular el tamaño muestral para dos muestras independientes utilizando el valor de d de Cohen. Se basa en la fórmula utilizada en el programa de G*Power, aunque no es del todo identica ya que falla a valores muy altos (d >= 5.65). Da un formato de resultado "Muestra total | n de casos - n de controles"

*6) Mean Difference:* Permite calcular el tamaño muestral para dos muestras independientes utilizando los valores de media y desviación estandar de casos y controles. Se basa en la fórmula utilizada en la página de OpenEpi, aunque no es del todo identica ya que esta página realiza ajuste a la fórmula clásica que da diferencias de 2 a 4 en algunos casos. Da un formato de resultado "Muestra total | n de casos - n de controles"
