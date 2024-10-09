import sys 
import os.path 
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..") 
import uuid, pytest

from data.database_interface import FeedbackDTO
from usecases import feedback as uc

@pytest.fixture()
def temp_catalog_feedback(tmp_path):
    '''Создаёт временный каталог feedback для тестов.'''
    catalog = tmp_path / 'data' / 'feedback'
    catalog.mkdir(parents=True, exist_ok=True)
    return catalog

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
    recieved_data = uc.save(author_id, receiver_id, feedback_content, feedback_id, temp_catalog_feedback)

    saved_data = FeedbackDTO(temp_catalog_feedback).get_feedback_by_id(feedback_id)

    assert reference_data == saved_data