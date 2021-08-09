from flask import blueprints

home_bp = blueprints.Blueprint('home', __name__)


@home_bp.get("/")
def get_home_info():
    return '''<h1>Country Area Archive</h1>
    <p>A prototype API for the areas of different countries.</p>'''
