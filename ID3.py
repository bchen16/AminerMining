import sys
import math
from collections import Counter

#returns a decision tree
def make_decision_tree(data,attributes,target):
    # data: the parsed dataset
    # attributes: all the attributes in the dataset
    # target: index of attribute list that is the target attribute intended to be the output

    target_values = [i[target] for i in data] # All the values in target attribute
    c = Counter(target_values)
    counter = c.most_common(1)[0]
    r = counter[0] # Return variable, if the attributes are empty, return PLURALITY-VALUE

    # No attribute
    if attributes == None or attributes == [] or len(attributes) == 1:
        return r

    # Only one value in target data
    if counter[1] == len(data):
        return r

    # Calculate the attribute with largest information entropy, pick that attribute for current tree building
    entropy_attr = []
    for a in range(0,len(attributes)):
        entropy_attr.append(calc_entropy(a,data,target))
    A = entropy_attr.index(max(entropy_attr))
    if A == target:
        A = second_largest(entropy_attr)
    
    # New decition tree with root A, implementing the tree using dictionary
    tree = {attributes[A]:{}}

    # Creating subtrees and adding it to the tree
    for i in get_values(A,data):
        newData = []
        for j in data:
            if j[A] == i:
                if A == len(attributes) - 1:
                    newData.append(j[0:A])
                else:
                    newData.append(j[0:A]+j[A+1:])

        # Eliminate current attribute in subtrees
        if A == len(attributes) - 1:
            newAttributes = attributes[0:A]
        else:
            newAttributes = attributes[0:A] + attributes[A+1:]

        # add the subtree to main tree
        tree[attributes[A]][i] = make_decision_tree(newData,newAttributes,target-1)

    return tree


# return second largest number in a list
def second_largest(l):
    data = max(l)
    l.remove(data)
    return l.index(max(l))

# returns the infromation entropy given attribute and data
def calc_entropy(attribute, data, target):
    #calculate Info(D)
    e1 = calc_info_d(data,target)

    #calculate InfoA(D)
    e2 = 0.0
    vals = get_values(attribute, data)
    for i in  vals:
        temp_data = []
        count = 0
        # Create sub-dataset
        for j in data:
            if j[attribute] == i:
                temp_data.append(j)
                count = count + 1
        e2 = e2 + count/len(data)*calc_info_d(temp_data,target)

    gain = e1 - e2
    return gain

# calculates info D
def calc_info_d(data, target):
    Di = []
    vals = get_values(target, data)
    e = 0.0

    # Count how many v is in data
    for v in range(0,len(vals)):
        Di.append(0)
        for i in data:
            if i[target] == vals[v]:
                Di[v] = Di[v] + 1
    # calculate:
    for i in Di:
        if i != 0:
            e = e - i/len(data)*math.log(i/len(data))
    return e
## return all the possible values under a specific attribute
def get_values(attribute,data):
    values = []
    for i in data:
        if not i[attribute] in values:
            values.append(i[attribute])
    return values

## returns data from file
def get_data(filename):
    with open(filename,'r') as f:
        lines = list(f.readlines())

    data = []
    for i in lines:
        data.append(i.split(','))
        #eliminate the '\n'
        if i != lines[len(lines) - 1]:
            data[len(data) - 1][-1] = data[len(data) - 1][-1][:-1]
    return data

print(make_decision_tree(get_data('./data/dt/WillWait-data.txt'),['Alternate','Bar','Fri/Sat','Hungry','Patrons','Price','Raining','Reservation','Type','WaitEstimate','WillWait'],10))
print(make_decision_tree(get_data('./data/dt/iris.data.discrete.txt'),['sepal length','sepal width','petal length','petal width','IRIS'],4))
