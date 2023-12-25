from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework import status
import pytest
from store.models import Collection
from model_bakery import baker



@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection


@pytest.fixture
def authenticate(api_client):
    def do_authentication(is_staff=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff))
    return do_authentication

@pytest.mark.django_db
class TestCreateCollection:
    # this below function test is written for understanding the concept of pytest
    # @pytest.mark.skip # Use this to skip the test
    def test_if_user_is_anonymous_return_401(self):
        #AAA - (Arange, Act, Asert)

        #Arange

        #Act 
        client = APIClient()
        response =  client.post('/store/collections/', {'title':'a'})

        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_return_403(self, authenticate, create_collection):
        authenticate()
        response = create_collection({'title':'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_data_is_invalid_return_400(self, authenticate, create_collection):
        authenticate(is_staff=True)
        response = create_collection({'title':''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None
        

    def test_if_data_is_valid_return_201(self, authenticate, create_collection):
        authenticate(is_staff=True)
        response = create_collection({'title':'a'})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_returns_200(self, api_client):
        #Arrange
        collection = baker.make(Collection)

        #Act
        response = api_client.get(f'/store/collections/{collection.id}/')

        #Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id, 
            'title': collection.title, 
            'products_count':0
        }
