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
    filename = os.path.join(pathname, url.split("/")[-1])
    filename = filename.split("?")[0]
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))
#Roadbikes
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

#Kids_bikes
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

#MountainBikes
URLS=[
'https://www.decathlon.com.br/rr-st-500-grey/p',
'https://www.decathlon.com.br/bicicleta-para-mountain-bike-rockrider-st-120/p',
'https://www.decathlon.com.br/--st-120-purple-w/p',
'https://www.decathlon.com.br/--btwin-rr-st-120-blue/p',
'https://www.decathlon.com.br/bicicleta-aro-29-para-mountain-bike-rockrider-st540/p',
'https://www.decathlon.com.br/bicicleta-aro-29-para-mountain-bike-rockrider-st520/p',
'https://www.decathlon.com.br/bicicleta-mountain-bike-aro-26-rockrider-340-btwin-10862/p',
'https://www.decathlon.com.br/bicicleta-feminina-para-mountain-bike-rockrider-340/p',
'https://www.decathlon.com.br/bicicleta-aro-29--para-mountain-bike-rockrider-st900-15832/p',
'https://www.decathlon.com.br/bicicleta-btt-xc-100-s-29--12v-preto-e-vermelho/p',
'https://www.decathlon.com.br/xc-100-s-29--rr/p',
'https://www.decathlon.com.br/xc-500-29--rr/p'
]

#UrbanBikes
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
        download(link,'MountainBikes')

# %% Renaming files
i=58
for file in os.listdir('MountainBikes/'):
    src = 'MountainBikes/'+file
    dst = 'MountainBikes/'+str(i)+'.jpg'
    i+=1
    os.rename(src,dst)
