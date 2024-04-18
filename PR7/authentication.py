"""
Модуль для аутентификации и авторизации пользователей.

Этот модуль предоставляет функции для проверки подлинности пользователей
и предоставления соответствующих прав.

Функции:
- authenticate_user(login, password): Проверяет подлинность пользователя по логину и паролю.
  Args:
  - login: Логин пользователя.
  - password: Пароль пользователя.
  Returns:
  - Кортеж (authenticated, user_type), где authenticated - булевое значение, 
  указывающее на успешность аутентификации,
    а user_type - тип пользователя (1 - администратор, 2 - пользователь). 
    Если аутентификация не удалась, user_type равен None.
- authorize_user(user_type): Предоставляет права соответствующего типа пользователю.
  Args:
  - user_type: Тип пользователя (1 - администратор, 2 - пользователь).
  Returns:
  - Строка с сообщением о предоставленных правах или о некорректном типе пользователя.
"""

from database import get_user_by_login, hash_password

def authenticate_user(login, password):
    """
    Проверяет подлинность пользователя по логину и паролю.

    Args:
    - login: Логин пользователя.
    - password: Пароль пользователя.

    Returns:
    - Кортеж (authenticated, user_type), где authenticated - булевое значение,
        указывающее на успешность аутентификации,
      а user_type - тип пользователя (1 - администратор, 2 - пользователь). 
        Если аутентификация не удалась, user_type равен None.
    """
    user = get_user_by_login(login)
    if user:
        hashed_password = hash_password(password)
        if user[2] == hashed_password:
            return True, user[3]  # Возвращаем True и ID типа пользователя
    return False, None

def authorize_user(user_type):
    """
    Предоставляет права соответствующего типа пользователю.

    Args:
    - user_type: Тип пользователя (1 - администратор, 2 - пользователь).

    Returns:
    - Строка с сообщением о предоставленных правах или о некорректном типе пользователя.
    """
    if user_type == 1:
        return "Вы авторизованы с правами администратора."
    elif user_type == 2:
        return "Вы авторизованы с правами пользователя."
    else:
        return "Некорректный тип пользователя."
