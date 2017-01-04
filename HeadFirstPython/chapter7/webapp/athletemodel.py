import pickle
from HeadFirstPython.chapter7.webapp.athletelist import AthleteList


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        data = data.strip().split(',')
        return AthleteList(data.pop(0), data.pop(0), data)
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return None


def put_to_store(files_list):
    """put all athletes to store in pickle"""
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athlete.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)

    except IOError as ioerr:
        print('File error(put_to_store):' + str(ioerr))
    return all_athletes


def get_from_store():
    all_athlete = {}
    try:
        with open('athlete.pickle', 'rb') as athf:
            all_athlete = pickle.load(athf)
    except IOError as ioerr:
        print('File eroor (get_from_store)：' + str(ioerr))
    return all_athlete
