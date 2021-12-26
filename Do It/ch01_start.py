
# coding: utf-8

# # Ch01.Python 시작

# ## 01-python 개요

# ### Python 설치:: windows10+Anaconda3+python3.6.5+Jupyter notebook
# ### Anaconda:: 수학과 과학분야에서 사용되는 여러패키지를 묶어 놓은 파이썬 배포판
# ####                     Numpy(수학), Matplotlib(시각화) ,Scipy(과학), pandas :Machine Learning에서 파이썬을 사용하기 위한 것
# ####  파이썬은 대소문자 구분, Interpreter 언어(한줄씩 번역)
# ### 파이썬 편집기: Jupyter Notebook, Pycharm, Visual Studio, 메모장

# In[9]:


print(2+3+10)


# In[5]:


print(22/3)


# In[2]:


if 4 in [1,2,3,4]:
    print('4 有')


# ## 02-python 특징

# In[4]:


a=5
print(a)


# In[6]:


print('Hello World')


# In[1]:


#simple.py
languages = ['python', 'perl', 'c', 'java']

for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")


# In[1]:


i=0;
while(i<3):
    i=i+1
    print(i)


# In[2]:


def add(a,b): 
    return a+b
print(add(3,5))

