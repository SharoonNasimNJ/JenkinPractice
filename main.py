def work(a):
    b = a+5
    sum = 0
    for i in range(b):
        for j in range(a):
            sum+=i*j
        sum+=i*sum
    return sum

print(work(4))
print("Sharoon Nasim Hello World!")
