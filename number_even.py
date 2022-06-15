#A four-digit integer is given. Find the number of even digits in it.
var_int=2438
#Create a variable "var_int" and assign it a four-digit integer value.
a = var_int%10
b = var_int//10%10
c = var_int//100%10
d = var_int//1000%10
print((d+1)%2+(b+1)%2+(c+1)%2+(a+1)%2)
#Print the number of even digits in the variable "var_int".