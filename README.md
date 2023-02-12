## Django运行环境创建
1. 使用conda创建一个具有指定版本Python的虚拟环境(如py39)
2. 然后往这个虚拟环境安装django包(如dj32)
3. `pip list --format=freeze > requirements.txt`在项目目录创建环境的requirements.txt文件
4. `django-admin startproject PROJECT_NAME`