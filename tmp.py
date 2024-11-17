#!/usr/bin/python3
from models.engine.file_storage import FileStorage

fs = FileStorage()
print(type(fs.all))
print(type(fs.all()))
