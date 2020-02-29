

text_List = ["Hi", "Hello","Hey","hey", "hi", "hello", "Bonjour", "bonjour"]
def greetHandler(a):
    text = ""
    for i in text_List:
        if i in a:
              text= """Welcome to the University of Calgary.\nHow may i help you?\nIf you would like to see all avaliable commands.
Please enter \"Commands\"."""

    return text
# print(greetHandler("Hi, idk what to write man"))
