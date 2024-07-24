# Bubble sort
def custom_sort(data):
    data = list(data.items())
    for n in range(len(data) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if int(data[i][0]) > int(data[i + 1][0]):
                swapped = True
                data[i], data[i + 1] = data[i + 1], data[i]
        if not swapped:
            continue
    return dict(data)