number_of_commands = int(input())
commands = []
start = [0, 0]

for i in range(number_of_commands):
    commands.append(input().lower().split())

for command in commands:
    if command[0] == "восток":
        start[0] += int(command[1])
    elif command[0] == "север":
        start[1] += int(command[1])
    elif command[0] == "запад":
        start[0] -= int(command[1])
    elif command[0] == "юг":
        start[1] -= int(command[1])
    else:
        "Something wrong"

print(start[0], start[1])
