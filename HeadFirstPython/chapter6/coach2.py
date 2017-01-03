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
        return data.strip().split(',')
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return None


james = get_coach_data('james2.txt')
james_dict = {}
james_dict["Name"] = james.pop(0)
james_dict["Dob"] = james.pop(0)
james_dict["Times"] = james
print(james_dict["Name"] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in james_dict["Times"]]))[0:3]))

julie = get_coach_data('julie2.txt')
julie_dict = {}
julie_dict["Name"] = julie.pop(0)
julie_dict["Dob"] = julie.pop(0)
julie_dict["Times"] = julie
print(julie_dict["Name"] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in julie_dict["Times"]]))[0:3]))

mikey = get_coach_data('mikey2.txt')
mikey_dict = {}
mikey_dict["Name"] = mikey.pop(0)
mikey_dict["Dob"] = mikey.pop(0)
mikey_dict["Times"] = mikey
print(mikey_dict["Name"] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in mikey_dict["Times"]]))[0:3]))

sarah = get_coach_data('sarah2.txt')
sarah_dict = {}
sarah_dict["Name"] = sarah.pop(0)
sarah_dict["Dob"] = sarah.pop(0)
sarah_dict["Times"] = sarah
print(sarah_dict["Name"] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah_dict["Times"]]))[0:3]))
