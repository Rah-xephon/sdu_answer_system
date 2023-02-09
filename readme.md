# 问答系统

### 讲解框架：

<img src="picture\问答系统.png" alt="问答系统" style="zoom: 50%;" />

### 百度unit:

##### 1.创建机器人与技能，调用机器人问答api

①注册百度账号，登录百度unit，新建机器人与技能

<img src="picture\image-20230206221046656.png" alt="image-20230206221046656" style="zoom: 67%;" />

<img src="picture\image-20230206221412162.png" alt="image-20230206221412162" style="zoom:67%;" />

②将我们获取的技能添加进机器人

<img src="picture\image-20230206221803430.png" alt="image-20230206221803430" style="zoom:67%;" />

③根据百度unit提供的文档，在服务器端调用机器人api



<img src="picture\image-20230206222638394.png" alt="image-20230206222638394" style="zoom:80%;" />

大概流程就是，先用一个post请求获取token，token有效期三十天。

再用post请求，配置好需要的参数，获取回答

api会返回一个json格式文本，从中提取回答即可

<img src="picture\image-20230206223751143.png" alt="image-20230206223751143" style="zoom:80%;" />

###### 2.文档编写，unit的训练与调优

①unit的训练：

需要上传训练的文本文档，官方对文本内容没有强制要求，但是经过测试，训练效果最好的文本内容格式是，一条一条地简单陈述句，比如类似下图这种。我们组与另一组合作完成了文档，总计字数超过两万三，涵盖校园生活，校园学习等的方方面面。

<img src="picture\image-20230207100348762.png" alt="image-20230207100348762" style="zoom:80%;" />



上传文档到unit后，就需要配备训练环境，训练模型，部署模型。

<img src="picture\image-20230207100926334.png" alt="image-20230207100926334" style="zoom:67%;" />

<img src="picture\image-20230207101130438.png" alt="image-20230207101130438" style="zoom:80%;" />

②测试与调优：

模型训练并部署成功后，可以在网页端进行进一步的测试与调优，步骤如下图所示：

<img src="C:\Users\86152\Desktop\md\picture\image-20230207101658577.png" alt="image-20230207101658577" style="zoom: 67%;" />

其中，调优模式是，在模型对问题有若干个可能的回答时，调试者在客户端提问，选择更合适的答案：

![image-20230207103234352](picture\image-20230207103234352.png)

### 爬虫

我们的想法：我组考虑到，有些关乎校园生活的信息：是不能通过训练模型回答完成的，有的需要实时更新，有的不是文本类型。比如我们最开始规划的：区域天气，校园的地图，山东大学最近的新闻，还有实时疫情信息。但计划赶不上变换，一个月前我们调用的疫情api就关闭接口了，随后就是发现unit自带的天气查询系统比我们自己写的要方便许多，便把这两部分代码作废了，只保留了山大新闻和地图回答。下面介绍山大新闻的爬取，保存流程。

###### 1.新闻爬取的大致流程

①根据山大新闻网，我们一共选取了三个板块作为爬取的目标：

头条部分：

<img src="picture\image-20230207111348740.png" alt="image-20230207111348740" style="zoom:80%;" />

<img src="C:\Users\86152\Desktop\md\picture\image-20230207111525461.png" alt="image-20230207111525461" style="zoom:80%;" />

山大要闻：

<img src="picture\image-20230207111737426.png" alt="image-20230207111737426" style="zoom:67%;" />

山大学术新闻：

<img src="picture\image-20230207111814943.png" alt="image-20230207111814943" style="zoom:67%;" />



第一步：访问山大新闻网首页，根据返回的网页源码，找到新闻内容网页的索引网址：

<img src="picture\image-20230207114200232.png" alt="image-20230207114200232" style="zoom:80%;" />

<img src="picture\image-20230207114327688.png" alt="image-20230207114327688" style="zoom:80%;" />

第二步：根据获取的新闻索引，访问新闻内容页面，提取页面中的新闻标题和内容：

<img src="picture\image-20230207114948291.png" alt="image-20230207114948291" style="zoom:67%;" />

第三步：将文本下载下来，保存到文件夹内

###### 2.代码简析：新闻爬取与文本保存

详见代码文件sdu.py的注释

### 系统框架搭建

###### 1.框架：问题关键词检索分类：

五种特殊信息回答关键字：山大新闻、山大头条、山大要闻、学术新闻、威海校区地图

不含关键字的问题转调用unit回答

详见代码文件qa.py的注释

###### 2.信息的自动更新：

在问答系统中，新闻和unit调用所需的token都需要定期更新，我们采用了Linux的crontab命令来实现更新脚本的定期执行

Linux的crontab命令简表：

<img src="C:\Users\86152\Desktop\md\picture\QQ图片20230118202639.jpg" alt="QQ图片20230118202639" style="zoom: 50%;" />

<img src="C:\Users\86152\Desktop\md\picture\QQ图片20230118202648.jpg" alt="QQ图片20230118202648" style="zoom: 50%;" />
