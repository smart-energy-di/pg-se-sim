# smart energy simulator

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://github.com/smart-energy-di/pg-se-sim/blob/36a3d5c1ccc3d8ae497d308d73c2b0176cb83967/LICENSE)

[![python tox](https://github.com/smart-energy-di/pg-se-sim/actions/workflows/tox.yaml/badge.svg)](https://github.com/smart-energy-di/pg-se-sim/actions/workflows/tox.yaml)
[![GitHub Watches](https://img.shields.io/github/watchers/smart-energy-di/pg-se-sim.svg?style=plastic&label=Watch&maxAge=2592000)](https://github.com/smart-energy-di/pg-se-sim/watchers)
[![GitHub Starts](https://img.shields.io/github/stars/smart-energy-di/pg-se-sim.svg?style=plastic&label=Star&maxAge=2592000)](https://github.com/smart-energy-di/pg-se-sim/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/smart-energy-di/pg-se-sim.svg?style=plastic&label=Fork&maxAge=2592000)](https://github.com/smart-energy-di/pg-se-sim/network)


## Why simulation within the "Smart Energy" topic?

The approach of a simulation has the following aspects:
- you can start small 
- small steps, iterative development of documented dependencies 
- complex systems are more difficult to put into theories and can be simulated or emulated much better
- simulation can later be transferred into emulation, emulations can then become part of the real world (like e.g. emulators in microelectronics)
- simulation results can be presented in different ways (to suit the target group) (multiple "views" and levels of abstraction on data)
- simulations are much more likely to invite participation
- good simulations have real interfaces that can be evaluated
- the whole playground can include multiple simulation approaches so that different levels of abstraction can be explored. Played together, it then becomes a big picture. 
- the big master plan initially only needs to be vision, the focus can be on dedicated parts
- a high level of professionalism in the "simulation framework" also motivates developers at the "big players" in the medium term. 
- the open source approach of a simulation on github also frees from dependencies on individuals (bus factor).
- good simulations can be automated. Changes to the code automatically lead to new documentation (CI/CD pipelines)
- simulations can be versioned



## This is a first draft to simulate different objects in a smart energy world.

stay tuned...


A docker environment or other test environments are not yet part of the project.

Hopefully, this will all develop in the process of many small iterative steps.

### Here is the very first output:

```console
$ python ./src/se_sim/cli.py \
       se_sim.plugins.input.v01example.read \
       se_sim.plugins.output.v01generator.Generator
(Simulation:
        (participant:'oven')
        (participant:'instantaneous water heater big')
        (participant:'instantaneous water heater small')
        (participant:'freezer')
        (participant:'freezer combination')
        (participant:'domestic waterworks')
        (participant:'heating cartridge in buffer tank')
        (participant:'air conditioning')
        (participant:'fridge')
        (participant:'Charger')
        (participant:'ventilation unit')
        (participant:'Network Attached Storage')
        (participant:'PV modules (DC side)')
        (participant:'PV Inverter')
        (participant:'Dishwasher')
        (participant:'power storage (AC side)')
        (participant:'Wallbox (AC side)')
        (participant:'heat pump heating')
        (participant:'heat pump domestic hot water')
        (participant:'hot water boiler')
        (participant:'washing machine')
        (participant:'Electricity storage heater')
)

```

### and here are the first steps with docker

#### build the image

```shell
$ docker build -t se_sim -f Dockerfile .
Step 1/7 : FROM python:3.11-alpine
[...]
Successfully tagged se_sim:latest
```

#### run the container

````shell
$ docker run --rm se_sim \
           se_sim.plugins.input.v01example.read \
           se_sim.plugins.output.v01generator.Generator
(Simulation:
        (participant:'oven')
        (participant:'instantaneous water heater big')
        (participant:'instantaneous water heater small')
        (participant:'freezer')
        (participant:'freezer combination')
        (participant:'domestic waterworks')
        (participant:'heating cartridge in buffer tank')
        (participant:'air conditioning')
        (participant:'fridge')
        (participant:'Charger')
        (participant:'ventilation unit')
        (participant:'Network Attached Storage')
        (participant:'PV modules (DC side)')
        (participant:'PV Inverter')
        (participant:'Dishwasher')
        (participant:'power storage (AC side)')
        (participant:'Wallbox (AC side)')
        (participant:'heat pump heating')
        (participant:'heat pump domestic hot water')
        (participant:'hot water boiler')
        (participant:'washing machine')
        (participant:'Electricity storage heater')
)

````

run docker instance with some debug output

````shell
$ docker run --rm se_sim --dp --dp \
            se_sim.plugins.input.v01example.read \
            se_sim.plugins.output.v01generator.Generator
[2023-02-14T21:29:38]    INFO - Program start                                                                                                 
(Simulation:
        (participant:'oven')
        (participant:'instantaneous water heater big')
        ...
        (participant:'Electricity storage heater')
)
[2023-02-14T21:29:38]    INFO - Program exit

````
