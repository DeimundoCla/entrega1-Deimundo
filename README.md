# Información para desafío
En NavBar está el elemento "Cargador de cotizaciones".
La búsqueda sólo devuelve USD, se hizo el intento de combinar los modelos, pero se hizo imposible. El intento está en rama: version06.



# Maquetación:

1) Home con botones para ingresar a las funciones principales de la página web: Conversor de divisas - Buscador de código Swift - Carga de cotizaciones por día y hora.
2) Formulario de carga de 4 cotizaciones, para simplificar la UX y crear una base de datos para generar consultas históricas de cotizaciones.
3) Formulario de búsqueda para las cotizaciones cargadas en base de datos por fecha y tipo de moneda.
4) Conversor de divisas tratando de integrar con API financiera para poder tener cotizaciones actualizadas de forma automática.
5) Buscador de código SWIFT con la creación de un archivo JSON al que realizarle los query por país - ciudad - banco matríz
6) Contacto para registro con la posibilidad de generar usuarios "premium" con acceso a cotizaciones bursátiles y criptomonedas.

# version 0.1
1)Se crea la plantilla en base a ejemplo de Bootstrap.

2)Cambios a fotos, estilos de header para creación de plantilla padre.

3)Carga de modelos y funciones (incompletas) para la creación del conversor de monedas.

# version 0.2 (RAMA quedó atrás, eliminada)
1)Se modifica plantilla HTML para reducir carga y limitarse sólo a los elementos requeridos.

2)Refinamiento de plantilla a estilo similar al final.

# version 0.3 (master)
1) Se agregaron multiples plantillas con base padre y modificaciones en styles.css
2) Primer intento de conversor de monedas más formulario de contacto.
3) Creación de admin y vinculación de modelos.
4) Refinamiento de la mayoría de botones, textos e interactuables.

# version 0.4 (master)
1) Se realizó la vinculación de los formularios de carga de cotizaciones con views (falta resolver problemas con el token CSFR)
2) Creación de la landing para responder si los datos se cargaron con éxito.

# version 0.4 (rama)
1) Se agrega hipervínculo en index para carga de cotizaciones.

# version 0.5 (master)
1) Se agregan formularios de carga de cotizaciones con éxito.
2) Base de datos: se actualizan tablas para contener nombres de las monedas.
3) Se crea formulario de búsqueda en págna de cotizaciones, no entrega resultados, revisar {% for loop %}
4) Refinamiento de botones, secciones, paddings en CSS.

# version 0.6 (rama)
1) Se intentó crear búsqueda compleja mediante varios modelos y varias query.
2) Pese a entender el proceso del query, se encontraron problemas para vincular lo que se hace con la búsqueda en la URL.
3) Se deja esta rama para continuar este formato de búsqueda en el futuro.

# version 0.7 (Master)
1) Se creó una búsqueda de cotizaciones por fecha, arreglando en la búsqueda la posibilidad de elegir fecha mediante formulario correspondiente.
2) Se le sumó a las cargas de cotizaciones la posibilidad de agregar la fecha mediante formulario correspondiente.
3) Se empieza a crear la 404 para manejar páginas no existentes, problemas al pasar de DEBUG=TRUE a FALSE.
