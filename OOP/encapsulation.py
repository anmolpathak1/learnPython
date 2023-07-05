#data + method
#protected member variable
#private member variable

class Parent:
    def __init__(self):
        self._a = 1                   #protected member variable
        self.__b = 2                  #private member variable


class child(Parent):
    def __init__(self):

        Parent.__init__(self)
        print("calling protected member of base class", self._a)

        self._a = 3
        print("modified the Protected varible from derived class" , self._a)


if __name__ == '__main__':
    obj2 = child()
    obj1 = Parent()


    print("parent a value", obj1._a)
    print("child a value", obj2._a)