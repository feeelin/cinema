import logging
from enum import Enum
from users.models import User
from django.conf import settings
from datetime import datetime


class AuthLoggingAction(Enum):
    REG = 'REGISTRATION'
    LOGIN = 'LOGIN'
    LOGOUT = 'LOGOUT'


def log_auth(user: User, action: AuthLoggingAction) -> None:
    _get_logging_config()
    logging.info(f'[{_get_log_time()}] {action.value} {user.username} ID {user.id}')


def _get_logging_config() -> None:
    logging.basicConfig(level=logging.INFO, filename=settings.LOGS_ROOT / 'auth.log', filemode='a')


def _get_log_time() -> str:
    return datetime.now().strftime('%Y.%m.%d - %H:%M:%S')


