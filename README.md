# Analisis_elecciones_presidenciales_2018
Por completar-en cosntruccion

## Objetivo del análisis
De todas las variables socioeconómicas del Censo de Población y Vivienda 2020 que pudieran
tener algún grado de asociación con la intención al voto por los candidatos a la presiden
cia Andrés Manuel López Obrador (AMLO) y Ricardo Anaya Cortés (RAC) se pretende identificar un
subconjunto de estas que pudiera describir la intensión al voto en favor  de: 

**AMLO** 

**RAC**

En otras palabras, se tiene un problema de selección de variables independiente para cada uno
de los candidatos. En el proyecto se realizarán las siguientes tareas:

1. Obtener una estimación por intervalo de la intensidad (peso) que tiene cada una de estas
variables en la intensión al voto. Separando en cada caso la intención al voto por AMLO y
RAC. 

2. Determinar grupos de variables que: Sólo impacten a uno de los candidatos, impacten a ambos pero que tengan mayor intensidad (peso) en uno de los candidatos e impacten ambos candidatos por igual.

Se utilizará el modelo de RLM para detectar posibles asociaciones entre las variables, así como
la intensidad de la asociación, i.e.

![imagen](Imagenes/Imagen1.png)

## Metodología
El proyecto esta dividido en partes: 

1. Primero, se obtienen los sub‑totales a nivel municipal para cada una de las variables presentes en las bases de datos de trabajo. En particular, la variable y_i se construye sumando y agregando los valores provenientes de los  [cómputos distritales](https://computos2018.ine.mx/#/descargaBase) hacia el nivel municipal. Posteriormente, se define un identificador único de municipio que permitirá vincular las distintas bases de datos. Todo este procedimiento se desarrolla en el script . Todo este procedimiento se desarrolla en el script `Votos.ipynb` usando, utilizando las bases `EDOScsv`, `LISTADO_CASILLAS_2018.csv`,  `presidencia.csv` y `Nombres_municipios.txt`, devolviendo la base `Votos_por_Municipio`.


