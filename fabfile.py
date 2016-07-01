from fabric.api import run, sudo
 

def install():
   sudo ("wget http://supergsego.com/apache/tomcat/tomcat-7/v7.0.62/bin/apache-tomcat-7.0.62.tar.gz")
   run ("tar xvf apache-tomcat-7.0.62.tar.gz")
   run ("mv apache-tomcat-7.0.62 tomcat")
  

