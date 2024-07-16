stage_data = {
    '26': {
        'SUB': "mystic1"
    },
    '26-1': {
        'start': [
            ['mystic1', (339, 512)],
            ['burst1', (701, 193)],
        ],
        'action': [
            {'t': 'click_and_teleport', 'p': (603, 559), 'ec': True, "desc": "1 lower right and tp"},
            {'t': 'click', 'p': (731, 189), "wait-over": True, 'ec': True, "desc": "2 upper right"},

            {'t': 'click', 'p': (612, 424), 'ec': True, "desc": "1 upper left"},
            {'t': 'click', 'p': (775, 276), 'ec': True, "wait-over": True, "desc": "2 right"},

            {'t': 'click', 'p': (445, 392), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (820, 409), 'ec': True, "wait-over": True, "desc": "2 lower right"},

            {'t': 'click', 'p': (434, 302), "desc": "1 upper left"},
        ]
    },
    '26-2': {
        'start': [
            ['mystic1', (791, 427)],
            ['burst1', (395, 419)],
        ],
        'action': [
            {'t': 'click', 'p': (722, 312), 'ec': True, "desc": "1 upper left"},
            {'t': 'click', 'p': (613, 397), 'ec': True, "wait-over": True, "desc": "2 right"},

            {'t': 'exchange_and_click', 'p': (648, 324), 'ec': True, "desc": "2 upper right"},
            {'t': 'choose_and_change', 'p': (648, 324), "desc": "change 1 2"},
            {'t': 'click', 'p': (588, 410), 'wait-over': True, "desc": "1 lower left"},

            {'t': 'click', 'p': (647, 493), 'ec': True, "desc": "1 lower right"},
            {'t': 'click', 'p': (824, 243), 'ec': True, "wait-over": True, "desc": "2 upper right"},

            {'t': 'exchange_and_click', 'p': (663, 210), 'ec': True, "desc": "2 upper right"},
            {'t': 'click', 'p': (619, 461), "desc": "1 lower left"},
        ]
    },
    '26-3': {
        'start': [
            ['mystic1', (525, 107)],
            ['burst1', (412, 351)],
        ],
        'action': [
            {'t': 'click', 'p': (735, 359), 'ec': True, "desc": "1 lower right"},
            {'t': 'click', 'p': (553, 451), "wait-over": True, 'ec': True, "desc": "2 lower right"},

            {'t': 'exchange_and_click', 'p': (674, 448), 'ec': True, "desc": "2 right"},
            {'t': 'choose_and_change', 'p': (674, 448), "desc": "swap 1 2"},
            {'t': 'click', 'p': (735, 532), 'wait-over': True, "desc": "1 lower right"},

            {'t': 'click', 'p': (824, 496), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (583, 364), "wait-over": True, 'ec': True, "desc": "2 lower left"},

            {'t': 'click', 'p': (824, 361), 'ec': True, "desc": "1 upper right"},
            {'t': 'click', 'p': (484, 448), "wait-over": True, 'ec': True, "desc": "2 lower left"},

            {'t': 'exchange_and_click', 'p': (449, 528), 'ec': True, "desc": "2 lower left"},
            {'t': 'click', 'p': (782, 326), "desc": "1 right"},
        ]
    },
    '26-4': {
        'start': [
            ['mystic1', (582, 261)],
            ['burst1', (400, 710)],
        ],
        'action': [
            {'t': 'click_and_teleport', 'p': (653, 210), 'ec': True, "desc": "1 upper left and tp"},
            {'t': 'click_and_teleport', 'p': (648, 588), 'ec': True, "wait-over": True, "desc": "2 lower right and tp"},

            {'t': 'exchange_and_click', 'p': (723, 336), 'ec': True, "desc": "2 upper left"},
            {'t': 'click', 'p': (567, 422), "wait-over": True, "desc": "1 lower right"},

            {'t': 'click', 'p': (719, 396), 'ec': True, "desc": "1 right"},
            {'t': 'choose_and_change', 'p': (698, 406), "desc": "swap 1 2"},
            {'t': 'click', 'p': (764, 493), 'ec': True, "wait-over": True, "desc": "2 lower right"},

            {'t': 'click', 'p': (857, 311), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (592, 597), 'ec': True, "wait-over": True, "desc": "2 lower left"},

            {'t': 'exchange_and_click', 'p': (642, 583), 'ec': True, "desc": "2 lower right"},
            {'t': 'click', 'p': (711, 246), "desc": "1 upper right"},

        ]
    },
    '26-5': {
        'start': [
            ['mystic1', (812, 144)],
            ['burst1', (470, 624)],
        ],
        'action': [
            {'t': 'exchange_and_click', 'p': (509, 412), 'ec': True, "desc": "2 upper left"},
            {'t': 'click', 'p': (592, 290), "wait-over": True, "desc": "1 left"},

            {'t': 'click', 'p': (544, 445), 'ec': True, "desc": "1 lower left"},
            {'t': 'click', 'p': (609, 397), 'ec': True, "wait-over": True, "desc": "2 upper right"},

            {'t': 'choose_and_change', 'p': (582, 377), "desc": "swap 1 2"},
            {'t': 'click', 'p': (516, 460), 'ec': True, "desc": "1 lower left"},
            {'t': 'click', 'p': (582, 207), "wait-over": True, 'ec': True, "desc": "2 upper left"},

            {'t': 'click', 'p': (488, 570), 'ec': True, "desc": "1 lower left"},
            {'t': 'click', 'p': (598, 190), 'ec': True, "wait-over": True, "desc": "2 upper left"},

            {'t': 'exchange_and_click', 'p': (529, 279), 'ec': True, "desc": "2 left"},
            {'t': 'click', 'p': (619, 458), "desc": "1 lower left"},
        ]
    },
}
