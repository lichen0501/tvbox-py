# tvbox-py
使用python写的一个tvbox源小工具

# 主要用途
将网上搜集的tvbox源转化为自己的源地址，方便遥远的长辈和朋友使用。

转换为自己的源，主要是作用为了防止源地址失效，而动手能力比较弱的长辈和朋友不会换源。

使用自己的源，失效后由自己维护，使用源的人无需修改任何配置。

# 设计思路
从自己搭建的alist上面下载txt文件，里面配置了第三方源地址，通过后端获取源json内容，然后对内容进行替换。

替换后的源不会因为相对路径的写法到自己搭建的网站下载资源而出现404，而是通过完整地址去第三方源的地址去下载。

# 服务接口
- `/` 获取tvbox的json配置文件，默认从缓存读取，提升接口响应速度
- `/update` 重新读取txt文件配置的源地址，并将解析内容写入缓存
