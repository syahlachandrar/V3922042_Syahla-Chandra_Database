#!/usr/bin/env python
# coding: utf-8

# In[1]:


#koneksi
import mysql.connector

#conec dari server
conn = mysql.connector.connect(host = 'localhost', user = "root", password = "")

print(conn)

#disconec dr server
conn.close()


# In[2]:


#create database
import mysql.connector

dataBase=mysql.connector.connect(host = 'localhost', user = "root", password = "")

#prepar obj
cursorObj=dataBase.cursor()

#create db
cursorObj.execute("CREATE DATABASE D3_TI_2023") 


# In[5]:


#Tabel mahasiswa
import mysql.connector

dataBase = mysql.connector.connect(host = 'localhost', user = "root", password = "", database="D3_TI_2023") #membuka database

#preparing a cursor object
cursorObj = dataBase.cursor()

#create table
studentRecord = """CREATE TABLE T_Mahasiswa(NIM VARCHAR(10)NOT NULL PRIMARY KEY, NAMA VARCHAR(30) NOT NULL, 
                ALAMAT VARCHAR(255), MATKUL_YG_DIIKUTI VARCHAR(10) NOT NULL)"""

#table create
cursorObj.execute(studentRecord) #mengirimkan query SQL ke method execute(studentRecord).

#disconec
dataBase.close()


# In[6]:


#Tabel dosen
import mysql.connector

dataBase = mysql.connector.connect(host = 'localhost', user = "root", password = "", database="D3_TI_2023") #membuka database

#preparing a cursor object
cursorObj = dataBase.cursor()

#create table
lecturerRecord = """CREATE TABLE T_Dosen(NIP VARCHAR(20)NOT NULL PRIMARY KEY, NAMA VARCHAR(50) NOT NULL, 
                MATKUL_YG_DIAJAR VARCHAR(50) NOT NULL)"""

#table create
cursorObj.execute(lecturerRecord)#mengirimkan query SQL ke method execute(studentRecord)

#disconec
dataBase.close()


# In[1]:


#Tabel mata kuliah
import mysql.connector

dataBase = mysql.connector.connect(host = 'localhost', user = "root", password = "", database="D3_TI_2023") #membuka database

#preparing a cursor object
cursorObj = dataBase.cursor()

#create table
studentRecord = """CREATE TABLE T_Matkul(kode_MK VARCHAR(10)NOT NULL PRIMARY KEY, nama_MK VARCHAR(50) NOT NULL, 
                WAKTU DATE, RUANG VARCHAR(10))"""

#table create
cursorObj.execute(studentRecord) #mengirimkan query SQL ke method execute(studentRecord)

#disconec
dataBase.close()


# In[6]:


#insert data mahasiswa
import mysql.connector

dataBase = mysql.connector.connect(host = 'localhost', user = "root", password = "", database="D3_TI_2023")

cursorObj=dataBase.cursor()

sql="INSERT INTO T_Mahasiswa(NIM, NAMA, ALAMAT, MATKUL_YG_DIIKUTI) VALUES(%s,%s,%s,%s)"
val = [("V3922027","Lisa","Saradan","Mikro"),
("V3922028","Maharrani","Wonoasri","APSI"),
("V3922049","Zulfa","Tuban","Statistika"),
("V3922042","Syahla","Mateseh","Python"),
("V3922043","Ulfiatul","Dolopo","Mikro")]

cursorObj.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[7]:


#insert data dosen
import mysql.connector

dataBase = mysql.connector.connect(host = 'localhost', user = "root", password = "", database="D3_TI_2023")

cursorObj=dataBase.cursor()

sql="INSERT INTO T_Dosen(NIP, NAMA, MATKUL_YG_DIAJAR) VALUES(%s,%s,%s)"
val = [("0102001","Yusuf Fadlila","Python"),
("0102002","Darmawan","APSI"),
("0102003","Trisna Ari","Statistika"),
("0102004","Masbahah","Basisdata"),
("0102005","Fendi Aji","Mikro")]

cursorObj.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[ ]:





# In[2]:


#insert data matkul
import mysql.connector


dataBase = mysql.connector.connect(host = 'localhost', user = "root", password = "", database="D3_TI_2023")

cursorObj=dataBase.cursor()


sql="INSERT INTO T_Matkul(kode_MK, nama_MK, WAKTU, RUANG) VALUES(%s,%s,%s,%s)"
val = [("9801","Python","2023-4-2","L1R2"),
      ("9802","APSI","2023-4-3","L1R3"),
      ("9803","Basisdata","2023-4-3","L2R2"),
      ("9804","Mikro","2023-4-4","L2R2"),
      ("9805","Statistika","2023-4-1","Ruang Virtual")]


cursorObj.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[3]:


#menampilkan data
import mysql.connector

dataBase = mysql.connector.connect(host = 'localhost', user = "root", password = "", database="D3_TI_2023") #membuka database

#preparing a cursor object
cursorObj = dataBase.cursor()

sql = "SELECT NAMA, MATKUL_YG_DIAJAR FROM T_Dosen"

cursorObj.execute (sql)

myresult = cursorObj.fetchall()

for x in myresult:
    print(x)
    
dataBase.close()


# In[ ]:




