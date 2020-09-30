with open('requests_accepted.txt', 'r') as file:
    data = file.read().split()

titles = {}

sum = 0

for i in range(len(data)-1):
    if "Connected" in data[i]:
        sum += 1
    if "occupation" in data[i]:
        j = i + 1
        title = ""

        while data[j] != "Connected":
            title += data[j]
            j += 1
        if title in titles:
            titles[title] += 1
        else:
            titles[title] = 1
print("%d people accepted your request\n" % sum)
print("list of titles that have accepted with counts: \n")
for key, value in titles.items():
    print(key)
    print(" : ")
    print(value)
