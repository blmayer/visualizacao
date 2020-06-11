import json

usages = json.load(open('code_complete.json'))

tree = {"name": "code", "children": []}
for use in usages:
    paths = use['file'].split('/')
    root = tree
    for i in range(len(paths)):
        if paths[i] not in [c['name'] for c in root['children']]:
            child = {"name": paths[i]}
            if i == len(paths)-1:
                child['size'] = use['value']
            else:
                child['children'] = []

            root['children'].append(child)
            root = child
        else:
            # Enter child
            child = [c for c in root['children'] if c['name'] == paths[i]]
            root = child[0]

            if i == len(paths)-1:
                root['size'] += use['value']

json.dump(tree, open("code_tree.json", 'w'))