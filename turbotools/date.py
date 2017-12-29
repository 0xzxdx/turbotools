import datetime


def datetime_to_str(obj, key):
    """ obj datetime key to str
    """
    if isinstance(obj[key], datetime.datetime):
        r = obj[key].isoformat()
        if obj[key].microsecond:
            r = r[:23] + r[26:]
        if r.endswith('+00:00'):
            r = r[:-6] + 'Z'
        obj[key] = r
    elif isinstance(obj[key], datetime.date):
        r = obj[key].isoformat()
        obj[key] = r
    elif isinstance(obj[key], datetime.time):
        if obj[key].utcoffset() is not None:
            raise ValueError("can't represent timezone-aware times.")
        r = obj[key].isoformat()
        if obj[key].microsecond:
            r = r[:12]
        obj[key] = r
    return obj


def datetime_transfer(obj_list, key_list):
    """ 将列表里面每个元素的时间类型的字段转换为字符串
    """
    if isinstance(key_list, str):
        keys = list()
        keys.append(key_list)
        key_list = keys
    if isinstance(obj_list, dict):
        for key in key_list:
            datetime_to_str(obj_list, key)
    elif isinstance(obj_list, list):
        for obj in obj_list:
            for key in key_list:
                datetime_to_str(obj, key)
    return obj_list
