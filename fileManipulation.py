import os
import sys
import pickle


def print_lol(the_list, indent=False, level=0 , fh = sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level + 1)
        else:
            if indent:
                for each_level in range(level):
                    print('\t', end='', file = fh)
            print(each_item, file = fh)


if __name__ == '__main__':
    os.chdir("D:\python\chapter3")
    man = []
    other = []

    try:
        with open("sketch.txt") as data:

        #if os.path.exists('sketch.txt'):
        # data = open('sketch.txt')

            for each_line in data:
                #if not each_line.find(':') == -1 :
                    try:
                        (role, line_spoken) = each_line.split(':',1)
                        line_spoken = line_spoken.strip()
                        if role == 'Man':
                            man.append(line_spoken)
                        elif role == 'Other Man':
                            other.append(line_spoken)
                        print(role, end='')
                        print(' said ', end='')
                        print(line_spoken, end='')
                    except ValueError:
                        print("there is no semicolon")
    except IOError as obj:
    #else:
        print("file error : " + str(obj))


    try:
        # with open("man.txt", 'w') as man_file, open("other.txt", 'w') as other_file:
        with open("man.txt", 'wb') as man_file, open("other.txt", 'wb') as other_file:
            pickle.dump(man,man_file)
            pickle.dump(other,other_file)
            # print_lol(man, fh=man_file)
            # print_lol(other, fh=other_file)

        # man_file = open("man.txt",'w')
        # other_file = open("other.txt",'w')
       # missing = open("missing.txt")

        # print(man,file=man_file)
        # print(other,file=other_file)

    # except IOError as obj:
    #     print("file error:" + str(obj))
    except pickle.PickleError as pe :
        print("pickle error : " + str(pe))

    # finally:
    #     # man_file.close()
    #     # other_file.close()
    #     if 'missing' in locals():
    #         missing.close()

    print("")
    print(man)
    print(other)

    print(" ")

    data = []
    try:
        with open("man.txt","rb") as missing:
            # print(missing.readline())
            data = pickle.load(missing)
            print_lol(data)
    except IOError as obj :
        print("missing file error :" + str(obj))
    except pickle.PickleError as pe:
        print("pickle error :" + str(pe))

