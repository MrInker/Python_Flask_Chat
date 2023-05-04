from datetime import timedelta

speaker = 'Alex'
duration = 110.0
duration_timedelta = timedelta(minutes=duration)
delta = timedelta(minutes=10)
print(duration_timedelta + delta)

# list
visitors = ['Dmitrii', 'Yarik', 'Kir']  # create list
# print(visitors[0])

# cycles
for i in visitors:
    print(i)

print(len(visitors))

# dictionaries

visitor_dict = {}
visitor_dict['Dmitrii'] = 'Hello All'
visitor_dict['Yarik'] = 'Hello Dim'
visitor_dict['Kir'] = 'Wazaaap?'

print(visitor_dict)
print(visitor_dict['Kir'])
print(len(visitor_dict))

# for in dict

for key, value in visitor_dict.items():
    print(F'Key: {key}, Value: {value}')
