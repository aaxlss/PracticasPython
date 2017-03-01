from Inheritance.Bar import Bar

# creating an instance of Bar in x

x = Bar()

# calling something variable from Foo class
print(x.something)

#calling the overinding method from Bar class
print(x.method_A())

#calling Foos_method from Foo class
print(x.Foos_method())

#callin Bar_method form Bar class
print (x.Bar_method())