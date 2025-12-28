# codigo para pasar los archivos csv al gz
import pandas as pd

Base = pd.read_csv(r"Bases_Censo/conjunto_de_datos_iter_00CSV20.csv", encoding="UTF-8")
Base.to_csv(r"Bases_Censo/Censo_INE2020.gz", index=False, compression="gzip")

Votos = pd.read_csv(r"Bases_Votos/presidencia.csv", sep="|", 
                    encoding="latin1",engine="python",skiprows=6)
Votos.to_csv(r"Bases_Votos/Elecciones.gz", index=False, compression="gzip")
