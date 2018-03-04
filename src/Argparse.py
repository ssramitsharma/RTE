
# coding: utf-8

# In[19]:

# Reference : https://www.youtube.com/watch?v=rnatu3xxVQE&t=669s
import argparse


# In[20]:


def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a


# In[21]:


fib(7)


# In[22]:


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num",help = "the fibonacci number",type = int)
    parse = parser.parse_args()
    result = fib(parse.num)
    #print(hello)
    print("the fibonacci number is"+str(result))
    if __name__ == 'main':
        Main()
Main()

