from classes import BBUser, Band, BandRequest, MemberRequest
from user import User
import mysql.connector

class Database:
#database_url = cleardb-opaque-75368
#'mysql://adffdadf2341:adf4234@us-cdbr-east.cleardb.com/heroku_db?reconnect=true'
#BandBuddy21
#username = b8aad7ed118563
#password = 993e9bb8
#host = eu-cdbr-west-03.cleardb.net
    def add_user(self, user):
        if (self.get_user(user.user_name) is None):
            cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
            cursor = cnx.cursor()
            query = "INSERT INTO player (user_name, password, instrument, city, level, age, gender, goal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(query, (user.user_name, user.password, user.instrument, user.city, user.level, user.age, user.gender, user.goal))
            cnx.commit()
            lastrowid = cursor.lastrowid
            cnx.close()
            return lastrowid
        else:
            return None

    def add_band(self, user, band):
        if (self.get_band(band.band_name) == None):
            cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
            cursor = cnx.cursor()
            query = "INSERT INTO band (band_name, leader, genre, level) VALUES (%s, %s, %s, %s);"
            cursor.execute(query, (band.band_name, user.username, band.genre, band.level))
            cnx.commit()
            lastrowid = cursor.lastrowid
            cnx.close()
            return lastrowid
        else:
            return None

    def add_member_request(self, user, band, request, timenow):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "INSERT INTO member_request (band_id, instrument, request_date, gender_pref, goal) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(query, (band[0], request.instrument, timenow, request.pref_gender, request.goal))
        cnx.commit()
        lastrow = cursor.lastrowid
        cnx.close()
        return lastrow

    def add_band_request(self, user, request, timenow):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "INSERT INTO band_request (creator_id, instrument, request_date, goal, genre) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(query, (user[0], user[4], timenow, request.goal, request.genre))
        cnx.commit()
        lastrow = cursor.lastrowid
        cnx.close()
        return lastrow

    def get_all_cities(self):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "SELECT * FROM city ORDER BY city_name;"
        cursor.execute(query)
        data = cursor.fetchall()
        cnx.close()
        return data

    def get_city(self, cityname):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "SELECT * FROM city WHERE city_name = %s;"
        cursor.execute(query, (cityname))
        city = cursor.fetchone()
        cnx.close()
        if city is not None:
            return city
        else: 
            return None

    def get_user(self, username):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "SELECT * FROM player WHERE user_name = %s;"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        cnx.close()
        if user is not None:
            return user
        else: 
            return None

    def get_user_with_id(self, user_id):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "SELECT * FROM player WHERE user_id = %s;"
        cursor.execute(query, (user_id,))
        user_id = cursor.fetchone()
        cnx.close()
        if user_id is not None:
            return user_id
        else: 
            return None

    def get_band(self, band_name):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "SELECT * FROM band WHERE band_name = %s;"
        cursor.execute(query, (band_name,))
        band = cursor.fetchone()
        cnx.close()
        if band is not None:
            return band
        else: 
            return None

    def get_band_with_username(self, username):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "SELECT * FROM band WHERE leader = %s;"
        cursor.execute(query, (username,))
        band = cursor.fetchone()
        cnx.close()
        if band is not None:
            return band
        else: 
            return None

    def get_user_id(self, username):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "SELECT user_id FROM player WHERE user_name = %s;"
        cursor.execute(query, (username,))
        user_id = cursor.fetchone()
        cnx.close()
        if user_id is not None:
            return user_id
        else: 
            return None

    def get_user_city(self, user_id):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "SELECT city FROM player WHERE user_id = %s;"
        cursor.execute(query, (user_id,))
        user_city = cursor.fetchone()
        cnx.close()
        if user_city is not None:
            return user_city
        else: 
            return None

    def increment_city_player_number(self, city_name):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "SELECT number_of_players FROM city WHERE city_name = %s;"
        cursor.execute(query, (city_name,))
        player_number = cursor.fetchone()[0]
        player_number +=1
        query = "UPDATE city SET number_of_players = %s WHERE city_name = %s;"
        cursor.execute(query, (player_number, city_name))
        cnx.commit()
        cnx.close()

    def increment_city_band_number(self, city_name):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "SELECT number_of_bands FROM city WHERE city_name = %s;"
        cursor.execute(query, (city_name,))
        band_number = cursor.fetchone()[0]
        band_number += 1
        query = "UPDATE city SET number_of_bands = %s WHERE city_name = %s;"
        cursor.execute(query, (band_number, city_name))
        cnx.commit()
        cnx.close()


    def get_all_bands(self):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "SELECT band.band_name, player.city, band.leader, band.genre, band.level FROM band INNER JOIN player ON band.leader = player.user_name;"
        cursor.execute(query)
        bands = cursor.fetchall()
        cnx.commit()
        cnx.close()
        return bands

    
    def get_all_band_requests(self):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "SELECT player.user_name, band_request.instrument, band_request.goal, band_request.genre, band_request.request_date FROM band_request INNER JOIN player ON band_request.creator_id = player.user_id ORDER BY band_request.request_date"
        cursor.execute(query)
        requests = cursor.fetchall()
        cnx.commit()
        cnx.close()
        return requests

    def get_all_member_requests(self):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "SELECT band.band_name, member_request.instrument, member_request.gender_pref, member_request.goal, member_request.request_date FROM member_request JOIN band ON member_request.band_id = band.band_id ORDER BY member_request.request_date"
        cursor.execute(query)
        data = cursor.fetchall()
        cnx.close()
        return data

    def get_band_request(self, request_id):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "SELECT * FROM band_request WHERE request_id = %s;"
        cursor.execute(query, (request_id,))
        request = cursor.fetchone()
        cnx.close()
        if request is not None:
            return request
        else: 
            return None

    def get_member_request(self, request_id):
        cnx = mysql.connector.connect(user="b8aad7ed118563", password="993e9bb8", host="eu-cdbr-west-03.cleardb.net", database="heroku_2fac82585434521")
        cursor = cnx.cursor()
        query = "SELECT * FROM member_request WHERE request_id = %s;"
        cursor.execute(query, (request_id,))
        request = cursor.fetchone()
        cnx.close()
        if request is not None:
            return request
        else: 
            return None