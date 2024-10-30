def check_prime(num):
    for i in range (2,num):
        if num%i==0:return False
        

n = int(input("Enter a number to check prime or not : "))
if check_prime(n)==False:
    print(n,'is NOT prime.')
else:
    print(n,'is prime')



