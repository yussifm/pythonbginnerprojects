# Lets create a madlib (a story-like) game 
# this will teach you how to concatenate strings in python


print("----------------WELCOME TO THE STORY LINE------------------------")
name = input("Your name: ") #name varieble
print("==========================^============================")
story_line_Selecter = input("choose your story line:\n1: Programmer \n2: Normal person \n :")
print("==========================^============================")



# STory line
if(story_line_Selecter == '1'):
    print("You chose to be a programmer ")
    verb1 = input("verb1: ")
    noun = input("a noun: ")
    story_of_programmer = f"  Hello my name is {name}\n  I love to df{verb1},\n\
    I spent more hours on my {noun},"
    print("==================> your story <======================")
    print(story_of_programmer)
    print("==================> your story <======================")

elif(story_line_Selecter =="2"):
    print("You chose to be normal ")
    verb1 = input("verb1: ")
    noun = input("a noun: ")
    story_of_normal = f"  Hello my name is {name}\n  am just a regular being that love {verb1}\n\
    I love spending time with my {noun}"
    print("==================> your story <======================")
    print(story_of_normal)
    print("==================> your story <======================")

else:
    print("come again")
    



