import pytest
from users.models import CustomUser as User

"""Factory for users"""

@pytest.fixture
def new_user_factory(db):
    def create_app_user(email:str, 
                        username:str, 
                        first_name:str="firstname",
                        password:str=None,
                        last_name:str="lastname", 
                        is_staff:bool=False, 
                        is_active:bool=True):
        
        user = User.objects.create_user(email=email, 
                                        user_name=username, 
                                        first_name=first_name, 
                                        password=password,
                                        last_name=last_name, 
                                        is_staff=is_staff, 
                                        is_active=is_active)
        return user
    return create_app_user

@pytest.fixture
def new_user(db, new_user_factory):
    return new_user_factory('newuser@email.com', 'Username', 'firstname', 'password', 'lastname')

@pytest.fixture
def new_user_no_email(db, new_user_factory):
    return new_user_factory('', 'uzo1','Uzo', 'passw')

@pytest.fixture
def new_superuser(db): 
    user = User.objects.create_superuser(email='dave@email.coM', 
                                         user_name='Dave10', 
                                        first_name='David', 
                                        last_name='',
                                        password=None)
       
    return user
