table_blue = ["b", "l", "u", "e"]
table_clues = ["c", "l", "u", "e", "s"]
# create the matrix with 0 values
words_table = [[0 for i in range(len(table_clues))] for i in range(len(table_blue))]

# rows
for i in range(0, len(table_blue)):
    # columns
    for j in range(0, len(table_clues)):
        if table_clues[j] == table_blue[i]:
            words_table[i][j] = words_table[i - 1][j - 1] + 1
        else:
            words_table[i][j] = max(words_table[i - 1][j], words_table[i][j - 1])

for i in words_table:
    print(i)
