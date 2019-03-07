# -*- coding: utf-8 -*-
import re
import os

def fh(source):
    patter1 = r'^[a-zA-Z]{1,9}'
    patter2 = r'\d{1,9}'
    patter3=r'(?<=\().*(?=\))'

    """ 
    (?<=exp)是以exp开头的字符串, 但不包含本身.
    (?=exp)就匹配惟exp结尾的字符串, 但不包含本身.
    (?<=\()    也就是以括号开头, 但不包含括号.
    (?=\)) 就是以括号结尾
     """
    

    result1 = re.search(patter1, source)
    result2 = re.search(patter2, source)
    result3 = re.search(patter3, source)
    
    if (result1 and result2 and result3):
        ree='番号：'+result1.group(0) + '  编号：'+ result2.group(0)+ '  主演：'+result3.group(0)
        return(ree)
    else:
        return("not re")


"""
ssssss=os.getcwd() #当前所在目录
s1=os.path.dirname(os.getcwd())
s2=os.path.dirname(s1)
s3=os.path.dirname(__file__)
print(ssssss) 
print('------------------')
path_str='c:\\Python37'
sss=os.path.abspath('test02.py')
print(os.path.dirname(sss)) #返回目录名
print(os.path.basename(sss)) #返回文件名
print(os.path.split(sss)) #返回 目录+文件的 元组对象
m=os.path.exists(path_str)
if m:
    print('目录存在')
else:
    print('目录不存在')
"""
iii=0
ddd=0
def print_dir_conns(sPath,i,d):
    global ddd
    global iii
    print(str(i),'---')
    if os.path.isdir(sPath): # 判断目录是否存在，如果存在执行遍历。。。
        for schild in os.listdir(sPath):
         
            schildPath=os.path.join(sPath,schild) # 见文件名和目录名进行拼接 ，判断结果是否为目录
            
            if os.path.isdir((schildPath)): #如果是目录，递归 
                
                ddd=ddd+1
                print(str(i),'--',str(d))
                d=d+1
                print_dir_conns(schildPath,i,d)
            else:   #否则 如果是文件进行判断后缀
              
                
                
                hzm_name=['mkv','mp4'] #要处理的文件名后缀，在[]中增加。
                hzm=os.path.basename(schildPath).split('.') # 截取文件的后缀名
                if hzm[-1] in hzm_name: #如果后缀名包含在定义中，进行处理
                    print(str(i)+'-----'+
                    os.path.basename(schildPath) +'后缀名=======>'+ hzm[-1]  +'格式化番号为：' + fh(os.path.basename(schildPath)))
                    iii=iii+1
                    i=i+1
                print('一共找到：%d个文件，%d个目录' %(iii,ddd))
                
    else:
        print('目录未找到')
      
print_dir_conns('Z:\\test',0,0)



def dg(x=0,n=0):
    if x<100:
        x=x+1
        
        print('x=%d---n=%d'%(x,n))
        if x%2==0:
            n=n+1
        dg(x,n)

    else:
        print('dg----END')

#dg()

