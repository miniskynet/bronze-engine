def cm():
    #importing the random module
    import random
    import mysql.connector

    #create function to print the game results
    def results(name,mode,ques):
        print()
        print('      Game results')
        print('Your name is',name)                            
        print('You played the game on',mode,'mode')
        print('You answered', ques,' questions')

    #storing the local host details to a dictionary
    Dict = {"host":"localhost",
            "database":"game_db",
            "user":"root",
            "password":""}

    #creating variables for score and name
    score = 0
    name = ''
    #creating an empty list to append gameplay results
    ques_lst = []
    #creating a list of operators needed for medium mode
    ops_med = ['+','-']
    #creating a list of operators needed for hard mode
    ops_hard = ['+','-','*']

    #take input for users name
    name = input("Enter your name: ")

    #take users preffered difficulty level
    print('Following input is case sensitive')
    dif = input("Enter preffered difficulty level(Easy/Medium/Hard): ")

    #ask how many questions are needed
    questions = int(input("How many questions do you need? : "))

    #running the program according to preffered difficulty level
    if dif == 'Easy':
        
        #create a loop to ask questions depending on how many questions
        #the player needed
        for i in range(questions):
            #create two variables to store the randomly generated values in range 0 to 10
            num1_e = random.randint(0,11)
            num2_e = random.randint(0,11)

            #store the value of the sum of the two randomly generated values
            #inside the 'ans' variable
            ans = num1_e + num2_e

            #taking user input and converting the input into an integer and assigning it to variable 'ques'
            ques = int(input(str(num1_e) + ' + ' + str(num2_e) + ' = '))

            #if the user input value is equal to 'ans'(real sum of the two random values), increase the 'score'
            #variables' value by '1' and append 'the player answer, the real answer' and that
            #the player answer is correct, to 'ques_lst'
            if ques == ans:
                score += 1
                ques_lst.append(str(num1_e)+' + '+str(num2_e)+' = '+str(ques)+' (answer is ' + str(ans) + ') [Correct]')
                
            #if the user input value does not equal to 'ans'(real sum of the two random values), keep the 'score'
            #variables' value as is and append 'the player answer, the real answer' and that  
            #the players answer is incorrect, to 'ques_lst'    
            else:
                ques_lst.append(str(num1_e)+' + '+str(num2_e)+' = '+str(ques)+' (answer is ' + str(ans) + ') [Incorrect]')
            
        #calling the function
        results(name,dif,questions)
        
        #print each element of 'ques_lst'
        for val in range(questions):
            print(ques_lst[val])

        #print the final score as a percentage
        print('Your score is',int((score/questions)*100),'%')

        #store the connection to local host in a variable called 'db'
        db = mysql.connector.connect(**Dict)

        #create a cursor object for traversal through the database
        cursor = db.cursor()
    
        #inserting values into table
        sql = "INSERT INTO customgame (name,correct,Total_questions,percentage) VALUES (%s,%s,%s,%s)"
        plyr = (name,score,questions,int((score/questions)*100))
        cursor.execute(sql,plyr)

        #commiting the changes to the database
        db.commit()

        #closing the database
        db.close


    if dif == 'Medium':
        #create a loop to ask questions depending on how many questions
        #the player needed
        for i in range(questions):
            #create two variables to generate random values in range 0 to 51
            
            num1_m = random.randint(0,51)
            num2_m = random.randint(0,51)

            #create variable to store random operand out of '+' and '-'
            operator = random.choice(ops_med)

            #if the operator generates the '+' operand
            #store the value of the sum of the two randomly generated values
            #inside the 'ans' variable
            if operator == '+':
                ans = num1_m + num2_m

            #if the operator generates the '-' operand
            #store the value of the subtraction of the two randomly generated values
            #inside the 'ans' variable
            if operator == '-':
                ans = num1_m - num2_m

            #taking user input and converting the input into an integer and assigning it to variable 'ques'
            ques = int(input(str(num1_m) + str(operator) + str(num2_m) + ' = '))

            #if the user input value is equal to 'ans'(real value), increase the 'score'
            #variables' value by '1' and append 'the player answer, the real answer' and that
            #the player answer is correct, to 'ques_lst'
            if ques == ans:
                score += 1
                ques_lst.append(str(num1_m)+ str(operator) +str(num2_m)+' = '+str(ques)+' (answer is ' + str(ans) + ') [Correct]')

            #if the user input value does not equal to 'ans'(real value), keep the 'score'
            #variables' value as is and append 'the player answer, the real answer' and that 
            #the player answer is incorrect, to 'ques_lst'
            else:
                ques_lst.append(str(num1_m)+ str(operator) +str(num2_m)+' = '+str(ques)+' (answer is ' + str(ans) + ') [Incorrect]')

        #calling the function
        results(name,dif,questions)

        #print each element of 'ques_lst'
        for val in range(questions):
            print(ques_lst[val])

        #print the final score as a percentage
        print('Your score is',int((score/questions)*100),'%')

        #store the connection to local host in a variable called 'db'
        db = mysql.connector.connect(**Dict)

        #create a cursor object for traversal through the database
        cursor = db.cursor()
    
        #inserting values into table
        sql = "INSERT INTO customgame (name,correct,Total_questions,percentage) VALUES (%s,%s,%s,%s)"
        plyr = (name,score,questions,int((score/questions)*100))
        cursor.execute(sql,plyr)

        #commiting the changes to the database
        db.commit()

        #closing the database
        db.close


    if dif == 'Hard':
        #create a loop to ask questions depending on how many questions
        #the player needed
        for i in range(questions):
            #create two variables to generate random values in range 0 to 51
            
            num1_h = random.randint(0,101)
            num2_h = random.randint(0,101)

            #create variable to store random operand out of '+','-' and '*'
            operator = random.choice(ops_hard)

            #if the operator generates the '+' operand
            #store the value of the sum of the two randomly generated values
            #inside the 'ans' variable
            if operator == '+':
                ans = num1_h + num2_h

            #if the operator generates the '-' operand
            #store the value of the subtraction of the two randomly generated values
            #inside the 'ans' variable
            if operator == '-':
                ans = num1_h - num2_h
                
            #if the operator generates the '*' operand
            #store the value of the multiplication of the two randomly generated values
            #inside the 'ans' variable
            if operator == '*':
                ans = num1_h * num2_h

            #taking user input and converting the input into an integer and assigning it to variable 'ques'
            ques = int(input(str(num1_h) + str(operator) + str(num2_h) + ' = '))

            #if the user input value is equal to 'ans'(real value), increase the 'score'
            #variables' value by '1' and append 'the player answer, the real answer' and that
            #the player answer is correct, to 'ques_lst'
            if ques == ans:
                score += 1
                ques_lst.append(str(num1_h)+ str(operator) +str(num2_h)+' = '+str(ques)+' (answer is ' + str(ans) + ') [Correct]')

            #if the user input value does not equal to 'ans'(real value), keep the 'score'
            #variables' value as is and append 'the player answer, the real answer' and that 
            #the player answer is incorrect, to 'ques_lst'
            else:
                ques_lst.append(str(num1_h)+ str(operator) +str(num2_h)+' = '+str(ques)+' (answer is ' + str(ans) + ') [Incorrect]')

        #calling the function
        results(name,dif,questions)

        #print each element of 'ques_lst'
        for val in range(questions):
            print(ques_lst[val])

        #print the final score as a percentage
        print('Your score is',int((score/questions)*100),'%')

        #store the connection to local host in a variable called 'db'
        db = mysql.connector.connect(**Dict)

        #create a cursor object for traversal through the database
        cursor = db.cursor()
    
        #inserting values into table
        sql = "INSERT INTO customgame (name,correct,Total_questions,percentage) VALUES (%s,%s,%s,%s)"
        plyr = (name,score,questions,int((score/questions)*100))
        cursor.execute(sql,plyr)

        #commiting the changes to the database
        db.commit()

        #closing the database
        db.close
        

        
                                
                                
        
