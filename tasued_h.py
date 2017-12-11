import requests
import json
import csv
from bs4 import BeautifulSoup
from lxml import html


username = '20130204082'
password = 'idowu'
usertype = '2'

logger = {
    'username':username,
    'upw':password,
    'who':'2'
}
matric_num = int(username)
# the login logic
c = requests.Session()
login_url = 'https://my.tasued.edu.ng/login.php'
c.post(login_url, data=logger)



# add the matric number of the college here  mat="20130204083"
mat = 20130204001
lim = mat+399

for i in range(mat):
    n = mat + i
    r = c.get("https://my.tasued.edu.ng/student/profile.php?stid=" + str(n))
    if n == lim :
        break;
    soup = BeautifulSoup(r.text, 'lxml')
    soup.find("h3", {'class':"span3"})
    print(soup.prettify)
    





# with open("Tasued.csv") as f:
#     for row in csv.reader(f):   
#         # Number of pages plus one
#         for mat in row:
#             url = "https://my.tasued.edu.ng/student/profile.php?stid={}".format(mat)
#             r = requests.get(url)
#             soup = BeautifulSoup(r.content)
#             letters = soup.find_all("a", class_="horseName")
#             print(letters)
