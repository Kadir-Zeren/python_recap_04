num1 = 25
num2 = float(num1)
print(type(num2))

best ='Clarusway'
best[2]
best[2:]

fruit = 'Orange'
print( 'Word: ', fruit)
print('First letter: ', fruit[0])
print('Second letter:', fruit[1])
print("3rd to 5th letters:", fruit[2:5])
print("Letter all after 3rd:", fruit[2:])

text = 'Clarusway'
text[3]
text[4:7]
text[6:]
text[0:6]
text[: 6]

city = 'Phoenix'
print(city[1:])# starts from index 1 to the end
print (city[ :6])# starts from zero to 5th index
print(city[ :: 2]) # starts from zero to end by 2 step
print(city[1 :: 2])# starts from index 1 to the end by 2 step
print(city[-3:])# starts from index -3 to the end
print(city[ ::- 1]) # negative step starts from the end to zero

text = 'Clarusway'
text[1:8]
text[1:8:2]
text[1 :: 3]
text[: : 2]
text[5:1]
text[5:1 :- 1] 
text[5:1 :- 2]
text[ ::- 1]

'python candir' [2:10:2]

text= 'kayak'
text == text[ ::- 1]
yeni_text = 'abcdef'
yeni_text == yeni_text[ ::- 1]
yeni_text[ ::- 1]
text = 'Clarusway'
text[8]
text[-1]
text [8] == text[-1]

animal = "hippopotamus"
print(animal[1:])
print(animal [ :6])
print(animal[ :: 2])
print(animal[1:7:2])
print(animal[-3:])
print(animal[ ::- 1])

text
text[-3 ::- 1]

vegetable = "Tomato"
print('length of the word', vegetable, 'is :', len(vegetable))

'a' + 'b'

text
text[:4] + text[-3:]
text[ : 5] + "k" + text[-3:]
text[ : 5]
text[ : 5] + 'k'
text[ : 5] + 'k' + text[-3:]
text[ : 5] + 'k' + text[6:]
len(text)
text

text[0]+text[len(text)//2] + text[-1]
len(text)
len(text)/2
len(text)//2
text

ilk = text[0]
ilk

son = text[-1] 
son

orta = len(text)//2
orta

ilk+text[orta]+son

orta = text[len(text)//2]
orta

ilk + orta + son

text

print(text, 'kelimesinin uzunlugu', len(text), 'harften olusur')

str_one = 'upper'
str_two = 'case'
str_comb = str_one + str_two
print('upper' + 'case' )
print(str_one + str_two)
print(str_comb)

str_one = 'upper'
str_two = 3 * 'upper'
str_comb = str_one * 3
print(str_two)
print(str_comb)
print(* str_one)

5 * 3
'abc' * 3

print(text)
print(*text)
print(3*'upper', sep='----- >')
print(3*'upper', sep='----->')

string_1 = 'I am angry ... '
string_2 = '1453'
' joseph@clarusway.com' # Do not use variable

string_1 = 'I am angry ... '
print(* string_1)
string_2 = '1453'
print(* string_2)
'joseph@clarusway.com'# Do not use variable
print(* 'joseph@clarusway.com')

str_one = 'upper'
str_one += 'case'
print(str_one)
str_one += 'letter'
print(str_one)
str_one += 'end'
print(str_one)

a = 5
a = a + 1
a

a += 1
a

name = 'Yasin'
print('Merhaba, %s' % name)

name = 'Yasin'
age = 43
meslek = 'Content Creator'

print('Merhaba, ismin %s yasin %d meslegin ise % s' % (name, age, meslek))

name = 'Yasin'
age = 43.5
meslek = 'Content Creator'
print( 'Merhaba, ismin %s yasin %f meslegin ise % s' % (name, age, meslek))

name = 'Yasin'
age = 43
meslek = 'Content Creator'
'Merhaba, ismin {} yasin {} meslegin ise {}'.format(name, age, meslek)

fruit = 'Orange'
vegetable = 'Tomato'
amount = 4
print('The amount of {} we bought is {} pounds' . format(fruit, amount))

name = 'All'
age = 43
meslek = 'Content Creator'

'Merhaba, ismin {} ,yasin {} meslegin ise {}'.format(name, age, meslek)
'Merhaba, ismin {} yasin {} meslegin ise {}'.format(name, age, meslek)
'Merhaba, ismin {2} yasin {0} meslegin ise {1}' .format(age, meslek, name)
'Merhaba, ismin {a} yasin {b} meslegin ise {c}' . format (b = age, c =meslek, a = name)
'Merhaba, ismin {} , yasin {} meslegin ise {}' .format(name, age, meslek)

print('{state} is the most {adjective} state of the {country}'.format(state='California',country='USA', adjective='crowded' ))

'Merhaba, ismin {} ,yasin {b} meslegin ise {c}' . format(name, b = age, c = meslek)
'Merhaba, ismin {} ,yasin {b} meslegin ise {c}' . format(name, c = meslek, b = age)
taban = 6
yukseklik = 4
'burada hesaplama gosterecegim {}' .format(taban*yukseklik/2)

print( '{0} is the most {adjective} state of the {country}'.format('California',country='USA',adjective='crowded'))

print("{}-{}-{}".format("12", "Feb", "Feb"))
print("{no}-{month}-{month}".format(no="12", month="Feb"))

print("{6} {5} {0} {1} {3} {4} {2}". format("a new", "job", "months", "in", 6, "have started", "I will"))

phrase = '{2} {3} {1} {0}'.format('circumstances','in all','generosity','wins')
print(phrase)

name = 'Ali'
age = 43
meslek = 'Content Creator'
f'merhaba benim adim {name} yasim {age} meslegim {meslek}'
print(f'merhaba benim adim {name} yasim {age} meslegim {meslek}')
print('Merhaba, ismin {} , yasin {b} meslegin ise {c}' . format(name, c = meslek, b = age))

print(f'merhaba benim adim {name} yasim {age} meslegim {meslek}','Merhaba, ismin {} ,yasin {b} meslegin ise {c}'.format(name,b=age,c=meslek)) 

fruit = 'Orange'
vegetable = 'Tomato'
amount = 6
output = f"The amount of {fruit} and {vegetable} we bought are totally {amount} pounds"
print(output)

f'burada hespalama yapiyor {taban*yukseklik/2}'

sample = f"{2 ** 3}"
print(sample)

name = "MARIAM"

my_name = 'MARIAM'
output = f"My name is {my_name. capitalize()}"
print(output)

print(F'My name is {name.capitalize()}')

f'saga hizalama {name:>20}'
f'saga hizalama {name:<20}'
f'saga hizalama {name:^20}'
f'saga hizalama {name:*^20}'

name = "Joseph"
job = "teachers"
domain = "Data Science"
message = (
f"Hi {name}. "
f"You are one of the {job} "
f"in the {domain} section."
)
print(message)

name = "Joseph"
job = "teachers"
domain = "Data Science"
message = f"Hi {name}. " \
f"You are one of the {job} " \
f"in the {domain} section."
print(message)

name = "Susan"
age = "young"
gender = "lady"
school = "CLRWY IT university"

name = "Susan"
age = "young"
gender = 'lady'
school = "CLRWY IT university"
output = (
f"{name} is a {age} "
f"{gender} and she is a student "
f"at the {school}. "
)
print (output)

'abcd'
print('abcd')