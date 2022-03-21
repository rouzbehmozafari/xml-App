import xml.etree.ElementTree as ET 
from Api.apiRequests import getJobListings
from htmlValueExtractor import htmlValueExtractor
from operatingSys.servieces import importXml

url = 'https://kunden.jobadpartner.de/publisher/api/jobvector_2020/?accessCode=WfxGIuBy' #source web XML address
xmlData = getJobListings(url)

xmlFolderAddress = "xmlFiles/fetchedXml.xml" # the target folder that we have imported our xml response

importXml(xmlFolderAddress,xmlData) #writes the fetched xml to desired address
root = ET.parse(xmlFolderAddress).getroot()

#generating Html files from xml data
htmlValueExtractor(root) 
