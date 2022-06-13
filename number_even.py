#A four-digit integer is given. Find the number of even digits in it.
x=4678
#Create a variable "var_int" and assign it a four-digit integer value.
a = x%10
b = x//10%10
c = x//100%10
d = x//1000%10
print((d+1)%2+(b+1)%2+(c+1)%2+(a+1)%2)
#Print the number of even digits in the variable "var_int".