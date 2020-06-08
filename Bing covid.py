''' 
    FRANCESCO GERRATANA WWW.NEXTECHNICS.COM 2020
    Scraping with python Bing COVID-19.
'''
import urllib 
import requests
import json
from operator import itemgetter
from tabulate import _table_formats, tabulate
import sys
import os
import subprocess

#Afghanistan
#Albania
#Algeria
#Andorra
#Angola
#Anguilla
#Antigua e Barbuda
#Arabia Saudita
#Argentina
#Armenia
#Aruba
#Australia
#Austria
#Azerbaigian
#Bahamas
#Bahrein
#Bangladesh
#Barbados
#Belgio
#Belize
#Benin
#Bermuda
#Bhutan
#Bielorussia
#Bolivia
#Bonaire
#Bosnia ed Erzegovina
#Botswana
#Brasile
#Brunei
#Bulgaria
#Burkina Faso
#Burundi
#Cabo Verde
#Cambogia
#Camerun
#Canada
#Cayman
#Cechia
#Ciad
#Cile
#Cina (continentale)
#Cipro
#Cisgiordania
#Città del Vaticano
#Colombia
#Congo
#Congo (RDC)
#Corea del Sud
#Costa Rica
#Croazia
#Cuba
#Curaçao
#Côte d’Ivoire (Costa d’Avorio)
#Danimarca
#Dominica
#Ecuador
#Egitto
#El Salvador
#Emirati Arabi Uniti
#Eritrea
#Estonia
#Etiopia
#Figi
#Filippine
#Finlandia
#Francia
#Gabon
#Gambia
#Georgia
#Germania
#Ghana
#Giamaica
#Giappone
#Gibilterra
#Gibuti
#Giordania
#Grecia
#Grenada
#Groenlandia
#Guadalupa
#Guam
#Guatemala
#Guernsey
#Guinea
#Guinea Equatoriale
#Guinea-Bissau
#Guyana
#Guyana francese
#Haiti
#Honduras
#India
#Indonesia
#Iran
#Iraq
#Irlanda
#Islanda
#Isola di Man
#Isole Falkland
#Isole Fær Øer
#Isole Marianne settentrionali
#Isole Turks e Caicos
#Isole Vergini Americane
#Isole Vergini Britanniche
#Israele
#Italia
#Jersey
#Kazakistan
#Kenya
#Kirghizistan
#Kosovo
#Kuwait
#Laos
#Lettonia
#Libano
#Liberia
#Libia
#Liechtenstein
#Lituania
#Lussemburgo
#Macedonia del Nord
#Madagascar
#Malawi
#Malaysia
#Maldive
#Mali
#Malta
#Marocco
#Martinica
#Mauritania
#Mauritius
#Mayotte
#Messico
#Moldova
#Monaco
#Mongolia
#Montenegro
#Montserrat
#Mozambico
#Myanmar
#Namibia
#Nepal
#Nicaragua
#Niger
#Nigeria
#Norvegia
#Nuova Caledonia
#Nuova Zelanda
#Oman
#Paesi Bassi
#Pakistan
#Panamá
#Papua Nuova Guinea
#Paraguay
#Perù
#Polinesia francese
#Polonia
#Portogallo
#Portorico
#Qatar
#RAS di Hong Kong
#RAS di Macao
#Regno Unito
#Repubblica Centrafricana
#Repubblica Dominicana
#Riunione
#Romania
#Ruanda
#Russia
#Saba
#Saint Lucia
#Saint Martin
#Saint-Barthélemy
#Saint-Pierre e Miquelon
#San Marino
#Senegal
#Serbia
#Seychelles
#Sierra Leone
#Singapore
#Siria
#Slovacchia
#Slovenia
#Somalia
#Spagna
#Sri Lanka
#Stati Uniti
#Sud Sudan
#Sudafrica
#Sudan
#Suriname
#Svezia
#Svizzera
#São Tomé e Príncipe
#Taiwan
#Tanzania
#Thailandia
#Timor Est
#Togo
#Trinidad e Tobago
#Tunisia
#Turchia
#Ucraina
#Uganda
#Ungheria
#Uruguay
#Uzbekistan
#Vanuatu
#Venezuela
#Vietnam
#Yemen
#Zambia
#Zimbabwe
#eSwatini

#response = requests.get("https://www.bing.com/covid/data")
#url = json.loads(response.text)

def covidscrapy(data,location):

    my_list = []
    totc, totd, totr= 0,0,0
    tc, td, tr= 0,0,0
    totp = 0
    st, sn = "",""
    somma = 0
    totpd = 0
    
    for each in data['areas']:
      if each['displayName'] == location:
        st = each['displayName']
        totc = each['totalConfirmed']
        totd = each['totalDeaths']
        totr = each['totalRecovered']
        totp = (each['totalConfirmed']-(each['totalDeaths']+each['totalRecovered']))
        my_list.append((st,"",totc,totd,totr,totp))
        for x in each['areas']:
           sn = x['displayName']
           tc = x['totalConfirmed']
           td = x['totalDeaths']
           tr = x['totalRecovered']

          #gestisco il valore None
           if tc is not None and td is not None and tr is not None:
                totpd = (tc-(td+tr))#si si si
           elif tc is None and td is not None and tr is not None:
                totpd = (td+tr)#no si si
           elif tc is None and td is None and tr is not None:
                totpd = (td+tr)#no no si
           elif tc is None and td is None and tr is None:
                totpd = (0)#no no no
           elif tc is None and td is not None and tr is None:
                totpd = (td)#no si no
           elif tc is not None and td is not None and tr is None:
                totpd = (tc-(td+0))#si si no
           elif tc is not None and td is None and tr is not None:
                totpd = (tc-(0+tr))#si no si
            
           somma = somma + x['totalConfirmed']
           my_list.append(("",sn,tc,td,tr,totpd))
        
    return sorted(my_list, key=itemgetter(2),reverse=True)


url = json.load(open('bing.json', encoding='utf-8'))

db = covidscrapy(url,input("Enter state: ").title())

header = ['STATO','REGIONE',' TOT CONFERMATI',' TOT DECESSI',' TOT GUARITI','TOT POSITIVI']
print(tabulate(db,header,tablefmt="grid"))

with open("file.txt", "w",encoding='utf-8') as output:
    output.write(str(tabulate(db,header,tablefmt="grid")))

subprocess.call(["cmd", "/k", "start", "", "file.txt"], stderr=subprocess.STDOUT)



