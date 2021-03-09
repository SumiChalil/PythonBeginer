##Program to illustrate for loop

blog_posts = ["","Cool programming tricks in Python","","Data sets in Python", "Let's Crack Python"]

for post in blog_posts :
    if post == "":
        continue
    else:
        print(post)

print("------------------------------")

my_String = "This is a String"
for char in my_String:
    print(char)

print("-------------------------------")
for x in range(0,10):
    print(x)

print("-------------------------------")

person = {"Name":"Karen Smith","Age":23,"Gender":"Female"}
for key in person:
    print(key,":",person[key])

print("-------------------------------")

blog_posts = {"Python":["Cool programming tricks in Python","Data sets in Python", "Let's Crack Python"],"Javascript":["Programming in javascrpit","javascript Tutorial"]}

for category in blog_posts:
    print("This is about",category)
    print("-----------------------")
    for post in blog_posts[category]:
        print(post)
