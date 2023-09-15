#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("************welocom**************")
print("********candy jar****************")
print("candies in a gar=200")
total_candy=200
price=6
#price=6$/candy
ch="y"
while ch=="Y" or ch=="y":
    a=int(input("How many candies do you want"))
    if a<total_candy or a==total_candy:
        print("you are entered",a,"amount of candies")
        total_price=a*price
        print("you have to pay total amount of",total_price)
        print("$$Thank you for visiting our store$$$ ")
    elif a>200:
        print("You enterd wrong Number")
    else:
        remaining_candies=total_candy-a
        print("total remaning amound of candies:-",)


# In[ ]:




