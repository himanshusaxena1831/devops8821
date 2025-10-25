def main_fun(name):
    def inner_fun():
        return name().upper()
    return inner_fun
@main_fun
def myfun():
    return "hello shivani whatsapp!"
print(myfun())

@main_fun
def other_fun():
    return "how are you!"
print(other_fun())
