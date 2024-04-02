print(" this program will continue to ask you to enter a number untill you enter -1 then it will calculate the average of the numbers you enterd ! ")
number_input=int(input("please enter a number\n"))
sum=number_input
i=1
while number_input!=-1:
 number=int(input("please enter a number\n"))

 if number==-1:
  break
 sum=sum+number
 i+=1
print(sum)    
print("i="+str(i))
average=sum/i
print("the averge of the numbers you entered is "+str(average)+".")
