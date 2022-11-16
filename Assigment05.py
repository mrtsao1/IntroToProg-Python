'''
Title: Assignment 05
Description: Working with Dictionaries and Files
             When the program starts, load each "row" of data
             in "ToDoToDoList.txt" into a python Dictionary.
             Add the each dictionary "row" to a python list "table"
Change Log: (Who, When, What)
MTsao, 2022-11-11, Created File
MTsao, 2022-11-13, Completed Load Data (Step #1), Print Menu (Step #2), Exit Program (Step #7)
MTsao, 2022-11-14, Completed Show Current Data (Step #3), Add item (Step #4)
MTsao, 2022-11-14, Completed Remove item (Step #5), Completed Save Data to File (Step #6)
'''

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add COMMENTS Here
strFile = open(objFile, "r")
for row in strFile:
    lstRow = row.split(",")  # returns a list
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
strFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for objRow in lstTable:
            print(objRow)
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("State the task: ")                   # prompt user for task
        strPriority = input("State the Priority level: ")     # prompt user for priority level
        newItem = {"Task": strTask, "Priority": strPriority}  # organize inputs into dictionary items
        lstTable.append(newItem)                              # add task/priority to existing list
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strFindTerm = input("What task do you want to delete?: ")  # prompt user for task to delete
        boolMatch = False  # create a bool to track status of search for task to delete
        for objRow in lstTable:
            if objRow['Task'] == strFindTerm:                          # task to delete was found
                lstTable.remove(objRow)                                # delete task/priority from list
                print("Deleted task \"", strFindTerm, "\" from list")  # notify user of status
                boolMatch = True
        if not boolMatch:  # task to delete was NOT found, notify user of status
            print("Unable to delete task. \"", strFindTerm, "\" was not found.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoToDoList.txt", "w")  # create/open output file
        for objRow in lstTable:                  # write data to output file
            objFile.write(objRow["Task"] + ',' + objRow["Priority"] + '\n')
        objFile.close()                          # close output file
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("Press the enter key to exit.")
        break  # and Exit the program
