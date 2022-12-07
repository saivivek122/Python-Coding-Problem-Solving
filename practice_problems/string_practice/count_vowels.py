vowel = set("aeiouAEIOU")
string = "python kd123"
print(vowel)
v = 0
c = 0
n = 0
for i in string:
    if i in vowel:
        v += 1
    elif ((i >= 'a' and i <= "z") or (i >= "A" and i <= "Z")):
        c += 1
    if i.isdigit():
        n += 1
print(v, c, n)
