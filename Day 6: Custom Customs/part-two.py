with open('input.in', 'r') as input:
    forms = input.read().split('\n\n')

forms = [list(map(lambda x: set(x), form.split())) for form in forms]
solution = sum(list(map(lambda x: len(x[0].intersection(*x)), forms)))
print(solution)
