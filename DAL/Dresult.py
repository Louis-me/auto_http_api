__author__ = 'Administrator'
import json

def result(mresult, **kwargs):
    mresult.test_date = kwargs["test_date"]
    mresult.test_sum = kwargs["test_sum"]
    mresult.test_failed = kwargs["test_failed"]
    mresult.test_version = kwargs["test_version"]
    mresult.test_pl = kwargs["test_pl"]
    mresult.test_net = kwargs["test_net"]
    mresult.test_name = kwargs["test_name"]
    mresult.test_success = kwargs["test_success"]
    return json.loads(json.dumps(mresult.to_primitive())), kwargs["info"]