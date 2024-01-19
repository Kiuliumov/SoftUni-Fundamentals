number = int(input())
electrons = 0
array_of_shells = []
while number > 0:
    electrons += 1
    shell = 2 * electrons ** 2
    if number >= shell:
        array_of_shells.append(shell)
        number -= shell
    else:
        array_of_shells.append(number)
        number = 0
print(array_of_shells)