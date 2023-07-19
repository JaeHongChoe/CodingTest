import sys

num = int(input())
grid =2 
for _ in range(num):
    grid = (grid * 2)-1
print(grid * grid)
