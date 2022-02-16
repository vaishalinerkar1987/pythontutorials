count = 1
while count <= 5:
    print(count)
    count += 1

    #while True:
       # stuff = input("String to be capitalize [type q to quit]: ")
        #if stuff == "q":
           # break
       # print(stuff.capitalize())

##while True:
    #value = input("Integer , please[type q to quit]: ")
    #if value == "q":      # q for quit
     #   break
      #  number = int(value)
       # if number % 2 == 0:            # for even number
        #    continue
         #   print(number, "squared is", number*number)

            ## Iterate with for and in

    word = "vaishali"
    #offset = 0
    #while offset <= len(word):
       #     print(word[offset])
     #       offset += 1


## most phonics way
    for letter in word:
                print(letter)

name = "Hitansh"
for letter in name:
    print(letter)

# cancel with the break
# in for in loop we can use break for some letters

name = "vaishali"
for letter in name:
    if letter == "h":  # it will break the name from letter h. will egt the output before h means vais
     break
    print(letter)

word = "india"
for letter in word:
    if letter == "d":
     break
print(letter)  ## break will break the word from letter d so will get answer in

### anything in a range wit for in loop
for x in range(0,5):
    print(x)

    for x in range(2 , -1,-1):
        print(x)
###  or
        list(range(0,5))
        print(list(range(0,5)))  ### it will give range between 0 to 5

        list(range(0,11,2))
        print(list(range(0,11,2)))   ## it will gives range between 0 to 11


########### exercise 6(2 nd exp)
    guess_me = 7
    number = 1

while   True:
if start < guess_me:
            print("to low")
elif number == guess_me:
            print("found it!")

elif number > guess_me:
        print("opps")
break
number+=1

