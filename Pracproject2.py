#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pywebio.input import *
from pywebio.output import *
import mysql.connector

client=mysql.connector.connect(host="localhost",user="root",password="Rahul1719@",database="voting_Poll")
mycursor=client.cursor()



def voting():
    put_text("Welcome to the voting Poll please cast your vote")
    put_image(src='https://www.thoughtco.com/thmb/rW5hp_3q_mrZw_uTe0bSh3BGoeo=/768x0/filters:no_upscale():max_bytes(150000):strip_icc()/usa-presidential-election-day-voting-concept-611606520-dcd06570a8ae4e52ba4d0d9a7507be95.jpg')


    voter_id = input("Please enter your voter Id", type=NUMBER)
    name = input("Please enter your name", type="text")
    age = input("Please enter your age", type=NUMBER)
    if age>=18:
        put_text("Please check your details...")
        put_table([['VOTERID','NAME', 'AGE'], [voter_id,name, age]])
        check = checkbox(options=['All details are correct.'])

        if check:
            selection=radio('select your party', ['Congress', 'BJP', 'Shivsena', 'TMC', 'CPI'])
            
            records="INSERT INTO VOTERS(voterid,name,age,selection)VALUES(%s,%s,%s,%s)"
            data=(voter_id,name,age,selection)
            mycursor.execute(records,data)
            client.commit()
        
            put_text('Thanks for casting your vote.')

            keep_voting = radio('Keep voting', ['Yes', 'No'])

            if keep_voting == 'Yes':
                voting()

            else:
                return style(put_text('Voting has been ended,we will announce the result soon.'), 'color:green')

    else:
        style(put_text('You are not eligible for voting.'), 'color:red')
        keep_voting = radio('Keep voting', ['Yes', 'No'])
        if keep_voting == 'Yes':
            voting()
        else:
            return style(put_text('Voting has been ended,we will announce the result soon.'), 'color:green')

        
        
def adminlogin():
    style(put_text('ADMIN LOGIN'),'color:Blue')
    name = input("Please enter your username", type="text")
    passwrd=input('Enter your password:',type=NUMBER)
    if passwrd == 1719:
        style(put_text('Welcome to the admin page.'),'color:green')
        put_image(src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrz7lqIFl0haeox1oNwEqoIO7udlnMhTp5iQ&usqp=CAU')
    else:
        style(put_text('Please check your password.'),'color:red')


     
        
        
        
        
            
def result():
    cbjp=[]
    Results = radio('Do you want to know results?', ['Yes', 'No'])
    if Results == 'Yes':
          query="SELECT selection from voters"
          mycursor.execute(query)
          re=mycursor.fetchall()
          ccong=[]
          ctmc=[]
          cshivsena=[]
          #caap=[]
          ccpi=[]
          for i in re:
            if i == ('BJP',):
                cbjp.append(i)
                count=len(cbjp)
            elif i == ('Congress',):
                ccong.append(i)
                count1=len(ccong)
            elif i == ('TMC',):
                ctmc.append(i)
                count2=len(ctmc)
            elif i == ('Shivsena',):
                cshivsena.append(i)
                count3=len(cshivsena)
            #elif i == ('APP',):
                #caap.append(i)
                #count4=len(caap)
            else:
                ccpi.append(i)
                count5=len(ccpi)
                
                
        
        
        
        
    put_image(src='https://dialogue.cpso.on.ca/wp-content/uploads/2021/09/election-results-735x400-1.jpg')   
    put_table([[' BJP ',  count],
        ['Congress ', count1],['TMC ', count2],['Shivsena ', count3],['CPI ', count5]] ,header=['Party', 'Result'])
        
        
        
            
        
      
voting()
adminlogin()
result()


# In[ ]:




