print(" this program will continue to ask you to enter a number untill you enter -1 then it will calculate the average of the numbers you enterd ! ")
number_input=int(input("please enter a number\n"))
sum=number_input
counter=1
#this is loop that asks the user to input 
# the if condition is important as i noticed while runing the progarm that it takes -1 into calculation if this condition is not there
while number_input!=-1:#while loop takes user input under condition
 number=int(input("please enter a number\n"))

 if number==-1:
  break
 sum=sum+number
 counter+=1
print(sum)    
print("i="+str(i))
average=sum/i
print("the averge of the numbers you entered is "+str(average)+".")
