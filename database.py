from movie import Movie
from classes import BBUser, Band, BandRequest, MemberRequest
from flask_mysqldb import MySQL
from user import User


class Database:
    def __init__(self, app):
        self.db = MySQL(app)

    def add_user(self, user):
        if (self.get_user(user.user_name) is None):
            cursor = self.db.connection.cursor()
            query = "INSERT INTO player (user_name, password, instrument, city, level, age, gender, goal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(query, (user.user_name, user.password, user.instrument, user.city, user.level, user.age, user.gender, user.goal))
            cursor.connection.commit()
            lastrowid = cursor.lastrowid
            print(lastrowid)
            return lastrowid
        else:
            return None

        

    def add_band(self, user, band):
        cursor = self.db.connection.cursor()
        query = "INSERT INTO band (band_name, leader, genre, level, city) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(query, (band.band_name, user.user_name, band.genre, band.level, band.city))
        connection.commit()
        lastrowid = cursor.lastrowid
        return lastrowid

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
        query = "SELECT * FROM player WHERE user_name = %s;"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        if user is not None:
            return user
        else: 
            return None

    def get_user_with_id(self, user_id):
        cursor = self.db.connection.cursor()
        query = "SELECT * FROM player WHERE user_id = %s;"
        cursor.execute(query, (user_id,))
        user_id = cursor.fetchone()
        if user_id is not None:
            return user_id
        else: 
            return None

    def get_user_id(self, username):
        cursor = self.db.connection.cursor()
        query = "SELECT user_id FROM player WHERE user_name = %s;"
        cursor.execute(query, (username,))
        user_id = cursor.fetchone()
        if user_id is not None:
            return user_id
        else: 
            return None

    def get_all_bands():
        cursor = self.db.connection.cursor()
        #use join to get the city of the leader

    
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

