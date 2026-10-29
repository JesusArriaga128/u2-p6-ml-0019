import pandas as pd 
import numpy as np 

serie_amigos=['Pedro','Morgan','Farfan','Adrian','Jesse','Alonso','Matias']
print('serie listado de amigos 0019')
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
serie_letras=['Veinte','cincuenta','cien','docientos','quinientos','mil']
print('serie listado valor de billetes MX 0019')
tabla_billetes=pd.Series(serie_billetes,serie_letras)
print(tabla_billetes)
## Diccionario dataframe 
# diccionario de valor de monedas y nombre 
print('Datos de diccionario a datafraem en pandas ')
dicc_monedas={
    'serie_billetes':[20,50,100,200,500,1000],
    'serie_letras':['Veinte','cincuenta','cien','docientos','quinientos','mil']
}
tabla_billetes=pd.DataFrame(dicc_monedas,index=['A','B','C','D','E','F'])
print(tabla_billetes)
print('casa decambio jesus arriaga 0019')

