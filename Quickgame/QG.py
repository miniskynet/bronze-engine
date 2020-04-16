def quick():
       
#importing modules 
    import random
    import mysql.connector
    
#creating variables
    score = 0
    ques_lst = []

#take players name
    name = input("Enter your name: ")

#create a 'for' loop to run the program 5 times
    for i in range(5):
        
    
    #using the random module to produce random integers and assigning them to two variables namely 'num1' and 'num2'
       num1 = random.randint(0,11)
       num2 = random.randint(0,11)
    
    #assigning the sum of 'num1' and 'num2' to variable called 'ans'
       ans = num1 + num2

    #taking user input and converting the input into an integer and assigning it to variable 'ques'
       ques = int(input(str(num1)+' + '+str(num2)+' = '))

    #if the user input value is equal to 'ans'(real sum of the two random values), increase the 'score'
    #variables' value by '1' and append 'the player answer, the real answer' and whether the player answer is
    #correct or incorrect
       if ques == ans:
           score += 1
           ques_lst.append(str(num1)+' + '+str(num2)+' = '+str(ques)+'(answer is '+str(ans)+')[Correct]')
       else:
           ques_lst.append(str(num1)+' + '+str(num2)+' = '+str(ques)+'(answer is '+str(ans)+')[Incorrect]')
    print()
    print('      Game results')
    print('Your name is ',name)
    print('You played quickgame')
    print('You answered 5 questions')
    for val in range(5):
        print(ques_lst[val])

    print('Your score is',int((score/5)*100),'%')

    #storing the local host details to a dictionary
    Dict = {"host":"localhost",
            "database":"game_db",
            "user":"root",
            "password":""}

    #store the connection to local host in a variable called 'db'
    db = mysql.connector.connect(**Dict)

    #create a cursor object for traversal through the database
    cursor = db.cursor()
    
    #inserting values into table
    sql = "INSERT INTO quickgame (name,correct,Total_questions,percentage) VALUES (%s,%s,%s,%s)"
    plyr = (name,score,"5",int((score/5)*100))
    cursor.execute(sql,plyr)

    #commiting the changes to the database
    db.commit()

    #closing the database
    db.close
    

     
    
    
