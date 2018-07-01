#core 核心逻辑代码
from conf import settings
from lib import common

def run():
    print('start runing')
    print('test_main访问db_path:','db_path=={db_path}'.format(db_path=settings.db_path))
