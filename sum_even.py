#A four-digit integer is given. Find the sum of even digits in it.
var_int=4934
#Create a variable "var_int" and assign it a four-digit integer value.
var_int1=var_int%10
var_int2=var_int//10%10
var_int3=var_int//100%10
var_int4=var_int//1000%10

#Create a variable "sum_even" and assign it
sum_even=0
#Find the sum of the even digits in the variable "var_int".
sum_even=(var_int1+1)%2*var_int1+(var_int2+1)%2*var_int2+(var_int3+1)%2*var_int3+(var_int4+1)%2*var_int4
print(sum_even)
