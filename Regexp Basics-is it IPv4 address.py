import re
def ipv4_address(address):
    ret = ""
    if re.match('[0-9.]',address):
        for n in address.split("."):
            if int(n) >=0 and int(n) <= 255:
                ret += n     
    return ret != None

ipv4_address("10.256.30+40")