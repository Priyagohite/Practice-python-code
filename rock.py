print("Rock, paper, scissor :")
user1=int(input("user_1-choose rock,paper and scissor:"))
user2=int(input("user_2-choose rock, paper and scissor:"))
print("rock=1")
print("paper=2")
print("scissor=3")
if(user1==user2):
    print("both are same! play again:")
elif(user1==1 and user2==2):
    print("win user2")
elif(user1==1 and user2==3):
    print("win user1")
elif(user1==2 and user2==1):
    print("win user1")
elif(user1==2 and user2==3):
    print("win user2")
elif(user1==3 and user2==1):
    print("win user2")
elif(user1==3 and user2==2):
    print("win user1")
else:
    print("Invalid choice: ")
     
