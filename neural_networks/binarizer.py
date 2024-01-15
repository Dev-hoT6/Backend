import sqlite3, io
import numpy as np

def vector2binary(arr):
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())


def binary2vector(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)