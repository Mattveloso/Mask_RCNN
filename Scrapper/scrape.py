import requests
from bs4 import BeautifulSoup
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs

def download(url, pathname):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # get the file name
    filename = os.path.join(pathname, url.split("/")[-3]+url.split("/")[-2]+url.split("/")[-1])
    filename = filename.split("?")[0]
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))

# %%

#Roadbikes from decathlon.com.br
# URLS=[
# 'https://www.decathlon.com.br/bicicleta-de-estrada-triban-100-btwin/p',
# 'https://www.decathlon.com.br/bicicleta-triban-rc100/p',
# 'https://www.decathlon.com.br/bicicleta-infantil-de-estrada-aro-650-triban-100/p',
# 'https://www.decathlon.com.br/bicicleta-de-estrada-triban-rc120/p',
# 'https://www.decathlon.com.br/bicicleta-feminina-de-estrada-triban/p',
# 'https://www.decathlon.com.br/bicicleta-estrada-ultra-af900/p',
# 'https://www.decathlon.com.br/bicicleta-de-estrada-triban-rc500/p',
# 'https://www.decathlon.com.br/bicicleta-de-estrada-triban-rc520/p',
# 'https://www.decathlon.com.br/bicicleta-de-estrada-triban-540-cinza-e-preto/p'
# ]

#URL = 'https://www.decathlon.com.br/bicicleta-de-estrada-triban-100-btwin/p'

#Kids_bikes decathlon.com.br
# URLS =[
# # 'https://www.decathlon.com.br/bicicleta-infantil-aro-20--b-twin-original-500-14826/p',
# # 'https://www.decathlon.com.br/bicicleta-infantil-de-equilibrio-aro-12-btwin-runride-100-verde/p',
# # 'https://www.decathlon.com.br/bicicleta-infantil-aro-14-robot-btwin/p',
# # 'https://www.decathlon.com.br/bicicleta-infantil-equilibrio-run-ride-btwin/p',
# # 'https://www.decathlon.com.br/bicicleta-infantil-aro-16-btwin-astronaute/p',
# # 'https://www.decathlon.com.br/bicicleta-infantil-aro-14-unicornio-btwin/p',
# # 'https://www.decathlon.com.br/bicicleta-infantil-de-equilibrio-aro-12-btwin-runride-500-laranja/p',
# # 'https://www.decathlon.com.br/-bicicleta-infantil-aro-20--rockrider-st500-/p',
# # 'https://www.decathlon.com.br/bicicleta-infantil-aro-24--rockrider-st500/p',
# # 'https://www.decathlon.com.br/bicicleta-infantil-aro-20-rockrider-st120-feminina/p',
# # 'https://www.decathlon.com.br/--btwin-rr-500-branca/p',
# # 'https://www.decathlon.com.br/bicicleta-infantil-aro-14-btwin-mini-monsters/p'
# 'https://www.decathlon.com.br/--btwin-rr-500-branca/p',
# 'https://www.decathlon.com.br/bicicleta-infantil-aro-14-btwin-mini-monsters/p',
# 'https://www.decathlon.com.br/bicicleta-infantil-de-equilibrio-aro-12-btwin-runride-500-rosa/p',
# 'https://www.decathlon.com.br/bicicleta-infantil-aro-20-racing-boy-btwin/p',
# 'https://www.decathlon.com.br/bicicleta-infantil-aro-16-doctor-girl-btwin/p',
# 'https://www.decathlon.com.br/bicicleta-infantil-aro-16-jack-pirabike-btwin/p',
# 'https://www.decathlon.com.br/rockrider-st900-vermelho-24-br0000286/p',
# 'https://www.decathlon.com.br/bicicleta-infantil-aro-20--rockrider-st120-masculina/p',
# 'https://www.decathlon.com.br/bicicleta-infantil-aro-24--poply-500/p',
# 'https://www.decathlon.com.br/monster-truck/p',
# 'https://www.decathlon.com.br/bicicleta-infantil-aro-16-btwin-exotic-princess/p',
# 'https://www.decathlon.com.br/bicicleta-infantil-aro-20-mistigirl-btwin/p'
# ]

#MountainBikes decathlon.com.br
# URLS=[
# 'https://www.decathlon.com.br/rr-st-500-grey/p',
# 'https://www.decathlon.com.br/bicicleta-para-mountain-bike-rockrider-st-120/p',
# 'https://www.decathlon.com.br/--st-120-purple-w/p',
# 'https://www.decathlon.com.br/--btwin-rr-st-120-blue/p',
# 'https://www.decathlon.com.br/bicicleta-aro-29-para-mountain-bike-rockrider-st540/p',
# 'https://www.decathlon.com.br/bicicleta-aro-29-para-mountain-bike-rockrider-st520/p',
# 'https://www.decathlon.com.br/bicicleta-mountain-bike-aro-26-rockrider-340-btwin-10862/p',
# 'https://www.decathlon.com.br/bicicleta-feminina-para-mountain-bike-rockrider-340/p',
# 'https://www.decathlon.com.br/bicicleta-aro-29--para-mountain-bike-rockrider-st900-15832/p',
# 'https://www.decathlon.com.br/bicicleta-btt-xc-100-s-29--12v-preto-e-vermelho/p',
# 'https://www.decathlon.com.br/xc-100-s-29--rr/p',
# 'https://www.decathlon.com.br/xc-500-29--rr/p'
# ]

#UrbanBikes decathlon.com.br
# URLS=[
# 'https://www.decathlon.com.br/bicicleta-feminina-lazer-aro-26-caloi-400/p',
# 'https://www.decathlon.com.br/bicicleta-masculina-city-tour-sport/p',
# 'https://www.decathlon.com.br/bicicleta-lazer-aro-26-caloi-400/p',
# 'https://www.decathlon.com.br/bicicleta-feminina-mountain-bike-aro-26-rockrider-300-btwin/p',
# 'https://www.decathlon.com.br/bicicleta-lazer-aro-26-caloi-rouge/p',
# 'https://www.decathlon.com.br/bicicleta-mountain-bike-aro-26-rockrider-300-btwin/p',
# 'https://www.decathlon.com.br/bicicleta-mountain-bike-lazer-aro-26-rockrider-100-btwin/p',
# 'https://www.decathlon.com.br/bicicleta-de-cidade-aro-28-elops-classica-520-btwin/p',
# 'https://www.decathlon.com.br/bicicleta-de-cidade-elops-520-quadro-baixo-vermelho/p',
# 'https://www.decathlon.com.br/bicicleta-masculina-riverside-520/p',
# 'https://www.decathlon.com.br/bicicleta-dobravel-tilt-500/p',
# 'https://www.decathlon.com.br/bicicleta-de-cidade-aro-700-hoprider-100/p',
# 'https://www.decathlon.com.br/bicicleta-feminina-riverside-520/p',
# 'https://www.decathlon.com.br/bicicleta-eletrica-caloi-easy-rider-e-vibe/p',
# 'https://decathlonpro.vteximg.com.br/arquivos/ids/2202461-150-150/folding-bike-tilt-100-black-unique1.jpg?v=636739846010300000',
# 'https://decathlonpro.vteximg.com.br/arquivos/ids/2016317-150-150/--caloi-city-tour-feminina-sport-m1.jpg?v=636645117832600000'
# ]

for URL in URLS:
    page=requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    # results = soup.find_all(id='image')
    # for result in results:
    #     link = result.find('a',class_='image-zoom')['href']
    #     print(link)
    pics = soup.find_all(id='botaoZoom')
    Bikes =[]
    for pic in pics:
        link = pic['zoom']
        #Bikes.append(link)
        download(link,'UrbanBikes') #change folder name here

# %%
#decathlon.de -----------------------------------------------------------------------
#Roadbikes
# source media="(min-width: 1080px)" srcset="https://contents.mediadecathlon.com/p1624689/k$ab0380ec93d95c5bba69a370f6dfe93a/sq/Rennrad+Ultra+900+CF+105+11+fach+schwarz.jpg?f=1000x1000" type="image/jpeg"/>
# URLS=[
# 'https://www.decathlon.de/p/rennrad-ultra-900-cf-105-11-fach/_/R-p-301046',
# 'https://www.decathlon.de/p/rennrad-triban-rc-100/_/R-p-305831',
# 'https://www.decathlon.de/p/rennrad-ultra-920-cf-ultegra-11-fach/_/R-p-301058',
# 'https://www.decathlon.de/p/rennrad-ultra-920-cf-ultegra-11-fach/_/R-p-301058',
# 'https://www.decathlon.de/p/rennrad-triban-rc500-scheibenbremse/_/R-p-301728',
# 'https://www.decathlon.de/p/rennrad-triban-rc520-scheibenbremse/_/R-p-301734',
# 'https://www.decathlon.de/p/rennrad-triban-rc-520-gravel/_/R-p-302303',
# 'https://www.decathlon.de/p/rennrad-damen-ultra-rcr-cf-105/_/R-p-304896',
# 'https://www.decathlon.de/p/rennrad-triban-rc520-flatbar-scheibenbremse/_/R-p-307286',
# 'https://www.decathlon.de/p/rennrad-damen-ultra-rcr-af-tiagra/_/R-p-304895',
# 'https://www.decathlon.de/p/rennrad-ultra-920-cf-potenza-11-fach-blau/_/R-p-308757',
# 'https://www.decathlon.de/p/rennrad-van-rysel-edr-af-ultegra/_/R-p-311959',
# 'https://www.decathlon.de/p/rennrad-ultra-940-cf-ultegra-di2/_/R-p-300789',
# 'https://www.decathlon.de/p/rennrad-edr-af-105-schwarz/_/R-p-305449',
# 'https://www.decathlon.de/p/fitnessrad-triban-regular-fb-damen-wei%C3%9F/_/R-p-168772',
# 'https://www.decathlon.de/p/rennrad-triban-rc-120-scheibenbremse-marineblau-orange/_/R-p-302301',
# 'https://www.decathlon.de/p/rennrad-triban-rc-120-grau/_/R-p-302496',
# 'https://www.decathlon.de/p/rennrad-triban-regular-damen-wei%C3%9F/_/R-p-302724',
# 'https://www.decathlon.de/p/fitnessrad-triban-rc-500-fb-disc-grau-mit-scheibenbremsen/_/R-p-306215',
# 'https://www.decathlon.de/p/rennrad-ultra-940-cf-ultegra-di2/_/R-p-300789'
# ]
#Or use the master url: https://www.decathlon.de/browse/c0-alle-sportarten-a-z/c1-fahrrad-welt/c3-rennrad/_/N-1o6rxbz?Ndrc=1
#Master_url='https://www.decathlon.de/browse/c0-alle-sportarten-a-z/c1-fahrrad-welt/c3-rennrad/_/N-1o6rxbz?Ndrc=1'
#unable to use master URL since it returns only so many results

#MountainBikes.de
URLS=[]
# Master_url = 'https://www.decathlon.de/browse/c0-alle-sportarten-a-z/c1-fahrrad-welt/c3-mountainbike/_/N-obq78x?Ndrc=3'

#UrbanBikes.de
Master_url = 'https://www.decathlon.de/browse/c0-alle-sportarten-a-z/c1-fahrrad-welt/c3-city-bike/_/N-alzbtm'
URLS=[
# 'https://www.decathlon.de/p/city-bike-28-zoll-city-speed-nexus-3-mint/_/R-p-X8541811',
# 'https://www.decathlon.de/p/city-bike-28-zoll-city-speed-nexus-3-dunkelgrau/_/R-p-X8541820',
# 'https://www.decathlon.de/p/e-bike-city-bike-28-zoll-elops-940e-lf-damen-shimano-steps-e6000-grau/_/R-p-100400',
# 'https://www.decathlon.de/p/city-bike-28-zoll-city-speed-nexus-3-wei%C3%9F/_/R-p-X8541810',
# 'https://www.decathlon.de/p/city-bike-28-zoll-elops-900-lf-damen-grau/_/R-p-143431',
# 'https://www.decathlon.de/p/city-bike-28-zoll-elops-920-lf-damen-dunkelgrau/_/R-p-143430',
# 'https://www.decathlon.de/p/e-bike-city-bike-28-elops-900e-lf-tiefer-einstieg/_/R-p-100398',
# 'https://www.decathlon.de/p/city-bike-28-zoll-city-speed-nexus-3-wei%C3%9F/_/R-p-X8541810',
# 'https://www.decathlon.de/p/city-bike-28-zoll-elops-900-lf-damen-grau/_/R-p-143431',
# 'https://www.decathlon.de/p/city-bike-28-zoll-elops-920-lf-damen-dunkelgrau/_/R-p-143430',
# 'https://www.decathlon.de/p/e-bike-city-bike-28-elops-900e-lf-tiefer-einstieg/_/R-p-100398',
# 'https://www.decathlon.de/p/city-bike-28-zoll-elops-520-lf-damen-mint/_/R-p-145734',
# 'https://www.decathlon.de/p/e-bike-city-bike-28-zoll-elops-500e-lf-schwarz/_/R-p-100394',
# 'https://www.decathlon.de/p/city-bike-28-zoll-elops-120-hf-herren-graublau/_/R-p-168865',
# 'https://www.decathlon.de/p/city-bike-28-zoll-hoprider-7-nexus-8/_/R-p-X8381580',
# 'https://www.decathlon.de/p/e-bike-city-bike-28-zoll-elops-920e-lf-damen-brose-drive-t-wei%C3%9F/_/R-p-300604',
'https://www.decathlon.de/p/e-bike-city-bike-28-zoll-elops-920e-hf-herren-brose-drive-t-grun/_/R-p-300606',
'https://www.decathlon.de/p/city-bike-28-zoll-elops-100-lf-damen-schwarz/_/R-p-168862',
'https://www.decathlon.de/p/city-bike-28-zoll-elops-520-hf-herren/_/R-p-168450',
'https://www.decathlon.de/p/e-bike-city-bike-28-elops-900e-lf-tiefer-einstieg/_/R-p-100398',
'https://www.decathlon.de/p/elops-520-mint-gebraucht-sehr-gut/_/R-p-X8613009'
]

#KidsBikes.de
# Master_url = 'https://www.decathlon.de/browse/c0-alle-sportarten-a-z/c1-fahrrad-welt/c3-kinderfahrrad/_/N-1g22ghd'
#
# Masterpage = requests.get(Master_url)
# MasterSoup = BeautifulSoup(Masterpage.content, 'html.parser')
# bicycles = MasterSoup.find_all('a',itemprop='url',class_='dkt-product__title__wrapper')
# for result in bicycles:
#     link = result['href']
#     URLS.append('https://www.decathlon.de/'+link)

# URLS=[
# "https://www.decathlon.de/p/dreirad-be-move-smoby-kinder-blau-grun/_/R-p-X8384791",
# 'https://www.decathlon.de/p/city-bike-poply-540-24-kinder-9-bis-12-jahre/_/R-p-145540https://www.decathlon.de/p/city-bike-poply-540-24-kinder-9-bis-12-jahre/_/R-p-145540',
# 'https://www.decathlon.de/p/trekkingrad-kinderfahrrad-20-zoll-original-500-dunkelblau-pink/_/R-p-168798',
# 'https://www.decathlon.de/p/trekkingrad-kinderfahrrad-24-zoll-original-500/_/R-p-168823',
# 'https://www.decathlon.de/p/trekkingrad-kinderfahrrad-20-zoll-original-100-wei%C3%9F/_/R-p-168794',
# 'https://www.decathlon.de/p/rennrad-26-zoll-triban-500-kinder/_/R-p-300985',
# 'https://www.decathlon.de/p/mountainbike-kinderfahrrad-20-zoll-rockrider-st500-neongelb/_/R-p-300771',
# 'https://www.decathlon.de/p/city-bike-poply-540-24-kinder-9-bis-12-jahre/_/R-p-145540'
# ]

for URL in URLS:
    #URL='https://www.decathlon.de/p/rennrad-ultra-900-cf-105-11-fach/_/R-p-301046?mc=8500479&c=SCHWARZ'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    pics = soup.find_all(type='image/jpeg',media='(min-width: 1080px)') #add id here
    for pic in pics:
        link = pic['srcset'] #add the link name here, probably zoom
        #Bikes.append(link)
        download(link,'bikes/UrbanBikes.de') #CHANGE HERE BEFORE RUNNING DIFFERENT BIKE TYPE

# %% Renaming files
i=439
for file in os.listdir('bikes/UrbanBikes.de/'):
    src = 'bikes/UrbanBikes.de/'+file
    dst = 'bikes/UrbanBikes.de/'+str(i)+'.jpg'
    i+=1
    os.rename(src,dst)
