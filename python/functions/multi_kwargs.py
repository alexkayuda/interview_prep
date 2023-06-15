# args collects all positional arguments into tuple
# kwargs collect all keyword arguments into map


# this will convert passed args to a map
def func1(**kwargs):
    print(kwargs)

def func2(name, age):
    print(f"Name: {name}, Age: {age}")

def both(*args, **kwargs):
    print(f"args: {args} and kwargs: {kwargs}")


func1(name="Bob", age=15)

details = {"name": "Bob", "age": 15}
func1(**details) #this will "unpack" map and send params to appropriate named fields
func2(**details) #same result

both(1,2,3,4,5, name="Bob")
both(1,2, name="Alice", age = 25)
both(1, name="John")

