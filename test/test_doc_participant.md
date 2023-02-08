# object "participant"

Let's play a little with an object "participant".


Output of a python console is checked in the test framework.

As in the following example:

```pycon
>>> x = 1
>>> x
1

```

```pycon
>>> from model.participant import Participant
>>> p=Participant(el_role='no_role',
...               en_title='en_title',
...               de_title='de_title')
>>> type(p)
<class 'model.participant.Participant'>

```
