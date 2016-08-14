import networkx as nx
import matplotlib.pyplot as plt
import csv

lst = [] 
people = []
count = 0
saga = []
elm = []
cend = []
with open('matches.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        lst.append(row)
print lst        
with open('people_colleges.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        people.append(row)
print people
slist = []
elist = []
clist = []
values = []
        
for person in people:
    if (person[1].find('Saga') != -1):
        saga.append(person[0])
        slist.append('b')
    elif (person[1].find('Elm') != -1):
        elm.append(person[0])
        elist.append('r')
    elif (person[1].find('Cendana') != -1):
        cend.append(person[0])
        clist.append('g')
    else:
        print person
      
G=nx.Graph()
G.add_nodes_from(saga)
G.add_nodes_from(elm)
G.add_nodes_from(cend)

for a in lst:
    G.add_edge(a[0], a[1][1:])
    count += 1

values = slist + elist + clist

nx.draw_random(G, node_color=values, alpha=0.5)
plt.savefig("1.png") # save as png
plt.show() # display
print count