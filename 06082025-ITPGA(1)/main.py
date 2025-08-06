#main
counter = 0
scoreLst = [None] * 4
print("=======Enter the four test scores below=======")

while(counter != 4):
    usrIn = input("Test score No." + str(counter+1) + " result: ")
    
    #Just in case the user enters something weird
    try:
        scoreLst[counter] = usrIn
    except Exception as e:
        print(f"Error adding score: {e}")
    
    if(counter == 4):
        print("Alright thats it")
    else:
        print("Got it!, next please")
    
    counter = counter + 1

#Get the average and print
average = 0
runningSum = 0
counter = 0 #reset
while(counter != 4):
    try: #Once again, just in case something goes wrong
        temp = int(scoreLst[counter]) #Prevents a data type mismatch ofc
        runningSum = runningSum + temp
    except Exception as e:
        print(f"Error converting score to int at index {counter}: {e}")

    counter = counter + 1
    if(counter == 4): #I know this is dumb but it makes me happy
        print("=======Average=======")

average = runningSum / 4
print(average)
