### Other things to Note:

1. **Constructors**:
```Python
class Name():
    def __init__(self): # Here __init__() is constructor
        .
        .
        .
```
2. **Automatic Garbage Collection**:
```Python
class Name():
    def set_name(self,name):
        self.name = name

>> c1 = Name()
>> c1.set_name('Test')
>> print(c1.name)

OUTPUT >> Test
```
Now if we delete an attribute, or set a new one to the same old name.. then?

```Python
>> c1.set_name('NK')
>> print(c1.name)

OUTPUT >> NK

```

Now important thing to consider in all of this above example is: MEMORY ALLOCATION!!

When we intially allocated c1 object an attribute "set_name" ('Test')

somewhere in the memory, a new instance is create with this attribute name.

Next when we change that reference to new name ('NK'), the previous instance is left aside and a new instance is create with new value.

If not used for sometime, the previous instance will be automatically removed from the memory after sometime.

**This is _automatic destruction of unreferenced objects is known as Garbage Collection._**