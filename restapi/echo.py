import json
from flask import blueprints, request
from restapi.query import get_data

echo_bp = blueprints.Blueprint('echo', __name__)


def get_request_info(request):
    return {"echo_information":
        {
            "path": request.url,
            "headers": dict(request.headers),
            "cookies": dict(request.cookies),
            "requesting_ip": request.environ.get('HTTP_X_REAL_IP', request.remote_addr),
        }
    }


def merge_dict(dict_a: dict, dict_b: dict):
    return {key: value for (key, value) in list(dict_a.items()) + list(dict_b.items())}


@echo_bp.get("/")
def get_echo():
    return get_request_info(request)


@echo_bp.get("/countries/")
def get_countries():
    return {**get_request_info(request), **get_data()}


@echo_bp.get('/countries/<int:country_id>/')
def get_country(country_id: int):
    return {**get_request_info(request), **get_data(country_id)}


@echo_bp.get('/countries/<int:country_id>/capital')
def get_capital(country_id: int):
    return {**get_request_info(request), **get_data(country_id, capital=True)}


@echo_bp.get('/countries/<int:country_id>/area')
def get_area(country_id: int):
    return {**get_request_info(request), **get_data(country_id, area=True)}
