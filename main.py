class Calculator: #calculator class
    input1=0
    input2=0
    def __init__(self,input1,input2):
        self.input1=input1
        self.input2=input2

    def adder(self): #addition method
        return str(self.input1+self.input2)

    def substractor(self): #subtraction method
        return str(self.input1-self.input2)

    def multiplier(self): #multiplication method
        return str(self.input1 * self.input2)

    def divider(self): #division method
        return str(self.input1/self.input2)

    def clear(self): #set to 0 method
        return str(0)

input1=input("Please enter the first number: ") #get user input for number
input2=input("\nPlease enter the second number: ") #get user input for second number
calculator = Calculator(int(input1),int(input2)) #instantiate calculator class
print("\nThe addition method of %s and %s is %s" %(input1,input2, calculator.adder())) #print adder method
print("\nThe subtraction method of %s and %s is %s" %(input1,input2, calculator.substractor())) #print subtract method
print("\nThe multiplication method of %s and %s is %s" %(input1,input2, calculator.multiplier())) #print multiply method
print("\nThe division method of %s and %s is %s" %(input1,input2, calculator.divider())) #print divide method
print("\nThe clear method of %s and %s is %s" %(input1,input2, calculator.clear())) #print 0
