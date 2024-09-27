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
    '''Тест проверяет работоспособность класса User:
    - создание экземпляра класса
    - выдачу данных экземпляра класса как словарь'''
    assert User(fix_user_data).toDict() == fix_user_data

def test_wrong_type_user_id(fix_user_data):
    '''Тест проверяет корректность отработки исключения 
    на строковый тип данных в поле userId'''
    wrong_data = fix_user_data
    wrong_data["userId"] = uuid.uuid4()
    with pytest.raises(Exception):
        User(wrong_data)

def test_wrong_type_sent_feedback_ids(fix_user_data):
    '''Тест проверяет корректность отработки исключения 
    на тип данных список в поле sentFeedbackIds'''
    wrong_data = fix_user_data
    wrong_data["sentFeedbackIds"] = "test_string"
    with pytest.raises(Exception):
        User(wrong_data)