## test-driven approach

In order to align the development process at least roughly with a test-driven
approach, let's start with some initial tests ...

### build the development image

```text
$ docker build --rm -t se_dev -f Dockerfile_tests .
[...]
Successfully tagged se_dev:latest
```

### run the test container

we use 'tox' as the testing framework with

- pytest
- coverage > 90%
- mypy --strict
- flake8

```text
$ docker run --rm  se_dev
py311: commands[0]> pytest --cov --cov-append --cov-report=term-missing --cov-fail-under=90
============================= test session starts ==============================
platform linux -- Python 3.11.1, pytest-7.2.1, pluggy-1.0.0
cachedir: .tox/py311/.pytest_cache
rootdir: /opt/app, configfile: pytest.ini
plugins: cov-4.0.0
collected 6 items

test/test_basics.py ..                                                   [ 33%]
test/test_doc_participant.md .                                           [ 50%]
test/test_participant.py ...                                             [100%]

---------- coverage: platform linux, python 3.11.1-final-0 -----------
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------
generator/__init__.py              0      0   100%
generator/genobject.py            16      0   100%
generator/participant.py          16      0   100%
model/__init__.py                  0      0   100%
model/participant.py              17      0   100%
model/simobject.py                 9      0   100%
simulation/__init__.py             0      0   100%
simulation/create_objects.py      24      0   100%
simulation/simulation.py          25      0   100%
test/__init__.py                   0      0   100%
test/test_basics.py               13      0   100%
test/test_participant.py          15      0   100%
utils/__init__.py                  0      0   100%
utils/log_loggers.py               5      0   100%
------------------------------------------------------------
TOTAL                            140      0   100%

Required test coverage of 90% reached. Total coverage: 100.00%

============================== 6 passed in 0.12s ===============================
py311: OK ✔ in 1.65 seconds
type: commands[0]> mypy --python-version 3.11 --strict generator model simulation utils se_sim.py
Success: no issues found in 13 source files
type: OK ✔ in 3.45 seconds
flake8: commands[0]> flake8 generator model simulation utils se_sim.py
  py311: OK (1.65=setup[1.05]+cmd[0.60] seconds)
  type: OK (3.45=setup[0.39]+cmd[3.06] seconds)
  flake8: OK (0.65=setup[0.38]+cmd[0.27] seconds)
  congratulations :) (5.82 seconds)
```

### see also GitHub Actions

These checks are automatically executed on GitHub:

[![python tox](https://github.com/smart-energy-di/pg-se-sim/actions/workflows/tox.yaml/badge.svg)](https://github.com/smart-energy-di/pg-se-sim/actions/workflows/tox.yaml)
