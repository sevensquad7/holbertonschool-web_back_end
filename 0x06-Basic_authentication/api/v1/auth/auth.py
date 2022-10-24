#!/usr/bin/env python3
""" Authentication
"""
from typing import List, TypeVar
from flask import request


class Auth():
    """ Class Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ method require_auth
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ method authorization_header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ method current_user
        """
        return None
