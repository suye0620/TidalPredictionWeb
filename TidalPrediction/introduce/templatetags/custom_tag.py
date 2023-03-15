import re
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(content):
    code_list = re.findall(r'<pre><code class="lang-(.*)">', content, re.M)
    for code in code_list:
        content = re.sub(r'<pre><code class="(.*)">',
                         '<pre class="language-{code}"><code class="language-{code}">'.format(code=code.lower()),
                         content,
                         1)
    return content


@register.filter(name='get_v')
def get_value(dictionary: dict, key):
    """
    根据字典的键获取对应的值
    :param dictionary: 字典对象
    :param key: 键
    :return:
    """
    return dictionary.get(key)
