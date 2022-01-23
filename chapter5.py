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

