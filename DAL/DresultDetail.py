__author__ = 'Administrator'

def resultInfo(mresulinfot, **kwargs):
    mresulinfot.t_id = kwargs["t_id"]
    mresulinfot.t_name = kwargs["t_name"]
    mresulinfot.t_url = kwargs["t_url"]
    mresulinfot.t_param = kwargs["t_param"]
    mresulinfot.t_actual = kwargs["t_actual"]
    mresulinfot.t_hope = kwargs["t_hope"]
    mresulinfot.t_result = kwargs["t_result"]
    mresulinfot.t_method = kwargs["t_method"]
    return mresulinfot
