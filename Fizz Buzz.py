#Fizz Buzz

x = list(range(1,101))
for y in x:
    if y % 3 == 0 and y % 5 == 0:
        print('FizzBuzz')
    elif y % 3 == 0:
        print('Fizz')
    elif y % 5 == 0:
        print('Buzz')
    else:
        print(y)
