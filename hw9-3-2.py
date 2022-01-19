# Author: CRS 01/14/22
print('Enter the net sales for')

previous = float(input('- Prior period:'))
current = float(input('- Current period:'))

change = (current - previous) * 100 / previous
try:
        if change > 0:
                result = f'Sales increase {abs(change)}%'
                print(result)
except ValueError:
        print("Enter real numbers.")
except TypeError:
        print("Input numbers.")
finally:
        print("Thanks for your inputs!")

result = f'Sales decrease {abs(change)}%'
