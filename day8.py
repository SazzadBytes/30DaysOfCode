testCase= int(input()) 
dict1 = {}  

for _ in range(testCase):
    entry = input().split()
    name, phone = entry[0], entry[1]
    dict1[name] = phone

while True:
    try:
        search = input()
        if search in dict1:
            print(f"{search}={dict1[search]}")
        else:
            print("Not found")
    except EOFError:
        break
