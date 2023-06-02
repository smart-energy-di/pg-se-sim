from se_sim.model.participant import Participant


def createSimObjects(obj_list: list[Participant]) -> None:
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='oven',
            de_title='Backofen',
            lwh=('10 cm', '10 cm', '10 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='instantaneous water heater big',
            de_title='Durchlauferhitzer groß',
            lwh=('20 cm', '20 cm', '20 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='instantaneous water heater small',
            de_title='Durchlauferhitzer klein',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='freezer',
            de_title='Gefrierschrank/Kühltruhe',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='freezer combination',
            de_title='Gefrierschrankkombination',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='domestic waterworks',
            de_title='Hauswasserwerk',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='heating cartridge in buffer tank',
            de_title='Heizpatrone im Pufferspeicher',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='air conditioning',
            de_title='Klimaanlage',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='fridge',
            de_title='Kühlschrank',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='Charger',
            de_title='Ladegeräte',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='ventilation unit',
            de_title='Lüftungsgerät',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='Network Attached Storage',
            de_title='Netzwerkgebundene Speicher (NAS)',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='producer',
            en_title='PV modules (DC side)',
            de_title='PV-Module (DC-Seite)',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='prosumer',
            en_title='PV Inverter',
            de_title='PV-Wechselrichter',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='Dishwasher',
            de_title='Spülmaschine',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='prosumer',
            en_title='power storage (AC side)',
            de_title='Stromspeicher (AC-seitig)',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='prosumer',
            en_title='Wallbox (AC side)',
            de_title='Wallbox (AC-seitig)',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='heat pump heating',
            de_title='Wärmepumpe Heizung',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='heat pump domestic hot water',
            de_title='Wärmepumpe Warmwasser',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='hot water boiler',
            de_title='Warmwasserboiler',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='washing machine',
            de_title='Waschmaschine',
            lwh=('30 cm', '30 cm', '30 cm')))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='Electricity storage heater',
            de_title='Stromspeicherheizung',
            lwh=('30 cm', '30 cm', '30 cm')))
