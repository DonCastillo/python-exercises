numbers = [1, 45, 32, 12, 60]

for number in numbers:
    if number % 8 == 0:
        #reject the list
        print('The numbers are unacceptable')
        break
else:
    print('All those numbers are fine') # execute this statement when the loop terminates normally