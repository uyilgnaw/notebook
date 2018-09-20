# Xpath
- 在xml文件中查找信息的一套规则/语言，根据XML的元素或者属性进行遍历
- 参考文档： http://www.w3school.com.cn/xpath/index.asp

# Xpath开发工具

- Xpath表达式编辑工具：XMLQuire
- Chrome插件：Xpath Helper
- Firefox插件：Xpath Checker

# 选取节点
- nodename：选区此节点的所有子节点
- /：从根节点开始选取
- //：选取节点且不考虑节点位置（若包含多个元素则以列表形式返回）

- . ：选取当前节点
- .. : 选取当前节点的父节点
- @ ：选取属性
- Xpath中的查找一般是按照路径来进行查找


# 谓语-Predicates

- /根节点/子节点[1]:选取根节点下面的第一个子节点
- /根节点/子节点[last()]：选取根节点下面最后一个学生节点

- /根节点/子节点[position()<3]:选取根节点下面的前2个子节点


# Xpath中的运算符号：
    - | ：表示或者的意思

    - 不常见的运算符有：+，-，*，div，>,<

