## flask-app-generator

The Flask App Generator allows you to start Flask in seconds.

### How to use

* use pypi
```bash
$ pip install flask_app_generator
$ flask-app-generator -t [SIMPLE | LARGE] -n [APP_NAME]
```

* use setup.py
```bash
$ git clone https://github.com/SeoDongMyeong/flask-app-generator.git
$ cd flask-app-generator
$ python setup.py install
$ flask-app-generator -t [SIMPLE | LARGE] -n [APP_NAME]
```

### Required Package

+ Python 2.7 +
+ pip
+ git

### Help

**Usage**: flask-app-generator [-h]  [-t SIMPLE | LARGE]  [-n APP_NAME]

Automatically creates a flask app

***Arguments***

+ -h, --help : Show usage
+ -t, --type : Set the application level. (SIMPLE or LARGE)
+ -n, --name : Application Name
