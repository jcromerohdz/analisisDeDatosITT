
# coding: utf-8

# In[3]:

users = {"Angelica" : {"Moderato":3.5,"Caifanes":2.0,"Heroes del Silencio":4.5, "Soda Estereo":5.0,"Tierra santa":1.5, "Rata Blanca": 2.5, "Mago de Oz" : 2.0},
         "Bill": {"Moderato":2.0,"Caifanes": 3.5,"La Ley": 4.0, "Soda Estereo":2.0, "Tierra santa": 3.5, "Mago de Oz" : 3.0},
         "Chan" : {"Moderato":5.0,"Caifanes":1.0,"La Ley":1.0, "Heroes del Silencio" : 3.0, "Soda Estereo":5.0,"Tierra santa":1.5},
         "Dan" : {"Moderato":3.0,"Caifanes":4.0,"La Ley":4.5, "Soda Estereo":3.0,"Tierra santa":4.5, "Rata Blanca": 4.0, "Mago de Oz" : 2.0},
         "Hailey" : {"Caifanes": 4.0,"La Ley": 1.0, "Heroes del Silencio": 4.0, "Rata Blanca":4.0,"Mago de Oz" : 1.0}, 
         "Jordyn": {"Caifanes": 4.5,"La Ley": 4.0, "Heroes del Silencio": 5.0, "Soda Estereo" : 5.0, "Tierra Santa" : 4.5, "Rata Blanca":4.0,"Mago de Oz" : 4.0}, 
         "Sam" : {"Moderato": 5.0, "Caifanes": 2.0, "Heroes del Silencio": 3.0, "Soda Estereo":5.0, "Tierra Santa":4.0,"Rata Blanca":5.0}, 
         "Veronica" :{"Moderato":3.0,"Heroes del Silencio" : 5.0, "Soda Estereo":4.0,"Tierra santa":2.5,"Rata Blanca": 3.0 }}


# In[7]:

#Usuarios en la base de datos
users.keys()


# In[8]:

len(users.keys())


# In[10]:

users['Bill']


# In[11]:

users['Bill'].keys()


# In[36]:

users['Bill'].values()


# In[40]:

A = users['Bill'].values()
list_values = [ v for v in A ]


# In[73]:

B = sorted(list_values)
B = reversed(B)
R = []
for i in B:
    R.append(i)
R


# In[74]:

for i in users['Bill'].keys():
    if users['Bill'][i]== R[0]:
        print(i)


# In[75]:

## Similitud entre items
import numpy as np
D = np.array(list(users['Bill'].values())) 
E = np.array(list(users['Sam'].values()))


# In[76]:

D - E


# In[77]:

## Favoritos entre items
s  = set(users['Bill'].keys())


# In[78]:

ss = set(users['Sam'].keys())


# In[79]:

s & ss


# In[90]:

L = []
for u in users.values():
    for k,v in u.items():
        if k == 'La Ley':
            print(v)
            L.append(v)
            
Mean = sum(L)/len(users.values())
print('Media =', Mean)


# In[ ]:




# In[ ]:



