#alguns exercicios de list comprehension tirados do site https://bbookman-github-io.translate.goog/Python-list-comprehension1/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc
#termino o resto depois

lista_a = [1, 2, 3, 4]
lista_b = [1, 2, 3, 4, 5, 6, 7] 

def soma(l1, l2):
    if len(l1) > len(l2):
        return [l1[ind] + l2[ind] for ind, x in enumerate(l2)]
    else:
        return [l1[ind] + l2[ind] for ind, x in enumerate(l1)]
        
print(soma(lista_a, lista_b))

def zipper(l1, l2):
    return [(l1[ind], l2[ind]) for ind, x in enumerate(l1)]
    
print(zipper(['a', 'b', 'c'], ['d', 'e', 'f']))

# Find all of the numbers from 1-1000 that are divisible by 7

def divisiveis_por_sete():
    return [x for x in range(1, 1001) if x % 7 == 0]
    
print(divisiveis_por_sete())

# Find all of the numbers from 1-1000 that have a 3 in them

def acha_tres():
    return [x for x in range(1, 1001) if '3' in str(x)]
    
print(acha_tres())

# Count the number of spaces in a string

def conta_espaco(string):
    return [string.count(' ') for x in string if ]
    
print(conta_espaco(' teste '))
