#A four-digit integer is given. Find the number of odd digits in it.
x=2356
#Create a variable "var_int" and assign it a four-digit integer value.
a =x%10
b =x//10%10
c =x//100%10
d =x//1000%10
print(a%2+b%2+c%2+d%2)

#Print the number of odd digits in the variable "var_int".
