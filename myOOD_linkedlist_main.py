from myOOD_linkedlist import LinkedList
l = LinkedList()
l.append(3)
l.append(3)
l.append(2)
l.append(4)
l.append(5)
l.print()
print("--------")
# l.clear()
l.copy()
l.print()
print("--------")
print(l.count(3))
print("--------")
l.extend([1,2,3])
l.print()
print("--------")
print(l.index(5))
print("--------")
l.insert(9,2)
l.print()
print("--------")
l.pop(1)
l.print()
print("--------")
l.remove(3)
l.print()
print("--------")
l.reverse()
l.print()