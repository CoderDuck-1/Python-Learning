d={'Jagmohan':9810070159, 'Geeta':8178661912, 'dhruv':9990169006}
print(d['Jagmohan'])
d['Lakshya']=9711713423

print(d)
print(d.items())
print(type(list(d.items())[1]))
print(d.keys())
print(d.values())

for key in d:
    print("Key: ", key, ", Value: ", d[key])

for k,v in d.items():
    print("Key: ", k, ", Value: ", v)

print('Jagmohan' in d)
print('Jagmohan' not in d)

d.clear() #deletes the dictionary