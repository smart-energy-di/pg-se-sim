# smart energy simulator

## This is a first draft to simulate different objects in a smart energy world.

stay tuned...


A docker environment or other test environments are not yet part of the project.

Hopefully, this will all develop in the process of many small iterative steps.

### Here is the very first output:

```console
> python se_sim.py --dp --dp --dm --dm --dm
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'oven')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'instantaneous water heater big')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'instantaneous water heater small')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'freezer')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'freezer combination')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'domestic waterworks')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'heating cartridge in buffer tank')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'air conditioning')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'fridge')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'Charger')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'ventilation unit')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'Network Attached Storage')
[2023-02-07T18:00:54]   DEBUG - New 'producer' object (en:'PV modules (DC side)')
[2023-02-07T18:00:54]   DEBUG - New 'prosumer' object (en:'PV Inverter')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'Dishwasher')
[2023-02-07T18:00:54]   DEBUG - New 'prosumer' object (en:'power storage (AC side)')
[2023-02-07T18:00:54]   DEBUG - New 'prosumer' object (en:'Wallbox (AC side)')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'heat pump heating')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'heat pump domestic hot water')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'hot water boiler')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'washing machine')
[2023-02-07T18:00:54]   DEBUG - New 'consumer' object (en:'Electricity storage heater')
[2023-02-07T18:00:54]    INFO - Number of objects  22
[2023-02-07T18:00:54]    INFO - Role: 'consumer':  18
[2023-02-07T18:00:54]    INFO - Role: 'prosumer':   3
[2023-02-07T18:00:54]    INFO - Role: 'producer':   1
[2023-02-07T18:00:54]    INFO - Program exit
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
$ docker run --rm se_sim --dm --dm --dm --dp --dp
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'oven')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'instantaneous water heater big')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'instantaneous water heater small')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'freezer')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'freezer combination')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'domestic waterworks')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'heating cartridge in buffer tank')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'air conditioning')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'fridge')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'Charger')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'ventilation unit')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'Network Attached Storage')
[2023-02-08T12:47:22]   DEBUG - New 'producer' object (en:'PV modules (DC side)')
[2023-02-08T12:47:22]   DEBUG - New 'prosumer' object (en:'PV Inverter')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'Dishwasher')
[2023-02-08T12:47:22]   DEBUG - New 'prosumer' object (en:'power storage (AC side)')
[2023-02-08T12:47:22]   DEBUG - New 'prosumer' object (en:'Wallbox (AC side)')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'heat pump heating')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'heat pump domestic hot water')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'hot water boiler')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'washing machine')
[2023-02-08T12:47:22]   DEBUG - New 'consumer' object (en:'Electricity storage heater')
[2023-02-08T12:47:22]    INFO - Number of objects  22
[2023-02-08T12:47:22]    INFO - Role: 'consumer':  18
[2023-02-08T12:47:22]    INFO - Role: 'prosumer':   3
[2023-02-08T12:47:22]    INFO - Role: 'producer':   1
[2023-02-08T12:47:22]    INFO - Program exit
````

