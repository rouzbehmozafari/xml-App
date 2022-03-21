import re
import html as f_html
import dominate
from dominate.tags import *

from operatingSys.servieces import makeHtmlFiles

# to validate the RGB color
_rgbstring = re.compile(r'#[a-fA-F0-9]{6}$')
def isrgbcolor(value):
    return bool(_rgbstring.match(value))


# making HTML nodes from given parameters
def create_page(
    unique_job_id,jobTitle,imageUrl,companyName,locationList,introduction,introductionTitle,responsibilities,responsibilitiesTitle,qualifications,qualificationsTitle,we_offer,we_offerTitle,contact_data,contact_dataTitle,heading_color,applyUrl
):
    doc = dominate.document(title = jobTitle)
    _div = doc.body.add(div(cls="joblisting" , id=unique_job_id))
    if len(imageUrl) > 0:
        _div.add(img(src=imageUrl))
    _div.add(h1(jobTitle))
    _div.add(h2(companyName))
    
    # cities
    citiesAll = ''
    if len(locationList) > 1:
        for city in locationList:
            citiesAll = citiesAll + city + ','
    elif len(locationList) == 1:
        citiesAll = locationList[0]
        _div.add(p(citiesAll))

    # making html contents
    # color
    if isrgbcolor(heading_color):
        doc.head.add(style("h2 {a} color :  {color} {b}".format(color=heading_color,a='{',b='}'))) 
    _divContents = _div.add(div(cls="content_sections"))
    if introductionTitle :
        _divContents.add(h2(introductionTitle))
    _divContents.add(p(introduction))
    if responsibilitiesTitle :
        _divContents.add(h2(responsibilitiesTitle))
    _divContents.add(p(responsibilities))
    if qualificationsTitle :
        _divContents.add(h2(qualificationsTitle))
    _divContents.add(p(qualifications))
    if we_offerTitle :
        _divContents.add(h2(we_offerTitle))
    _divContents.add(p(we_offer))
    if contact_dataTitle :
        _divContents.add(h2(contact_dataTitle))
    _divContents.add(p(contact_data))
    
    # unicode and encode
    _meta = doc.head.add(meta())
    _meta['http-equiv'] = 'Content-Type'
    _meta['content'] = 'text/html; charset=utf-8'
    doc['lang'] = 'de'
    doc = str(doc).replace('nbsp;', ' ').replace('&ndash;', '-').replace('&amp;', '&')
    doc = f_html.unescape(doc)
    
    HtmlFileAddress = "outputs/id_{address}.html".format(address=unique_job_id) #target folder address for output html files

    # writing data in folder 
    makeHtmlFiles(HtmlFileAddress,doc)