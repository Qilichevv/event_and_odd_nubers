#A four-digit integer is given. Find the sum of odd digits in it.
var_int=4377
#Create a variable "var_int" and assign it a four-digit integer value.
a1=var_int%10
a2=var_int//10%10
a3=var_int//100%10
a4=var_int//1000%10
#Create a variable "sum_even" and assign it 0.
sum_even=0
#Find the sum of the odd digits in the variable "var_int".
print((a1%2*a1)+(a2%2*a2)+(a3%2*a3)+(a4%2*a4))