import requests

class UserAPI:
    BASE_URL = 'https://jsonplaceholder.typicode.com/users'

    @staticmethod
    def get_users():
        """Retrieve a list of users."""
        try:
            response = requests.get(UserAPI.BASE_URL)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro ao obter usuários: {e}")
            return []

    @staticmethod
    def get_user_tasks(user_id):
        """Retrieve tasks for a specific user."""
        try:
            response = requests.get(f'{UserAPI.BASE_URL}/{user_id}/todos')
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro ao obter tarefas para o usuário {user_id}: {e}")
            return []

    @staticmethod
    def create_user(user_data):
        """Create a new user."""
        try:
            response = requests.post(UserAPI.BASE_URL, json=user_data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro ao criar usuário: {e}")
            return {}

    @staticmethod
    def get_user(user_id):
        """Retrieve a single user by ID."""
        try:
            response = requests.get(f'{UserAPI.BASE_URL}/{user_id}')
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro ao obter usuário {user_id}: {e}")
            return {}

    @staticmethod
    def update_user(user_id, user_data):
        """Update an existing user by ID."""
        try:
            response = requests.patch(f'{UserAPI.BASE_URL}/{user_id}', json=user_data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro ao atualizar usuário {user_id}: {e}")
            return {}

    @staticmethod
    def delete_user(user_id):
        """Delete a user by ID."""
        try:
            response = requests.delete(f'{UserAPI.BASE_URL}/{user_id}')
            response.raise_for_status()
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"Erro ao deletar usuário {user_id}: {e}")
            return False

def display_options():
    """Display the menu options."""
    print("Opções:")
    print("1 - Ver todos os usuários")
    print("2 - Ver tarefas de um usuário")
    print("3 - Operações com usuários (CRUD)")

def show_users():
    """Display all users."""
    users = UserAPI.get_users()
    if users:
        for user in users:
            print(f"{user['id']} - {user['username']}")

def show_tasks(user_id):
    """Display tasks of a specific user."""
    tasks = UserAPI.get_user_tasks(user_id)
    if tasks:
        for task in tasks:
            print(f"Tarefa: {task['title']}")

def create_user():
    """Create a new user."""
    name = input("Nome do usuário: ")
    new_user = {
        "name": name,
        "username": name,
        "email": "exemplo@dominio.com"
    }
    user = UserAPI.create_user(new_user)
    if user:
        print(f"Usuário criado: {user}")

def read_user(user_id):
    """Read and display a user by ID."""
    user = UserAPI.get_user(user_id)
    if user:
        print(f"Usuário {user_id}: {user}")

def update_user(user_id):
    """Update a user's information."""
    new_name = input("Novo nome do usuário: ")
    user_data = {"username": new_name}
    user = UserAPI.update_user(user_id, user_data)
    if user:
        print(f"Usuário atualizado: {user}")

def delete_user(user_id):
    """Delete a user by ID."""
    if UserAPI.delete_user(user_id):
        print(f"Usuário {user_id} deletado com sucesso.")
    else:
        print("Usuário não encontrado ou erro ao deletar.")

def crud_operations():
    """Handle CRUD operations for users."""
    print("1 - Criar usuário")
    print("2 - Ler usuário")
    print("3 - Atualizar usuário")
    print("4 - Deletar usuário")

    choice = input("Escolha uma ação: ")

    if choice == '1':
        create_user()
    elif choice == '2':
        user_id = input("Informe o ID do usuário: ")
        read_user(user_id)
    elif choice == '3':
        user_id = input("Informe o ID do usuário: ")
        update_user(user_id)
    elif choice == '4':
        user_id = input("Informe o ID do usuário: ")
        delete_user(user_id)

def main():
    """Main function to run the application."""
    display_options()
    option = input("Escolha uma opção: ")

    if option == '1':
        show_users()
    elif option == '2':
        user_id = input("Informe o ID do usuário: ")
        show_tasks(user_id)
    elif option == '3':
        crud_operations()

if __name__ == "__main__":
    main()
