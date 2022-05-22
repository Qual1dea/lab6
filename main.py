import time
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

try:
    np.set_printoptions(precision=3, linewidth=150)
    start = time.time()
    N = int(input('Введите количество строк/столбцов матрицы > 3: '))
    while N < 4:
        N = int(input('Введите количество строк/столбцов матрицы > 3:'))
    K = int(input('Введите число К:'))
    A = np.random.randint(-10, 10, (N, N))        # задаем матрицу A
    F = np.copy(A)                                # задаем матрицу F
    print('Матрицa A:\n', A)
    a, b = 0, 1                       # переменная для подсчета количество нулей в C в нечетных столбцах
    for i in range(N):
        for j in range(N):
            if i < (N // 2) and j > (N // 2 - (N - 1) % 2):
                if j % 2 == 0 and A[i][j] == 0:
                    a += 1
                if i == 0 or i == (N // 2 - 1) or j == (N // 2 + N % 2) or j == (N - 1):
                    b += int(A[i][j])
    print(a, b,)
    if a > b:
        for i in range(N // 2):       # если нулей больше то поменять местами B и C симметрично
            F[i] = F[i][::-1]
    else:                             # иначе B и Е поменять местами несимметрично
        for i in range(N // 2):
            for j in range(N // 2):
                F[i][j], F[i + N // 2 + N % 2][j + N // 2 + N % 2] = F[i + N // 2 + N % 2][j + N // 2 + N % 2], F[i][j]
    print('Матрицa F:\n', F)

    if np.linalg.det(A) > sum(np.diagonal(F)):
        if np.linalg.det(A) == 0:
            print("Матрица А вырожденная, дальнейшие вычисления невозможны")
        else:
            print(f"(A^(-1)A^T–KF^(-1))\n{((np.dot(np.linalg.matrix_power(A, -1), np.transpose(A))) - (np.dot(K, np.linalg.matrix_power(F, -1))))}")
    else:
        if np.linalg.det(F) == 0 or np.linalg.det(np.tril(A)) == 0:
            print("Матрица F или G вырожденная, дальнейшие вычисления невозможны")
        else:
            print(f'Нижняя Треугольная Матрица G:\n{np.tril(A)}')
            print(f"A+G^(-1)-F^(-1))*K\n{(A + np.linalg.inv(np.tril(A)) - np.linalg.inv(F)) * K}")
    print(f"Programm time: {time.time()-start}")

    z = ((np.dot(np.linalg.matrix_power(A, -1), np.transpose(A))) - (np.dot(K, np.linalg.matrix_power(F, -1))))
    x = ((A + np.linalg.inv(np.tril(A)) - np.linalg.inv(F)) * K)
    figure = plt.figure()
    zxc = figure.add_subplot()
    if np.linalg.det(A) > sum(np.diagonal(F)) and np.linalg.det(A) != 0:
        plt.title('plot')        # 1 matplotlib
        plt.xlabel('column number')
        plt.ylabel('row number')
        for j in range(N):
            plt.plot([i for i in range(N)], z[j][::], marker='o')
        plt.grid()
        plt.show()
        plt.title("Bar")         # 2 matplotlib
        plt.xlabel("column number")
        plt.ylabel("row number")
        for i in range(N):
            plt.bar([i for i in range(N)], z[::-1][i], width=1)
        plt.grid()
        plt.show()
        for j in range(N):       # 3 matplotlib
            plt.hist(z[j])
        plt.grid()
        plt.show()
        f, ax = plt.subplots(figsize=(9, 6))                   # 1 seaborn
        sns.heatmap(z, annot=True, linewidths=.5, ax=ax)
        plt.show()
        sns.catplot(data=pd.DataFrame(z), kind="violin")       # 2 seaborn
        plt.show()
        p = sns.lineplot(data=pd.DataFrame(np.transpose(z)))   # 3 seaborn
        p.set_xlabel("column number", fontsize=15)
        p.set_ylabel("value", fontsize=15)
        plt.show()
    elif np.linalg.det(F) != 0 and np.linalg.det(np.tril(A)) != 0:
        plt.title("plot")         # 1 matplotlib
        plt.xlabel("column number")
        plt.ylabel("row number")
        for j in range(N):
            plt.plot([i for i in range(N)], x[j][::], marker='o')
        plt.grid()
        plt.show()
        plt.title("Bar")           # 2 matplotlib
        plt.xlabel("column number")
        plt.ylabel("row number")
        for i in range(N):
            plt.bar([i for i in range(N)], x[::-1][i], width=1)
        plt.grid()
        plt.show()
        for j in range(N):         # 3 matplotlib
            plt.hist(x[j])
        plt.grid()
        plt.show()
        f, ax = plt.subplots(figsize=(9, 6))                   # 1  seaborn
        sns.heatmap(x, annot=True, linewidths=.5, ax=ax)
        plt.show()
        sns.catplot(data=pd.DataFrame(x), kind="violin")       # 2  seaborn
        plt.show()
        p = sns.lineplot(data=pd.DataFrame(np.transpose(x)))   # 3  seaborn
        p.set_xlabel("column number", fontsize=15)
        p.set_ylabel("value", fontsize=15)
        plt.show()
except ValueError:
    print("Введённые данные не число, перезапустите программу!")
