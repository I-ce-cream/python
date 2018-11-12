def extract_file_name(name):
    #m = re.match(r'(\d+\_)(\w+\.\w+)(\.\w+)',dirty_file_name)
    #for s in m.groups():
    #    if re.match(r'\w+\.\w+',s):
    #        return s
    #return m.group(0)
    name2 = str(reversed(name)) 
    return name[(name.find('_')+1):(-1-(name2.find('_')))]

extract_file_name("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION")