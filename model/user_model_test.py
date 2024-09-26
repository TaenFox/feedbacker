from user import User
import uuid, json
import pytest



@pytest.fixture(scope="module")
def fix_user_data():
    '''Пресет пользовательских данных'''
    return  {
        "userId": str(uuid.uuid4()),
        "sentFeedbackIds": [],
        "recievedFeedbackIds":[]
    }

def test_create_user_model(fix_user_data):
    '''Тест проверяет работоспособность класс User:
    - создание экземпляра класса
    - выдачу данных экземпляра класса как словарь'''
    assert User(fix_user_data).toDict() == fix_user_data