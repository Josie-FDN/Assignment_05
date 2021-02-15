#----------------------------------------------------------------------------------#   

# Title: CDInventory.py   

# Desc: Starter Script for Assignment 05  

# Change Log: (Who, When, What)  

# DBiesinger, 2030-Jan-01, Created File  

# jgnanaraj, 2021-Feb-14, Modified File and added requirements   

#-----------------------------------------------------------------------------------#  

# Declare variables


strChoice = '' # User input
tblDict = []  # list of dictionaries to hold data
rowDict = {} # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('\nThe Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()
    
    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # Added the functionality of loading existing data
        tblDict=[]      
        # read the file line by line into in-memory dictionary 
        # keep adding by appending the dictionary to a list
        objFile=open(strFileName,'r')
        for row in objFile:
            lstRow=row.strip().split(',')
            rowDict={'CD ID':int(lstRow[0]), 'CD Title':lstRow[1],'Artist':lstRow[2]}
            tblDict.append(rowDict)
        objFile.close()  
        pass

    if strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        lstRow = [intID, strTitle, strArtist]
        rowDict={'CD ID':intID,'CD Title':strTitle,'Artist':strArtist}
        tblDict.append(rowDict)        
        pass
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID\t   CD Title\t  Artist')
        
        for row in tblDict:
            print(row)
        print('\n')    
        pass    
            
    elif strChoice == 'd':
        entry_Del = int(input('Enter the ID of the entry you want to delete: '))
        
        for row in tblDict:
            if entry_Del == row['CD ID']:
                tblDict.remove(rowDict)
        pass                
    
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile=open(strFileName,'w')
        for row in tblDict:
            strRow=''
            for item in row.values():
                strRow=strRow+str(item)+','
            strRow=strRow[:-1]+'\n'   
            objFile.write(strRow)     
        objFile.close()
        print('CD inventory saved to file.\n')
        pass           
    
    else:
        print('Please choose either l, a, i, d, s or x!')
        