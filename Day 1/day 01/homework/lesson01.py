name= "tekla" 
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "tekla" არის ცვლადისთვის მნიშვნელობა

surname="azrumelashvili"

print(name) 
#პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

name = "tekla" #ეს არის str (string) ტიპის ცვლადი
age = 10 #ეს არის int (integer) მთელი რიცხვი 
height = 145.5     #ეს არის floatt ტიპის ცვლადი (ათწილადი)
#boolean (bool) ტიპის ცვლადი

knows_programming = True #True ან False 
is_ugly = False #snakecase(უბრალოდ წერის სტილი სტანდარტულად)

isUgly = False #ჯავასკრიპტული camelcase 


print(name + " " + surname) 

#სტრინგი არის ბრჭყალები მოქცეული სიმბოლოები               
# print(name + age)

#print(type (age))
#print(type (name))
#print(type (surname))
#print(type (height))
#print(type (knows_programming))

print(name + " " + str(age))  

print("მე ვარ " + name + " ჩემი გვარია " + surname + " მე ვარ " + str(age) + " წლის " + " ჩემი სიმაღლეა " +  str(height) + " სმ " + " ვიცი თუ არა პროგრამირება? "+ str(knows_programming) + " ვარ თუ არა მახინჯი? " + str(is_ugly))