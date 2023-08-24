import math
def gen_prime1(x=2):
    while True:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                break

        else:
            yield x
        x += 1


%%time
i = gen_prime1(10000)
for c in range(10):
    print(next(i), end=" ")
print("")
