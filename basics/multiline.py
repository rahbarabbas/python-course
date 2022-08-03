data="" #empty string
while True:
    line=input('line>>>')
    if not line:
        break
    data=data+' '+line

print('You have entered the following data')
print(data)