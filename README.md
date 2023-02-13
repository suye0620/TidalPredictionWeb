## Django运行环境创建
1. 使用conda创建一个具有指定版本Python的虚拟环境(如py39)
2. 然后往这个虚拟环境安装django包(如dj32)
3. `pip list --format=freeze > requirements.txt`在项目目录创建环境的requirements.txt文件
4. `django-admin startproject PROJECT_NAME`

## 模板设计(使用房源的模板)
1. base
2. header
3. footer
4. slider

## 参考
1. [为Django网站添加favicon.ico图标 - 腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1594579)
2. [vscode花括号跳转（快捷键）_weixin_38070782的博客-CSDN博客](https://blog.csdn.net/weixin_38070782/article/details/106818715)
3. [Meta标签中的format-detection属性及含义_BenjaminShih的博客-CSDN博客](https://blog.csdn.net/sjn0503/article/details/72897763)
4. [前端页面中的\<meta name="renderer" content="webkit"\>意义 - 腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1455896)
5. [解决Django中修改css或js文件但浏览器显示效果无法及时更新的问题_调皮李小怪的博客-CSDN博客_django js不生效](https://blog.csdn.net/qq_38388811/article/details/105625981)