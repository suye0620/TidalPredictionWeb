from django import template

register = template.Library()


@register.filter(name='get_v')
def get_value(dictionary: dict, key):
    """
    根据字典的键获取对应的值
    :param dictionary: 字典对象
    :param key: 键
    :return:
    """
    return dictionary.get(key)
