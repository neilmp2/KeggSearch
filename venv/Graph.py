import networkx as nx
import json
import re


with open("reactions.json", "r") as read_file:
    data = json.load(read_file)

extracted_data = []
for l in range(6):
    for j in range(len(data['children'][l]['children'])):
        for i in range(len(data['children'][0]['children'][j]['children'])):
            for item in data["children"][0]["children"][j]["children"][i]["children"]:
                extracted_data.append(item['name'].split("\t"))

# remove extra spaces
fully_extracted_data = []
for i in range(len(extracted_data)):
    l = []
    for j in range(len(extracted_data[i])):
        x = (re.sub(' +', ' ', extracted_data[i][j]))
        l.append(x)
    fully_extracted_data.append(l)



def generate_graph():
    """
    Creates the graph from the file reactions.json
    :return: The graph
    """

    reactions = nx.Graph()

    for elem in fully_extracted_data:
        if len(elem) == 2:
            r = elem[0]
            c1 = elem[1]
            reactions.add_edge(r, cs1)

        elif len(elem) == 3:
            r = elem[0]
            c1 = elem[1]
            c2 = elem[2]
            cs1 = c1.split(' ')[0]
            cs2 = c2.split(' ')[0]
            reactions.add_edge(r, cs1)
            reactions.add_edge(r, cs2)
    return reactions

def create_compdict():
    """
    :return: dictionary of {PDB ID : 'name'} for all molecules
    """

    comps = []
    for elem in fully_extracted_data:
        if len(elem) == 3:
            comps.append([elem[1]])
            comps.append([elem[2]])

    keys = []
    for elem in comps:
        keys.append(elem[0].split(' ')[0])

    values = []
    for elem in comps:
        values.append(elem[0].split(' ')[1])

    compound_dictionary = {}
    for i in range(len(keys)):
        compound_dictionary[keys[i]] = values[i]

    return compound_dictionary




biograph = generate_graph()
compdict = create_compdict()
running = 1


while running == 1:
    keylist = list(compdict.keys())
    vallist = list(compdict.values())
    valid = False #condition for inner while loops

    while valid == False:
        try:
            print('Enter the name of the starting compound')
            starting = input()
            start_code = keylist[vallist.index(starting)]
            valid = True
        except ValueError:
            print('That compound does not exist. Check your spelling!')

    valid = False
    while valid == False:
        try:
            print('Now enter the name of the desired product')
            desired = input()
            desire_code = keylist[vallist.index(desired)]
            valid = True
        except ValueError:
            print('That compound does not exist. Check your spelling!')


    try:
        shortest= nx.shortest_path(biograph, start_code, desire_code)
        print(shortest)
    except nx.exception.NetworkXNoPath:
        print("Unfortunately, this path does not exist, which means an enzyme based reaction chain is not available.")
