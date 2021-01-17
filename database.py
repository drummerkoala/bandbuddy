from movie import Movie
from classes import BBUser, Band, BandRequest, MemberRequest
from flask_mysqldb import MySQL
from user import User


class Database:
    def __init__(self, app):
        self.db = MySQL(app)
        self.movies = {}
        self._last_movie_key = 0

    def add_user(self, user):
        cursor = self.db.connection.cursor()
        query = "INSERT INTO player (user_name, band_id, instrument, city, level, age, gender, goal) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(query, (user.user_name, user.band_id, user.instrument, user.city, user.level, user.age, user.gender, user.goal))
        connection.commit()
        lastrow = cursor.lastrowid
        return lastrow

    def add_band(self, user, band):
        cursor = self.db.connection.cursor()
        query = "INSERT INTO band (band_name, leader, genre, level, city) VALUES (?, ?, ?, ?, ?);"
        cursor.execute(query, (band.band_name, user.user_name, band.genre, band.level, band.city))
        connection.commit()
        lastrow = cursor.lastrowid
        return lastrow

    def add_member_request(self, user, band, request, timenow):
        cursor = self.db.connection.cursor()
        query = "INSERT INTO member_request (band_id, instrument, request_date, gender_pref, goal) VALUES (?, ?, ?, ?, ?);"
        cursor.execute(query, (band.band_id, request.instrument, timenow, request.gender_pref, request.goal))
        connection.commit()
        lastrow = cursor.lastrowid
        return lastrow

    def add_band_request(self, user, request, timenow):
        cursor = self.db.connection.cursor()
        query = "INSERT INTO band_request (creator_id, instrument, request_date, goal, genre) VALUES (?, ?, ?, ?, ?);"
        cursor.execute(query, (user.user_id, request.instrument, timenow, request.goal, request.genre))
        connection.commit()
        lastrow = cursor.lastrowid
        return lastrow

    def get_all_cities(self):
        cursor = self.db.connection.cursor()
        query = "SELECT * FROM city ORDER BY city_name;"
        cursor.execute(query)
        data = cursor.fetchall()
        return data

    def get_city(self, cityname):
        cursor = self.db.connection.cursor()
        query = "SELECT * FROM city WHERE city_name = ?;"
        cursor.execute(query, (cityname))
        city = cursor.fetchone()
        if city is not None:
            return city
        else: 
            return None

    def get_user(self, username):
        cursor = self.db.connection.cursor()
        query = "SELECT * FROM player WHERE user_name = ?;"
        cursor.execute(query, (username))
        user = cursor.fetchone()
        if user is not None:
            return user
        else: 
            return None

    
    def get_all_band_requests(self):
        cursor = self.db.connection.cursor()
        query = "SELECT * FROM band_request ORDER BY request_date;"
        cursor.execute(query)
        data = cursor.fetchall()
        return data

    def get_all_member_requests(self):
        cursor = self.db.connection.cursor()
        query = "SELECT * FROM member_request ORDER BY request_date;"
        cursor.execute(query)
        data = cursor.fetchall()
        return data

    def get_band_request(self, request_id):
        cursor = self.db.connection.cursor()
        query = "SELECT * FROM band_request WHERE request_id = ?;"
        cursor.execute(query, (request_id))
        request = cursor.fetchone()
        if request is not None:
            return request
        else: 
            return None

    def get_member_request(self, request_id):
        cursor = self.db.connection.cursor()
        query = "SELECT * FROM member_request WHERE request_id = ?;"
        cursor.execute(query, (request_id))
        request = cursor.fetchone()
        if request is not None:
            return request
        else: 
            return None

    def delete_member_request(self, request_id):
        cursor = self.db.connection.cursor()
        query = "DELETE FROM member_request WHERE request_id = ?;"
        cursor.execute(query, (request_id))

    def delete_band_request(self, request_id):
        cursor = self.db.connection.cursor()
        query = "DELETE FROM band_request WHERE request_id = ?;"
        cursor.execute(query, (request_id))

