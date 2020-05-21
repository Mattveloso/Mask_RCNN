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

URL = 'https://www.decathlon.com.br/bicicleta-de-estrada-triban-100-btwin/p'
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
    download(link,'RoadBike')
