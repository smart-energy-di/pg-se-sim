# via docker

## build the image

```shell
$ docker build -t se_sim -f Dockerfile .
```

```text
Step 1/7 : FROM python:3.11-alpine
Step 2/7 : COPY requirements_prd.txt /opt/app/requirements_prd.txt
Step 3/7 : WORKDIR /opt/app
Step 4/7 : RUN pip install --no-cache-dir --root-user-action=ignore -r requirements_prd.txt
Step 5/7 : COPY ./src /opt/app
Step 6/7 : ENV PYTHONPATH "${PYTHONPATH}:/opt/app"
Step 7/7 : ENTRYPOINT ["python","./se_sim/cli.py"]
...
Successfully tagged se_sim:latest
```

## run the container

```shell
$ docker run --rm se_sim \
       se_sim.plugins.input.v01example.read \
       se_sim.plugins.output.v01generator.Generator
```

```text
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

run docker instance with some debug output

```shell
$ docker run --rm se_sim --dp --dp \
            se_sim.plugins.input.v01example.read \
            se_sim.plugins.output.v01generator.Generator
```

```text
[2023-02-14T21:29:38]    INFO - Program start                                                                                                 
(Simulation:
        (participant:'oven')
        (participant:'instantaneous water heater big')
        ...
        (participant:'Electricity storage heater')
)
[2023-02-14T21:29:38]    INFO - Program exit
```
