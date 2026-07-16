a = int(input("enter your age: "))


#If statement no: 1
if(a%2 == 0):
    print("a is even")


#End of IF statement no:1

#If statement no :2
if(a>=18):
    print("you are above the age of concent")
    print("good for you")

elif(a<0):
    print("you are entring an invalid age")

elif(a==0):
    print("you are entring 0 which is not a valide age")

else:
    print("you are below the age of concent")
#end of If statement no :2

print("end of program")