import requests
import  urllib3
import  bs4

url = "https://en.wikinews.org/wiki/Main_Page"
extracted_urls = []
req = requests.get(url)
resp = req.text
soup = bs4.BeautifulSoup(resp , 'html.parser')

for link in soup.find_all("a"):
    link = str(link.get('href'))
    if link.startswith("https://en."):
        print(f"{link} link is internal link")
    else:
        print(f"{link} link is External link")



