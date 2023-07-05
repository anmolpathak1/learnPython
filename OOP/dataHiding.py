#there are not private modifier for variable in python
#instead variable are hidden using the __variable name.

class Solution:
    __privateSolution = 0

    def sum(self):
        self.__privateSolution += 1
        print(self.__privateSolution)


if __name__ == '__main__':
    obj = Solution()
    obj.sum()

    #print(obj.__privateSolution)                     #can't be accessed here.
    print(obj._Solution__privateSolution)


