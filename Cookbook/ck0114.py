"""Sorting Objects Without Native Comparison Support"""


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User{}'.format(self.user_id)


"""Solved 1"""
users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=lambda x: x.user_id))

"""Solved 2"""
from operator import attrgetter

print(sorted(users, key=attrgetter('user_id')))

"""lambda or attrgetter()  may be one of personal preference ,However ,attrgetter() is often a tad bit faster and also
    has the added feature of allowing multiple fields to be extracted simultaneously"""
