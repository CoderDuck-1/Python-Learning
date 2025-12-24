# An iterator is an object that provides a way to access elements of a collection (like a list or array) one at a time,
# in a sequential manner
# we can use iter in forward and reverse sequence both

class RemoteControl():
    def __init__(self):
        self.channels=["HBO", "CNN","ABC","ESPN"]
        self.index=-1

    def __iter__(self):
        return self #returns an iterable object of the class RemoteControl

    def __next__(self):
        self.index+=1
        if self.index==len(self.channels):
            raise StopIteration # stopiteration is pre defined exception in iterators that is raised to stop the iteration further
        return self.channels[self.index]

r = RemoteControl()
iter=iter(r)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))






