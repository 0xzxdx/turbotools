import random
import string


def get_random_str(length=32, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    """在chars中生成length长度的字符串
    """
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))
