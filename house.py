name = input("what's your name?")

# similar to switch for other languages
match name:
    case "Harry" | "Hermione" | "Ron": # similar to "or"
        print ("Griffindor")
    case "Draco":
        print ("Slytherin")
    case _: # catch all, similar to else
        print ("Who?")