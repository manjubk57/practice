l=[1,2,3,4,5]
even=lambda num:num%2==0
print(list(map(even,l)))


s="asadadadassasas"
cp=lambda ch :{i:ch.count(i) for i in ch if i not in {} }
print(cp(s))
