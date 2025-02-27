import pytest
from unittest.mock import MagicMock
from user_service import UserService

@pytest.fixture
def mock_repository():
    """Mock del repositorio de usuarios."""
    return MagicMock()

def test_get_user_by_id(mock_repository):
    """Prueba que el servicio devuelve un usuario por su ID."""
    mock_repository.find_by_id.return_value = {"id": 1, "name": "Alice"}
    
    service = UserService(mock_repository)
    user = service.get_user_by_id(1)
    
    assert user["name"] == "Alice"
    mock_repository.find_by_id.assert_called_once_with(1)

def test_create_user_success(mock_repository):
    """Prueba la creación exitosa de un usuario."""
    mock_repository.find_by_email.return_value = None  # Simula que el usuario no existe
    mock_repository.save.return_value = {"id": 2, "name": "Bob", "email": "bob@example.com"}

    service = UserService(mock_repository)
    user_data = {"name": "Bob", "email": "bob@example.com"}
    user = service.create_user(user_data)

    assert user["name"] == "Bob"
    mock_repository.save.assert_called_once_with(user_data)

def test_create_user_already_exists(mock_repository):
    """Prueba que no se cree un usuario duplicado."""
    mock_repository.find_by_email.return_value = {"id": 3, "name": "Charlie", "email": "charlie@example.com"}

    service = UserService(mock_repository)
    user_data = {"name": "Charlie", "email": "charlie@example.com"}

    with pytest.raises(ValueError, match="El usuario ya existe"):
        service.create_user(user_data)
    
    mock_repository.save.assert_not_called()
