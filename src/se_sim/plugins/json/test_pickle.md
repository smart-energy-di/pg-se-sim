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
>>> plugin_obj = cli_utils.locate("se_sim.plugins.test.inp.Test01")
>>> data_out = cli_utils.compute_plugin(data_inp, data_out,
...                                     plugin_obj,
...                                     plugin_params,
...                                     runtime_infos)
>>>

```


```pycon
>>> pprint(sorted(data_out.items()))
    [('data', [<se_sim.model.participant.Participant object at ...>]),
     ('data_type', 'v0simulation'),
     ('history', [])]

```




```pycon
>>> plugin_obj = cli_utils.locate("se_sim.plugins.json.pickle.StdOut")
>>> data_out = cli_utils.compute_plugin(data_inp, data_out, 
...                                     plugin_obj,
...                                     plugin_params,
...                                     runtime_infos)
[{"py/object": "se_sim.model.participant.Participant", "_uuid": "...", "el_role": "consumer", "en_title": "oven", "de_title": "Backofen", "lwh": {"py/tuple": ["0.57 m", "0.59 m", "0.595 m"]}}]

```

```pycon
>>> plugin_params = {'pretty': True}
>>> data_out = cli_utils.compute_plugin(data_inp, data_out, 
...                                     plugin_obj,
...                                     plugin_params,
...                                     runtime_infos)
    [
      {
        "_uuid": "...",
        "el_role": "consumer",
        "en_title": "oven",
        "de_title": "Backofen",
        "lwh": [
          "0.57 m",
          "0.59 m",
          "0.595 m"
         ]
      }
    ]


```


#### what comes out of the plugin

```pycon

```
