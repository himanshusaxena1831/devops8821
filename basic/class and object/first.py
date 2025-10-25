class person:
    def __init__(self, name, age, city, contary):
        self.name = name
        self.age = age
        self.city = city
        self.contary = contary
    def greet(self):
        print("hello world. I'm  " + self.name, self.age, self.city, self.contary)
# print(p1.name, p1.city, p1.age, p1.contary)
p1 = person("yaksh", 26, "meerut", "india")
p1.greet()