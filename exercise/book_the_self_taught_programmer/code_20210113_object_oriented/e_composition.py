# using composition to express ownership between objects


class Dog:
    def __init__(self, v1_name, v2_breed, v3_owner):
        self.name = v1_name
        self.breed = v2_breed
        self.owner = v3_owner


class Person:
    def __init__(self, v_name):
        self.name = v_name


mick = Person("Mick Jagger")
# pass 'Person' object as parameter 'owner' while creating 'Dog' object
stan = Dog("Stanley", "Bulldog", mick)

print(stan.owner.name)


#######
# EOF #
#######
