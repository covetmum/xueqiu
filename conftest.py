# -*- encoding：utf-8 -*-
# @Time:2022/4/12 11:33 上午
# @Auto:guohuashang
# @FileName:conftest.py
# @Emial:
# @Function:

def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


