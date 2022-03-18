import xml.etree.ElementTree as ET 
from Api.apiRequests import getJobListings
from operatingSys.servieces import importXml

url = 'http://localhost:8080/' #source XML address


#writes the fetched xml to desired address
xmlFolderAddress = "xmlFiles/fetchedXml.xml" # the target folder that we have imported our xml response




root = ET.parse(xmlFolderAddress).getroot()

for joblisting in root[0:]:
    for i in (joblisting.iter('language')):
        if i.text != 'EN': #this will be changed to not equal to in later commits
            for elem in joblisting.findall('job_data/jobtitle'):
                jobtitle = elem.text
            
            for elem in joblisting.findall('job_data/layout_data/images/header'):
                imageUrl = elem.text
                
            for elem in joblisting.findall('job_data/company_data/companyname'):
                companyName = elem.text
            
            locationList = []
            for location in joblisting.findall('job_data/joblocations/location'):
                for cityName in joblisting.findall('job_data/joblocations/location/city'):
                    city = cityName.text
                    print(city)
                    city = city.replace(' ', '')
                    city = city.replace('\n', '')
                    for location in joblisting.findall('job_data/joblocations/location/city/postalcode'):
                        postalCode = location.text
                        postalCode = postalCode.replace(' ', '')
                        postalCode = postalCode.replace('\n', '')
                        cityAndZip = postalCode + city
                        locationList.append(cityAndZip)
            
            print(
                # imageUrl,jobtitle,companyName,
                locationList)
            # def create_page():
            #     doc = dominate.document(title = jobtitle)
            #     print(doc)
            # create_page()