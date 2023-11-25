import random
import time
def start():
        atmpt=5
        while atmpt:
            
            user=int(input('enter guss no:'))
            num=random.randint(1,10)                
            if user==num:
               print('you won!')
               break            
            else:
                                        
                print(f"oppsss you have failed! sorry you have {atmpt} left")
                print('try again')
                atmpt-=1 

            if atmpt==0:                   
                time.sleep(2)
                print("sorry you have failed this gome! you lost 5 attempts in gussing")
                
        time.sleep(3)    
        print("*******welecom back to gussing game*******") 
        name=input("enter ur name:")
        time.sleep(2)  
        usr=input(f"do u wanna play back {name}[yes or no]:")
        if usr.lower() !='yes':
           quit()
        time.sleep(2) 
        start()
           
            
start()