import pytest
from users.models import CustomUser as User

"""Factory for users"""

@pytest.fixture()
def user_1():
    user = User.objects.create_user('Test-user')
    print('create-user')
    return user

@pytest.fixture
def new_user_factory(db):
    def create_app_user(email:str, user_name:str, password:str=None, first_name:str="firstname",
                        last_name:str="lastname", is_staff:bool=False, is_active:bool=True):
        
        user = User.objects.create_user(email=email, user_name=user_name, password=password, 
                                        first_name=first_name, last_name=last_name, is_staff=is_staff, 
                                        is_active=is_active)
        return user
    return create_app_user

@pytest.fixture
def new_superuser_factory(db):
    def create_app_user(email:str, user_name:str, password:str=None, first_name:str="firstname",
                        last_name:str="lastname", is_staff:bool=False, is_active:bool=True):
        
        user = User.objects.create_superuser(email=email, user_name=user_name, password=password, 
                                        first_name=first_name, last_name=last_name)
        return user
    return create_app_user

@pytest.fixture
def new_user(db, new_user_factory):
    return new_user_factory('uzo@Email.com', 'Uzo')

@pytest.fixture
def new_superuser(db, new_superuser_factory):
    return new_superuser_factory('emaiL', 'Uzo')
