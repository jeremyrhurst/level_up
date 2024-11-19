'''
Calculate Pi using monte carlo method

area of a circle: pr^2
area of a square: 4r^2

area of circle / area of square

pr^2/4r^2 = p/4

p/4 = no of points inside circle / no of points inside square

p = 4 * no of points inside circle / no of points inside square

0,0 ----------------------0,1
    |                    |
    |                    |
    |                    |
    |                    |
    |                    |
    |                    |
    |---------------------          
   1,0                   1,1

point x,y: x^2 + y^2 <= 1

1 - generate a random x between 0, 1
2 - generate a random y between 0, 1
3 - calculate x^2 + y^2
4 - if x^2 + y^2 <= 1 counter_circle++
5 - counter_square++
6 - go back to 1, n times
7 - after loop in 6 is done, calculate pi = 4 * (counter_circle/counter_square) => 3.141526...


map -> mapping work to workers
reduce -> reducing to a output returning to the mapper
'''

import random
# Calculate pi using the monte carlo method
def calculate_pi(n):
    counter_circle = 0
    counter_square = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            counter_circle += 1
        counter_square += 1
    return 4 * (counter_circle/counter_square)

print(calculate_pi(10000)) 