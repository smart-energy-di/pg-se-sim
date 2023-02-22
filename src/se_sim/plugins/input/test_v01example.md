#### some imports

```pycon
>>> from pprint import pprint
>>> from typing import Any
>>> from se_sim.utils import cli_utils

```

#### what data goes into the plugin

```pycon
>>> data_inp: dict[str, Any] = {'history': [],
...                             'data': None,
...                             'data_type': 'v0simulation'}
>>> data_out = data_inp
>>> plugin_params = {}
>>> runtime_infos = {}

```

#### locate and run plugin

```pycon
>>> plugin_obj = cli_utils.locate("se_sim.plugins.input.v01example.read")
>>> data_out = cli_utils.compute_plugin(data_inp, data_out, 
...                                     plugin_obj,
...                                     plugin_params,
...                                     runtime_infos)

```

#### what comes out of the plugin

```pycon
>>> pprint(sorted(data_out.items()))
[('data', None),
 ('data_type', 'v0simulation'),
 ('history', ['created data 0815']),
 ('v0simulation',
  [<se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>,
   <se_sim.model.participant.Participant object at ...>])]

```
