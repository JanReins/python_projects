name = input("What's your name? ").strip().title()

#Split user name into firstname and lastname
first, last = name.split(" ")

print(f"hello, {last}")