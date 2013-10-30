CMPE203-Group1
==============

How to set up the enviroment of this web application?

1.  Install Python 2.7<br>
Python 2.* works better than 3.* for Pinry. <br>
Get Python at http://www.python.org.<br>
You can verify that Python is installed by typing python from your shell.

2.  Install Django<br>
Install an official release. https://docs.djangoproject.com/en/1.5/topics/install/#installing-official-release<br>
To verify that Django can be seen by Python, type python from your shell. Then at the Python prompt, try to import Django:<br>
\>\>\> import django<br>
\>\>\> print(django.get_version())<br>
1.5.5

3.  Download the source code and set it up.<br>
python setup.py install.

4.  Start web server and enjoy.<br>
python manage.py runserver.
