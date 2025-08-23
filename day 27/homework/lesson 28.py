words = ["python", "  hello world  ", "capitalize test", "find method"]
for word in words:
    print("upper():", word.upper())
    print("capitalize():", word.capitalize())
    print("lower():", word.lower())
    print("find('o'):", word.find("o"))
    print("-" * 30)