print(7 + 3 + 2) #Output 13
x = 10
y = 13
print(x // y) #Outputs 3  (floor division)
print(x % y) #Output 1 (Remainder)

import math

players = 10
teams_of = 3
ways_to_choose = math.comb(players, teams_of)
print(f"Ways to choose a team: {ways_to_choose}") #Output is 120

import math

def triangle_area_heron(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

side1, side2, side3 = 3, 4, 5
area = triangle_area_heron(side1, side2, side3)
print(f"Triangle Area: {area}") # Outputs 6.0
    