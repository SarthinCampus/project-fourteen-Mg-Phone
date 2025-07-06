items = input().split(',')

seen = set()
unique_items = []
for item in items:
    item = item.strip()
    if item not in seen:
        unique_items.append(item)
        seen.add(item)

for item in unique_items:
    print(item)
