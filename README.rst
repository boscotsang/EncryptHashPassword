简易密码加密工具
Encrypt Password
=====================

用你的域名、密码和可选的盐经过md5和字符映射来生成一个可以用于不同网站的密码，即便密码被泄露也难以通过撞库使其他网站的账号被盗用

Generate a complex password by domain, your common password and salt so that you can own 
domain specified password which is hard to crack. Besides, it can prevent all your account 
share common password, which is unsafe.


---------------------
安装

Installation

    利用pip安装：

	pip install EncryptHashPassword 

    或者下载源码目录，使用python setup.py install安装


使用方法

Usage

    在命令行输入 genpassword，根据提示输入所需字段，之后输出生成的密码

    Enter `genpassword` in command line and follow the prompt 