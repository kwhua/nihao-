import random
import string

code = ""
for x in range(6):
    num = string.digits
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    x = random.choice(num+lower+upper)
    code = code + str(x)
print(code)

