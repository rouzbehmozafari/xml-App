#writes the fetched xml to desired address
def importXml(filePath,data):
    with open(filePath,'w',encoding="utf-8") as f:
        # delete the old xml content
        f.seek(0)  # sets  point at the beginning of the file
        f.truncate()  # Clear previous content
        # writing new data
        f.write(data)
        f.close() # Close file
        
def makeHtmlFiles(filePath,data):
    with open(filePath,'a',encoding="utf-8") as f:
        # delete the old xml content
        f.seek(0)  
        f.truncate()  
        # writing new data
        f.write(data)
        f.close() 