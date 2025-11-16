def cons(head, tail=None):
    if tail is None:
        return [head]
    else:
        return [head] + tail

def sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum(lst[1:])

l = cons(3, 
        cons(2, 
            cons(1, [])))
print(f'Result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')

print(sum(l))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')