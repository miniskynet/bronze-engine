#create variables
q = 0
#create a while loop to run the program as long as the player enters '4' to exit
while q != 4:
    #print the game menu
    print()
    print('          Game Menu')
    print()
    print('1. Quick Game')
    print('2. Custom Game')
    print('3. Display past game details')
    print('4. Exit')
    print()
    
    #take user input for preffered game mode
    option = input("Enter your option: ")
    
    #if users selects the quickgame, import the quickgame module
    if option == '1':
        import Quickgame.QG
        #call the quick function inside the module 
        Quickgame.QG.quick()
        
    #if user selects the customgame, import the customgame module    
    if option == '2':
        import Customgame.custom
        #call the cm function inside the module
        Customgame.custom.cm()

    #if user wants to display past game details
    #import quickgame or customgame modules accordingly
    if option == '3':
        print("Select from the following")
        print("1. Quick game details")
        print("2. Custom game details")
        user = input("Which details would you like to display? : ")
        if user == "1":
            import Pastdetails.QG_db
        if user == "2":
            import Pastdetails.CG_db
    
    #if player enters '4' the loop breaks and the game exits   
    if option == '4':
        q = 4
   
    
