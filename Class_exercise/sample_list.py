myneighbours=["hemu"]
myneighbours.append("harshith")
print(myneighbours)
myneighbours.insert(0,"dev")
print(myneighbours)
myneighbours.append("hemanth")
print(myneighbours)
myneighbours.insert(0,"vetri")
print(myneighbours)

#copying list to another list
myneighbours2=myneighbours.copy()

#clearing the list
myneighbours.clear()
print(myneighbours)

#deleting the list
del myneighbours

print(myneighbours2)
