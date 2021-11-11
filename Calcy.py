
# Calcy Project


while True:
    operaters = input("Please Enter (A) addition, (S) Subtraction, (M) Multiplication , (D) Division  :  ")
    a = operaters.lower
    num_1 = int(input("Enter the first number : "))
    num_2 = int(input("Enter the first number : "))
    
    if(a == "a"):
        print(f"The Answer is  : {num_1+num_2} ")
    elif(a == "d"):
        print(f"The Answer is  : {num_1/num_2} ")
    elif(a == "m"):
        print(f"The Answer is  : {num_1*num_2} ")
    elif(a == "s"):
        print(f"The Answer is  : {num_1-num_2} ")
        
