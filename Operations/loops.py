#loops allows to write some codes that will automatically loopthrough the list

#forLopp

cars = ['bmw', 'tesla', 'benz', 'Toyota']
for car in cars:
    if car == 'Toyota':
        print(car.upper())
    else:
        print(car.capitalize())

#while loop

number = 0

while number <= 10:
    print(number)
    number = number + 1
else:
    print('while loop ended and value of number is ' + str(number))
