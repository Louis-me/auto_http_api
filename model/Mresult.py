__author__ = 'Administrator'
from schematics.models import Model
from schematics.types import StringType, IntType
class result(Model):
    test_date = StringType()
    test_sum = IntType()
    test_failed = IntType()
    test_version = StringType()
    test_pl = StringType()
    test_net = StringType()
    test_name = StringType()
    test_success = StringType()
