import pytest
from django.http import HttpRequest
from rest_framework.test import APIClient


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def http_request() -> HttpRequest:
    """
    Fixture to provide a mock HttpRequest object.
    """
    request = HttpRequest()
    request.method = "GET"
    request.path = "/test-url/"
    return request
