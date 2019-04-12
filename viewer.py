import csv

header = []
id_map = {}

def print_by_id(id):
    if id in id_map:
        i = 0
        for col in header:
            print("%s: %s" % (col, id_map[id][i]))
            i += 1
        print()
        return True
    return False

def print_by_name(name):
    found = 0
    for _, value in id_map.items():
        if name.lower() in value[3].lower():
            print_by_id(value[0])
            found += 1
    if found:
        print("Found %d items matching %s" % (found, name))
    else:
        print("Item %s not found!" % (name))

print("Enter id or part of item name to view its entry")
print("Type exit to ... exit")
with open('items.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    is_header = True
    for row in csv_reader:
        if is_header:
            [header.append(col) for col in row]
            is_header = False
        else:
            id_map[row[0]] = []
            [id_map[row[0]].append(col) for col in row]
            
while True:
    id = input()
    if id:
        if id.lower() == 'exit':
           break 

        if not print_by_id(id):
            print_by_name(id)

