import sys 
import os.path 
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..") 
import uuid, pytest

from data.database_interface import FeedbackDTO, UserDTO
from usecases import feedback as uc_feedback, user as uc_user
from model.user import User as UserObj

@pytest.fixture()
def temp_catalog_feedback(tmp_path):
    '''Создаёт временный каталог feedback для тестов.'''
    catalog_feedback = tmp_path / 'data' / 'feedback'
    catalog_feedback.mkdir(parents=True, exist_ok=True)
    return catalog_feedback

@pytest.fixture()
def temp_catalog_user(tmp_path):
    '''Создаёт временный каталог user для тестов.'''
    catalog_user = tmp_path / 'data' / 'user'
    catalog_user.mkdir(parents=True, exist_ok=True)
    return catalog_user

def test_data_sent_with_feedback(temp_catalog_feedback):
    feedback_id = str(uuid.uuid4())
    author_id = str(uuid.uuid4())
    receiver_id = str(uuid.uuid4())
    feedback_content = "test context string"
    reference_data = {
        "feedback_id": feedback_id,
        "content": feedback_content,
        "author_id": author_id,
        "receiver_id": receiver_id
    }
    uc_feedback.save(
        author_id, receiver_id, feedback_content, feedback_id, temp_catalog_feedback)
    saved_data = FeedbackDTO(temp_catalog_feedback).get_feedback_by_id(feedback_id)
    assert reference_data == saved_data

def test_create_new_user(temp_catalog_user):
    result_user:UserObj = uc_user.new(temp_catalog_user)
    result_data = result_user.to_dict()
    user_id = result_data['user_id']

    saved_data = UserDTO(temp_catalog_user).get_user_by_id(user_id)
    assert result_data == saved_data

def test_is_exist_user_true(temp_catalog_user):
    some_user:UserObj = uc_user.new(temp_catalog_user)
    existing_user_id = some_user.user_id
    result = uc_user.is_exist(existing_user_id, temp_catalog_user)
    assert result==True

def test_is_exist_user_false(temp_catalog_user):
    some_id = str(uuid.uuid4())
    result = uc_user.is_exist(some_id, temp_catalog_user)
    assert result==False

def test_get_user(temp_catalog_user):
    new_user:UserObj = uc_user.new(temp_catalog_user)
    get_user:UserObj = uc_user.get(new_user.user_id, temp_catalog_user)
    assert new_user.to_dict() == get_user.to_dict()

def test_modify_user(temp_catalog_user):
    new_user:UserObj = uc_user.new(temp_catalog_user)
    modified_data = new_user.to_dict()
    modified_data["sent_feedback_ids"].append("test value")
    modified_user:UserObj = uc_user.modify(new_user, temp_catalog_user)
    assert modified_data == modified_user.to_dict()