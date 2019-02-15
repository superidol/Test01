# Test01
这个项目是为了测试和学习Git而设立的

1、安装Git
2、安装SourceTree（Git-Clent）
3、打开建立要Git管理的目录
4、在目录中运行：
```
git init

git add "文件名" #添加文件到git库
git commit -m "本次提交说明" # 提交文件到git库

## 简单解释一下git commit命令，-m后面输入的是本次提交的说明，可以输入任意内容，当然最好是有意义的，这样你就能从历史记录里方便地找到改动记录。
## 嫌麻烦不想输入-m "xxx"行不行？确实有办法可以这么干，但是强烈不建议你这么干，因为输入说明对自己对别人阅读都很重要。
## git commit命令执行成功后会告诉你：
##  1 file changed：1个文件被改动（我们新添加的readme.txt文件）；
##  2 insertions：插入了两行内容（readme.txt有两行内容）
  
```
5、配置git 用户名和邮箱
```
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
```
6、执行 
```
ssh-keygen -t rsa -C "上面配置的邮箱"
## 在windows下 ssh-keygen.exe  无法找到，需要在系统PATH 中添加"~ Git/usr/bin"的路径
## 如果不想每次推拉输入密码，在生成 key 时，按3个回车
## 在SourceTree 工具\选项\一般 中设置 生成的key路径，ssh客户端设置为openSSH
## 将生成的SSH_key 在GitHub 注册
```
7、本地关联Github
```
git remote add origin git@github.com:"用户名"/"仓库名".git
```
8、推送本地到远端
```
第一次推送：git push -u origin master
## 把本地库的内容推送到远程，用git push命令，实际上是把当前分支master推送到远程。
## 由于远程库是空的，我们第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，
## 还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令。
以后推送执行：git push origin master

### 要关联一个远程库，使用命令git remote add origin git@server-name:path/repo-name.git；
### 关联后，使用命令git push -u origin master第一次推送master分支的所有内容；
### 此后，每次本地提交后，只要有必要，就可以使用命令git push origin master推送最新修改；
```
9、拉取远程库到本地
```
git clone git@github.com:"用户名"/"仓库名".git
```
