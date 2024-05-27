curso = "  pYThon    "

print(curso.upper())
print(curso.lower())
print(curso.title())
print(curso.strip()+".")
print(curso.rstrip()+".")
print(curso.lstrip()+".")

curso2 = "Python"

print(curso2.center(15,"#"))

curso2 = "Python"
coisa ="Lindo"
test0 = 3.14159
test = {"curso2" : "Python","coisa" : "Lindo"}


print("eu sou %s!" %curso2)
print("eu sou {1} e {0} !".format(curso2,coisa))
print("eu sou {curso2} e {coisa} !".format(curso2=curso2,coisa=coisa))
print("eu sou {curso2} e {coisa} !".format(**test))
print(f"Eu faço curso de {curso2}")
print(f"Eu faço curso de {test0:.2f}")

curso2 = "Python"
print("\n",curso2[0])
print(curso2[:6])
print(curso2[:3])
print(curso2[3:])
print(curso2[1:4])
print(curso2[0:5:2])
print(curso2[::-1])

print(f''' \no curso de {curso2}
          é muito bom
       ''')

curso2 = "Python"
