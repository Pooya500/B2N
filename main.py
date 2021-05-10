import requests
from bs4 import BeautifulSoup as bs

long_link = input("Enter your link : ")


def b2n(long_link):
    try:
        url = 'https://b2n.ir/create.php'
        params = {'url': long_link}
        r = requests.get(url, params=params)
        soup = bs(r.content, features="lxml")
        final = soup.findAll('div', attrs={'class': 'url_box'})
        final = final[0].find("input")
        final = final['value']
        return final

    except:
        error = "Something went wrong."
        return error


print(b2n(long_link))
