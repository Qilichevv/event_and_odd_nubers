#A four-digit integer is given. Find the sum of odd digits in it.
a=4325
#Create a variable "var_int" and assign it a four-digit integer value.
a1=a%10
a2=a//10%10
a3=a//100%10
a4=a//1000%10
#Create a variable "sum_even" and assign it 0.
sum_even=0
#Find the sum of the odd digits in the variable "var_int".
print((a1%2*a1)+(a2%2*a2)+(a3%2*a3)+(a4%2*a4))