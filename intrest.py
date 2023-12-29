# Take principal period and rate of intrest input from user

P = float(input('Enter the principle in INR'))
N = float(input('Enter the number of years'))
R = float(input('Enter the rate of interest p.a'))

## Calculate the simple interest
I = P*R*N/100
 
 ## claculating the total amount 
A= P+I
 
## print above result
print(f'Simple Intrest : {I:.2f} INR')
print(f'Total amount : {A:.2f} INR')