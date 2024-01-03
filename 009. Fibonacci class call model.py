# Created via GPT
#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Create a class called person, declare its properties separately, and create an instance
class Person:
    # attribute field
    name = "William"
    age = 45
    # method
    def great(self): # After creating an instance, self points to the instance itself.
        print(f'Hi, my name is :{self.name}')# should use self.name instead of name here
# Create an Object   
pl = Person()
# Call the method
pl.great()


# In[6]:


# OOP: Object-Oriented Programming
# Class and instance
# Create a class called person
class Person:
    def __init__(self):
        self.name = "Alice"
    def great(self):
        print(f'Hi, my name is: {self.name}')
pl = Person()
pl.great()


# In[7]:


# Create a class called person with init_name
class Person:
    def __init__(self, init_name):
        self.name = init_name
    def great(self):
        print(f'Hi, now my name is :{self.name}')
pl = Person('David')
pl.great()


# In[11]:


# Inheritance and polymorphism 1
class Animal():
    def __init__(self, name):
        self.name = name
    def great(self):
        print(f"Hello, I am an {self.name}")
class Dog():
    def __init__(self, name):
        self.name = name
    def great(self):
        print(f"WongWong.., I am {self.name}")
animal = Animal('animal')
animal.great()
dog = Dog("dog")
dog.great()


# In[13]:


# Inheritance and polymorphism 2
# Call the animal function directly in the dog function instead of re-declaring self in the dog function
class Animal():
    def __init__(self, name):
        self.name = name
    def great(self):
        print(f"Hello, I am an {self.name}")
class Dog(Animal):
    def great(self):
        print(f"WongWong.., I am {self.name}")
animal = Animal('animal')
animal.great()
dog = Dog("dog")
dog.great()


# In[15]:


# Inheritance and polymorphism 3, add one more function in Dog()
class Animal():
    def __init__(self, name):
        self.name = name
    def great(self):
        print(f"Hello, I am an {self.name}")
class Dog(Animal):
    def great(self):
        print(f"WongWong.., I am {self.name}")
    def run(self):
        print(f'I am running')
animal = Animal('animal')
animal.great()
dog = Dog("dog")
dog.great()
dog.run()


# In[26]:


# Inheritance and polymorphism 4, add Cat() and use polymorphism
class Animal():
    def __init__(self, name):
        self.name = name
    def great(self):
        print(f'Hello, I am an: {self.name}')
class Dog(Animal):
    def great(self):
        print(f'WongWong.., I am: {self.name}')
class Cat(Animal):
    def great(self):
        print(f'MiaoMiao.., I am: {self.name}')
def Hello(animal):
    animal.great()
dog = Dog('dog')
Hello(dog)
cat = Cat('cat')
Hello(cat)


# In[27]:


# Define Iterators and next to perform a for loop
# Methods to Solve the Fibonacci Sequence
class Fib():
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
# 1, 1, 2, 3, 5, 8 ...

fib = Fib()
for i in fib:
    if i > 10:
        break
    print(i) #1, 1, 2, 3, 5, 8


# In[30]:


# Access restrictions (for security reasons)
class Animal():
    def __init__(self, name):
        self.__name = name
    def great(self):
        print(f'Hello, I am an: {self.name}')
animal = Animal('al')
animal.__name # error


# In[31]:


# module call (**same as Python Standard Library**)
# if Animal.py(the module to be called) is in the current operating directory
# from animal import Animal
# animal = Animal("animal")
# animal.great()

# from animal import Dog, Cat
# dog = Dog("duoduo")
# dog.great()
# cat = Cat("Kitty")
# cat.great()

# import an entire module
# import animal
# cat = animal.Cat('kitty')

# import all classes from a model
# from animal import *
# cat = Cat('Kitty')

# Using aliases
# from animal import Cat as c
# cat = c("kitty")


# In[32]:


# Naming conventions:
# name class: Camel nomenclature(CamelCase)
# Examples and modules: snake_case
# spatial organization code (write the declaration first, then write the code after the space)
# Standard library>self-written library


# In[ ]:




