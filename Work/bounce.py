# bounce.py
#
# Exercise 1.5

height_start = 500
ratio = 3/5
bounce = 10

for i in range(bounce):
    height_update = height_start * ratio
    height_start = height_update
    print(i, round(height_update, 4))

print(f'the bounce is {bounce} and ratio is {ratio}')