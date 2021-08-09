from flask import Flask
from restapi.countries import countries_bp
from restapi.echo import echo_bp
from restapi.home import home_bp

app = Flask(__name__)

# Prevent sorting
app.config['JSON_SORT_KEYS'] = False

app.register_blueprint(home_bp, url_prefix='/')
app.register_blueprint(countries_bp, url_prefix='/api/v1/countries')

# Testing endpoint
app.register_blueprint(echo_bp, url_prefix='/api/v1/echo/')


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.errorhandler(500)
def page_not_found(e):
    return "<h1>404</h1><p>We cannot find the country that you requested for :/</p>", 404


if __name__ == '__main__':
    app.run(port=9532)
