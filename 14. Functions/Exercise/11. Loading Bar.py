def draw(percentage):
    if percentage == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    else:
        loading = ['[','.','.','.','.','.','.','.','.','.','.',']']
        for i in range(1,percentage//10 + 1):
            loading[i] = '%'
        return f'{percentage}% {"".join(loading)}\nStill loading...'

percent = int(input())
load = draw(percent)
print(load)
