#suma de números positivos

num = [5, 10, -50, 70, -6, -5, -8]
t = 0
for n in num:
    if n < 0:
        continue
    
    t = t + n

print("Total: ", t)