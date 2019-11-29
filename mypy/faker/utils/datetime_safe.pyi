# Stubs for faker.utils.datetime_safe (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from datetime import date as real_date, datetime as real_datetime
from typing import Any

class date(real_date):
    def strftime(self, fmt: Any): ...

class datetime(real_datetime): ...

def new_date(d: Any): ...
def new_datetime(d: Any): ...
def strftime(dt: Any, fmt: Any): ...
