from datetime import datetime
from flask import abort, current_app, render_template, request, redirect, url_for, flash
from forms import MovieEditForm, LoginForm, NewBandForm, NewUserForm, BandRequestForm, MemberRequestForm
from movie import Movie
from classes import BBUser, Band, BandRequest, MemberRequest
from flask_login import login_required, login_user, current_user, logout_user
from user import get_user
from passlib.hash import pbkdf2_sha256 as hasher


def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)

def signup_page():
    new_user = NewUserForm()
    if  request.method == "GET":
        return render_template("signup_page.html")
    db = current_app.config["db"]
    new_user.user_name = request.form["Username"]
    new_user.password = hasher.hash(request.form["Password"])
    new_user.age = request.form["Age"]
    new_user.gender = request.form["Gender"]
    new_user.instrument = request.form["Instrument"]
    new_user.city = request.form["City"]
    new_user.level = request.form["Level"]
    new_user.goal = request.form["Goal"]
    user_check = db.add_user(new_user)
    if (user_check != None):
        flash("Success!")
        return redirect(url_for("home_page"))
    else:
        flash("Username already exists!")
        return render_template("signup_page.html")

@login_required
def band_add_page():
    new_band = NewBandForm()
    if request.method == "GET":
        return render_template("new_band.html")
    db = current_app.config["db"]
    current_user_id =current_user.user_id
    new_band.band_name = request.form["Band Name"]
    new_band.city = db.get_user_city(current_user_id)
    new_band.genre = request.form["Genre"]
    new_band.level = request.form["Level"]
    band_id = db.add_band(current_user, new_band)
    if (band_id != None):
        flash("Success!")
        return redirect(url_for("home_page"))
    else:
        flash("Band already exists!")
        return render_template("new_band.html")

@login_required
def member_request_add_page():
    new_request = MemberRequestForm()
    if  request.method == "GET":
        return render_template("member_request.html")
    if form.validate_on_submit():
        db = current_app.config["db"]
        new_request.goal = request.form["Goal"]
        new_request.instrument = request.form["Instrument"]
        new_request.pref_gender = request.form["Gender"]
        ################################### CREATE BAND PAGE FIRST THEN CONTINUE FROM HERE
        
        lastrow = db.add_member_request(member_request)
        flash("Request added!")
        return render_template("member_request.html")

def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        db = current_app.config["db"]
        username = form.data["username"]
        user_id = db.get_user_id(username)
        if user_id is not None:
            user = get_user(user_id)
            password = form.data["password"]
            if hasher.verify(password, user.password):
                login_user(user)
                flash("You have logged in.")
                next_page = request.args.get("next", url_for("home_page"))
                return redirect(next_page)
        flash("Invalid credentials.")
    return render_template("login.html", form=form)


def logout_page():
    logout_user()
    flash("You have logged out.")
    return redirect(url_for("home_page"))



def member_request_page(request_id):
    
    request = db.get_member_request(request_id)
    if request is None:
        abort(404)
    return render_template("member_request.html", request=request)

def band_request_page(request_id):
    db = current_app.config["db"]
    request = db.get_band_request(request_id)
    if request is None:
        abort(404)
    return render_template("band_request.html", request=request)

def movie_page(movie_key):
    db = current_app.config["db"]
    movie = db.get_movie(movie_key)
    if movie is None:
        abort(404)
    return render_template("movie.html", movie=movie)

def member_requests_page():
    db = current_app.config["db"]
    print(current_user)
    if request.method == "GET":
        member_requests = db.get_all_member_requests()
        return render_template("member_requests.html", requests=member_requests)
    else:
        if not current_user.is_admin: #change it to check if the  current user is the creator of the form
            abort(401)
        return render_template("member_requests.html")
        #implement later
        
def band_requests_page():
    db = current_app.config["db"]
    if request.method == "GET":
        band_requests = db.get_all_band_requests()
        return render_template("band_requests.html", requests=band_requests)
    else:
        if not current_user.is_admin: #change it to check if the  current user is the creator of the form
            abort(401)
        return render_template("band_requests.html")
        #implement later
    return render_template("band_requests.html")

def movies_page():
    db = current_app.config["db"]
    if request.method == "GET":
        movies = db.get_movies()
        return render_template("movies.html", movies=sorted(movies))
    else:
        if not current_user.is_admin:
            abort(401)
        form_movie_keys = request.form.getlist("movie_keys")
        for form_movie_key in form_movie_keys:
            db.delete_movie(int(form_movie_key))
        flash("%(num)d movies deleted." % {"num": len(form_movie_keys)})
        return redirect(url_for("band_requests_page"))    

@login_required
def member_request_add_page():
    form = MemberRequestForm()
    if form.validate_on_submit():
        instrument = form.data["instrument"]
        goal = form.data["goal"]
        gender = form.data["pref_gender"]
        member_request = MemberRequest(instrument, goal, gender)
        db = current_app.config["db"]
        lastrow = db.add_member_request(member_request)
        flash("Request added!")
        return render_template("member_request.html")

@login_required
def band_request_add_page():
    form = BandRequestForm()
    if form.validate_on_submit():
        goal = form.data["goal"]
        genre = form.data["genre"]
        request = BandRequest(goal, genre)
        db = current_app.config["db"]
        lastrow = db.add_band_request()
        flash("Request added!")
        return render_template("band_request.html")


def validate_movie_form(form):
    form.data = {}
    form.errors = {}

    form_title = form.get("title", "").strip()
    if len(form_title) == 0:
        form.errors["title"] = "Title can not be blank."
    else:
        form.data["title"] = form_title

    form_year = form.get("year")
    if not form_year:
        form.data["year"] = None
    elif not form_year.isdigit():
        form.errors["year"] = "Year must consist of digits only."
    else:
        year = int(form_year)
        if (year < 1887) or (year > datetime.now().year):
            form.errors["year"] = "Year not in valid range."
        else:
            form.data["year"] = year

    return len(form.errors) == 0

