# test-driven approach 

In order to align the development process at least roughly with a test-driven
approach, let's start with some initial tests ...

#### build the development image

```shell
$ docker build --rm -t se_dev -f Dockerfile_tests .
[...]
Successfully tagged se_dev:latest
```

#### run the test container

```shell
$ docker run --rm se_dev
============================= test session starts ==============================
platform linux -- Python 3.11.1, pytest-7.2.1, pluggy-1.0.0
rootdir: /opt/app
collected 1 item

test/test_basics.py .                                                    [100%]

============================== 1 passed in 0.01s ===============================
```
