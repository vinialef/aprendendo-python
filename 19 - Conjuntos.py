c_a = {1,2,3,4}
c_b = {2,3,4,5}
print(c_a.union(c_b))
print(c_a.intersection(c_b))
print(c_a.difference(c_b))
print(c_b.difference(c_a))
print(c_a.symmetric_difference(c_b))

c_c = {1,2,3}
print(c_c.issubset(c_a))
print(c_a.issuperset(c_c))
print(c_c.issuperset(c_a))

c_d = {6,7,8,9}
print(c_d.isdisjoint(c_c))

c_d.add(10)
print(c_d)

print(len(c_d))

print(10 in c_d)
print(11 in c_d)