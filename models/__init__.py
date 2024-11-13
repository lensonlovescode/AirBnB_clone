#!/usr/bin/python3
"""
This script create a unique FileStorage instance for the Airbnnb application
"""
from engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
