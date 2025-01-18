# encapulate variables and method with the object
##################################################
class Restangle:
    def __init__(self, v_width, v_length):
        self.width = v_width
        self.length = v_length

    def area(self):
        return self.width * self.length


restangle_1 = Restangle(10, 20)
print(restangle_1.width)
print(restangle_1.length)
print(restangle_1.area())


# hide data
class Data:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def change_data(self, v_index, v_replacement):
        self.data[v_index] = v_replacement


data_1 = Data()
data_1.data

data_1.data[0] = 100
data_1.data


data_1.change_data(1, 200)
data_1.data


# private/underscore/unsafe variable and
# private/underscore/unsafe methods
# statement 'pass' is generally used as a placeholder.
class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._private = "unsafe"

    def public_method(self):
        # pass
        print("[info] public method to client.")

    def _private_method(self):
        # passprivate
        print("[warn] internal use only.")


demo_1 = PublicPrivateExample()
demo_1.public
demo_1._private
demo_1.public_method()
demo_1._private_method()

#######
# EOF #
#######
