from schema import Schema, Optional

countries_schema = Schema(
    {
        "echo_information": {
            "path": str,
            "headers": {
                "Host": str,
                Optional("Upgrade-Insecure-Requests"): str,
                "Accept": str,
                "User-Agent": str,
                Optional("Accept-Language"): str,
                "Accept-Encoding": str,
                "Connection": str
            },
            "cookies": {},
            "requesting_ip": str
        },
        "countries": [
            {
                "country_code": str,
                "capital": str,
                "total_area": int
            }
        ]
    }
)

country_schema = Schema(
    {
        "echo_information": {
            "path": str,
            "headers": {
                "Host": str,
                Optional("Upgrade-Insecure-Requests"): str,
                "Accept": str,
                "User-Agent": str,
                Optional("Accept-Language"): str,
                "Accept-Encoding": str,
                "Connection": str
            },
            "cookies": {},
            "requesting_ip": str
        },
        "country_code": str,
        "capital": str,
        "total_area": int
    }
)

area_schema = Schema(
    {
        "echo_information": {
            "path": str,
            "headers": {
                "Host": str,
                Optional("Upgrade-Insecure-Requests"): str,
                "Accept": str,
                "User-Agent": str,
                Optional("Accept-Language"): str,
                "Accept-Encoding": str,
                "Connection": str
            },
            "cookies": {},
            "requesting_ip": str
        },
        "total_area": float
    }
)

capital_schema = Schema(
    {
        "echo_information": {
            "path": str,
            "headers": {
                "Host": str,
                Optional("Upgrade-Insecure-Requests"): str,
                "Accept": str,
                "User-Agent": str,
                Optional("Accept-Language"): str,
                "Accept-Encoding": str,
                "Connection": str
            },
            "cookies": {},
            "requesting_ip": str
        },
        "capital": str,
    }
)
