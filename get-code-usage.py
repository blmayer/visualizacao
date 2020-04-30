import json
import os


root_dir = '/Users/blmayer/poupachef/back-end'
go_paths = []
stats = []
classes = [
    'User', "Store", 'Quotation', 'Cart', 'Supplier', 'Delivery', 'Product'
]


# Recursive search
def search_down(root, entry):
    if os.path.isfile(os.path.join(root, entry)):
        if entry.endswith('.go'):
            go_paths.append(os.path.join(root, entry))
    else:
        for deep_entry in os.listdir(os.path.join(root, entry)):
            search_down(os.path.join(root, entry), deep_entry)


# Main execution
search_down(root_dir, "")
for go_path in go_paths:
    class_stats = {x: 0 for x in classes}
    file_stats = {'file': os.path.relpath(go_path, root_dir)}

    # Read file
    with open(go_path) as go_file:
        # Read first line to get package name
        header = go_file.readline()
        file_stats['package'] = header.split(' ')[1].strip()

        # Read the rest and update stats
        lines = go_file.readlines()
        for line in lines:
            words = line.split(' ')
            for word in words:
                for go_class in classes:
                    if word.find(go_class) > -1:
                        class_stats[go_class] += 1

    # Save information
    for stat in class_stats:
        if class_stats[stat] > 0:
            info = {
                'class': stat,
                'value': class_stats[stat],
                'package': file_stats['package'],
                'file': file_stats['file']
            }
            
            # print('appending', info)
            stats.append(info)

# print(stats[:5])
json.dump(stats, open('code_complete.json', 'w'))
