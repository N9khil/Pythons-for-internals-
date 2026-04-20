e = True or False

print(e)

a= "32"
b=float(a)
print(b)


a = int(input("Enter num 1 : "))
b = int(input("Enter num 2 : "))

print("Sum is : ",a+b)


a= float(input("Enter divident : "))
b=int(input("Enter divider : "))
print(a%b)

# to not give endl in consecutive print statement

print("hello",end="")
print("nigga")





# # STRING # # #  


# string can ne made in 3 diffrent way
a='hello'
b="hello"
c='''hello'''

# to slice a string ,do as below
a="hello"
b=a[1:3]
print(b)

# to calculate length of a string use a len function
a="hello"
print(len(a))

# to check if that string is ending with that specific 
a="helllo" 
print(a.endswith("llpo"))

# to check if that string is starting with that specific 
a="hello"
print(a.startswith("hell"))

# to capitalise everything use capatalise finction
a="hello"
print(a.capitalize())

# to add a element to string at desired place
list = ['a','b','c']
list.insert(3,'hello')
print(list)

# add element at end
list.append('nigga')

list.remove('hello')
print(list)

string="this is me"
string.capitalize()  # this is to capitalsie first letter of string 
print(string.find("me"))
print(string.replace("is","are"))



# # Tupples are strings nut their values cant be changed until changed to list # # #

tup= (1,2,3)
tup[0]=1 #error

# to change
tup=list(tup)
tup[0]=4
tup=tuple(tup)
print(tup)

#  We ca assign keys and values to list/tupple


# #  Dictionaries # # #

# dictonary let us store values with keys and values

lst = {'Nigga_1':1,'Nigga_2':2,'Nigga_3':3,'Nigga_4':4}
print(lst['Nigga_3'])  # to specify take out a element
lst['Nigga_4']=5
print(lst)

print(lst.keys())  # to see all keys 
print(lst.values())  # to see all values



# # FUNCTIONS # # #

def fun( a ,  b):
    return (a+b)/2
print(fun(2,3))


# # files IO(input,output) # # #

file=open("Nikhil.txt","rb+")  #this will bring "nikhil.txt" file to read & write mode
print(file.mode) # in which mode we have opened our file 
print(file.name) # which file we are at 
file.write(bytes("Mera PAPA ,India hai","UTF-8"))
print(file.read()) # to read rhe file
file.close()  # why to close a file, if we dont close anyone else will not be able to work with same file



# # OOPS # # # 


class Employee:
    __name = None
    __salary = 0
    __age = 45

    def set_name(self,name):
        self.__name = name
    def get_name(self):
        print(self.__name)
Nikhil=Employee()                  #defining nikhil as object of class Employee
Nikhil.set_name("NIGGA")           # setting name to object allocated to nikhil as NIGGA 
Nikhil.get_name()      