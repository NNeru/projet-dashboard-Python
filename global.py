import pandas as pd
import datetime
import json
from urllib.request import urlopen

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

import plotly
import plotly.graph_objects as go
import plotly.io as pio
import plotly_express as px
from dash.dependencies import Input, Output

#Définition de l'application

app = dash.Dash(__name__)
pd.options.mode.chained_assignment = None  # default='warn'
app.config["suppress_callback_exceptions"] = True

# ---------------------------------------
# On importe et nettoie les données à l'aide de pandas

catnat=pd.read_csv('catnat_gaspar.csv',encoding='utf8',delimiter=';',low_memory=False)
temperature=pd.read_csv('temperature-quotidienne-regionale.csv',encoding='utf8',delimiter=';')
climat=pd.read_csv('Climat_csv.csv',encoding='utf8',delimiter=';')
climat=climat.rename(columns={'Région':'Region','Date':'Année'})
#-----------------------------------------
temperature=temperature.rename(columns={'Date' : 'Date','Code INSEE région':'Code_Région','Région':'Region','TMin (°C)':'Température_Min_(°C)','TMax (°C)':'Température_Max_(°C)','TMoy (°C)':'Température_Moy_(°C)'})

#On crée un dataframe qui contient les temperature par régions pour chaque année
temperature_by_year_Regions = temperature.groupby(['Region','Date'])['Température_Moy_(°C)'].mean().reset_index()
temperature_by_year_Regions = temperature.groupby(['Region','Date'])['Température_Moy_(°C)'].mean().reset_index()
temperature_by_year_Regions['Date']=pd.DatetimeIndex(temperature_by_year_Regions['Date']).year
temperature_by_year_Regions['Date']=pd.to_numeric(temperature_by_year_Regions['Date'])
temperature_by_year_Regions = temperature_by_year_Regions.groupby(['Region','Date'])['Température_Moy_(°C)'].mean().reset_index()


#température par saison en 2016

#les Normales de saison
normaleEte=19.9
normaleAutumn=13.1
normalePrintemps=11.6
normaleHiver=5.4

temperature['Date']=pd.to_datetime(temperature['Date'])

temperatureAutumn2016=temperature[temperature['Date']<='2016-11-30']
temperatureAutumn2016=temperatureAutumn2016[temperature['Date']>='2016-09-01']

temperatureHiver2016=temperature[temperature['Date']<='2016-03-01']
temperatureHiver2016=temperatureHiver2016[temperatureHiver2016['Date']>='2016-01-01']

temperaturePrintemps2016=temperature[temperature['Date']<='2016-05-31']
temperaturePrintemps2016=temperaturePrintemps2016[temperature['Date']>='2016-03-02']

temperatureEte2016=temperature[temperature['Date']<='2016-08-31']
temperatureEte2016=temperatureEte2016[temperature['Date']>='2016-06-01']

#température par saison en 2017
temperatureHiver2017=temperature[temperature['Date']<='2017-03-01']
temperatureHiver2017=temperatureHiver2017[temperatureHiver2017['Date']>='2017-01-01']


temperatureAutumn2017=temperature[temperature['Date']<='2017-11-30']
temperatureAutumn2017=temperatureAutumn2017[temperature['Date']>='2017-09-01']

temperaturePrintemps2017=temperature[temperature['Date']<='2017-05-31']
temperaturePrintemps2017=temperaturePrintemps2017[temperature['Date']>='2017-03-02']

temperatureEte2017=temperature[temperature['Date']<='2017-08-31']
temperatureEte2017=temperatureEte2017[temperature['Date']>='2017-06-01']

#température par saison en 2018
temperatureHiver2018=temperature[temperature['Date']<='2018-03-01']
temperatureHiver2018=temperatureHiver2018[temperatureHiver2018['Date']>='2018-01-01']

temperatureAutumn2018=temperature[temperature['Date']<='2018-11-30']
temperatureAutumn2018=temperatureAutumn2018[temperature['Date']>='2018-09-01']

temperaturePrintemps2018=temperature[temperature['Date']<='2018-05-31']
temperaturePrintemps2018=temperaturePrintemps2018[temperature['Date']>='2018-03-02']

temperatureEte2018=temperature[temperature['Date']<='2018-08-31']
temperatureEte2018=temperatureEte2018[temperature['Date']>='2018-06-01']

#température par saison en 2019
temperatureHiver2019=temperature[temperature['Date']<='2019-03-01']
temperatureHiver2019=temperatureHiver2019[temperatureHiver2019['Date']>='2019-01-01']

temperatureAutumn2019=temperature[temperature['Date']<='2019-11-30']
temperatureAutumn2019=temperatureAutumn2019[temperature['Date']>='2019-09-01']

temperaturePrintemps2019=temperature[temperature['Date']<='2019-05-31']
temperaturePrintemps2019=temperaturePrintemps2019[temperature['Date']>='2019-03-02']

temperatureEte2019=temperature[temperature['Date']<='2019-08-31']
temperatureEte2019=temperatureEte2019[temperature['Date']>='2019-06-01']

#température par saison en 2020
temperatureHiver2020=temperature[temperature['Date']<='2020-03-01']
temperatureHiver2020=temperatureHiver2020[temperatureHiver2020['Date']>='2020-01-01']

temperatureAutumn2020=temperature[temperature['Date']<='2020-11-30']
temperatureAutumn2020=temperatureAutumn2020[temperature['Date']>='2020-09-01']

temperaturePrintemps2020=temperature[temperature['Date']<='2020-05-31']
temperaturePrintemps2020=temperaturePrintemps2020[temperature['Date']>='2020-03-02']

temperatureEte2020=temperature[temperature['Date']<='2020-08-31']
temperatureEte2020=temperatureEte2020[temperature['Date']>='2020-06-01']

# violin avec les température pour mois 2016

temperature_month_2016=temperature[temperature['Date']>='2016-01-01']
temperature_month_2016=temperature[temperature['Date']<='2016-12-31']
temperature_month_2016=temperature_month_2016.reset_index()

liste=[]

for i in range(4758):
    liste.append(temperature_month_2016['Date'][i].month)

temperature_month_2016.head()
data={'Temperature':temperature_month_2016['Température_Moy_(°C)'],'Date':temperature_month_2016['Date'],'mois':liste}

temperature_month_2016=pd.DataFrame(data=data)

# violin avec les température par mois 2017

temperature_month_2017=temperature[temperature['Date']>='2017-01-01']
temperature_month_2017=temperature[temperature['Date']<='2017-12-31']
temperature_month_2017=temperature_month_2017.reset_index()

liste=[]

for i in range((len(temperature_month_2017['Date']))):
    liste.append(temperature_month_2017['Date'][i].month)

temperature_month_2017.head()
data={'Temperature':temperature_month_2017['Température_Moy_(°C)'],'Date':temperature_month_2017['Date'],'mois':liste}

temperature_month_2017=pd.DataFrame(data=data)

# violin avec les température par mois 2018

temperature_month_2018=temperature[temperature['Date']>='2018-01-01']
temperature_month_2018=temperature[temperature['Date']<='2018-12-31']
temperature_month_2018=temperature_month_2018.reset_index()

liste=[]

for i in range((len(temperature_month_2018['Date']))):
    liste.append(temperature_month_2018['Date'][i].month)


data={'Temperature':temperature_month_2018['Température_Moy_(°C)'],'Date':temperature_month_2018['Date'],'mois':liste}

temperature_month_2018=pd.DataFrame(data=data)

# violin avec les température par mois 2019

temperature_month_2019=temperature[temperature['Date']>='2019-01-01']
temperature_month_2019=temperature[temperature['Date']<='2019-12-31']
temperature_month_2019=temperature_month_2019.reset_index()

liste=[]

for i in range((len(temperature_month_2019['Date']))):
    liste.append(temperature_month_2019['Date'][i].month)

temperature_month_2019.head()
data={'Temperature':temperature_month_2019['Température_Moy_(°C)'],'Date':temperature_month_2019['Date'],'mois':liste}

temperature_month_2019=pd.DataFrame(data=data)

# violin avec les température par mois 2020

temperature_month_2020=temperature[temperature['Date']>='2020-01-01']
temperature_month_2020=temperature[temperature['Date']<='2020-12-31']
temperature_month_2020=temperature_month_2020.reset_index()

liste=[]

for i in range((len(temperature_month_2020['Date']))):
    liste.append(temperature_month_2020['Date'][i].month)

temperature_month_2020.head()
data={'Temperature':temperature_month_2020['Température_Moy_(°C)'],'Date':temperature_month_2019['Date'],'mois':liste}

temperature_month_2020=pd.DataFrame(data=data)


#température moyenne de chaque région pour chaque année
temp2016=temperature[temperature['Date']>='2016-01-01']
temp2016=temp2016[temp2016['Date']<='2016-12-31']
temp2016=temp2016.groupby('Region')['Température_Moy_(°C)'].mean().reset_index()

temp2017=temperature[temperature['Date']>='2017-01-01']
temp2017=temp2017[temp2017['Date']<='2017-12-31']
temp2017=temp2017.groupby('Region')['Température_Moy_(°C)'].mean().reset_index()

temp2018=temperature[temperature['Date']>='2018-01-01']
temp2018=temp2018[temp2018['Date']<='2018-12-31']
temp2018=temp2018.groupby('Region')['Température_Moy_(°C)'].mean().reset_index()

temp2019=temperature[temperature['Date']>='2019-01-01']
temp2019=temp2019[temp2019['Date']<='2019-12-31']
temp2019=temp2019.groupby('Region')['Température_Moy_(°C)'].mean().reset_index()


#Regroupement des température d'hiver
tHi2016=temperatureHiver2016['Température_Moy_(°C)'].mean()
tHi2017=temperatureHiver2017['Température_Moy_(°C)'].mean()
tHi2018=temperatureHiver2018['Température_Moy_(°C)'].mean()
tHi2019=temperatureHiver2019['Température_Moy_(°C)'].mean()
tHi2020=temperatureHiver2020['Température_Moy_(°C)'].mean()

dataHiver={'Temperature_moyenne':[tHi2016,tHi2017,tHi2018,tHi2019,tHi2020],'Date':[2016,2017,2018,2019,2020]}
dataHiver=pd.DataFrame(data=dataHiver)
#On soustrait les moyenne à la normale pour avoir l'écart
tHi=dataHiver['Temperature_moyenne']-normaleHiver
dHi=dataHiver['Date']
cHi= ['red' if tHi[i]>0 else 'blue' for i in range(5)]

data={'Temperature_moyenne':tHi,'Date':dHi, 'color':cHi}
EcartHi=pd.DataFrame(data=data)

#Regroupement des température de printemps
tPrin2016=temperaturePrintemps2016['Température_Moy_(°C)'].mean()
tPrin2017=temperaturePrintemps2017['Température_Moy_(°C)'].mean()
tPrin2018=temperaturePrintemps2018['Température_Moy_(°C)'].mean()
tPrin2019=temperaturePrintemps2019['Température_Moy_(°C)'].mean()
tPrin2020=temperaturePrintemps2020['Température_Moy_(°C)'].mean()

dataPrintemps={'Temperature_moyenne':[tPrin2016,tPrin2017,tPrin2018,tPrin2019,tPrin2020],'Date':[2016,2017,2018,2019,2020]}
dataPrintemps=pd.DataFrame(data=dataPrintemps)


tPrin=dataPrintemps['Temperature_moyenne']-normalePrintemps
dPrin=dataPrintemps['Date']
cPrin= ['red' if tPrin[i]>0 else 'blue' for i in range(5)]

data={'Temperature_moyenne':tPrin,'Date':dPrin,'color':cPrin}
EcartPrin=pd.DataFrame(data=data)
#Regroupement des température d'Eté
tEte2016=temperatureEte2016['Température_Moy_(°C)'].mean()
tEte2017=temperatureEte2017['Température_Moy_(°C)'].mean()
tEte2018=temperatureEte2018['Température_Moy_(°C)'].mean()
tEte2019=temperatureEte2019['Température_Moy_(°C)'].mean()
tEte2020=temperatureEte2020['Température_Moy_(°C)'].mean()

dataEte={'Temperature_moyenne':[tEte2016,tEte2017,tEte2018,tEte2019,tEte2020],'Date':[2016,2017,2018,2019,2020]}
dataEte=pd.DataFrame(data=dataEte)
dataEte

tEte=dataEte['Temperature_moyenne']-normaleEte
dEte=dataEte['Date']
cEte= ['red' if tEte[i]>0 else 'blue' for i in range(5)]


data={'Temperature_moyenne':tEte,'Date':dEte, 'color':cEte}
EcartEte=pd.DataFrame(data=data)
#Regroupement des température d'Automne
tAu2016=temperatureAutumn2016['Température_Moy_(°C)'].mean()
tAu2017=temperatureAutumn2017['Température_Moy_(°C)'].mean()
tAu2018=temperatureAutumn2018['Température_Moy_(°C)'].mean()
tAu2019=temperatureAutumn2019['Température_Moy_(°C)'].mean()
tAu2020=temperatureAutumn2020['Température_Moy_(°C)'].mean()

dataAutumn={'Temperature_moyenne':[tAu2016,tAu2017,tAu2018,tAu2019,tAu2020],'Date':[2016,2017,2018,2019,2020]}
dataAutumn=pd.DataFrame(data=dataAutumn)
dataAutumn

tAu=dataAutumn['Temperature_moyenne']-normaleAutumn
dAu=dataAutumn['Date']
cAu= ['red' if tAu[i]>0 else 'blue' for i in range(5)]

data={'Temperature_moyenne':tAu,'Date':dAu,'color':cAu}
EcartAu=pd.DataFrame(data=data)

#On récupèr ela température par mois pour chaque année
temperature_by_month_annee = temperature.groupby(['Region','Date'])[['Température_Moy_(°C)']].mean().reset_index()
temperature_by_month_annee['Année']=pd.DatetimeIndex(temperature_by_month_annee['Date']).year
temperature_by_month_annee['Date']=pd.DatetimeIndex(temperature_by_month_annee['Date']).month
temperature_by_month_annee = temperature_by_month_annee.groupby(['Année','Date'])[['Température_Moy_(°C)']].mean().reset_index()


# -----------------nettoyage des données pour les catastrophes naturelles

#on enlève les colonnes qui ne nous sommes pas nécéssaires
catnat=catnat.drop(['dat_maj','dat_deb','dat_fin','dat_pub_jo','lib_commune'],axis=1)

# on renomme les colonnes
catnat=catnat.rename(columns={'cod_nat_catnat':'Code_nationale_catnat','cod_commune':'Code_postale','num_risque_jo':'Num_risque','lib_risque_jo':'Type_de_catnat','dat_pub_arrete':'Date_arreté'})

# on change le type de code postale en type str
catnat['Code_postale']=catnat['Code_postale'].astype(str)

# pour récupérer le code de département on prend les deux premiers chiffre du code postale
catnat['Code_Departement']=catnat['Code_postale'].str[:2]

# maintenant on va regrouper les départements en Regions
catnat['Region']=catnat['Code_postale']

# Département du Centre Val de Loire

catnat.loc[(catnat.Code_Departement == '28') | (catnat.Code_Departement == '45') |(catnat.Code_Departement == '41') |(catnat.Code_Departement == '37') |(catnat.Code_Departement == '18') |(catnat.Code_Departement == '36'),'Region'] = 'Centre-Val de Loire'

# Département de Bretagne

catnat.loc[(catnat.Code_Departement == '29') | (catnat.Code_Departement == '22') |(catnat.Code_Departement == '56') |(catnat.Code_Departement == '35'),'Region'] = 'Bretagne'

# Département Corse

catnat.loc[(catnat.Code_Departement == '2A') | (catnat.Code_Departement == '2B'),'Region'] = 'Corse'

# Département Ile-de-France

catnat.loc[(catnat.Code_Departement == '75') | (catnat.Code_Departement == '93') |(catnat.Code_Departement == '94') |(catnat.Code_Departement == '92')|(catnat.Code_Departement == '77') |(catnat.Code_Departement == '78')|(catnat.Code_Departement == '91') |(catnat.Code_Departement == '95'),'Region'] = 'Ile-de-France'

# Département Normandie

catnat.loc[(catnat.Code_Departement == '76') | (catnat.Code_Departement == '27') |(catnat.Code_Departement == '61') |(catnat.Code_Departement == '50')|(catnat.Code_Departement == '14')|(catnat.Code_Departement == '59'),'Region'] = 'Normandie'

#Département Nouvelle Aquitaine

catnat.loc[(catnat.Code_Departement == '86') | (catnat.Code_Departement == '79') |(catnat.Code_Departement == '87') |(catnat.Code_Departement == '17')|(catnat.Code_Departement == '16') |(catnat.Code_Departement == '24')|(catnat.Code_Departement == '33') |(catnat.Code_Departement == '40')|(catnat.Code_Departement == '47') |(catnat.Code_Departement == '19') |(catnat.Code_Departement == '23')|(catnat.Code_Departement == '64'),'Region'] = 'Nouvelle-Aquitaine'

# Département Occitanie

catnat.loc[(catnat.Code_Departement == '32') | (catnat.Code_Departement == '65') |(catnat.Code_Departement == '82') |(catnat.Code_Departement == '31')|(catnat.Code_Departement == '09') |(catnat.Code_Departement == '46')|(catnat.Code_Departement == '81') |(catnat.Code_Departement == '11')|(catnat.Code_Departement == '66') |(catnat.Code_Departement == '34')|(catnat.Code_Departement == '12') |(catnat.Code_Departement == '48') |(catnat.Code_Departement == '30'),'Region'] = 'Occitanie'

# Département Pays de la Loire

catnat.loc[(catnat.Code_Departement == '72') | (catnat.Code_Departement == '53') |(catnat.Code_Departement == '49') |(catnat.Code_Departement == '44')|(catnat.Code_Departement == '85'),'Region'] = 'Pays de la Loire'
    
# Département Provence Alpes Cote d'Azur

catnat.loc[(catnat.Code_Departement == '05') | (catnat.Code_Departement == '04') |(catnat.Code_Departement == '06')|(catnat.Code_Departement == '84') |(catnat.Code_Departement == '13')|(catnat.Code_Departement == '83'),'Region'] = 'Provence-Alpes-Côte d Azur'

    
# Département Hauts de France

catnat.loc[(catnat.Code_Departement == '62') | (catnat.Code_Departement == '59') |(catnat.Code_Departement == '80') |(catnat.Code_Departement == '02')|(catnat.Code_Departement == '60'),'Region'] = 'Hauts-de-France'

# Département Grand-Est

catnat.loc[(catnat.Code_Departement == '08') | (catnat.Code_Departement == '55') |(catnat.Code_Departement == '51') |(catnat.Code_Departement == '54')|(catnat.Code_Departement == '10') |(catnat.Code_Departement == '57')|(catnat.Code_Departement == '52') |(catnat.Code_Departement == '88')|(catnat.Code_Departement == '67')|(catnat.Code_Departement == '68'),'Region'] = 'Grand-Est'
     

# Département Bourgogne-Franche-Comté

catnat.loc[(catnat.Code_Departement == '89') | (catnat.Code_Departement == '58') |(catnat.Code_Departement == '21') |(catnat.Code_Departement == '71')|(catnat.Code_Departement == '39') |(catnat.Code_Departement == '25')|(catnat.Code_Departement == '70') |(catnat.Code_Departement == '90'),'Region'] = 'Bourgogne-Franche-Comté'

# Département Auvergne-Rhône-Alpes

catnat.loc[(catnat.Code_Departement == '03') | (catnat.Code_Departement == '42') |(catnat.Code_Departement == '69') |(catnat.Code_Departement == '01')|(catnat.Code_Departement == '74') |(catnat.Code_Departement == '73')|(catnat.Code_Departement == '38') |(catnat.Code_Departement == '26')|(catnat.Code_Departement == '07')|(catnat.Code_Departement == '43')|(catnat.Code_Departement == '63')|(catnat.Code_Departement == '15'),'Region'] = 'Auvergne-Rhône-Alpes'




# on retire les DOM TOM 

catnat=catnat[catnat['Code_Departement']!='97']

# on reset les index

catnat=catnat.reset_index()
catnat=catnat.drop(columns='index')

# on récupère l'année à partir de la date exacte de la catastrophe naturelle
catnat['Année']=pd.DatetimeIndex(catnat['Date_arreté']).year
catnat=catnat[catnat['Année']>=2016]


# on crée des dataframes des catnats pour chaque année

catnat2016=catnat[catnat['Année']==2016]
catnat2017=catnat[catnat['Année']==2017]
catnat2018=catnat[catnat['Année']==2018]
catnat2019=catnat[catnat['Année']==2019]
catnat2020=catnat[catnat['Année']==2020]

#on récupère le nombre de catnat pour chaque région et chaque année
nb_catnat_region_2016=catnat2016.groupby('Region')[['Num_risque']].count().reset_index()
nb_catnat_region_2016=nb_catnat_region_2016.rename(columns={'Num_risque':'nb_catnat'})
nb_catnat_region_2016['Année']=2016

nb_catnat_region_2017=catnat2017.groupby('Region')[['Num_risque']].count().reset_index()
nb_catnat_region_2017=nb_catnat_region_2017.rename(columns={'Num_risque':'nb_catnat'})
nb_catnat_region_2017['Année']=2017

nb_catnat_region_2018=catnat2018.groupby('Region')[['Num_risque']].count().reset_index()
nb_catnat_region_2018=nb_catnat_region_2018.rename(columns={'Num_risque':'nb_catnat'})
nb_catnat_region_2018['Année']=2018

nb_catnat_region_2019=catnat2019.groupby('Region')[['Num_risque']].count().reset_index()
nb_catnat_region_2019=nb_catnat_region_2019.rename(columns={'Num_risque':'nb_catnat'})
nb_catnat_region_2019['Année']=2019

nb_catnat_region_2020=catnat2020.groupby('Region')[['Num_risque']].count().reset_index()
nb_catnat_region_2020=nb_catnat_region_2020.rename(columns={'Num_risque':'nb_catnat'})
nb_catnat_region_2020['Année']=2020

nb_catnatYear_region = pd.concat([nb_catnat_region_2016,nb_catnat_region_2017,nb_catnat_region_2018,nb_catnat_region_2019,nb_catnat_region_2020],keys='tuple')


# on crée un dataframe avec les catastrophes naturelles regroupées par Regions par année

catnat_annee=catnat.groupby(by=['Année'])['Type_de_catnat'].count().reset_index()
catnat_annee=catnat_annee.rename(columns={'Type_de_catnat':'nombre_de_catnat'})
catnat_annee=catnat_annee[catnat_annee['Année']>=2016]
catnat_annee=catnat_annee[catnat_annee['Année']<=2020]

#On crée un dataframe qui compte le nombre de catastrophe naturelle par mois par ans

catnat_month_annee = catnat.groupby(['Region','Date_arreté'])[['Num_risque']].count().reset_index()
catnat_month_annee['Année']=pd.DatetimeIndex(catnat_month_annee['Date_arreté']).year
catnat_month_annee['Date_arreté']=pd.DatetimeIndex(catnat_month_annee['Date_arreté']).month
catnat_month_annee = catnat_month_annee.groupby(['Année','Date_arreté'])[['Num_risque']].sum().reset_index()
catnat_month_annee=catnat_month_annee.rename(columns={'Date_arreté' : 'Date','Num_risque':'Nombre_catnat'})
catnat_month_annee=catnat_month_annee[catnat_month_annee['Année']>=2016]

#on crée un dataframe qui récupère le nombre de catastrophe naturelles par type pour chaque année
type2016 = catnat2016.groupby(['Année','Type_de_catnat'])[['Num_risque']].count().reset_index()
type2017 = catnat2017.groupby(['Année','Type_de_catnat'])[['Num_risque']].count().reset_index()
type2018 = catnat2018.groupby(['Année','Type_de_catnat'])[['Num_risque']].count().reset_index()
type2019 = catnat2019.groupby(['Année','Type_de_catnat'])[['Num_risque']].count().reset_index()
type2020 = catnat2020.groupby(['Année','Type_de_catnat'])[['Num_risque']].count().reset_index()
typeYears = pd.concat([type2016,type2017,type2018,type2019,type2020])
typeYears = typeYears.rename(columns={'Num_risque':'Nombre_catnat'})

#Code pour afficher le graph chloropleth
counties=json.load(open('regions.json'))
state_id_map={}

for feature in counties['features']:
    feature['id']=feature['properties']['code']
    state_id_map[feature['properties']['nom']]=feature['id']

df_catnat=nb_catnatYear_region
df_catnat['id']=df_catnat['Region'].apply(lambda x: state_id_map)
#On utilise un dico pour récuperer le nom des régions
dico={'Ile-de-France': '11',
 'Centre-Val de Loire': '24',
 'Bourgogne-Franche-Comté': '27',
 'Normandie': '28',
 'Hauts-de-France': '32',
 'Grand-Est': '44',
 'Pays de la Loire': '52',
 'Bretagne': '53',
 'Nouvelle-Aquitaine': '75',
 'Occitanie': '76',
 'Auvergne-Rhône-Alpes': '84',
 "Provence-Alpes-Côte d Azur": '93',
 'Corse': '94'}


size=df_catnat.shape[0]
for i in range(size):
    df_catnat['id'][i]=dico.get(df_catnat['Region'][i]) 

pio.renderers.default='vscode'

temperature_by_year_Regions=temperature_by_year_Regions.rename(columns={'Date':'Année'})
tempe_climat=climat.merge(temperature_by_year_Regions)
tempe_climat=tempe_climat.merge(nb_catnatYear_region)

# ------------------------------------------------------------------------------
#On crée la fonction qui va contstruire le titre du dashboard 
def build_banner():
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H2("TEMPERATURE, CATASTROPHES NATURELLES ET CLIMAT")
                ],
            )
        ],
    )

#Fonction qui crée chaque tab
def build_tabs():
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="tab1",
                className="custom-tabs",
                children=[
                    dcc.Tab(
                        id="Recclim",
                        label="Réchauffement climatique",
                        value="tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="temp_fac",
                        label="Température/Facteurs climatiques",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="catnat",
                        label="Evolution des catastrophes naturelles",
                        value="tab3",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="temp_catnat",
                        label="Température/Catastrophes",
                        value="tab4",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            )
        ],
    )


#Fonction qui construit le contenu de la première tab
def build_tab_1():
    return [
        html.Div(
            id="top-row-graphs",
            children=[
                html.Div(
                    className="row",
                    children=[
                        
                    ],
                ),
                html.Div(
                    className="row",
                    id="bottom-row",
                    children=[
                        html.H3("Température 2016"),
                        # Histogramme
                        html.Div(
                            # barplot
                            id="violin-container",
                            className="six columns",
                            children=[
                                dcc.Graph(id="violin"),
                            ],
                        ),
                        html.H3("Année"),
                        dcc.Dropdown(id="slct_year",
                    options=[
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018},
                     {"label": "2019", "value": 2019},
                     {"label": "2020", "value": 2020}],
                    multi=False,
                    value=2016,
                    style={'width': "40%"}
                    ),
                        html.Div(
                            # barplot
                            id="barplot-container",
                            className="six columns",
                            children=[
                                dcc.Graph(id="barplot"),
                            ],
                        )
                    ],
                ),
                #4 saisons
                html.Div([ 
                    html.Div([
                    dcc.Graph(id="histog_aut"),
                        ],style={'display' : 'inline-block'}),
                    html.Div([
                        dcc.Graph(id="histog_hiv")
                        ],style={'display' : 'inline-block'})                      
                            
              ],className="row flex-display",),
                html.Div([ 
                    html.Div([
                        dcc.Graph(id="histog_print"),
                        ],style={'display' : 'inline-block'}),
                    html.Div([
                        dcc.Graph(id="histog_ete")
                        ],style={'display' : 'inline-block'})
            ]
        )
        
    ])
    
]
#Fonction qui construit le contenu de la deuxième tab
def build_tab_2():
    return [
       html.Div(
            id="top-row-graphs5",
            children=[
                html.Div(
                    className="row",
                    children=[
                        
                    ],
                ),
                html.Div(
                    className="row",
                    id="bottom-row",
                    children=[
                        # Histogramme
                        html.Div(
                            # barplot
                            id="violin-container",
                            className="six columns",
                            children=[
                                dcc.Graph(id="vent_temp"),
                            ],
                        ),
                        html.Div(
                            # barplot
                            id="barplot-container",
                            className="six columns",
                            children=[
                                dcc.Graph(id="precipitation_temp"),
                            ],
                        ),
                        html.Div(
                            # barplot
                            id="barplot-container",
                            className="six columns",
                            children=[
                                dcc.Graph(id="soleil_temp"),
                            ],
                        )
                    ],
                )   
    ])
    ]
#Fonction qui construit le contenu de la troisème tab
def build_tab_3():
    return [
       html.Div(
            id="top-row-graphs",
            children=[
                html.Div(
                    className="row",
                    children=[
                        
                    ],
                ),
                html.Div(
                    className="row",
                    id="bottom-row",
                    children=[
                        # Catnat/annee
                        html.Div(
                            # barplot
                            id="catnat-container",
                            className="six columns",
                            children=[
                                dcc.Graph(id="catnat_annee"),
                            ],
                        ),
                        html.H3("Année"),
                        dcc.Dropdown(id="slct_years",
                    options=[
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018},
                     {"label": "2019", "value": 2019},
                     {"label": "2020", "value": 2020}],
                    multi=False,
                    value=2016,
                    style={'width': "40%"}
                    ),
                        
                        html.Div(
                            # barplot
                            id="barplot-container",
                            className="six columns",
                            children=[dcc.Graph(id="map")
                               ],
                        )
                    ],
                ),
                #4 saisons
                html.Div([ 
                    html.H3("Type de catastrophe"),
                        dcc.Dropdown(id="slct_catnat",
                    options=[
                     {"label": "Avalanche", "value": "Avalanche"},
                     {"label": "Chocs mécaniques liés à l'action des vagues", "value": "Chocs mécaniques liés à l'action des vagues"},
                     {"label": "Inondations et chocs mécaniques liés à l'action des vagues", "value": "Inondations et chocs mécaniques liés à l'action des vagues"},
                     {"label": "Inondations et coulées de boue", "value": "Inondations et coulées de boue"},
                     {"label": "Inondations par remontée de la nappe phréatique et mouvements de terrain", "value": "Inondations par remontée de la nappe phréatique et mouvements de terrain"},
                     {"label": "Inondations par remontées de nappe naturelle", "value": "Inondations par remontées de nappe naturelle"},
                     {"label": "Inondations par remontées de nappe phréatique", "value": "Inondations par remontées de nappe phréatique"},
                     {"label": "Inondations, coulées de boue et glissements de terrain", "value": "Inondations, coulées de boue et glissements de terrain"},
                     {"label": "Mouvements de terrain", "value": "Mouvements de terrain"},
                     {"label": "Mouvements de terrain consécutifs à la sécheresse", "value": "Mouvements de terrain consécutifs à la sécheresse"},
                     {"label": "Mouvements de terrain différentiels consécutifs à la sécheresse et à la réhydratation des sols", "value": "Mouvements de terrain différentiels consécutifs à la sécheresse et à la réhydratation des sols"},
                     {"label": "Séisme", "value": "Séisme"},
                     {"label": "Tassement de terrain", "value": "Tassement de terrain"}],
                    multi=False,
                    value=2016,
                    style={'width': "40%"}
                    ),
                    html.Div([
                        dcc.Graph(id="catnat_type"),
                        ])                     
                            
              ]),
        
    ])
    ]
#Fonction qui construit le contenu de la quatrième tab
def build_tab_4():
    return [
        html.Div(
            id="top-row-graphs4",
            children=[ 
                html.Div(
                    className="row",
                    children=[
                       dcc.Graph(id="temperature_month_year")
                    ],
                ),
                html.Div(
                    className="row",
                    id="bottom-row",
                    children=[
                        dcc.Graph(id="catnat_month_year")
                    ]
                    
                )
            ])
        
    
    ]        

# ------------------------------------------------------------------------------
# On crée l'interface de l'application à l'aid ede nos fonctions
app.layout = html.Div(
    id="big-app-container",
    children=[
        build_banner(),
        html.Div(
            id="app-container",
            children=[
                build_tabs(),
                # Main app
                html.Div(id="app-content"),
            ],
        )
        ],
    )

# -------------------------------------------
# On fait les callbacks qui nous permettent de connecter nous data à l'appli et les afficher

#callback 1ere tab
@app.callback(
    [Output(component_id='violin', component_property='figure'),
     Output(component_id='barplot', component_property='figure'),
     Output(component_id='histog_aut', component_property='figure'),
     Output(component_id='histog_hiv', component_property='figure'),
     Output(component_id='histog_print', component_property='figure'),
     Output(component_id='histog_ete', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)

def page_1(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    dff = temperature_by_year_Regions.copy()
    dff = dff[dff["Année"] == option_slctd]

    fig_bar=px.bar(dff,title='Moyenne des températures par Région',x='Température_Moy_(°C)',y='Region')

    fig_vio = go.Figure()

    months = [1,2,3,4,5,6,7,8,9,10,11,12]

    for month in months:
        fig_vio.add_trace(go.Violin(x=temperature_month_2016['mois'][temperature_month_2016['mois'] == month],
                            y=temperature_month_2016['Temperature'][temperature_month_2016['mois'] == month],
                            name=month,
                            box_visible=True,
                            meanline_visible=True))

    fig_aut=px.bar(EcartAu,title="Ecart de température par rapport à la normale de saison - Automne 13.1°C",x='Date',y='Temperature_moyenne',color='color')
    fig_aut.update_yaxes(range=[-1.2, 5.3], row=1, col=1)

    fig_hiv=px.bar(EcartHi,title="Ecart de température par rapport à la normale de saison - Hiver 5.4°C",x='Date',y='Temperature_moyenne',color='color')
    fig_hiv.update_yaxes(range=[-1.2, 5.3], row=1, col=1)  

    fig_print=px.bar(EcartPrin,title="Ecart de température par rapport à la normale de saison - Printemps 11.6°C",x='Date',y='Temperature_moyenne',color='color')
    fig_print.update_yaxes(range=[-1.2, 5.3], row=1, col=1)  

    fig_ete=px.bar(EcartEte,title="Ecart de température par rapport à la normale de saison - Eté 19.9°C",x='Date',y='Temperature_moyenne',color='color')
    fig_ete.update_yaxes(range=[-1.2, 5.3], row=1, col=1)                        
    return fig_vio, fig_bar, fig_aut, fig_hiv, fig_print,fig_ete

#callback 2e tab
@app.callback(
    [Output(component_id='vent_temp', component_property='figure'),
    Output(component_id='precipitation_temp', component_property='figure'),
    Output(component_id='soleil_temp', component_property='figure')],
    [Input(component_id='top-row-graphs5', component_property='children')]
)

def page_2(year_select):
    

    fig_vent_temp = px.scatter(tempe_climat,title='Vitesse du vent maximale/Temperature',x='Température_Moy_(°C)',y="Vitesse maximale du vent",color="Region",size='nb_catnat',animation_frame="Année",hover_name="Region",log_x=True, size_max=55, range_x=[10,20], range_y=[90,160])

    fig_precip_temp = px.scatter(tempe_climat,title='Hauteur de précipitation (en mm)/Temperature',x='Température_Moy_(°C)',y="Hauteur des precipitations",color="Region",size='nb_catnat',animation_frame="Année",hover_name="Region",log_x=True, size_max=55, range_x=[10,20], range_y=[370,1250])

    fig_soleil_temp = px.scatter(tempe_climat,title='Ensoleillement (en heures)/Temperature',x='Température_Moy_(°C)',y="Heures d'ensoleillement",color="Region",size='nb_catnat',animation_frame="Année",hover_name="Region",log_x=True, size_max=55, range_x=[10,20], range_y=[900,3700])
    
    return fig_vent_temp,fig_precip_temp,fig_soleil_temp

#callback 3e tab
@app.callback(
    [Output(component_id='catnat_annee', component_property='figure'),
     Output(component_id='map', component_property='figure'),
     Output(component_id='catnat_type', component_property='figure')],
    [Input(component_id='slct_years', component_property='value'),
    Input(component_id='slct_catnat', component_property='value')]
)

def page_3(option_slctds,catnat_select):
    dff2 = df_catnat.copy()
    dff2 = dff2[dff2["Année"] == option_slctds]

    fig_cat_annee = px.bar(catnat_annee,title='Nombre de catastrophes naturelles par année',x='Année',y='nombre_de_catnat')

    fig_map=px.choropleth(dff2,title='Nombre de catastrophes naturelles chaque année',locations='id',geojson=counties,color='nb_catnat',scope='europe')
    fig_map.update_geos(fitbounds="locations",visible=False)

    dff3 = typeYears.copy()
    dff3 = dff3[dff3["Type_de_catnat"] == catnat_select]

    fig_type = px.bar(dff3,title='Nombre de catastrophes par type', x='Année', y='Nombre_catnat')


    return fig_cat_annee,fig_map, fig_type

#callback 4e tab
@app.callback(
    [Output(component_id='temperature_month_year', component_property='figure'),
    Output(component_id='catnat_month_year', component_property='figure')],
    [Input(component_id='top-row-graphs4', component_property='children')]
)

def page_4(year_select):
    

    fig_temp_year = px.bar(temperature_by_month_annee,x='Date',y='Température_Moy_(°C)',title='Histogramme des température par mois pour chaque année',facet_col="Année",facet_col_wrap=3,
    labels={'Date': 'Mois', 'Température_Moy_(°C)':'Température' })

    fig_cat_year = px.bar(catnat_month_annee,x='Date',y='Nombre_catnat',title='Histogramme des catastrophes naturelles par mois pour chaque année',facet_col="Année",facet_col_wrap=3,
    labels={'Date': 'Mois', 'Nombre_catnat':'Nombre de catastrophe' })

    return fig_temp_year,fig_cat_year

# Callback qui permet la construction et le fonctionnement des tab quandd on clique
@app.callback(
    [Output("app-content", "children")],
    [Input("app-tabs", "value")]
)
def render_tab_content(tab_switch):
    if tab_switch == "tab1":
        return build_tab_1()
    elif tab_switch == "tab2":
        return build_tab_2()
    elif tab_switch == "tab3":
        return build_tab_3()
    elif tab_switch == "tab4":
        return build_tab_4()
    
# --------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)





















