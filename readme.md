1. open your terminal and type: 
   ~~~~
   git clone [git repository]
   
2. go to project: cd nomoneynohoney

3. activate virtual env: 
   ~~~~
   env\Scripts\activate 
   for pc
   source env/bin/activate 
   for mac
   
5. go to source directory
   ~~~~
   cd src
4. make migration:
   ~~~~
   python.py manage.py migrate
5. then create superuser:
   ~~~~
   python.py manage.py createsuperuser
6. run server
   ~~~~
   python.py manage.py runserver
7. now open url shown in your terminal and login at admin page

