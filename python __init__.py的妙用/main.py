print("## normal module ##")
import moduleB
print("-------------------------------------")
print()

print("## package module ##")
import packageA
print("-------------------------------------")
print()

print("## get variable in package ##")
from packageA import x
print(x)
print("-------------------------------------")
print()


print("## get all variable in package ##")
from packageA import *
print(moduleA.y)
print(y)
print("-------------------------------------")
print()


print("## get author and version in package ##")
import packageA
print(packageA.__author__)
print(packageA.__version__)
print("-------------------------------------")
print()



    