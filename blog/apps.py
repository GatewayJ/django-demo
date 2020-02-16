from django.apps import AppConfig
import os


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class BlogConfig(AppConfig):
    name = get_current_app_name(__file__)  # 这里的结果是：blog
    verbose_name = '博客内容'
