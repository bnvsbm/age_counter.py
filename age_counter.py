try:
    bill1 = int(input('Enter your bill:'))
    discount1 = int(input('Enter your dicount:'))

    bill2 = int(input('Enter your bill:'))
    discount2 = int(input('Enter your dicount:'))

    person1 = bill1-discount1
    person2= bill2-discount2
    print('Total bill for the first person is :', person1)
    print('Total bill for the second person is :', person2 )

except ZeroDivisionError:
    print('Division by zero is not allowed')
except ValueError:
    print('Please enter a whole number')