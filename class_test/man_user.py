from user import User

class Man(User):
    def __init__(self, name, age):
        super().__init__(name, age)


user1 = Man("ddd",18)
user2 = Man("ddddd",24)

user1.talk()
user2.talk()
user1.move()
user2.move()