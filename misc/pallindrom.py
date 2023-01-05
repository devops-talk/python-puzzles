first_string=input("please enter a string: ").strip()
second_string=first_string[::-1]
if first_string==first_string[::-1]:
    print("voila! we have pallindrom string")
else:
    print("keep trying")