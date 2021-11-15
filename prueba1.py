import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Aquí están las librerías para poder instalar geopandas: https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona
# 

#calles_amazonas = gpd.read_file(r'calles/Amazonas/Amazonas.shp')

#calles_amazonas.plot()
#plt.show()

departamentos = gpd.read_file(r'peru/departamentos/DEPARTAMENTOS.shp')
departamentos.plot()
plt.savefig('mapa-departamentos.png')
plt.show()
plt.close()