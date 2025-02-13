from oops_project import chatbook

user1 = chatbook()
print(user1._chatbook__name)   #trick to get encapsulated attributes

# user1.set_id("10")
# print(user1.get_id())

# print(user1.get_user())
# user1.set_user("ajog")
# print(user1.get_user())

# user1 = chatbook()
# print(user1.id)
# user2 = chatbook()
# print(user2.id)
# user3 = chatbook()
# print(user3.id)


chatbook.set_id(10)
print(chatbook.get_id())