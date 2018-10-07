def shoelace(v):
    area = 0.
    n = len(v)
    for i in range(n):
        j = (i + 1) % n
        area += v[i][0] * v[j][1]
        area -= v[i][1] * v[j][0]
    area = abs(area) / 2.
    return area


if __name__ == "__main__":
    q = False
    count = 0
    v = []
    while q is False:
        v_ = (float(input('Enter x-component for vertex' + str(count) + ': ')),
              float(input('Enter y-component for vertex' + str(count) + ': ')))
        v.append(v_)
        if count >= 2 and input('Enter q to calculate, or enter to continue: ') == 'q':
            q = True
        count += 1
    print(shoelace(v))
