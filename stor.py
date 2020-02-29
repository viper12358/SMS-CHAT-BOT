def storHandler(s):
    s = s.lower()
    if any(word in s for word in ["how", "where"]) and any(word in s for word in ["purchase", "buy", "get"]):
        if any(word in s for word in ["medication", "pills", "prescriptions"]):
            return "You can purchase medication at the Stor located in Mac Hall across Dairy Queen"
        if any(word in s for word in ["pencil", "pen", "calculator", "eraser"]):
            return "You can purchase school supplies at Stor located in Mac Hall across Dairy Queen"
        if any(word in s for word in ["textbook", "notebook", "binder", "note book", "printer", "hoodie", "shirt"]):
            return "You can purchase those at the book stor located on the first floor of Mac Hall. DO YOU NEED DIRECTIONS?"
    return
