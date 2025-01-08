'''for i in range(4):
    print("-", end = " ")
    for j in range(4):
        print("#", end = " ")
    print()'''


n_list = [["-", "-", "-", "#", "#"], ["-", "#", "-", "-", "-"],
          ["-", "-", "#", "-", "-"], ["-", "#", "#", "-", "-"],
          ["-", "-", "=", "-", "-"]]

for i in enumerate(n_list):
    print(i, end = " ")
    for j in i:
        print(j, end = " ")
    print()