# A generator is a simple way of creating an iterator
# benefits of using generator:
# 1- No need to define iter() and next() method
# 2- No need to raise stopiteration exception.

def remote_control_next():
    yield "HBO"
    yield "CNN"
    yield "ABC"
    yield "ESPN"
# the yield keyword returns the value and retains the last returned state

itr= remote_control_next()
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

for channel in remote_control_next():
    print(channel)

#example for fibonacci sequence
def fib():
    a, b = 0, 1
    while True:
        yield a
        a=b
        b=a+b

for i in fib():
    if i>1000:
        break
    print(i)


