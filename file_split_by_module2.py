# package

#import mypackage.user2
#bob = mypackage.user2.AdminUser("bob",  23 )

#import mypackage.user2 as mymodule
#bob = mymodule.AdminUser("bob", 23)

from mypackage.user2 import AdminUser
bob = AdminUser("bob", 23)

print(bob.name)
bob.say_hi()
bob.say_hello()
