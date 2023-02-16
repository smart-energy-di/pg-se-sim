# via Python pyenv

## create a virtual python environment

```shell
$ python3.11 -m venv ~/.virtualenvs/se_sim
```

and activate it

> **_NOTE:_** Depending on the shell, you can either use
> - Activate.ps1
> - activate 
> - activate.csh
> - activate.fish

```shell
$ source ~/.virtualenvs/se_sim/bin/activate
```

now the environment is empty

```shell
$ pip list
Package    Version
---------- -------
pip        22.3.1
setuptools 65.6.3
```

now first install the production part of the environment

('git clone' assumed and changed into the directory)

```shell
$ pip install -r requirements_prd.txt
```

```shell
$ pip list
Package    Version
---------- -------
click      8.1.3
pip        22.3.1
PyYAML     6.0
setuptools 65.6.3
```


current workaround for python to find a module that is not actually installed

```shell
export PYTHONPATH=src/
```

and lift off ...

```shell
$ python ./src/se_sim/cli.py \
    se_sim.plugins.input.v01example.read \
    se_sim.plugins.json.out.StdOut:pretty=true
```
