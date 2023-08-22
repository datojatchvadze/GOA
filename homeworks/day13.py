#hw==printing how many consonant letters are in my name and surname
#first way
x = 'dato jatchvadze'
y = 0
for char in x:
    if char in  'bcdfghjklmnpqrstvwxyz':
        y += 1
print(y)
#second way
full_name = ['d','a','t','o','j','a','t','c','h','v','a','d','z','e']
i = 0
sum_of_consonants = 0
z1 = full_name[i]
while(i < len(full_name)):
    if full_name[i]  == 'b' or full_name[i]  == 'c' or full_name[i] == 'd' or full_name[i]  == 'f' or full_name[i]  == 'g' or full_name[i]  == 'h' or full_name[i]  == 'j' or full_name[i] == 'k' or full_name[i]  == 'l' or full_name[i]  == 'm' or full_name[i]  == 'n'or full_name[i]  == 'p' or full_name[i]  == 'q' or full_name[i]  == 'r' or full_name[i]  == 's' or full_name[i]  == 't' or full_name[i]  == 'v' or full_name[i]  == 'w' or full_name[i]  == 'x' or full_name[i]  == 'y' or full_name[i]  == 'z':
        sum_of_consonants += 1
    i += 1
print(sum_of_consonants)
   