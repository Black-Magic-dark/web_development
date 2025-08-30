
import random
def game():
    print("you are playing game..")
    score=random.randint(5,50)
    f=open("practicefilequestion/hiscore.txt","r")
    if(hiscore!=""):
        hiscore=int(hiscore)
    else:
        hiscore=0



    print(f"ur score is :{score}")
    if(score>hiscore):

      with open("practicefilequestion/hiscore.txt","w") as f:
          f.write(str(score))   
    return score 
game()
     