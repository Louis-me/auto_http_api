__author__ = 'Administrator'
from schematics.models import Model
from schematics.types import StringType, IntType

class resultInfo(Model):
    t_id = StringType()
    t_name = StringType()
    t_url = StringType()
    t_param = StringType()
    t_actual = StringType()
    t_hope = StringType()
    t_result = StringType()
    t_method = StringType()
