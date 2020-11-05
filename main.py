from distribuciones import distribuciones



''''''

sum = 0
for i in range(5):
    a = distribuciones["Poisson"](i, 10)
    sum = sum + a.probabilidad()
print(1-sum)

p = distribuciones["Binomial"](1,2,.3)
help(p)