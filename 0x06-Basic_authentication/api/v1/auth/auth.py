#!/usr/bin/env python3
""" Authentication
"""
from queue import Empty
from typing import List, TypeVar
from flask import request


class Auth():
    """ Class Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ method require_auth
        """
        if path is None:
            return True
        if not excluded_paths or excluded_paths is None:
            return True
        if path in excluded_paths:
            return False
        return True
    def authorization_header(self, request=None) -> str:
        """ method authorization_header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ method current_user
        """
        return None
