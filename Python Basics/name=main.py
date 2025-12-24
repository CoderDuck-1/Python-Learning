if __name__ == "__main__":
    print("dhubbi is farzi")
print(__name__)

# "if__name__==__main__ :" is used as an entry point in Python programs like "void main(){}" in C++
# The default value of __name__ is __main__
# The value of __name__ is not __main__ when we call it inside a function from another file/module. It's value is the same as name of other file/ module.