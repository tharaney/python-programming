list=[]
Number = int(input("\nPlease Enter the Range Number: "))
 
# Initializing First and Second Values of a Series
i = 0
First_Value = 0
Second_Value = 1
           
# Find & Displaying Fibonacci series
while(i < Number):
           if(i <= 1):
                      Next = i
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           print(Next)
           list.append(Next)
           i = i + 1
print list
