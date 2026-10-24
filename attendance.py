students=["Dharani","Dharshini","Deepan","Ruthran"]
print(students)
name=input("enter your name:")
name=name.strip().title()
print("you typed :",name)
if name in students:
    print(name,"present")
else:
    print(name,"not found")
