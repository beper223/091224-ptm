def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    max_num = max(max(row) for row in triangle)
    max_width = len(str(max_num))
    total_width = (max_width + 1) * (n - 1) + max_width
    with open('pascal_triangle.txt', 'a', encoding='utf-8') as out:
        for row in triangle:
            row_str = " ".join(f"{num:>{max_width}}" for num in row)
            print(row_str.center(total_width),file=out)
    print("Треугольник Паскаля записан в файл 'pascal_triangle.txt'.")

numm = 20
pascal_triangle(numm)