# There is standard built in exception class in python
# User defined exception
# raise keyword is used to raise an exception manually in python.
# finally keyword executes the code inside of it no matter  if the exception is raised or not

try:
    raise Exception("Exception")
except Exception as e:
    print(e)

class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def print_exception(self):
        print("User defined exception: ", self.msg)
    def handle(self):
        print("Accident occured: take detour.")

try:
    raise Accident("Crash between two cars.")
except Accident as e:
    e.print_exception()
    e.handle()
finally:
    pass 