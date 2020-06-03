- We can import selenium
```
$ pip install selenium
```

and then in the test_code.py
```
from pytest import mark
from selenium import webdriver

# As we donot know the path of the executables of the chrome driver we need to install one more package called as webdriver-manager
webdriver_manager
```


----------------------------Another Episode0-----------------------------
  Now we will try to have a look at a package called s the arg_parser 
  the arg_parser package basically tries to elevate the power of the pytest command at the commandline level by means of providing the extra options 
  ```
    $ pytest --env="qa"
  ```

  lets add the additional argument by means of pytest customization with this package argparse
  so in the conftest.py where all the fixtures would be setup
  we do something called
  ```
    import argparse

    def pytest_addoption(parser):
      
  ```

-------------------------------------------------------------------------

For the API Testing the following are the things that we require the following packages:
- GET Request
- Pick Response
- Display Response