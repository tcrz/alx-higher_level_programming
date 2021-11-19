
def add_tuple(tuple_a=(), tuple_b=()):
    newtuple_a = ''
    newtuple_b = ''

    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        print("both available:" )
        newtuple_a = tuple_a
        newtuple_b = tuple_b
    if len(tuple_a) >= 2:
        print("only tuple a  available." )
        newtuple_a = tuple_a
    if len(tuple_b) >= 2:
        print("only tuple b available." )
        newtuple_b = tuple_b
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        print("tuples missing one or more:")
        print("a:",tuple_a)
        print("b",tuple_b)
        print("----replaced: tuples----")
        if len(tuple_a) == 0:
            newtuple_a = 0, 0,
            print("newtuple_a: {} ".format(newtuple_a))
        elif len(tuple_a) == 1:
            newtuple_a = tuple_a[0], 0,
            print("newtuple_a: {} ".format(newtuple_a))
        if len(tuple_b) == 0:
            newtuple_b = 0, 0,
            print("newtuple_b: {} ".format(newtuple_b))
        elif len(tuple_b) == 1:
            newtuple_b = tuple_b[0], 0,
            print("newtuple_b: {} ".format(newtuple_b))

    sum_tuple = newtuple_a[0] + newtuple_b[0], newtuple_a[1] + newtuple_b[1]

    print("sum:.....")
    # print()
    return (sum_tuple)


tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
print(add_tuple((), (4, 8, 8)))

