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