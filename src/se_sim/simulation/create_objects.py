from se_sim.model.participant import Participant


def createSimObjects(obj_list: list[Participant]) -> None:
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='oven',
            de_title='Backofen'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='instantaneous water heater big',
            de_title='Durchlauferhitzer groß'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='instantaneous water heater small',
            de_title='Durchlauferhitzer klein'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='freezer',
            de_title='Gefrierschrank/Kühltruhe'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='freezer combination',
            de_title='Gefrierschrankkombination'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='domestic waterworks',
            de_title='Hauswasserwerk'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='heating cartridge in buffer tank',
            de_title='Heizpatrone im Pufferspeicher'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='air conditioning',
            de_title='Klimaanlage'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='fridge',
            de_title='Kühlschrank'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='Charger',
            de_title='Ladegeräte'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='ventilation unit',
            de_title='Lüftungsgerät'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='Network Attached Storage',
            de_title='Netzwerkgebundene Speicher (NAS)'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='producer',
            en_title='PV modules (DC side)',
            de_title='PV-Module (DC-Seite)'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='prosumer',
            en_title='PV Inverter',
            de_title='PV-Wechselrichter'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='Dishwasher',
            de_title='Spülmaschine'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='prosumer',
            en_title='power storage (AC side)',
            de_title='Stromspeicher (AC-seitig)'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='prosumer',
            en_title='Wallbox (AC side)',
            de_title='Wallbox (AC-seitig)'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='heat pump heating',
            de_title='Wärmepumpe Heizung'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='heat pump domestic hot water',
            de_title='Wärmepumpe Warmwasser '))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='hot water boiler',
            de_title='Warmwasserboiler'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='washing machine',
            de_title='Waschmaschine'))
    # ----------------------------------------------------------------------
    obj_list.append(
        Participant(
            el_role='consumer',
            en_title='Electricity storage heater',
            de_title='Stromspeicherheizung'))
