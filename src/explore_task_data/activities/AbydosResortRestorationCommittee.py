

stage_data = {
    "challenge2_sss": {
        'start': [
            ['pierce1', (552, 183)],
            ['burst1', (765, 514)]
        ],
        'action': [
            {'t': 'click', 'p': (686, 276), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (601, 487), 'ec': True, 'wait-over': True, "desc": "2 left"},

            {'t': 'click', 'p': (534, 270), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (526, 418), 'ec': True, 'wait-over': True, "desc": "2 upper left"},

            {'t': 'exchange_and_click', 'p': (514, 367), 'ec': True, "desc": "2 upper left"},
            {'t': 'choose_and_change', 'p': (514, 367), "desc": "swap 1 2"},
            {'t': 'click', 'p': (391, 359), 'wait-over': True, "desc": "1 right"},

            {'t': 'click_and_teleport', 'p': (606, 388), 'wait-over': True, "desc": "1 choose self and tp"},
            {'t': 'click', 'p': (835, 461), "desc": "1 lower right"},
        ]
    },
    "challenge2_task": {
        'start': [
            ['pierce1', (552, 183)],
        ],
        'action': [
            {'t': 'click', 'p': (710, 263), 'wait-over': True, "desc": "right"},
            {'t': 'click', 'p': (588, 272), 'wait-over': True, "desc": "left"},
            {'t': 'click', 'p': (525, 347), 'wait-over': True, "desc": "lower left"},
            {'t': 'click_and_teleport', 'p': (401, 344), 'wait-over': True, "desc": "left and tp"},
            {'t': 'click', 'p': (839, 469), "desc": "lower right"},
        ]
    },
    "challenge4_sss": {
        'start': [
            ['burst1', (883, 476)],
            ['pierce1', (461, 520)],
            ['burst2', (199, 115)]
        ],
        'action': [
            {'t': 'click', 'p': (895, 440), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (630, 440), 'ec': True, "desc": "2 right"},
            {'t': 'click', 'p': (644, 324), 'ec': True, 'wait-over': True, "desc": "3 right"},

            {'t': 'click_and_teleport', 'p': (838, 342), 'ec': True, "desc": "1 upper right and tp"},
            {'t': 'click', 'p': (769, 416), 'ec': True, "desc": "2 upper right"},
            {'t': 'click_and_teleport', 'p': (653, 309), 'ec': True, 'wait-over': True, "desc": "3 right and tp"},

            {'t': 'click', 'p': (644, 320), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (665, 406), 'ec': True, "desc": "2 upper left"},
            {'t': 'choose_and_change', 'p': (665, 406), "desc": "swap 2 3"},
            {'t': 'click', 'p': (547, 404), 'ec': True, 'wait-over': True, "desc": "3 left"},

            {'t': ['exchange', 'click_and_teleport'], 'p': (755, 464), 'wait-over': True, "desc": "2 choose self and tp"},
            {'t': 'click', 'p': (556, 291), "desc": "2 upper right"},
            {'t': 'choose_and_change', 'p': (624, 375), "desc": "swap 1 2"},
            {'t': 'click', 'p': (738, 380), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (541, 508), "desc": "3 left"},

        ]
    },
    "challenge4_task": {
        'start': [
            ['burst1', (229, 223)],
            ['pierce1', (1171, 588)],
        ],
        'action': [
            {'t': 'click', 'p': (628, 344), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (892, 443), 'ec': True, 'wait-over': True, "desc": "2 right"},

            {'t': 'click', 'p': (633, 332), 'ec': True, "desc": "1 right"},
            {'t': 'end-turn'},

            {'t': 'click_and_teleport', 'p': (519, 335), 'wait-over': True, "desc": "1 choose self and tp"},
            {'t': 'click', 'p': (713, 479), 'ec': True, "desc": "1 lower left"},
            {'t': 'end-turn'},

            {'t': 'click', 'p': (378, 371), 'ec': True, "desc": "1 left"},
            {'t': 'end-turn'},

            {'t': 'click', 'p': (615, 385), 'ec': True, "desc": "1 right"},
            {'t': 'end-turn'},

            {'t': 'click_and_teleport', 'p': (564, 266), 'ec': True, "desc": "1 upper right and tp"},
            {'t': 'end-turn'},

            {'t': 'click', 'p': (577, 249), 'ec': True, "desc": "1 upper right"},
            {'t': 'end-turn'},

            {'t': 'click', 'p': (601, 309), 'ec': True, "desc": "1 right"},
            {'t': 'end-turn'},
        ]
    }
}
