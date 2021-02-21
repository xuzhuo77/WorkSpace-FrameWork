def can_divide_by_three(number):
    if number % 3 == 0:
        return True
    else:
        return False


selected_numbers = []
for number in range(1, 11):
    if can_divide_by_three(number):
        selected_numbers.append(number)
print(selected_numbers)

"""
filter
"""
a=lambda x: True if x%3==1 else False
y=list(filter(a,range(1,20)))
print(y)

import pandas as pd
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

result = pd.merge(left, right, on=["key1", "key2"])
print(result)