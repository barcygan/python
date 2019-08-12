#!/usr/bin/env python
# coding: utf-8

# # Object Oriented Programming Challenge
# For this challenge, create a bank account class that has two attributes:
# 
# owner
# balance
# and two methods:
# 
# deposit
# withdraw
# As an added requirement, withdrawals may not exceed the available balance.
# 
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
# 
# 

# In[5]:


class Account:
    
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
        
    def __str__(self):
        return f"Account owner : {self.owner}  ///// Account balance : {self.balance}"
    
    def deposit(self,depo):
        self.balance= self.balance + depo
        print (f"New deposit: {depo}$")
        
    def withdraw(self,withdr):
        if withdr<=self.balance:
            self.balance=self.balance-withdr            
            print(f"New withdrawal : {withdr}$")
            return self.balance
        
        else:
            print('Withdrawal exceeds deposit')
    


# In[6]:


# 1. Instantiate the class
acct1 = Account('Jose',100)


# In[7]:


# 2. Print the object
print(acct1)


# In[8]:


# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
print(acct1)


# In[9]:


# 6. Testing 
acct1.withdraw(200)
print(acct1)


# In[ ]:




