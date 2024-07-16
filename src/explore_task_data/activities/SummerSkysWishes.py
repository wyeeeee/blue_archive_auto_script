stage_data = {
    "SUB": "burst1",
    "story1": {
        'start': [
            ['burst1', (344, 264)],
        ],
        'action': [
            {'t': 'click_and_teleport', 'p': (630, 330), 'wait-over': True, "desc": "right and tp"},
            {'t': 'click', 'p': (720, 464), "desc": "lower left"},
        ]
    },
    "story3": {
        'start': [
            ['burst1', (490, 387)],
        ],
        'action': [
            {'t': 'click', 'p': (451, 483), 'wait-over': True, "desc": "lower left"},
            {'t': 'click_and_teleport', 'p': (401, 421), "desc": "left and tp"},
        ]
    },
    "story4": {
        'start': [
            ['burst1', (464, 347)],
        ],
        'action': [
            {'t': 'click_and_teleport', 'p': (562, 436), 'wait-over': True, "desc": "lower left and tp"},
            {'t': 'click_and_teleport', 'p': (657, 398), 'wait-over': True, "desc": "choose self and tp"},
            {'t': 'click', 'p': (436, 398), "desc": "lower left"},
        ]
    },
    "story5": {
        'start': [
            ['burst1', (406, 306)]
        ],
        'action': [
            {'t': 'click', 'p': (562, 462), 'wait-over': True, "desc": "lower right"},
            {'t': 'click', 'p': (570, 416), 'wait-over': True, "desc": "lower right"},
            {'t': 'click', 'p': (592, 446), 'wait-over': True, "desc": "lower right"},
            {'t': 'click', 'p': (681, 493), "desc": "lower right"},
        ]
    },
    "challenge3_sss": {
        'start': [
            ['burst1', (1095, 476)],
            ['pierce1', (357, 501)],
            ['burst2', (39, 443)]
        ],
        'action': [
            {'t': 'click', 'p': (666, 382), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (607, 490), 'ec': True, "desc": "2 left"},
            {'t': 'click', 'p': (561, 341), 'ec': True, 'wait-over': True, "desc": "3 upper right"},

            {'t': 'click_and_teleport', 'p': (549, 397), 'ec': True, "desc": "1 lower left and tp"},
            {'t': 'click', 'p': (576, 427), 'ec': True, "desc": "2 upper left"},
            {'t': 'click_and_teleport', 'p': (491, 409), 'wait-over': True, "desc": "3 choose self and tp"},
            {'t': 'choose_and_change', 'p': (672, 345), "desc": "swap 2 3"},
            {'t': 'click', 'p': (618, 270), 'ec': True, 'wait-over': True, "desc": "3 upper left"},

            {'t': ['exchange', 'click_and_teleport'], 'p': (719, 490), 'wait-over': True, "desc": "2 choose self and tp"},
            {'t': 'click', 'p': (386, 385), 'ec': True, "desc": "2 left"},
            {'t': 'exchange_twice_and_click', 'p': (839, 293), 'ec': True, "desc": "3 upper right"},
            {'t': 'choose_and_change', 'p': (740, 364), "desc": "swap 1 3"},
            {'t': ['exchange_twice', 'click_and_teleport'], 'p': (719, 300), 'ec': True, "desc": "3 choose self and tp"},
            {'t': 'click', 'p': (654, 311), 'wait-over': True, "desc": "1 right"},

            {'t': 'exchange_and_click', 'p': (562, 338), 'ec': True, "desc": "2 upper right"},
            {'t': 'click', 'p': (887, 336), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (844, 483), 'ec': True, 'wait-over': True, "desc": "3 lower left"},

            {'t': 'exchange_and_click', 'p': (439, 510), 'ec': True, "desc": "2 lower left"},
            {'t': 'click', 'p': (769, 297), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (663, 400), "desc": "3 upper left"},
        ]
    },
    "challenge3_task": {
        'start': [
            ['burst1', (1095, 476)],
            ['pierce1', (357, 501)],
            ['burst2', (39, 443)]
        ],
        'action': [
            {'t': 'click', 'p': (666, 382), 'ec': True, "desc": "1 left"},
            {'t': 'click_and_teleport', 'p': (607, 490), 'ec': True, "desc": "2 left and tp"},
            {'t': 'click', 'p': (449, 350), 'ec': True, 'wait-over': True, "desc": "3 upper left"},

            {'t': 'click', 'p':(546, 413), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (433, 466), 'ec': True, "desc": "2 lower left"},
            {'t': 'choose_and_change', 'p': (556, 452), "desc": "swap 2 3"},
            {'t': 'click', 'p': (494, 541), 'ec': True, 'wait-over': True, "desc": "3 lower left"},

            {'t': 'click_and_teleport', 'p': (604, 504), "desc": "1 choose self and teleport"},
            {'t': 'click', 'p': (567, 383), 'ec': True, "desc": "1 lower right"},
            {'t': 'end-turn'},

            {'t': 'click', 'p': (619, 421), 'ec': True, "desc": "1 right"},
            {'t': 'end-turn'},

            {'t': 'click', 'p': (778, 359), 'ec': True, "desc": "1 right"},
            {'t': 'end-turn'},

            {'t': 'click', 'p': (893, 354), 'ec': True, "desc": "1 right"},
            {'t': 'end-turn'},


        ]
    },
}
