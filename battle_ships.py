size_rows = int(input())
matrix = []
for row in range(size_rows):
    row_elements = [int(x) for x in input().split()]
    matrix.append(row_elements)
destroyed_ships = 0
commands = input().split()
for command in commands:
    split_command = command.split("-")
    row = int(split_command[0])
    col = int(split_command[1])
    if matrix[row][col] > 0:
        matrix[row][col] -= 1
        if matrix[row][col] == 0:
            destroyed_ships += 1
print(destroyed_ships)
