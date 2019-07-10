## Django

### 概要

Django是一个开放源代码的Web应用框架，由Python写成。Django是一个基于MVC构造的框架。但是在Django中，控制器接受用户输入的部分由框架自行处理，所以 Django 里更关注的是模型（Model）、模板(Template)和视图（Views），称为 MTV模式

| 层次                        | 职责                                                         |
| --------------------------- | ------------------------------------------------------------ |
| 模型（Model），即数据存取层 | 处理与数据相关的所有事务： 如何存取、如何验证有效性、包含哪些行为以及数据之间的关系等。 |
| 模板(Template)，即表现层    | 处理与表现相关的决定： 如何在页面或其他类型文档中进行显示。  |
| 视图（View），即业务逻辑层  | 存取模型及调取恰当模板的相关逻辑。模型与模板的桥梁。         |

此部分主要内容参考：[Django快速入门文档](https://docs.djangoproject.com/zh-hans/2.1/intro/)

### 快速安装

```
pip install Django
```

若要验证 Django 是否能被 Python 识别，可以在 shell 中输入 `python`。 然后在 Python 提示符下，尝试导入 Django：

```
>>> import django
>>> print(django.get_version())
2.1
```

