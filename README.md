# Python-Training

List
- mutable ordered collection
- list = []
- append, pop([index]), slice[1:n], sort(key=, reverse=)

Tuples
- immutable ordered collection

Dictionaries
- mutable ordered collection of key-value pair
- person={"name": "", "age":}

Sets
- mutable ordered collection of unique values
- automatically removes duplicates
- set={1,2....}

*Args
- The special syntax *args in function definitions is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list. 


def fun(arg1, *argv):

    print("First argument :", arg1)
    
    for arg in argv:
    
        print("Argument *argv :", arg)
        
fun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

//hello gone as arg1 and rest as *argv

**Kwargs
- The special syntax **kwargs in function definitions is used to pass a variable length argument list. We use the name kwargs with the double star **.
- A keyword argument is where you provide a name to the variable as you pass it into the function.
- It collects all the additional keyword arguments passed to the function and stores them in a dictionary.

  def fun(**kwargs):
  
    for k, val in kwargs.items():
  
        print("%s == %s" % (k, val))
  
fun(s1='Geeks', s2='for', s3='Geeks')


Module:
- A module is a Python file that contains code (e.g., functions, classes, variables).
- Used for organizing and reusing code across different programs.
- You import modules using import module_name.
- Modules have a global scope for functions and variables defined within them.
- Cannot be instantiated.
 
