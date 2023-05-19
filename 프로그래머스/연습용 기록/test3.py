import copy

folders = [["animal", "root"], ["fruit", "root"]]
files = [["cat", "1B", "animal"], ["dog", "2B", "animal"], ["apple", "4B", "fruit"]]
selected = ["animal"]
excepted = ["apple"]

hm = {"root":[]}

for folds in folders:
    hm[folds[0]] = []

hm4file = copy.deepcopy(hm)


for name,size,folder in files:
    if name in excepted:
        continue
    else:
        hm4file[folder].append((name,size))

print(hm4file)

for child,parent in folders:
    hm[parent].append(child)


tree = {"root" : {"files" : hm4file["root"]}}
count = 0
sizes = 0


def recursion(start,tree,select):
    global count, sizes
    for i in hm[start]:
        tree[i] = {"files" : hm4file[i]}
        if select or i in selected:
            for name,size in hm4file[i]:
                count += 1
                if size[-2] == "K":
                    sizes += int(size[:-2]) *1024
                else:
                    sizes += int(size[:-1])

            recursion(i,tree[i],True)
        else:
            recursion(i, tree[i], False)


if "root" in selected:
    for name, size in hm4file["root"]:
        count += 1
        if size[-2] == "K":
            sizes += int(size[:-2]) * 1024
        else:
            sizes += int(size[:-1])
    recursion("root",tree["root"],True)
else:
    recursion("root", tree["root"], False)

print(tree)
print(sizes,count)