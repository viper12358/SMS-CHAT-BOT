def securityHandler(string):
    sms = ""
    security = "security"
    mental = ["mentalhealth", "mental", "stress"]

    if security in string:
        sms = """         Please call 403.220.5333 or 
        come to MacEwan Student Centre, Room 260 
        to get in touch with campus security personnels"""
    elif string.lower() != security:
        ayaya = string.replace(" ", "")
        for x in mental:
            if ayaya.lower() == x:
                sms = """Please call 403-210-9355 to contact our mental health service"""

    return sms

# def securityOptionHandle(num):
#     something = ""
#     if num == "1":
#         print()

#     return something


def main():
    print(securityHandler("mental"))
    print(securityHandler("mental health"))
    print(securityHandler("stress"))
    print(securityHandler("security"))

# main()

