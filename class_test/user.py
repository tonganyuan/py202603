class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def talk(self):
        print(f"my name is {self.name}")
    
    def move(self):
        print(f"{self.name} 走了100步")

user1 = User("zhangsan",18)
user2 = User("李四",24)

user1.talk()
user2.talk()
user1.move()
user2.move()
