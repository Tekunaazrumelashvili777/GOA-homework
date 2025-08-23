my_list = ["ვაშლი", "ბანანი", "კარამელი", "კატა", "კომბო"]

index = int(input("შეიყვანე რიცხვი: "))

if index >= len(my_list):
    print("გურამი error")
else:
    print(my_list[index])