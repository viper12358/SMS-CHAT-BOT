pizzas = ["Pizza", "Calzone", "pizza", "calzone"]
desserts = ["Dessert", "Dessert", "Cake", "Candy", "Ice Cream", "icecream"]
burgers = ["Burger", "Fries", "burger", "fries"]
coffees = ["Coffee", "coffee", "Tea", "tea", "Coffee/Tea"]
japan = ["japan"]
chinese = ["chinese"]
vietnames = ["vietnamese"]
korea = ["korean"]
ethnic = ["greek"]


def foodHandler1(food):
    msg = ""
    if food.lower() == "food":
         msg = """Can you tell me what type of food you are looking for? You can choose from:\n 
            Japanese
            Chinese
            Vietnamese
            Korean
            Greek

or Simply say:

            Calzone
            Coffee
            Tea
            Burger
            Fries
            Pizza
            Dessert
            Cake
            Candy
            Ice cream
            """
    return msg

def foodHandler(food):

    text = ""

    for n in coffees:
        if (n.lower() in food):
            text = "For Coffee/Tea visit:\n\nMacHall:\n\nTim Hortons\nCoffee Company\nA&W\nFuel for Gold\nStarbucks\nLa Prep\nBake Chef\n\nTaylor Family Digital Library:\n\nGood Earth Coffeehouse"
    

    for n in burgers:
        if (n.lower() in food):
            text = "For Burgers/Fries visit:\n\nMacHall:\n\nTim Hortons\nA&W\nCarls Jr\nKorean BBQ House\nThe Den\nLounge & Grill"


    for n in pizzas:
        if (n.lower() in food):
            text = "For Pizza/Calzones visit:\n\nMacHall: Vietnamese Bake Chef, Subway, The Den Lounge & Grill\n\nICT: Pizza Konz\n\nYamnuska Hall: Dominos"

    for n in desserts:
        if (n.lower() in food):
            text = "For Desserts visit:\n\nMacHall:\n\nTim Hortons\nBake Chef\nSubway\nThe Den\nLounge & Grill\nSubway\nWetzels Pretzels\nCoffee Company\nDairy Queen\nStor\n\nTaylor Family Digital Library:\n\nGoodearth Coffee House"

    for n in japan:
        if (n.lower() in food):
            text = """For Japanese-styled food:
            MacHall: Sushi Express, Kobe Beef
            Education Classroom Buiding (EDC): Bento Sushi"""

    for n in chinese:
        if (n.lower() in food):
            text = """For Chinese-styled food:
            MacHall: Wok Tok, Oriental Noodles"""

    for n in vietnames:
        if (n.lower() in food):
            text = """For Vietnamese-styled food:
            MacHall: Bake Chef Vietnamese Sub, Oriental Noodle"""

    for n in korea:
        if (n.lower() in food):
            text = """For Korean-styled food:
            MacHall: Korean BBQ"""

    for n in ethnic:
        if (n.lower() in food):
            text = """I can recommend:
            MacHall: OPA-for Greek-Styled food"""


    return text 


