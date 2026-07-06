# #dictionares
l={"shivani":55,"shivaraj":67,"rahul":67,"e2e":77}
for student,marks in l.items():
    print(f"{student}-----{marks}")

stu=["shivarj","karthik","kiran"]
mark=[76,87,65]
stud_mark={}
for i in range(len(stu)):
    stud_mark[stu[i]]=mark[i]
print(stud_mark)

# list comprehesion uppercase
city=["benngalur","mangalue","mydur"]
upper_case=[i.upper() for i in city]
print(upper_case)

data = "apple,banana,mango"
fruits = data.split(",")
print(fruits)