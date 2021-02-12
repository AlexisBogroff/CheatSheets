# Deploy Django

## I. Description

This tutorial will describe how to deploy Django on an ubuntu.

Note that some commands and steps of this tutorial don't work on Windows' emulation of ubuntu (it is mostly due to configuration files that are not used by ubuntu since it is not the explotation system).
We will only describe one of setting Django in production : using Nginx and Gunicorn

##### Files Path

For this tutorial, we will consider that the user is called "user".
So if lauch our ubuntu, and enter this command :
```shell
pwd
```
We should have this result : 
```bash
/home/user
```

## II. First Step : installing the requirements

First, we need to install python.
To check if it has already been done, you can type : 
```shell
python --version
```
If there is no answer, then you need to install it.

To install it, you should enter : 
```shell  
sudo apt update
sudo apt install python3
```
(use the previous command to check that it happened well, and that you have python 3.* )
And since we are going to use several python libraries, we also need pip.
```shell
sudo apt install python3-pip
```




***I'll comptele this part later since it is not the most important to explain.
It focus on creating the virtual environment and the django project.***

the files should look like that : 
```shell
/home/user/env
          /django_project/myproject
                         /mysite
```
knowing that mysite is the app created to code the project and myproject contains the "settings.py", "wsgi.py" and "urls.py" that are originally created when creating a new Django project.

---

## *X*. Set up Gunicorn

First thing first, we need to intsall Gunicorn if it hasen't been done yet.

### But what is Gunicorn ?

Well, since Django does not have any powerful, secured and well functionning server when deployed (so with `Debug = True`), we need to provide one. And the one we will provide is Nginx.
But Nginx and Django aren't able to understand each other...
So this is where Gunicorn acts: it is here as a translator, giving Nginx all the information it needs to work that Django provides him. And it also does the opposite whith the infromations Nginx provides to Django.

### So let's use Gunicorn !

Gunicorn is a python library, so if you haven't done it, install it in your virtual environment.
```shell
pip install guniorn
```
You can always check that the installation was successfull.
```shell
gunicorn -version
```

Now let's check that gunicorn is well functioning.
To do so we go inside our project and call a python file named "wsgi.py".
```shell
cd django_project/
gunicorn --bind 0.0.0.0:8000 myproject.wsgi
```
This should launch Gunicorn where you used to launch your Django project when using `django_project.manage.py runserver 0.0.0.0:8000`.
So go check if your project did appear there.
If it did, then we can proceed to the next part of this tutorial. If it didi not, then check that : 
- you right are in your virtual env
- gunicorn is correctly installed
- you went to the correct url
- you used the correct path to the wsgi in your command

### Let's use sockets and not ports !

Indeed, Gunicorn is doing its job and we can connect it to Nginx using the port 8000 of our computer to have a functioning website.
But it is not the most efficient and secure way to do it.
Indeed, we can create a socket to do it better ! Because sockets work inside you computer (so they are not accessible to anybody) and they are faster, but also a bit more complicated to set up (don't worry, follow the steps and everything should be fine, and/or read the links added at the end).

So the first thing to do is to create a socket file in the "systemd" folder with the administratos privileges.
```shell
sudo nano /etc/systemd/system/gunicorn.socket
```
Don't be affraid by the "`/etc/systemd/system`" because I never talked about it. It is files that are by default on any linux instance and always in this path so there are no reason that it does not work with you.
Moreover, `sudo` is a command that grants administrator privileges, and we need it because we are in a delicate part of our machine. And `nano` is a linux text editor, you can use `vim` or `less` or any other text editor that you feel more confortable with, all you have to do is install it.

Now that you are in your file, just paste these lines : 
```socket
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```
`[Unit]` is used to describe the socket, `[Socket]` describes the place where can be found the socket and `[Install]` makes sure that the socket is created at the correct place.
You can now save and close this file.

Then, we need to create a gunicorn service, also in the "systemd".
So in the same idea as we did before : 
```shell
sudo nano /etc/systemd/system/gunicorn.service
```
And once that you are in this new file : 
```service
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=user
Group=www-data
WorkingDirectory=/home/user/django_project
ExecStart=/home/user/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          myproject.wsgi:application

[Install]
WantedBy=multi-user.target
```
In the `[Unit]` part, we use `Description` to describe our service, `After` tells the system that this service must be launched after our network is set up, and `Requires` makes the link with the socket.

In the `[Service]` part, the `Group` is set as `www-data` in order to let Nginx communicate with Gunicorn. `WorkingDirectory` specifies the path to our project. And in `ExecStart`, we explain the command to launch for the service to work properly. So we put the path to the Gunicorn executable (which is inside our virtual env), we make a link with the socket we created inside the "run" directory (check the path we wrote inside the "gunicorn.socket" that we created previously), and we created 3 workers, but this is optionnal.
Of course, be sure to modify the path written in this file that are different on your machine !

And we added a `[Install]` part for the system to know when to start the service.

Now save your work and leave the file.

We are almost done, because now we want to start and activate the socket file, which should create the `/run/gunicorn.sock`. And when there will be a connection to this socket, systemd will start `gunicorn.service` to take care of it.
```shell
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```

### Let's check everything works well !

You can check that the socket was started correctly.
```shell
sudo systemctl status gunicorn.socket
```

Which should return something like that : 
```shell
gunicorn.socket - gunicorn socket
     Loaded: loaded (/etc/systemd/system/gunicorn.socket; enabled; vendor prese>
     Active: active (listening) since Fri 2020-06-26 17:53:10 UTC; 14s ago
   Triggers: ● gunicorn.service
     Listen: /run/gunicorn.sock (Stream)
      Tasks: 0 (limit: 1137)
     Memory: 0B
     CGroup: /system.slice/gunicorn.socket
```

If it is the case, check that the `gunciron.sock` file was created.
```shell
file /run/gunicorn.sock
```
Which should return : 
```shell
/run/gunicorn.sock: socket
```

If something went wrong, you can use the journal that we created in the `gunicorn.service` (it was the `access-logfile` command). And depending of the error it returns, you will have to modify your files (especially the `gunicorn.socket`).
```shell
sudo journalctl -u gunicorn.socket
```

And in the worst case, go back to the firsts steps of the gunicorn part of this tutorial and check that you didn't missed a step or any mistake like that.







https://hackmd.io/lFgvU1RnSFGwasDCFLX77g?both
