import os

class Athelete :
    def __init__(self,name,dob = None,times = []):
        self.name = name
        self.dob = dob
        self.times = times

    def getTimes(self):
        sorted(set([sanitize(each_t) for each_t in self.times])[0:3])

    def add_time(self,time_list):
        self.times.append(time_list)


    def add_times(self,time_lists):
        self.times.extend(time_lists)

class AtheleteList(list) :

    def __init__(self,name,dob = None,times = []):
        list.__init__(times)
        self.name = name
        self.dob = dob
        self.extend(times)

    def getTimes(self):
        sorted(set([sanitize(each_t) for each_t in self])[0:3])



def sanitize(time_string):
    if ':' in time_string:
        splitter = ':'
    elif '-' in time_string:
        splitter = '-'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)

    return mins + "." + secs


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.read().strip().split(",")
            obj =  AtheleteList(data.pop(0),data.pop(0),data)

            # data_dict = {'name': data.pop(0), 'dob': data.pop(0), 'times': str(sorted(set([sanitize(each_t) for each_t in data]))[0:3])}

        # return data_dict['name'] + " fastest time is " + data_dict['times']
        return obj.name + "fastest time is " + obj.getTimes()
    except IOError as errorobj:
        print("file not found : " + str(errorobj))
        return None


if __name__ == '__main__':

    os.chdir("D:\python\chapter3")
    # with open("julie.txt", "r") as julie, open("james.txt", "r") as james, open("mikey.txt", "r") as mikey,\
    #         open("sarah.txt", "r") as sarah:
    julie_list = get_coach_data("julie.txt") # sorted(julie.read().strip().split(","))
    print(julie_list)
    james_list = get_coach_data("james.txt")
    print(james_list)
    mikey_list = get_coach_data("mikey.txt")
    print(mikey_list)
    sarah_list = get_coach_data("sarah.txt")
    # (sarah_name, sarah_dob) = sarah_list.pop(0), sarah_list.pop(0)
    # sarah_data = {'name': sarah_list.pop(0), "DOB": sarah_list.pop(0), "Times": sarah_list}

    # clean_julie = []
    # clean_james = []
    # clean_mikey = []
    # clean_sarah = []
    #
    # for each_t in julie_list:
    #     clean_julie.append(sanitize(each_t))
    # for each_t in james_list:
    #     clean_james.append(sanitize(each_t))
    # for each_t in mikey_list:
    #     clean_mikey.append(sanitize(each_t))
    # for each_t in sarah_list:
    #     clean_sarah.append(sanitize(each_t))

    # clean_julie = sorted([sanitize(each_t) for each_t in julie_list])
    # clean_james = sorted([sanitize(each_t) for each_t in james_list])
    # clean_mikey = sorted([sanitize(each_t) for each_t in mikey_list])
    #
    # clean_sarah = sorted([sanitize(each_t) for each_t in sarah_list])
    #
    # print("  ")
    # print(clean_julie)
    # print(clean_james)
    # print(clean_mikey)
    # print(clean_sarah)
    #
    # # top three times
    # julie_top3 = []
    # james_top3 = []
    # mikey_top3 = []
    # sarah_top3 = []
    # for each_t in clean_julie:
    #     if each_t not in julie_top3:
    #         julie_top3.append(each_t)
    #
    # for each_t in clean_james:
    #     if each_t not in james_top3:
    #         james_top3.append(each_t)
    #
    # for each_t in clean_mikey:
    #     if each_t not in mikey_top3:
    #         mikey_top3.append(each_t)
    #
    # for each_t in clean_sarah:
    #     if each_t not in sarah_top3:
    #         sarah_top3.append(each_t)
    #
    # print(julie_top3[0:3])
    # print(james_top3[0:3])
    # print(mikey_top3[0:3])
    # print(sarah_name + " fastest 3 records are " + str(sarah_top3[0:3]))
    # print(sarah_data['name'] + " fastest 3 records are " + str(sarah_data['Times'][0:3]))
