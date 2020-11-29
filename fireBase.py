#Written by Andrew Bailey
#currently I could not get firebase tools to operate correctly but this needs to happen before this program will work
from firebase import firebase

#initalize the firebase connection using custom link
FBConn = firebase.FirebaseApplication('https://cloud-project-31b31.firebaseio.com/', None)
check = True

while (check == True):
    #begin switch case list with table of contents to execute user's desired option
    println("What data would you like to record? \n 1. Temperature \n 2. Humidity \n 3. Precipitation \n 4. Print latest data\n Enter x to close\n )
    option = int(input("enter corresponding number: ")
    

    # case statements for ech availible options
    if (option == 1):

        temperature = int(input("What is the temperature? "))
        TempUpload = {
            'Temp' : temperature
            }
        result = FBConn.post('/MyTestData/', TempUpload)

    elif (option = 2):
        humidity = int(input("What is the humidity? "))
        HumidUpload = {
            'Humid' : humidity
            }
        result = FBConn.post('/MyTestData/', HumidUpload)

    elif (option == 3):
        precip = int(input("How much precipatation has there been? (in cm)"))
        PrecipUpload = {
            'Precip' : precip
            }
        result = FBConn.post('/MyTestData/', PrecipUpload)
    
    elif (option == 4):
        # case option for printing data from server
        print (result)
    
    elif (option == 'x'):
        #case statment to break out of loop if the User is done recording and retrieving data
        check = False

    else:
        println("incorrect input, please try again\n") 
        
