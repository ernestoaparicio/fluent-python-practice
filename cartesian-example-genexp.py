# The generator expression yields items one by one; a list with all six T-shirt variations is never produced in this example.

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

for tshirt in ((c, s) for c in colors for s in sizes):
    print(tshirt)
