# copy and paste from manage invitations down to wherever, then
# throw into a .txt file named "pasted.txt"

# todo? add metrics on who I am requesting?

with open('requests_sent.txt', 'r') as file:
    data = file.read().split()

companies = {}
sum = 0
for i in range(len(data)-1):
    if "Withdraw" in data[i]:
        sum += 1
    if data[i] == "at":
        company = data[i+1].replace(',','')
        companies[company] = True


print("you requested to connect with %d people" % sum)
print("a list of the companies: ")
for key, value in companies.items():
    print(key)
