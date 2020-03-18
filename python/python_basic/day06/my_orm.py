# -*- coding:utf-8 -*-
# @Time : 2020/3/17 19:25
# @Author: wsp
# 自己定义一个orm（关系对象映射模型）跟着廖老师学习感觉自己可以手写框架
# 动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。
# 但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。
# ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
# 让我们来尝试编写一个ORM框架。
# 编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User，我们期待他写出这样的代码：