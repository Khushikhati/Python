rock='''    
      _ _ _ _ _ _ _
_ _ _'      _ _ _ _)
          (_ _ _ _ _)
          (_ _ _ _ _)
          (_ _ _ _)
 _ _ _._ _(_ _ _)
'''
paper='''
      _ _ _ _ _ _ _
_ _ _'      _ _ _ _)_ _ _ _
                _ _ _ _ _ _)
             _ _ _ _ _ _ _ _)
            _ _ _ _ _ _ _ _ _)
_ _ _._ _ _ _ _ _ _ _ _ _ _ )            
'''
scissor='''
     _ _ _ _ _ _ 
_ _ _'     _ _ _)_ _ _
                _ _ _ )
           _ _ _ _ _ _ _)  
           (_ _ _)   
_ _ _._ _(_ _)
'''
import random
game_images=[rock,paper,scissor]
print('enter your choice:')
user_choice=int(input('enter 0 for rock, 1 for paper, 2 for scissor='))
if(user_choice>2 or   user_choice<0):
    print('you have entered an invalid number, so you loss')
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print('computer_choice is=',game_images[computer_choice])
    if(computer_choice==user_choice):
        print('draw')
    elif(user_choice==0 and computer_choice==2):
        print('you win') 
    elif(user_choice==2 and computer_choice==0):
        print('you loss') 
    elif(computer_choice > user_choice): 
        print('you loss')
    elif(user_choice > computer_choice):
        print('you win') 

                                            