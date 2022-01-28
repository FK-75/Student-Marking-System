#here i am importing other modules into my program so i can use the functions stored in them to carry out the tasks i need to in my code.
import matplotlib.pyplot as plt # the matplotlib module allows me to create graphs using the data i find in the CSV file.
import csv #  the csv module allows me to import the CSV into python and allows python to read the CSV so i can extract data from the CSV file to create the graphs.
import numpy as np # the numpy module is used for arrays which allows me to deal with complex functions in python.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
filename = input("enter filename you wish to open ") # the user will be asked which file they want to open. As long as the file is saved in the same directory as the .py file. the file will be opened and read. 
with open(filename + '.csv') as csv_file: # this part of the code takes the user's input of the file name and adds .csv to the end of it so that python and open the file correctly
    csv_reader = csv.reader(csv_file, delimiter=',') # this reads the file and seperates the data using commas as a delimiter.
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    line_count = 0 # this is a variable called line_count which counts the lines in the csv. this will be used later to eliminate the title row from the data.
    data = [] # this is used to create a data set that will store the student information and scores in the format needed. 
    
    for row in csv_reader:
        
        # this part of the code checks the cells in the CSV for rows that are empty.
        for i, x in enumerate(row):
            if len(x)< 1: # if a row is empty then the code will place a 0 in the cell. 
                x = row[i] = 0
        
        if line_count == 0: # here the code will check if the file is reading the first row
            column_headers = row # if so then the first row is saved under column headers as they are the headers. 
            line_count += 1 # this will then add one to the line count so it can move on to the student information such as name, ID, modules and scores. 
            
        else:
            nrow = [] # this creates a new data list named new row. this will store the data once it has been sliced
            
            for i in range(0,10): # this sets the range for the for loop. 0 and 10 are selected because the first row is 0 and the last row is 10. 
                if row[i] == 0: 
                    pass
                # if  a row is equal to 0 then the row is skipped.
                else:
                    if i == 1:
                        nrow.append(row[i]); # = Empty_string + Blank_string
                        # this piece of code is taking the names of the students and is adding them as strings to the list nrow
                    elif i == 0:
                        nrow.append(int(row[i]))
                        # this piece of code is taking the id numbers of the students and is adding them as integers to the list nrow
                    elif row[i] != "":
                        nrow.append((column_headers[i], int(row[i])))
                        # this piece of code is taking the scores of the students in the modules and is adding them as integers to the list nrow. it is then placing the module title stored in column headers and placing it next to them.

            data.append(nrow) # this is storing the information stored in nrow and placing it in the dataset called data.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    # this while loop will run the code and after the user has selected a choice and the code is executed. the user will be asked if they want to run the program again. if they choose y then the code will loop back to the beginning. else if the user selects n then the code will end.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # this section of code will validate the choice input to make sure that the user inputs a valid choice.
    while True:
        try:
            print("Foundation Year Student Information System", end="\n\n") 
            choice = int(input("Please choose one of: \n 1 - display student's marks \n 2 - display scatter plot of module's mark  \n 3 - exit the system\nYour choice? "))
            # this is the choice question that will repeat until a valid choice is selected.
        except ValueError:
            print("\nSorry, choice must be integer\n")
            continue
            # if the user inputs letters instead of integers then an error message will appear and the code will loop back to the question.
        if choice <= 0:
            print("\nSorry, your response must not be negative or 0.\n")
            continue
            # if the user inputs a number equal to or less than 0 then an error message will appear and the code will loop back to the question.
        elif choice > 3:
            print("\nSorry, your response must not be higher than 3.\n")
            # if the user inputs a number greater than 3 then an error message will appear and the code will loop back to the question.
        else:
            #choice made by the user is valid.
            #we're ready to exit the loop.
            break
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if choice == 1:
        # this section of code will validate the student id input to make sure that the user inputs a valid student id.
        while True:
            try:
                student_id = int(input("\nPlease enter student ID number? "))
                # this is the student id question that will repeat until a valid student id is entered.
            except ValueError:
                print("Sorry, please enter integers only")
                continue
                # if the user inputs letters instead of integers then an error message will appear and the code will loop back to the question.
            if student_id <= 0:
                print("Sorry, your response must not be negative or equal to 0.")
                continue
                # if the user inputs a number equal to or less than 0 then an error message will appear and the code will loop back to the question.
            elif student_id == "":
                print("Sorry, Input not valid.")
                continue
                # if the user doesn't enter anything and presses enter then an error message will appear and the code will loop back to the question.
     #-----------------------------------------------------------------------------------------------------------------------#    
            else:
                studentData = 0
                for i in data:
                    if student_id in i: # checks if student id in in the CSV
                        studentData = list(i)# if the student ID exists then create a list of their data
                        
        
                        modules = (studentData[2][0],studentData[3][0],studentData[4][0],studentData[5][0],studentData[6][0],studentData[7][0]) # selects the module title for each module that the student took
                        x_pos = np.arange(len(modules)) # this arranges the data and arranges space between each graph so that it fits.
                        marks = (studentData[2][1],studentData[3][1],studentData[4][1],studentData[5][1],studentData[6][1],studentData[7][1]) # extracts the score associated with the modules
        
   
                        plt.bar(x_pos, marks, label='Marks') # this is the data used to create the bar chart with the x position of the data being the modules and the y being the marks
                        plt.xticks(x_pos, modules)# aligns the 0 at the beginning of the axis.
    
                        plt.xlabel('Modules') # x axis title so the user knows that the x axis is the modules
                        plt.ylabel('Marks') # y axis title so the user knows that the y axis is the marks for the student
                        plt.title('Module Marks for ' + studentData[1]) # this will print a title for the graph that will be followed by the name of the student that matches the ID number entered.
                        plt.legend()
                        plt.show() # this creates and shows the graph
                        break # this will break the loop because the input is valid

                else:
                    print("\nInvalid ID number\n")
                    continue # this will loop back to the student ID question
                # if student ID doesn't exist print Invalid ID number message.

                break # this will loop to the question asking if the user wants to restart the program
            
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    if choice == 2:
        # if the user selects choice 2
        moduleData = []
        result = []
        validation_modules = []
        # here i create the datasets needed for me to store data to carry out the tasks needed.
    #-----------------------------------------------------------------------------------------------------------------------#    
        for i in data:
            for a in i[2:]:
                validation_modules.append(a[0])
                # this code is used to validate the module number entered.
                # this part of the code will list all of the modules that the user can enter for the input to be valid.

        while True:
            try:
                print('')
                moduleNum = input("Please enter a module")
                # this is where the program will ask the user to input the module number 
                if moduleNum not in validation_modules:
                    raise ValueError
                # if the module Number isn't in the list of modules available to choose from. then a ValueError is raise
            except ValueError:
                print("Not a valid Module")
                print("")
                # if a ValueError is raised then an error message stating that it is not a valid module is displayed.
                continue
            else:
                    break

    #-----------------------------------------------------------------------------------------------------------------------#    
        
        for i in data:
            for j in i[2:]:
                if j[0] == moduleNum:
                    moduleData.append(j[1])

        # this section of the code will take all the scores that are related to the module selected by the user and will place them all in a list. 
        
        for element in data: # goes through rows of data
            sums = 0 
            Keep_me = False # this is used to see if the data is modules that will be in the sum or modules that will be in the x axis.
            
            
            for i in element[2:]: # going along row
                if moduleNum != i[0]: # if the module number entered is not the data in the row at the time
                    for number in i:
                        if type(number) == int:
                            sums = sums + number # then it is added to the sum that will be used to calculate the average
                else:
                    Keep_me = True # else the data is the module that was selected and the data is stored seperately and will be used for the x axis

            if Keep_me == True:
                average = sums/5 # this will take the average of the data in the sum and will divide it by 5 because 1 module has been removed so 5 modules remain.
                result.append(average) # this average is calculated and stored in the dataset called result.

                
     #-----------------------------------------------------------------------------------------------------------------------#    


        plt.scatter(moduleData, result) # this is the code used to create the scatter graph using the moduleData (scores from module selected) and result is the y axis (average of other modules)
        plt.xlabel('Modules marks') # this is the x axis title. this is the module marks in the module selected.
        plt.ylabel('Average in other modules') # this is the y axis title. this is the average module mark in the other modules.
        plt.title('Term 1 Module comparison for ' + moduleNum) # this is the overall graph title. "Term 1 Module comparison for" followed by the module number that the user enters
        x = [0,100] # x axis for line of best fit 
        y = [0,100] # y axis for line of best fit
        plt.plot(x,y) # plotting code to plot line of best fit
        plt.show() # this code will generate and display the graph for the module marks.

    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if choice == 3:
        print("End")
        # if the user selects choice 3 then "End" is printed and the loop is broken
        break

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     

    while True:
        # this is the end part of the first While loop
        answer = input('\nRun again? (y/n):')
        print("")
        # the user will be asked if they want to run the code again. the user will answer y (yes) or n (no)
        if answer in ('y', 'n'):
            break
        # if the user doesn't enter y or n then the code will go back to the question in the loop and will print invalid input
        print ('\nInvalid input./n')
    if answer == 'y':
        continue
    # if the user answers y then the code loops to the beginning
    else:
        print ('End')
        break
    #else the code prints "END" and the loop breaks and the program stops.
