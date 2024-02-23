x_coords = range(-30, 30)
y_coords = range(15, -15, -1)
result = []
for y in y_coords:
    row_str = ""
    for x in x_coords:
        if ((x*0.05)**2 + (y*0.1)**2 - 1)**3 - (x*0.05)**2 * (y*0.1)**3 <= 0:
            char = "Love"[(x-y) % 4]
        else:
            char = " "
        row_str += char
    result.append(row_str)
print('\n'.join(result))