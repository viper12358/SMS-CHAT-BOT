import re

room = {
    "st":"Science Theater", 
    "ms":"Math Science",
    "sb":"Science B",
    "sa":"Science A",
    "ict":"Information Communication Technology",
    "ss":"Social Science",
    "en":"Engineering",
    "es":"Earth Science",
    "bs":"Bio Science",
    "cha":"Craigie Hall Block A",
    "chb":"Craigie Hall Block B",
    "chc":"Craigie Hall Block C",
    "chd":"Craigie Hall Block D",
    "che":"Craigie Hall Block E",
    "ad":"Administration Building",
    "ecb":"Education Classroom Block",
    "et":"Education Tower",
    "sh":"Scurfield Hall",
    "ena":"Engineering Block A",
    "enb":"Engineering Block B",
    "enc":"Engineering Block C",
    "end":"Engineering Block D",
    "ene":"Engineering Block E",
    "enf":"Engineering Block F",
    "eng":"Engineering Block G",
    "pf":"Professional Faculty"
    }


# command = ["building", "classroom", "room", "Building", "Classroom", "Room", "How", "how", "get", "Get", "what", "What"]


def splitNumberAndChar(s):
    return list(filter(None, re.split(r'(\d+)', s)))


def stringMapping(string):
    result = ""
    response = ""
    try:
        response = string.lower()    
        response = response.replace(" ","")
        response = splitNumberAndChar(response)
        # print(response)
        floor = response[1][0]
        for key in room:
            if response[0] == key and int(floor) > 0:
                result = room[key] + " Room " + response[1] + " Floor number " + floor
            elif response[0] == key and int(floor) == 0:
                result = room[key] + " Room " + response[1] + " Ground Floor"
    except:
        result = "No such room exist!"
    
    return result


def main():
    # print("Gimme a room")
    # print(stringMapping(str(room)))
    print(stringMapping("heheh"))
    print(stringMapping("ST148"))
    print(stringMapping("st 148"))
    print(stringMapping("eng 201"))
    # print(stringMapping("ENA 203"))
    # print(stringMapping("MS 189"))
    # print(stringMapping("CHD01"))
    # print(stringMapping("fuckyou"))

main()
