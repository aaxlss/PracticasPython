import ModulesFile

#imprimir variable var1
print (ModulesFile.var1)

#imprimir variable var2
print(ModulesFile.var2)

#llamando al metodo nums
print (ModulesFile.nums(1,2,3,4,5,6))

#llamando al metodo numsArgs
array = ['a', 'b', 'c', 'd']
print (ModulesFile.numsArgs(*array))

#llamando al metodo keyValue
print(ModulesFile.keyValue(a = "hola", b = "mundo", c="2017"))

#llamando al metodo arrayKeyValue
keyValue = {'a': "hola", 'b':"mundo", 'c' :2017}
print ModulesFile.arrayKeyValue(**keyValue)