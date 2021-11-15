import gspread as gs
import pandas as pd

# Las siguientes líneas descargan la pestaña del archivo googlesheet a un dataframe

key = '1VKi4Wcsx8KNcydRT-YiZqFU82am8LH1Y8a2pIP2u_Vs'
pestanna = 'RR'
gc = gs.service_account(filename='accesos.json')
sh = gc.open_by_key(key)
worksheet = sh.worksheet(pestanna)
dataframe = pd.DataFrame(worksheet.get_all_records())

# Lo que sigue exporta el dataframe a un archiv .csv

dataframe.to_csv('rr.csv') 

