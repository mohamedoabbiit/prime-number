num_input=int(input("Enter and positive number to check is its prime numebr: "))
#an positive number > than 1 wich has no faqctor except 1 and the number itself is called a prime numer
#2,3,5,7 are prime number because they dont have any factor for exmaple 4 = 2*2 so 4 is not a prime number 
# Check the factor of number 

if num_input>1: # first make sure num is greater than 1
#cehck for factor from 2 to the number provided num    
    for fact in range(2,num_input):
        if num_input%fact==0:
            print(num_input,"is not a prime number")
            break
    else:
        print(num_input,"is not a prime number") 
         
else:
    print(num_input,"is not a prime number")         
