listOfText_coffee = ["Coffee", "coffee", "Tea", "tea", "Coffee/Tea"]
listofFood = ["Food", "food"]
foodType = ["Burger", "Sub", "Sandwich", "Pizza", "Korean", "Vietnamese", "Chinese", "Japanese"]
def food(x):
    txt = ""
    for k in listOfText_coffee:
        if (k in x):
            txt = "MacHall:\n\nTim Hortons\nCoffee Company\nA&W\nSubWay\nFuel for Gold\nStarbucks\nLa Prep\nBake Chef" + \
                    "\n\nTaylor Family Digital Library:\n\nGood Earth Coffeehouse\n\nICT:\n\nGood Earth Coffeehouse" +\
                    "\n\nScience Theatres:\n\nTaste"

    for f in listofFood:
        if (f in x):
            txt = "There is a food court located at MacHall!! Check it out."

    for q in foodType:
        if (q.lowercase() in x):
            if x.lowercase() == "japanese":
                txt = """Japanese Sushi Express in Machall
                         Bento Sushi in Education Classroom Building"""
    return txt

print(food("Japanese"))
