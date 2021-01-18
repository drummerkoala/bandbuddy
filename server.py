from flask import Flask
from flask_login import LoginManager

import views
from database import Database
from movie import Movie
from user import get_user


lm = LoginManager()


@lm.user_loader
def load_user(user_id):
    return get_user(user_id)


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/login", view_func=views.login_page, methods=["GET", "POST"])
    app.add_url_rule("/logout", view_func=views.logout_page)
    app.add_url_rule("/band_requests", view_func=views.band_requests_page, methods=["GET", "POST"])
    app.add_url_rule("/member_requests", view_func=views.member_requests_page, methods=["GET", "POST"])
    app.add_url_rule("/new_member_request", view_func=views.member_request_add_page, methods=["GET", "POST"])
    app.add_url_rule("/new_band_request", view_func=views.band_request_add_page, methods=["GET", "POST"])
    app.add_url_rule("/signup", view_func=views.signup_page, methods=["GET", "POST"])
    lm.init_app(app)
    lm.login_view = "login_page"

    db = Database(app)
    app.config["db"] = db

    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)