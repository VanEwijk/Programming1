import cbsodata
import pandas as pd

#https://opendata.cbs.nl/statline/portal.html?_la=nl&_catalog=CBS&tableId=70262ned&_theme=298
#https://opendata.cbs.nl/statline/portal.html?_la=nl&_catalog=CBS&tableId=80142ned&_theme=289
#https://opendata.cbs.nl/statline/portal.html?_la=nl&_catalog=CBS&tableId=37259ned&_theme=257
list_names = ['Bodemgebruik per gemeente', 'Overledenen; 4 doodsoorzaken, regio', 'Bevolkingsontwikkeling; regio']
code_cbs = ['70262ned', '80142ned', '37259ned']
for index, name in enumerate(list_names):
    data = pd.DataFrame(cbsodata.get_data(code_cbs[index]))
    data.to_csv(f'{name}.csv', sep='\t')