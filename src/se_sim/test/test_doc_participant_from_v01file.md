### object "participant"

#### or create some participants from example file

````pycon
>>> from se_sim.simulation.simulation import Simulation
>>> AllSimObjects = Simulation()
>>> AllSimObjects.create_from_json('./src/se_sim/simulation/v01example.json')
>>> len(AllSimObjects)
2

````

#### very first generator output ;-)

````pycon
>>> env = {}
>>> AllSimObjects.generate(env)
    (Simulation:
            (participant:'oven')
            (participant:'instantaneous water heater big')
)

````
