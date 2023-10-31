# nested loop
# *
# **
# ***
# ****
# *****

# user input
rows = int(input("Enter no.of rows: "))

# for rows
for i in range(1, rows + 1):
    # for columns
    for j in range(0, i):
        print("*", end=" ")
    # for line change
    print("")
