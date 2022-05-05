# function is piece of code get executed only when you call it

# this is how you can create and involk function in python

def check_age(age):
    if age < 18:
        print('You are not adult')
    else:
        print('Adult Person')


check_age(19)
check_age(16)
check_age(35)


def check_price(price):
    if price < 100:
        print('cheap')
    else:
        print('expensive')


check_price(150)
check_price(50)

# built in function

print('hello'.endswith('o'))
print('hello'.endswith('O'))
