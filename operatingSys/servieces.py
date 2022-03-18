import os

#writes the fetched xml to desired address
def importXml(filePath,data):
    fd = os.open(filePath,os.O_RDWR)
    
    # delete the old xml content
    f = open(filePath, "a") # Create a blank file
    f.seek(0)  # sets  point at the beginning of the file
    f.truncate()  # Clear previous content
    f.close() # Close file
    
    # writing new data
    ret = os.write(fd,data.encode())
    
    # removine empty lines
    with open(filePath) as xmlfile:
        lines = [line for line in xmlfile if line.strip() is not ""]

    with open(filePath, "w") as xmlfile:
        xmlfile.writelines(lines)