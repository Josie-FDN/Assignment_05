#---------------------------------------------------------------# 
# Title: Lab05_A_starter.py 
# Desc: Lab05-A starter script for Assignment 05 
# Change Log: (Who, When, What) 
# DBiesinger, 2030-Jan-01, Created File 
#jgnanaraj, 2021-feb-14, Modified File 
#---------------------------------------------------------------# 

  
# Declare variabls  

  
strChoice = '' # User input  
lstTbl = []  # list of lists to hold data  
lstAdd = {} 
lstRow = []  # list of data row  
strFileName = 'CDInventory.txt'  # data storage file  
objFile = None  # file object  
cd_inventory = []    

# Get user Input  
print('Write or Read file data.')  

while True:  

    print('\n[a] add data to list\n[w] to write data to file\n[r] to read data from file')  
    print('[d] display data\n[exit] to quit')  

    strChoice = input('a, w, r, d, or exit: ').lower()  # convert choice to lower case at time of input  
    print('\n')  

    if strChoice == 'exit':  
        break  

    if strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'  

        # Add data to list in memory  
          print("\n Add CD Details:")    
          print('\n')    

          title = input("CD Title:")       
          name = input("Artist Name:")  

          new_cd = [title, name]  
          cd_inventory.append(new_cd)  

           
    elif strChoice == 'w':  
        # List to File  
        dataFile = open('CDInventory.txt', 'a')       

        # TODO add code here to write from in-memory list to file  
        for cd in cd_inventory:  
         dataFile.write("{}, {}\n".format(cd[0], cd[1]))  
        dataFile.close()   
        pass  

     
    elif strChoice == 'r':  

        # TODO read the file line by line into in-memory list. 
        dataFile = open('CDInventory.txt', 'r') 
        pass  

     
    elif strChoice == 'd':  

        # Display data  
        print("\n Display CD Details added")    
        print('\n')    
        print('Artist', 'Title') 

        for cd in cd_inventory:  
         print("{}, {}".format(cd[0], cd[1]))   
        pass  

  
    else:  
        print('Please choose either a, w, r or exit!') 