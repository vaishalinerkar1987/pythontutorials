#60 sec/min * 60 min/hr *24 hr/day

seconds_per_day = 86400
print(seconds_per_day)

print("no comment: it makes the # harmless.")
  # continuation character using back slash \

sum = 0
sum += 1
sum += 2
sum += 3
print(sum)

sum = 1 + \
    2 + \
    3 + \
    4 + \
    5
print(sum)

sum = (1 + 2+ 3+ 3)
print(sum)

########compare with if , elif and else
disaster = True
if disaster:
    print("wow")
else:
    print("eveeee")

fruit = True
if fruit:
    print(fruit) ###### indicates the value of fruit is True
    print("wow")
else:
    print("sauer")

company = False
if company:
    print("good")
else:
    print("not so good")


#### little tiny program using the conditional comparison if and else

#(TT--- spicy  , TF= not so good, FT= try to prepare good, FF=disaster )

curry = False
large =False
if curry:
    if large:
        print("spicy")
    else:
        print("not so good")
else:
    if large:
        print("try to prepare good")
    else:
        print("disaster")


######## if there are more than two possibilities to test then use if, elif,and else

color = "beautifull"

if color == "red":
    print("it is a tomato")
elif color == "green":
    print("it is parrot")
elif color== "yellow":
    print("it is a soup")
else:
    print("color is so :" , color)

    ######### comparison operators are equality, inequality,lessthan,leassthan equal to
    #### logiacal operators are and or not gate

# boolean false, empty list []
# empty tuple ()
# empty  dic  {}
# empty set  is set()

some_list = []  # if we add [1,2,3,"visa"] in a string we will get "there is something in a list"
if some_list:
    print("there is something in a list")
else:
    print("it is empty")

    ### multiple comparison
    # suppose we have letter, want to know weather it is vowel
    # vovels are 'a' ,'e', 'i', 'o','u'

letter = "i"
if letter == 'a' or letter == 'e' or letter == 'i' \
        or letter == 'o' or letter == 'u':
    print(letter , 'is vowel')
else:
    print(letter , 'is not vowel')


#if we need to make comparision like that seperated by or-- you can use python membership operator is in
# use previous example....

vowels = 'aeiou'
letter = 'i'
letter in vowels
if letter in vowels:
    print(letter, 'is a vowel')
else:
    print(letter , 'is not a vowel')

    ################# using set
vowel_set = {'a','e','i','o','u'}
letter = 'u'
letter in vowel_set
if letter in vowel_set:
    print(letter , 'is a vowel')
else:
    print(letter, 'is not a vowel')

####### using list
letter = 'i'
vowel_list = [] # because there is nothing in list[] it is empty
letter in vowel_list
if letter in vowel_list:
        print(letter, "is vowel")
else:
        print(letter, "is not a vowel")
   ######## using tuple
vowel_tuple = () # because there is nothing in parenthesis() it is empty
letter in vowel_tuple
if letter in vowel_tuple:
    print(letter , "is a vowel in tuple")
else:
    print(letter , "is not a vowel in tuple")


    ########
    tweet_limit = 250
    tweet_string ="blah" * 20
    diff = tweet_limit - len(tweet_string)
    if diff >= 0:
        print("besser tweet")
    else:
        print("not so goood")

        #### using walrus expression
        # name := expression
    tweet_limit = 250
    tweet_string = "blah" * 20

    if diff := tweet_limit - len(tweet_string) >= 0:
        print("besser tweet")
    else:
        print("not so goood")