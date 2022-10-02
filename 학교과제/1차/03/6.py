#5자리까지만 나오고 6자리는 버리는 형식을 사용해라 그러고 3.14159가 정확히 나오는 최소 i의 시점을 찾아야된다.
import math

log_pi = math.log(2)

i = 1

while(math.exp(log_pi) < 3.14159):
    log_pi += math.log(4 * i ** 2) - math.log(4 * i ** 2 - 1)
    print(math.exp(log_pi))
    i = i + 1

print(i)