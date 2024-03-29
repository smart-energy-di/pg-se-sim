### object "participant"

Let's play a little with an object "participant".


Output of a python console is checked in the test framework.

As in the following example:

```pycon
>>> x = 1
>>> x
1

```

#### create a participant here:

```pycon
>>> from se_sim.model.participant import Participant
>>> p=Participant(el_role='no_role',
...               en_title='en_title',
...               de_title='de_title',
...               lwh=("0.57 m", "0.59 m", "0.595 m"))
>>> type(p)
<class 'se_sim.model.participant.Participant'>

```

#### check en_title and de_title
```pycon
>>> p.en_title
'en_title'
>>> p.de_title
'de_title'

```


#### or create some participants from source code

````pycon
>>> from se_sim.simulation.simulation import Simulation
>>> AllSimObjects = Simulation()
>>> AllSimObjects.create_objects()
>>> len(AllSimObjects)
22

````

#### select the 'oven' object

````pycon
>>> AllSimObjects.get_obj_by_en_title('title_not_in_list')
>>> AllSimObjects.get_obj_by_en_title('oven')
<se_sim.model.participant.Participant object at ...>

````

#### very first generator output ;-)

````pycon
>>> env = {}
>>> AllSimObjects.generate(env)
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
