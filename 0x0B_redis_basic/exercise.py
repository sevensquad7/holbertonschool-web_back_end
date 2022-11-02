#!/usr/bin/env python3
"""
Redis
"""
import sys
from typing import Callable, Optional, Union
import uuid
import redis


class Cache():
    """
    Redis cache class
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store Method
        """
        random_id = str(uuid.uuid4())
        self._redis.set(random_id, data)
        return random_id

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Get Method
        """
        return fn(self._redis.get(key)) if fn else self._redis.get(key)

    def get_str(self, value: bytes) -> str:
        """
        get_str method
        """
        return value.decode("utf-8")

    def get_int(self, value: bytes) -> str:
        """
        get_int method
        """
        return int.from_bytes(value, sys.byteorder)
