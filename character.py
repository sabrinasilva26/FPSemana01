character1 = str(input("What is your character name? "))
hpch1=int(input("Health points? "))
lvlch1=int(input("Level? "))
character2 = str(input("What is your character name? "))
hpch2=int(input("Health points? "))
lvlch2=int(input("Level? "))
character3 = str(input("What is your character name? "))
hpch3=int(input("Health points? "))
lvlch3=int(input("Level? "))


print(character1)
print(hpch1)
print(lvlch1)
print(character2)
print(hpch2)
print(lvlch2)
print(character3)
print(hpch3)
print(lvlch3)

array=[
    [character1,(hpch1,lvlch1)],
    [character2,(hpch2,lvlch2)],
    [character3,(hpch3,lvlch3)]
]

print(array)

def arrumação_characterlvl(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j][1][1]<array[j+1][1][1]:
                array[j],array[j+1] = array[j+1], array[j]
arrumação_characterlvl(array)

for i in array:
    print(i[0])