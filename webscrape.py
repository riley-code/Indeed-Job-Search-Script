import requests
from bs4 import BeautifulSoup

inp = input('How many pages would you like to query? ')

new_inp = int(inp) * 10

jobList = list()
jobLocation = list()
pageList = list()
jobdict = {}
count = 0
frequency = {}


n = range(0,250,10)
for x in n:
    pageList.append(x)

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61'}
    url = f'https://www.indeed.com/jobs?q&l=28012&radius=15&start={page}&vjk=f1d808a4828d01d8'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

c = extract(int(new_inp))

def transform(soup):
    divs = soup.find_all('span', title=True)
    loc = soup.find_all('div', class_ = 'companyLocation')

    for areas in loc:
        new_areas_1 = str(areas)
        new_areas_2 = new_areas_1.split(",")
        new_areas_3 = new_areas_2[0]
        jobLocation.append(new_areas_3[29:])

    for items in divs:
        jobList.append(items['title'])

    for key in jobList:
        for value in jobLocation:
            jobdict[key] = value
            jobLocation.remove(value)
            break

transform(c)

def poplocation(jobdict):

    for x in jobdict.values():
        if x not in frequency:
            frequency[x] = 1
        elif x in frequency.keys():
            frequency[x] = frequency[x] + 1

poplocation(jobdict)

with open('JobSearchResults.txt', 'w') as results:
    results.write(str(jobdict))
    results.write(str(frequency))