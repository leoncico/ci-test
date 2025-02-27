class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_user_by_id(self, user_id):
        """Obtiene un usuario por su ID."""
        return self.user_repository.find_by_id(user_id)

    def create_user(self, user_data):
        """Crea un nuevo usuario si no existe."""
        existing_user = self.user_repository.find_by_email(user_data["email"])
        if existing_user:
            raise ValueError("El usuario ya existe")
        return self.user_repository.save(user_data)
