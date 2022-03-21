# Extracting xml tags to variables:
# ex:
#     jobTitle = 'Python Entwickler '
#     responsibilities = '...'
from functions import create_page


def htmlValueExtractor(root):
    for joblisting in root:
        for i in (joblisting.iter('language')):
            if i.text == 'DE': 
                unique_job_id = joblisting.get('unique_job_id')
                for elem in joblisting.findall('job_data/jobtitle'):
                    jobTitle = elem.text.replace('\n', '')
                for elem in joblisting.findall('job_data/layout_data/images/header'):
                    imageUrl = elem.text
                for elem in joblisting.findall('job_data/company_data/companyname'):
                    companyName = elem.text.replace('\n', '')
                
                # City list
                locationList = []
                for location in joblisting.findall('job_data/joblocations/location'):
                    for cityName in joblisting.findall('job_data/joblocations/location/city'):
                        city = cityName.text
                        city = city.replace(' ', '')
                        city = city.replace('\n', '')

                        if len(joblisting.findall('job_data/joblocations/location/postalcode')) != 0 :
                            for location in location.iter('postalcode'):
                                postalCode = location.text
                                postalCode = postalCode.replace(' ', '')
                                postalCode = postalCode.replace('\n', '')
                                cityAndZip = postalCode +','+ city
                                locationList.append(cityAndZip)
                        else:
                                cityAndZip = city
                                locationList.append(cityAndZip)
                        
                # Contents
                for elem in joblisting.findall('job_data/introduction'):
                    introduction = elem.text
                    introductionTitle = elem.get('title')
                for elem in joblisting.findall('job_data/responsibilities'):
                    responsibilities = elem.text
                    responsibilitiesTitle = elem.get('title')
                for elem in joblisting.findall('job_data/qualifications'):
                    qualifications = elem.text
                    qualificationsTitle = elem.get('title')
                for elem in joblisting.findall('job_data/we_offer'):
                    we_offer = elem.text
                    we_offerTitle = elem.get('title')
                for elem in joblisting.findall('job_data/contact_data'):
                    contact_data = elem.text
                    contact_dataTitle = elem.get('title')
                    
                # extracting color
                heading_color = ''
                for elem in joblisting.findall('job_data/layout_data/colors/heading_color'):
                    heading_color = elem.text.replace('\n', '').replace(' ', '')
                for elem in joblisting.findall('job_data/application_procedure/url'):
                    applyUrl = elem.text
        create_page(
    unique_job_id,jobTitle,imageUrl,companyName,locationList,introduction,introductionTitle,responsibilities,responsibilitiesTitle,qualifications,qualificationsTitle,we_offer,we_offerTitle,contact_data,contact_dataTitle,heading_color,applyUrl
)