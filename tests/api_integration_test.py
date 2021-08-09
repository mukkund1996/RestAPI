import requests
import pytest
import socket

from tests.response_schema import countries_schema, country_schema, area_schema, capital_schema


def test_get_countries():
    url = f"http://127.0.0.1:9532/api/v1/echo/countries/"
    response = requests.get(url)

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200

    # Validate response content type header
    assert response.headers["Content-Type"] == "application/json"

    response_body = response.json()

    # Validating the schema of the response JSON
    countries_schema.validate(response_body)

    # Validating the IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    assert response_body["echo_information"]["requesting_ip"] == ip_address

    # Validating the url
    assert response_body["echo_information"]["path"] == url


@pytest.mark.parametrize("country_id", [1, 2, 4, 5, 10])
def test_get_country(country_id):
    url = f"http://127.0.0.1:9532/api/v1/echo/countries/{country_id}/"
    response = requests.get(url)

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200

    # Validate response content type header
    assert response.headers["Content-Type"] == "application/json"

    response_body = response.json()

    # Validating the schema of the response JSON
    country_schema.validate(response_body)

    # Validating the IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    assert response_body["echo_information"]["requesting_ip"] == ip_address

    # Validating the url
    assert response_body["echo_information"]["path"] == url


@pytest.mark.parametrize("country_id", [1, 2, 4, 5, 10])
def test_get_capital(country_id):
    url = f"http://127.0.0.1:9532/api/v1/echo/countries/{country_id}/capital"
    response = requests.get(url)

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200

    # Validate response content type header
    assert response.headers["Content-Type"] == "application/json"

    response_body = response.json()

    # Validating the schema of the response JSON
    capital_schema.validate(response_body)

    # Validating the IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    assert response_body["echo_information"]["requesting_ip"] == ip_address

    # Validating the url
    assert response_body["echo_information"]["path"] == url


@pytest.mark.parametrize("country_id", [1, 2, 4, 5, 10])
def test_get_area(country_id):
    url = f"http://127.0.0.1:9532/api/v1/echo/countries/{country_id}/area"
    response = requests.get(url)

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200

    # Validate response content type header
    assert response.headers["Content-Type"] == "application/json"

    response_body = response.json()

    # Validating the schema of the response JSON
    area_schema.validate(response_body)

    # Validating the IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    assert response_body["echo_information"]["requesting_ip"] == ip_address

    # Validating the url
    assert response_body["echo_information"]["path"] == url


@pytest.mark.parametrize("url", [
    "http://localhost:9532/api/v1/echo/countrie",  # Typo in the subdomain
    "http://localhost:9532/api/v1/countrie",
    "http://localhost:9532/api/v1/countries/area",  # Missing index
    "http://localhost:9532/api/v1/echo/countries/1000",  # Invalid index
    "http://localhost:9532/api/v1/countries/10000",
])
def test_resource_error(url):
    response = requests.get(url)
    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 404