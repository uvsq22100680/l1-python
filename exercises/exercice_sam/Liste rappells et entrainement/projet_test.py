solution = list()
for i in range(4):
    solution.append([])
    for j in range(4):
        solution[i].append(hex(i*4+j+1)[2:]) # ??
 # derniers case = "X"
print(solution)