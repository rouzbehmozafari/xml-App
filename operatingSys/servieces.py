#writes the fetched xml to desired address
def importXml(filePath,data):
    with open(filePath,'w') as f:
        # delete the old xml content
        f.seek(0)  # sets  point at the beginning of the file
        f.truncate()  # Clear previous content
        # writing new data
        f.write(data)
        f.close() # Close file
    
    # removine empty lines
    with open(filePath) as xmlfile:
        lines = [line for line in xmlfile if line.strip() is not ""]

    with open(filePath, "w") as xmlfile:
        xmlfile.writelines(lines)