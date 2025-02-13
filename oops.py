# # how to make the method private inside class
# class Example:
#     def __init__(self):
#         self.__private_method()

#     def __private_method(self):
#         print("This is a private method")

#     def public_method(self):
#         self.__private_method()  # Can be accessed within the class

# obj = Example()
# obj.public_method()  # ✅ This works

# obj.__private_method()  # ❌ This will raise an AttributeError


# obj._Example__private_method()  # ✅ Works, but not recommended
# # Use private methods when you don’t want them to be accessed directly.
# # Follow the convention, but remember that Python doesn’t enforce strict private methods like other languages (e.g., Java, C++).





class employee:
    def __init__(self):
        print(id(self))
        self.id=123
        self.designation="SDE"
        self.salary=50000

    def presentation(self,topic):
        print(f"presentation has to be given at this topic {topic}")

    def travel(self,city):
        print(f"employee has to go to {city} city to meet the client ")


sam = employee()
# sam.name = "sam altman"
# sam.travel("bangalore")

print(id(sam))
# print(sam.name)

openai = employee()
print(id(openai))


# print(type(sam))