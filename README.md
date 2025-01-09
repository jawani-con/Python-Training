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

 
