# simple while loop print value from 1 to 5
# assign value 1 to thhe count
count = 1
#while loop compared the value of count and 5
while count <= 5:
 ## inside the loop print the value count
    print(count)
 ## it is incremented by 1 with the statement
    count += 1
 # and so on python goes back to the top of the loop, compares count with 5, count is 2, loop are executed
###



## program second
count = 10
while count <= 16:
       print(count)
       count +=1

count =15
while count >=1:
    print(count)
    count -= 1  ## count from 15 to 1

# cancel with break
while True:
    stuff = input("string is capitalize [type q to quit]: ")
    if stuff == "q":
        break
        print(stuff.capitalize())
#####
while True:
    value = input("Integer, [q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0:
     continue
     print(number, "is squared", number*number)
     ###################----------------###########

     count = 1
     while count <= 7:
         print(count)
         count += 2

         count = 1
         while count <= 6:
             print(count)
             count += 1