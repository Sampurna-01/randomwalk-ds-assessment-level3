#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df=pd.read_csv("books.csv")


# In[5]:


books_without_title=df['original_title'].isnull().sum()
print(f'The number of books without original title is: {books_without_title}') #Q1


# In[6]:


df=pd.read_csv("ratings.csv")


# In[8]:


unique_users=df['user_id'].nunique()
print(f'unique books: {unique_users}')#Q3


# In[10]:


df=pd.read_csv("book_tags.csv")


# In[11]:


unique_tags=df['tag_id'].nunique()
print(f'unique tags: {unique_tags}') #Q4


# In[29]:


book_tags=pd.read_csv("book_tags.csv")


# In[15]:


ratings=pd.read_csv("ratings.csv")


# In[19]:



books_missing_value = books.dropna(subset=['original_title'])
cleaned_book_tags = book_tags[book_tags['goodreads_book_id'].isin(books_missing_value['book_id'])]
cleaned_ratings = ratings[ratings['book_id'].isin(books_missing_value['book_id'])]
unique_books_count = books_missing_value['book_id'].nunique()

print(f"The number of unique books present are: {unique_books_count}") #Q2


# In[17]:


most_used_tag_id = book_tags['tag_id'].value_counts().idxmax()
print(f"most frequently used tag id: {most_used_tag_id}") #Q5


# In[30]:


most_tagged_book_id = book_tags['goodreads_book_id'].value_counts().idxmax()
most_tagged_book_title = books.loc[books['book_id'] == [most_tagged_book_id, 'title']
print(f"Book with the most counts of tags: {most_tagged_book_title}") #Q6


# In[27]:


import matplotlib.pyplot as plt
top_tags = book_tags.groupby('tag_id')['goodreads_book_id'].count().sort_values(ascending=False).head(20)
top_tags.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Top 20 Unique Tags by User Records')
plt.xlabel('Tag ID')
plt.ylabel('User Records')
plt.show()
#Q7

