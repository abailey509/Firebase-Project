from firebase import firebase

FBConn = firebase.FirebaseApplication('https://cloud-project-31b31.firebaseio.com/', None)

while True:
    temperature = int(input("What is the temperature? "))

    data_to_upload = {
        'Temp' : temperature
    }

    result = FBConn.post('/MyTestData/', data_to_upload)

    print (result)