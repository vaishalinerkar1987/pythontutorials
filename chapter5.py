a = "hey , 'man'"
print(a)

b= ''' My passion is to learn new things.
        I am very confidant about my work..
        where we can find out english orthopedic doc?
'''
print(b)

print('give',"us",'''some''',"""space""") # oder declare variable a.. oder assign value to variable a.

a = 'give',"us",'''some''',"""space"""
print(a)

print("""'Good morning frau kaupe!'
         said me to my teacher.""")

# create empty string which has no character at all but it perfectly valid
#type empty string on google console ... get the output
#'' o/p is ''
#"" o/p is ''
#'''''' o/p is ''
#"""""" o/p is ''


str(98.6)
print(type(str(98.6))) #oder declare variable and assign value to the variable
a = str(98.6)
print(type(a))   # we can use this using variable
print(a)


######### escape character \n
chapter='I ,\nam, \nvery , \nconfident'
print(chapter)

fruits="I, \nlike, \nbanana, \n apple"
print(fruits)

#escape sequence tab \t(tab) used to allign test
print('\tabc')
print('a\tbc')
print('bc\ta')
print('c\tvaishu')

testimony="\"I did nothing\" he said. \"or that other thing.\""
print(testimony)

character = "\"i like that\" what? \"but will not do that.\""
print(character)

#  literal backslash ... you can type it between both of them.\".......\"
fact = "the world largest duck was 54.2\" by 43.2\" by 3'"
print(fact)


#### back slash bends backwards
speech ='the backslash(\\) bends over backwards to please you.'
print(speech)

speech="the subject(\\)about specch recognition"
print(speech)

info = r'to get \n new line in a normal string.'
print(info)

#### raw string r with escape characetr \n  if we use in sentence it will not print on next line
gender = r'''hello girls and boys.\ntoday will have fun day'''
print(gender)
gender='hello boys and girls.\ntoday will have fun evening'
print(gender)

##literal string or string variable in python by using + operator
s ='if we need to summetion of 5 ' + ' 6'
print(s)

vowels='a'"e"'''i'''"""o"""'u'
print(vowels)

a="Duck."
b=a
c="Grey Duck."
print(a+b+c)
print(a,b,c)

##Duplicate string with * operator
start = 'Na ' *4 + '\n'
print(start)
middle='hey' *3 + '\n'
print(middle)
middle='hey ' *3 + '\n'
print(middle)

####
start ='hey ' *2
print(start)
middle='Na ' *6 + '\n'
print(middle)
end ='hello ' * 9 + '\n'
print(end)
print(start + middle + end)

### get a character with []
letters ='abcdefghijklmnopqrstuvwxyz'
print(letters)
# letters[0] will get the answer a
# letters[2] will get the answer c and so on....
# letters[-2] will get the ans y. start the counting from right last side going to the left side are ..
# 1,2,3,5,6,----1,-2 are offsets

name ="henny"
name.replace("h", "p")
# it will replace the letter "h" instead of "p" on google console..
#slice will include character from the offset start to one before end.
###################### using offset
letters='safdfgf'
print(letters)
print(letters[3])
print(letters[5])
print(letters[:])
print(letters[1:])
print(letters[2:])   ### start from offset 2 value  to f-... end

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters)
letters[3]
print(letters[3])    # offset strts from 0....to end
print(letters[5])
print(letters[:])
print(letters[3:])    # offset strts from 1 to end..you can get the value from offset 3...
print(letters[8:])
print(letters[1:])
print(letters[12:16]) ## it will count from offset 12 ...extract offset 16
print(letters[-3:])  # it will starts from end.. from offset -1 is z,offset -2 is y and so on
print(letters[18:-3])  # use offset between after 18 and before  -3
print(letters[-6:-2])
print(letters[::7])  # from start to end in steps of  7 characters
print(letters[4:20:3]) # offset starts from 4 to 19 by 3.
print(letters[19::4])  # from offset 19 to the end of 4.
print(letters[:21:5])# start to offset 20 by 4
print(letters[-1::-1])
print(letters[::-1])
print(letters[-50:])
print(letters[:70])


# how to calculate the length with string
letters = 'abcdefghijk'
print(len(letters))
letters =''
print(len(letters))
letters ='vaishali, chanchaöl,hitansh'
print(len(letters))
print(letters.split(','))

# split() function which breaks the string into list of the smaller strings based on the some seperator

task ='monday i have an appointment with doc,tuesday need to go to clinic for check up,wednesday need to submit task'
print(task)   # split function a.split()
print(task.split(','))  # split function in parenthesis with arguments
print(task.split()) # split function in parenthesis without argument thats how python knows calling function

#### combine by using join()
## join() function which collpase the list of string into single string

list = ['brother', 'sister', 'task']
list_add=', '.join(list)   ##string.join( list ) it collapse the list of string into single string
## opposite exact to split()
print(list_add)

### replace('', '') form
setup ='electronics is my fav subject'
print(setup.replace('electronics', 'IT'))

setuptools='work is hard'
setuptools.replace('work','life')  ## use replace() function
print(setuptools.replace('work','life'))

setup='a duck goes into a bar'
setup.replace('a','a famous',100)
print(setup.replace('a','a famous', 100))

## strip with strip
# strip() function , if we want to get rid of white space character ('', '\t' , '\n' for empty string, tab bar, and on the next line)
# string variable world contains the string'earth'
# strip() on the both ends. var.lstrip() and  var.rstrip() only from thr right side
world = "   earth    "
world.strip()       ### these are strip function. print on next line in parenthesis
print(world.strip())
world.strip('')
print(world.strip(''))
world.lstrip()
print(world.lstrip())
world.rstrip()        # this is var.rstrip() function
print(world.rstrip())
world.strip('!')  # if the character were not there, nothing will happens
print(world.strip('!'))


blurt='subject......!?'
blurt.strip()
print(blurt.strip())
blurt.strip('.!?')  ### we want to remove this from the stribg so use strip()
print(blurt.strip('.!?'))

blurt='name..?!'
print(blurt)
blurt.strip()
print(blurt.strip())
blurt.strip('..?!')     ### we can remove last character from the  variable using blurt
print(blurt.strip('..?!'))

poem ='rain is a boring everything is boring'
print(poem)
poem[:12]  # copy as usual in print function
print(poem[:12])   ## offset  starts from 0 to 11 and it will end at 12 offset
poem[:9]
print(poem[:9]) ## offset starts from 0 to 8 and end at offset 9

poem[6:]
print(poem[6:])  # offset will start after 6. that means from 9 onwards
poem[10:]
print(poem[10:])

poem[3:7]
print(poem[3:7]) # it gives value between offset 3 to offset 7
poem[9:12]
print(poem[9:12])

### calculate the length
len(poem)
print(len(poem))

# does it start with rain
poem.startswith('rain')           ############## use startwith()
print(poem.startswith('rain'))

### how to end with
poem.endswith('go away')
print(poem.endswith('go away'))

##### you can declare variable word and assign value boring to this word
### find()  and index() we can use for finding offset of the substring... it will count the offset from star postion
word='boring'
poem.find(word)
print(poem.find(word))   ### oder

poem.find('boring')
print(poem.find('boring'))
poem.index('rain')
print(poem.index('is'))

##### rfind() and rindex()  it will count the of the last boring
poem.rfind('boring')
print(poem.rfind('boring'))
poem.rindex('everything')
print(poem.rindex('everything'))

word='duck'
poem.find(word)
print(poem.find(word))   ### oder

poem.find('duck')
print(poem.find('duck'))

#### for index()
#word='duck'
#poem.index(word)   ### it throws error
#print(poem.index(word))


poem.rfind(word)
print(poem.rfind(word))
# how many times this letters rain occures in poem
poem.count('rain')
print(poem.count('rain'))
poem.count('boring')
print(poem.count('boring'))

##### strip means you can remove the character,
# capitalize means first letter of sentence we get in capital.
# title means get all first letter of the word in capital
setup = "i am going to caffee,,."
setup.strip('.')
print(setup.strip(',,.'))
setup.strip('caffee')
print(setup.strip('caffee,,.'))  # it will remove string with the character

setup.capitalize()
print(setup.capitalize())

setup.title()
print(setup.title())

## convert all character into upper case
setup.upper()
print(setup.upper())  ## it gives all letters in capital

# convert all case into lower case
setup.lower()
print(setup.lower())

# swap uppercase and lower case
setup.swapcase()
print(setup.swapcase())

# center string within 30 spaces
setup.center(30)
print(setup.center(30))

# right justify
setup.rjust(30)
print(setup.rjust(30))

#left justify
setup.ljust(30)
print(setup.ljust(30))

'%s' % 24
print('%s' % 24)

'%f' % 2.03
print('%f' % 2.03)

#an integer and literal
'%d%%' % 23
print('%d%%' % 23) # oder

ex='%d%%' % 50
print(ex)

name = 'salman'
dog = 'lila'
weight = 28
'my favourite name is %s'  % name
print('my favourite name is %s'  % name)
'my dog name is %s' % dog
print('my dog name is %s' % dog)
'he is weight %s' % weight
print('he is weight %s' % weight)

thing='wood'
'%s' % thing
print('%s' % thing)
'%15s' % thing
print('%15s' % thing)
## this + sign indicates right allign
'%+12s' % thing
print('%+12s' % thing)
## this - sign indicates left allign
'%-12s' % thing
print('%-12s' % thing)


thing = 84.3
print(thing)
'%f' % thing
print('%f' % thing)



