list_Of_Commands = ["Help", "Hello", "Campus","Security", "Coffee/Tea", "Food", "map"]
list_Check = ["Command","Command", "command", "commands", "COMMANDS"]

# def allCommands(s):
#     txt ="The following are a list of Commands:\n"
#     for k in list_Check:
#         if (k in s):
#             for i in list_Of_Commands:
#                 txt+= "- "+"\"" + i+ "\"" +"\n"
#             break
#     return txt


def commandHandler(string):
    text = ""
    if any(x in string for x in list_Check):
        text = """This is the list of commands:
    Help
    Hello
    Mental Health
    Security
    Food
    Map
    Quote
    Memes
    Fact
    Interesting
    Learn
    Deep
    Comic
    How do i get from <room> to <room>
                                        
    Abbreviations for room:
    "eng": "Engineering",
    "es": "Earth Science",
    "ms": "Math Science",
    "sa": "Science A",
    "sb": "Science B",
    "ss": "Social Sciences",
    "bs": "Biological Sciences",
    "st": "Science Theaters",
    "education": "Education Classroom Block",
    "pf": "Professional Faculties",
    "ad": "Administration",
    "admin": "Administration",
    "social science": "Social Sciences",
    "ccit": "CCIT",
    "ict": "ICT",
    "ms": "Math Sciences
    
    EX: How do i get from eng 201 to ict 102"""
    return text

# print(allCommands("commands"))
# print(commandHandler("commands"))

