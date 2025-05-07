#!/usr/bin/env python3

def admin_login(username, password):
    if (username=="admin" or username=="ADMIN" )and password=="12345":
       return "Access granted"
    else :
       return "Access denied"
    
print(admin_login("admin","12345"))

    #your code here
pass

def hows_the_weather(temperature):
    if temperature < 40 :
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <=65:
        return "It's a little chilly out there!"
    elif temperature >85:
        return "It's too dang hot out there!"
    else :
        return "It's perfect out there!"
    
print(hows_the_weather(50)) 

#     # your code here
#    pass

def fizzbuzz(num):
    if num % 3==0 and num % 5==0:
        return "FizzBuzz"
    elif num % 3==0:
        return "Fizz"
    elif num % 5==0:
        return "Buzz"
    else:
        return num

print(fizzbuzz (15)) 
    # your code here pass

def calculator(operation, num1, num2):
    if operation == '+':
        return num1+num2
    elif operation =='-':
        return num1 -num2
    elif operation =='*':
        return num1 *num2
    elif operation =='/':
        return num1 /num2
    else:
        print("Invalid operation!")
        return None
    
print(calculator("nope",1,2))

    
    # your code here
pass

# dog ="cuddly"
# if dog == "hungry":
#     owner = "refiling food bowl"
# elif dog == 'thirsty':
#     owner = "reffiling water bowl"
# elif dog =="playful"
#     owner ="play tag"
# elif dog == "cuddly"
#     owner = "pet him"
# else : 
#     owner = "bathing"
# def divide (num1,num2):
#     try:
#         quotient = num1/num2
#         print(quotient)
#     except ZeroDivisionError:
#         print("Error: num2 cannot be 0")
#     except TypeError:
#         print("Error:Input must be number")

#     finally: 
#         print("wooooooooi")

# divide(10,2)
# divide(10,0)
# divide("cat",2)
# divide(4,2)