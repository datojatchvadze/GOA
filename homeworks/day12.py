#hw1==creating list of my name and surname and then counting vowels in it
full_name = ['d','a','t','o','j','a','t','c','h','v','a','d','z','e']
x = 0
y = 0
while(x < len(full_name)):
    if x == 'a' or 'e' or 'i' or 'o' or 'u': 
        y = y + 1
        x = x + 1
       
print(y)
#hw2==first three element of the list are names,last three are surnames of myself and parents.then printing names with correct surnames
family_name = ['dato','devi','xatuna','jatchvadze','jatchvadze','gvaberidze']
print(family_name[0] + family_name[3])
print(family_name[1] + family_name[4])
print(family_name[2] + family_name[5])
    



