# allow user to input a direction (n, s, e, w)
    # after each move
    # print name and description of players current room
    # print an error if player chooses a move with no room to go to
# user input determines next step in program
# 


# Intro to Python III TK challenge

# Open a Python interpreter and complete the following:
# Define a class that has a class method that references a class attribute when called.
# Do this once using the @classmethod decorator and a second time without using the decorator.
# Reflect on which method you prefer and why.

# @classmethod 
# class Counter:
#     count = 0
#     def __init__(self):
#         Counter.count += 1
#     def exclaim(self):
#         print('im a counter')
#     @classmethod
#     def children(cls):
#         print(f"Counter class has {cls.count} created instances")

# counter_one = Counter()
# counter_two = Counter()
# Counter.children()

# without @classmethod, personally I like this, looks cleaner
# class Counter:
#     count = 0
#     def __init__(self):
#         Counter.count += 25
#     def children():
#         print(f"Counter class has {Counter.count} instances created")

# count1 = Counter()
# count2 = Counter()
# Counter.children()