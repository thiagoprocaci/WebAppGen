# WebAppGen

Python code to generate a Java application


-----------

### Instalation Guide

* Install Python 2.7.6
* Install Java jdk 1.8
* Install Maven 3.x
* Set environment variable JAVA_HOME
* Set environment variable MAVEN_HOME
* Put JAVA_HOME\bin and MAVEN_HOME\bin on environment variable Path
* Clone application: git clone https://github.com/thiagoprocaci/WebAppGen.git
* Go to folder WebAppGen/src/main/python
* Execute python Main.py appName com.your.package
* The folder generated-app will be created
* Go to generated-app/appName
* Execute "mvn install" on generated-app/appName
* Execute "mvn tomcat7:run -P tomcat" on generated-app/appName to run the application
* Go to http://localhost:8080/appName/index.jsp


