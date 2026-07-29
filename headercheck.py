import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy",
    "Permissions-Policy",
    "Cache-Control"
]


def check_security_headers(url):
    response = requests.get(url, timeout=10)

    result = {}

    for header in SECURITY_HEADERS:
        result[header] = header in response.headers

    return result