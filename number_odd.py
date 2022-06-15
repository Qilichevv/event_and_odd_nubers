#A four-digit integer is given. Find the number of odd digits in it.
var_int=2355
#Create a variable "var_int" and assign it a four-digit integer value.
a =var_int%10
b =var_int//10%10
c =var_int//100%10
d =var_int//1000%10
print(a%2+b%2+c%2+d%2)

#Print the number of odd digits in the variable "var_int".
