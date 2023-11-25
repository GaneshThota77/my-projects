statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "ganesh":"offline",
}
count=0
for i,j in statuses.items():
    if j=='online':
        count=count+1
print(count)