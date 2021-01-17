class BBUser:
    def __init__(self, username, password, age, gender, instrument, city, level, goal):
        self.username = username
        self.password = password
        self.age = age
        self.gender = gender
        self.instrument = instrument
        self.city = city
        self.level = level
        self.goal = goal

class Band:
    def __init__(self, band_name, leader, genre, level, city):
        self.band_name = band_name
        self.leader = leader
        self.genre = genre
        self.level = level
        self.city = city

class BandRequest:
    def __init__(self, instrument, goal, genre):
        self.instrument = instrument
        self.goal = goal
        self.genre = genre

class MemberRequest:
    def __init__(self, instrument, goal, gender_pref=None):
        self.instrument = instrument
        self.goal = goal
        self.gender_pref = gender_pref
        