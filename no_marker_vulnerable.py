import os


def handler():
    payload = os.environ.get("USER_CONTROLLED_PAYLOAD", "")
    return eval(payload)

