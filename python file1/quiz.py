marks=0
while True:
    
    def exam():
        print('***********************************WELCOME TO THE QUIZ GAME *****************************************\n')
        name=str(input('Enter your name :'))
            
        accepting=input(f'Do you want to play quiz game {name} [YES or NO]:')
        if accepting !='yes':  
            quit()
        marks=0
        print('Who is the owner of Reliance ?\na)Ambani\nb)Dhoni\nc)Kohli\nd)Neetu')
        answer=input('Enter your option :')
        if answer=='a':
            marks=marks+1
            print(f'congratulations you got {marks}')
        else:
                
            print(f'sorry you failed because of you got {marks} marks')
            


    
    # print('***********************************WELCOME TO THE QUIZ GAME *****************************************\n')
    # name=str(input('Enter your name :'))
        
    # accepting=input('Do you want to play quiz game [YES or NO]:')
    # if accepting !='yes' or 'YES':  
    #     quit()
    # from time import sleep
    # for i in range(1,3):
    #     sleep(2)
    #     print(i)
    exam() 
          
        




