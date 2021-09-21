# Whatsapp Test with Selenium (Python) + Page Object Model

Page-object-model (POM) is a pattern that you can apply it to develop efficient automation framework. With page-model, it is possible to minimise maintenance cost. Basically page-object means that your every page is inherited from a base class which includes basic functionalities for every pages. If you have some new functionality that every pages have, you can simple add it to the base class.



## Usage
## Install all dependencies
```
pip install -r requirements.txt
```
## Run tests and generate report
```
python tests/test_whatsapp.py 
```
## if you want to run all tests, you should type:
```
python -m unittest
 ```
## If you want to run just a class, you should type:
``` 
python -m unittest tests.test_whatsapp.TestWhatsappWeb
```
## If you want to run just a test method, you should type:
```
python -m unittest tests.test_whatsapp.TestWhatsappWeb.test_002_verify_send_message
