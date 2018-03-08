# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}.")


# OK, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}.")


# this just take one argument
def print_one(arg):
    print(f"arg: {arg}")


# this one takes no argument
def print_none():
    print("I got nothing.")


print_two('hehe', 'xixi')
print_two_again('helo', 'xiha')
print_one('haole')
print_none()

