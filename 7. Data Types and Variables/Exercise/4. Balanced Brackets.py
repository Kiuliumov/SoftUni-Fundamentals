n = int(input())
stack = []

for _ in range(n):
    line = input()
    for char in line:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack or stack.pop() != '(':
                print("UNBALANCED")
                exit(0)

if stack:
    print("UNBALANCED")
else:
    print("BALANCED")




