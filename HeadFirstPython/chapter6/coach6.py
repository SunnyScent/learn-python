class AthleteList(list):
    def __init__(self, a_name, a_dob, a_times):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted(set(sanitize(t) for t in self))[0:3]


def sanitize(time_string):
    """This function to format the time_string"""
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        data = data.strip().split(',')
        return AthleteList(data.pop(0), data.pop(0), data)
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return None

james = get_coach_data('james2.txt')
print(james.name + "'s fastest times are: " + str(james.top3()))

julie = get_coach_data('julie2.txt')
print(julie.name + "'s fastest times are: " + str(julie.top3()))

mikey = get_coach_data('mikey2.txt')
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))

sarah = get_coach_data('sarah2.txt')
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))
