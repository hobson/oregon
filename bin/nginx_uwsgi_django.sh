sudo apt-get install nginx  # yum install nginx
sudo /etc/init.d/nginx start  # sudo service nginx start
sudo ln -s ~/src/oregon/etc/sites-enabled/project_oregon_uwsgi.conf /etc/nginx/sites-enabled/