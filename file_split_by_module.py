# class User:
#     def __init__(self, name):
#         self.name = name
#     def say_hi(self):
#         print("hi {0}".format(self.name))
        
# class AdminUser(User):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#     def say_hello(self):
#         print("hello {0} ({1})".format(self.name, self.age))
#     def say_hi(self):
#         print("[admin] hi {0}".format(self.name))
#上がmoduleに記載されている

# import user ＃user.pyを読み込む
# from user import AdminUser # user.pyからAdminUserクラスのみ読み込む
from user import AdminUser,  User #複数のクラスを指定して読み込むにはカンマ区切りで指定する

# bob = user.AdminUser("bob", 23)
bob = AdminUser("bob", 23)
tom = User("tom")

print(bob.name)
bob.say_hi()
bob.say_hello()

# .ipynbだとmoduleの読み込みに一手間必要
