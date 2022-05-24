# задача 1
class FormulaError(Exception):
    pass

def calc(datastring):
    data = datastring.split(" ")

    if (len(data) != 3):
        raise FormulaError
    
    try:
        first, sec = float(data[0]), float(data[2])
    except ValueError:
        raise FormulaError
    
    if data[1] == '+':
        return first + sec
    elif data[1] == '-':
        return first - sec
    elif data[1] == '*':
        return first * sec
    elif data[1] == '/':
        return first / sec
    else:
        raise FormulaError

''' test
while True:
    print(calc(input))

'''
    
# задача 2
class ReverseIter:
 
    """Итератор, который обращает список."""
 
    def __init__(self, datalist):
        self.num = len(datalist)
        self.data = datalist
 
    def __iter__(self):
        return self
 
    def __next__(self):
        self.num -=1
        if(self.num < 0):
            raise StopIteration
        else:
            return self.data[self.num]

''' test
data = [1, 2, 3]
for i in ReverseIter(data):
    print(i)
'''


# задача 3
def fib_generator(n):
    first = 0
    second = 1
    num = 1
    while num<=n:
        if num == 1:
            yield first
        elif num == 2:
            yield second
        else:
            first, second = second, first + second
            yield second
        num += 1

def fib_list(n):
    return list(fib_generator(n))

''' test
for i in fib_generator(20):
    print(i)

print(fib_list(10))
'''
