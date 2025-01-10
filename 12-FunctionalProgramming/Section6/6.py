cptlzLast = lambda name: f"{name[0].upper()}, {name[1]}"
array = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]
print(*list(map(cptlzLast, array)), sep="\n")