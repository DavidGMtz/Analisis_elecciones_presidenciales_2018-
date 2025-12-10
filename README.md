# Analisis_elecciones_presidenciales_2018
Por completar-en cosntruccion

## Objetivo del análisis
De todas las variables socioeconómicas del Censo de Población y Vivienda 2020 que pudieran
tener algún grado de asociación con la intención al voto por los candidatos a la presiden
cia Andrés Manuel López Obrador (AMLO) y Ricardo Anaya Cortés (RAC) se pretende identificar un
subconjunto de estas que pudiera describir la intensión al voto en favor de \\
**AMLO**\\
**RAC**\\
En otras palabras, se tiene un problema de selección de variables independiente para cada uno
de los candidatos. En el proyecto se realizarán las siguientes tareas:

1. Obtener una estimación por intervalo de la intensidad (peso) que tiene cada una de estas
variables en la intensión al voto. Separando en cada caso la intención al voto por AMLO y
RAC.
2. Determinar grupos de variables que i) sólo impacten a uno de los candidatos, ii) impacten
a ambos pero que tengan mayor intensidad (peso) en uno de los candidatos y iii) impacten a
ambos candidatos por igual.
Se utilizará el modelo de RLM para detectar posibles asociaciones entre las variables, así como
la intensidad de la asociación, i.e.
\[
yi = β0 +β1xi,1 +···+βpxi,p + i, para i = 1...,N.
\]
En donde
\(y_i\) es el número de votos (o porcentaje) recibidos por el candidato en cuestión en el municipio
i-ésimo.
\(x_{i,j}\) es el valor de la variable socioeconómica j-ésima en el municipio i-ésimo con \(i = 1,...,N \)
y \(N\) es el número total de municipios en toda la república Mexicana. Finalmente, \(j = 1,...,p\)
y \(p\) es el número total de variables socioeconómicas que se haya decidido incluir en el análisis.
\(i\) es un error aleatorio con media cero y varianza constante, donde se asume que los errores no se dostribuyen de forma normal.