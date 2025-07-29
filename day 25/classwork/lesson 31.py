def grade_status(score):
    if score >= 90:
        print("შესანიშნავი")
    elif score >= 60:
        print("დამაკმაყოფილებელი")
    else:
        print("ჩაჭრილია")
print(grade_status(95))  
print(grade_status(75))  
print(grade_status(40))  
