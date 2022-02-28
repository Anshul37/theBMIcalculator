from datetime import datetime

now = datetime.now()
def calculator():
    #BMI CALCULATOR
    #BMI is body mass index

    #This welcomes the user and tells the user about what BMI stands for
    #and how it is calculated with its standard formula, and how it will
    #be calculated based on the user's inputs.


    print """
    \tHello, Let us help you calculate your Body Mass Index (BMI).
    \tBMI is a statistical measure of the weight of a person scaled
    \taccording to height, used to estimate if a person is underweight
    \tor overweight. The units of BMI are defined as kg/m2, which is
    \tapproximately equal to 703 X lb/in2.

    \t\t The formula for BMI is: bmi = weight/(height*height)

    \t\t\tBMI ranges are as follow:\n\n
    \t\tUnderweight = < 18.5\n
    \t\tHealthy Weight = 18.5 - 24.9\n
    \t\tOverweight = 25 - 29.5\n
    \t\tObese = 30 and above.

    \t\tNOW LET'S CALCULATE YOURS

    """

    #the following lines takes various inputs from the user.
    #vital datas include weight and height to calculate the BMI
    #other datas collected will be the name and the age of the user
    #The age and name will be important so that in case of future 
    #modification of the program to write to files, it will save each
    #BMI value with the corresponding user's name 
    name = raw_input("Hello, what is your name: ")
    age = int(raw_input("\nHow old are you " + name.title() + ": "))
    weight = float(raw_input("\nPlease enter your weight in kilogram " + name.title() + ": "))
    height = float(raw_input("\nPlease enter your height in metres  " + name.title() + ": "))

    #Here, the user datas entered are displayed to the user.
    #There will be future modification here to enable user
    #check for error in their input and enter again if there
    #exist an error, without having to restart the program, i.e
    #when the program is running

    print ""
    print ""
    print "Ok, " + name.title() + ", you are " + str(age) + " years old."
    print "You are " + str(height) + " metres tall, and you weigh " + str(weight) + " kilograms."

    #The actual BMI is calculated with the lines below


    bmi = weight/(height*height)
    print ""
    print ""
    raw_input("Press Enter to see the BMI calculated based on your inputs")
    print ""
    print ""

    #The display of the BMI is handled by these conditions based 
    #on the calculated value of the BMI and the category it falls.

    if (bmi < 18.5):
        print "Your BMI is " + str(bmi) + ". You are at risk of underweight " + name.title() + "."
    elif (18.5 <= bmi < 19.5):
        print "Your BMI is " + str(bmi) + ". Your weight is healthy " + name.title() + ", but you are close to underweight."
    elif (19.5 <= bmi < 24.5):
        print "Your BMI is " + str(bmi) + ". Your weight is healthy " + name.title() + "."
    elif (24.5 <= bmi < 25):
        print "Your BMI is " + str(bmi) + ". Your weight is healthy " + name.title() + ", but you are close to overweight."
    elif (25 <= bmi < 28.5):
        print "Your BMI is " + str(bmi) + ". You are overweight " + name.title() + ", you should be careful and watch your diet."
    elif (28.5 <= bmi < 30):
        print "Your BMI is " + str(bmi) + ". You are overweight " + name.title() + ", you should be careful and watch your diet because you are near obese."
    else:
        print "Your BMI is " + str(bmi) + ". You are obese, and you risk a lot of health problem " + name.title() + "."
		
	
		
    print ""
    print "\n\nYour BMI was calculated on {}/{}/{} at {}:{}:{}".format(now.day, now.month, now.year, now.hour, now.minute, now.second)
    print ""
    print "Thank you " +  name.title() + " for using this BMI calculator by Sulaiman."

    def writeToFile():
        bmiFile = open("BMI for {} on {}-{}-{} at {}.{}.{}.txt".format(name.title(), now.day, now.month, now.year, now.hour, now.minute, now.second), "wb")
        bmiFile.write("The Following datas were recorded for the patient on {}/{}/{} at {}:{}:{}  \n".format(now.day, now.month, now.year, now.hour, now.minute, now.second))
        bmiFile.write("Patient's name: " + name.title() + "\n  ")
        bmiFile.write("\nPatient's age: " + str(age) + "\n  ")
        bmiFile.write("\nPatient's weight in Kg: " + str(weight) + "\n  ")
        bmiFile.write("\nPatient's height in metres: " + str(height) + "\n  ")
        if (bmi < 18.5):
            bmiFile.write(("Your BMI is " + str(bmi) + ". You are at risk of underweight " + name.title() + "."))
        elif (18.5 <= bmi < 19.5):
            bmiFile.write(("Your BMI is " + str(bmi) + ". Your weight is healthy " + name.title() + ", but you are close to underweight."))
        elif (19.5 <= bmi < 24.5):
            bmiFile.write(("Your BMI is " + str(bmi) + ". Your weight is healthy " + name.title() + "."))
        elif (24.5 <= bmi < 25):
            bmiFile.write(("Your BMI is " + str(bmi) + ". Your weight is healthy " + name.title() + ", but you are close to overweight."))
        elif (25 <= bmi < 28.5):
            bmiFile.write(("Your BMI is " + str(bmi) + ". You are overweight " + name.title() + ", you should be careful and watch your diet."))
        elif (28.5 <= bmi < 30):
            bmiFile.write(("Your BMI is " + str(bmi) + ". You are overweight " + name.title() + ", you should be careful and watch your diet because you are near obese."))
        else:
            bmiFile.write(("Your BMI is " + str(bmi) + ". You are obese, and you risk a lot of health problem " + name.title() + "."))
    
    writeToFile()
    reply = ['yes', 'no']
    reply = raw_input("Do you like this program: ")
    if (reply == "yes"):
        print "Thank you."
    elif (reply == "no"):
        print "We will improve next time."

    print "For contact and enquiries, please call\n07057495929, 08088777456, 07033131921\nEmail: nafsulaiman@gmail.com Thank you."
    answer = raw_input("Would you like to run the program again: ")
    if answer == 'no':
        raw_input("Press the Enter key to exit.")
    else:
        print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
        calculator()
    
calculator()
