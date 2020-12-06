with open('input.in', 'r') as input:
    forms = input.read().split('\n\n')

solution = sum(list(map(lambda x: len(set(x.replace('\n', ''))), forms)))
print(solution)
