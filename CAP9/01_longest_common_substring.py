dp_table_blue = ["b", "l", "u", "e"]
dp_table_clues = ["c", "l", "u", "e", "s"]
dp_table = [[0 for i in range(len(dp_table_clues))] for i in range(len(dp_table_blue))] 

for i in range(0, len(dp_table_blue)):
    for j in range(0, len(dp_table_clues)):
        if dp_table_clues[j] == dp_table_blue[i]:
            dp_table[i][j] = dp_table[i-1][j-1] + 1
        else:
            dp_table[i][j] = 0

for i in dp_table:
    print(i)