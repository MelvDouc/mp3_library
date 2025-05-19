from flask import Blueprint as BP, render_template

bp = BP("views", __name__)


@bp.route("/")
def home() -> str:
    return render_template("home.jinja")
