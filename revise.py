import os


def sanitize_data(time):
    if '-' in time:
        delimiter = "-"
    elif ':' in time:
        delimiter = ':'
    else:
        return time
    (mins,secs) = time.split(delimiter)
    return mins + '.' + secs


def get_coach_data(file):

    for each_line in file:
        data = each_line.strip(" ").split(",")
        record = {'name':data.pop(0),'dob':data.pop(0),'record' : sorted(set([sanitize_data(each_t) for each_t in data]))[0:3]}
    return record

if __name__ == '__main__':

    # os.chdir("D:\python\chapter3")
    #
    # man = []
    # other = []
    #
    # try:
    #     file = open("sketch.txt")
    #
    #
    #     for each_line in file:
    #
    #         try:
    #             (role, said) = each_line.split(":", 1)
    #             print(role, end='')
    #             print(said)
    #             if role == 'Man':
    #                 man.append(said)
    #             elif role == 'Other Man':
    #                 other.append(said)
    #         except ValueError as obj:
    #             print("does not contain :" + str(obj))
    #
    #     #writing to file.
    #     try:
    #         f = open("test.txt", "w")
    #         f.write(str(man))
    #         f.write(str(other))
    #     except IOError as obj:
    #         print("cannot write to file", str(obj))
    # except IOError as obj:
    #     print("file does not exists." + str(obj))

    #Data Comprehension.

    #read 4 files and print them

    os.chdir("D:\python\chapter3")
    james = open("james.txt")
    mikey = open("mikey.txt")
    julie = open("julie.txt")
    sarah = open("sarah.txt")

    jamesRecordMap = get_coach_data(james)

    # for each_line in mikey:
    #     data = each_line.strip(" ").split(",")
    #     mikeyRecordMap = {'name':data.pop(0),'dob':data.pop(0),'record' : data}
    #
    # for each_line in julie:
    #     data = each_line.strip(" ").split(",")
    #     julieRecordMap = {'name':data.pop(0),'dob':data.pop(0),'record' : data}
    #
    # for each_line in sarah:
    #     data = each_line.strip(" ").split(",")
    #     sarahRecordMap = {'name':data.pop(0),'dob':data.pop(0),'record' : data}

    print(jamesRecordMap)
    # print(mikeyRecordMap)
    # print(julieRecordMap)
    # print(sarahRecordMap)

