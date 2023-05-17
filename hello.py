# Ask user for their name
name = input("What's your name?").strip().title()

# Remove whitespace from str and capitalize user's name, can add above
    # name = name.strip().title()

# Split user name into first name and last name
first, last = name.split(" ")

# Say hello to user
print (f"hello, {first}")
