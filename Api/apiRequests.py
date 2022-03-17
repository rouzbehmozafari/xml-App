import requests

# handling special charactars to avoid Errors while reading xml
def encodeXMLText(text):
    text = text.replace("&", "&amp;")
    return text

# fetches xml data from server 
def getJobListings(url):
    response = requests.get(url)
    xmlData = encodeXMLText(response.text)
    return xmlData