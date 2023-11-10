rows = int(input("Enter Diamond Pattern Rows: "))
input_string = "FORMULAQSOLUTIONS"
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
   
    for k in range(i, 0, -1):
        print(input_string[k - 1], end="")
   
    for l in range(2, i + 1):
        print(input_string[l - 1], end="")
   
    print()

for i in range(rows - 1, 0, -1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
   
    for k in range(i, 0, -1):
        print(input_string[k - 1], end="")
   
    for l in range(2, i + 1):
        print(input_string[l - 1], end="")
   
    print()