from flask import blueprints, request
from restapi.query import get_data

countries_bp = blueprints.Blueprint('countries', __name__)


@countries_bp.get("/")
def get_countries():
    return get_data()


@countries_bp.get('/<int:country_id>/')
def get_country(country_id: int):
    return get_data(country_id)


@countries_bp.get('/<int:country_id>/capital')
def get_capital(id: int):
    return get_data(id, capital=True)


@countries_bp.get('/<int:country_id>/area')
def get_area(id: int):
    return get_data(id, area=True)
