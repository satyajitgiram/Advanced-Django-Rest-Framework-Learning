from rest_framework.test import APIClient
from rest_framework import status
import pytest


@pytest.mark.django_db
class TestCreateCollection:
    # @pytest.mark.skip # Use this to skip the test
    def test_if_user_is_anonymous_return_401(self):
        #AAA - (Arange, Act, Asert)

        #Arange

        #Asert 
        client = APIClient()
        response =  client.post('/store/collections/', {'title':'a'})

        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED