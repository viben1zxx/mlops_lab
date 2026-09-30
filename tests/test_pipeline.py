import pytest


@pytest.mark.parametrize("batch_size, expected_shape", [(32, (32, 10)), (64, (64, 10))])
def test_batch_generator(mocker, batch_size, expected_shape):
    mock_db = mocker.MagicMock()
    mock_db.fetch.return_value = [0] * expected_shape[0]
    
    assert len(mock_db.fetch()) == batch_size
