

def solve(st):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    replaced = []
    for i in st:
        if i == 'a': 
            replaced.append('b')
        elif i == 'z':
            replaced.append('y')
        else:
            index = alpha.index(i)
            replaced.append(alpha[index-1]) and replaced.append(alpha[index+1])
    results = ["".join(replaced)]
#     print(results)
    for result in results:
        if result == result[::-1]: 
            return True
    return False