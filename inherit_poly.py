# class User:
#     def __init__(self,username):
#         self.username=username

#     def log(self):
#         print(f"{self.username} is login ")

# class Admin(User):
#     def delets(self,user):
#         print(f"{self.username} delete user {user} ")

# ad=Admin("shivaraj")
# ad.log()
# ad.delets("homba")


# poly marphisam

# class notification:
#     def send(self):
#         print("send notifcation ")

# class Mail(notification):
#     def send(self):
#         print("mail send")

# class Sms(notification):
#     def send(self):
#         print("sent sms")

# notify=[Mail(),Sms()]
# for i in notify:
#     i.send()


# #inheritence

# class Vechel:
#     def start(self):
#         print("vechel start ")
# class Bick(Vechel):
#     def raid(self):
#         print("bick is redy to ride ")

# car=Bick()
# car.start()
# car.raid()


##poly marphisam

class Shape:
    def calculate_aria(self):
        print("caluclate aria")
class Circle(Shape):
    def __init__(self,radios):
        self.radios=radios
        
    def calculate_aria(self):
        return 3.14159 * self.radios**2
    
class Rectangle(Shape):
    def __init__(self,width,hight):
        self.width=width
        self.hight=hight
    def calculate_aria(self):
        return self.width * self.hight
    
shape=[
    Circle(88),
    Rectangle(67,99),
    Circle(89),
    Rectangle(99,77)

]
for i in shape:
    print(f"aria : {i.calculate_aria():}")


