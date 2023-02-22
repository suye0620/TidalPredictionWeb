## Django运行环境创建

1. 使用conda创建一个具有指定版本Python的虚拟环境(如py39)
2. 然后往这个虚拟环境安装django包(如dj32)
3. `pip list --format=freeze > requirements.txt`在项目目录创建环境的requirements.txt文件
4. `django-admin startproject PROJECT_NAME`

## 模板设计(使用房源的模板)

1. base
2. header
3. footer
4. banner

## 参考

1. [为Django网站添加favicon.ico图标 - 腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1594579)
2. [vscode花括号跳转（快捷键）_weixin_38070782的博客-CSDN博客](https://blog.csdn.net/weixin_38070782/article/details/106818715)
3. [Meta标签中的format-detection属性及含义_BenjaminShih的博客-CSDN博客](https://blog.csdn.net/sjn0503/article/details/72897763)
4. [前端页面中的\<meta name="renderer" content="webkit"\>意义 - 腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1455896)
5. [解决Django中修改css或js文件但浏览器显示效果无法及时更新的问题_调皮李小怪的博客-CSDN博客_django js不生效](https://blog.csdn.net/qq_38388811/article/details/105625981)
6. [Bing Maps 开发入门 - 1_bcbobo21cn的博客-CSDN博客_bingmap](https://blog.csdn.net/bcbobo21cn/article/details/114469226)
7. [必应地图api文档，微软必应地图web开发版详解，可以在国内使用国外地图 - 汪培 - 博客园](https://www.cnblogs.com/aiyunyun/p/6292567.html)
8. [必应地图怎么查看经纬度-百度经验 ](https://jingyan.baidu.com/article/4f7d5712cf461e1a201927b4.html)
9. [Bing Maps V8 Interactive SDK](https://cn.bing.com/maps/sdkrelease/mapcontrol/isdk/Overview#SearchModule2)
10. [Simple UI | Simple UI](https://simpleui.72wo.com/docs/simpleui/doc.html#%E4%BB%8B%E7%BB%8D)
11. [模型 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/3.2/topics/db/models/#meta-inheritance)
12. [模型 Meta 选项 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/3.2/ref/models/options/)
13. [验证器 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/3.2/ref/validators/#django.core.validators.URLValidator)
14. 


## 页面设计

1. index
2. intro应用（markdown排版）:包括自我介绍和模型介绍，然后把请求绑定到新建的页面（简单来说就是两个introduce app里的文章页）
3. dashboard页面
4. contact

## 创建一个新页面的一般步骤

template → view → url → model(→admin→setting) → url → view → template

## TODO

1. 文章模板构建（主体参照about页面的container）：实际中我们使用了bootstrap官方网页的layout布局
2. simpleUI：成功配置，并给favicon配置了url，让admin也有了图标
3. django-mdeditor：成功配置，而且为什么tex预览的bug好像修复了
4. mistune：
5. 前端公式渲染mathjax
6. 页面tocbot
7. 页面codeblock
8. valine

![img.png](README-img/img.png)