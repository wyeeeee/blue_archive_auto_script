stage_data = {
    '19-1-sss-present-task': {
        'start': {
            'pierce1': (889, 426),
            'mystic1': (304, 245),
        },
        'action': [
            {'t': 'click', 'p': (655, 437), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (571, 264), 'ec': True, 'wait-over': True, 'desc': "2 upper right"},

            {'t': 'click', 'p': (611, 329), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (631, 368), 'ec': True, 'wait-over': True, 'desc': "2 lower right"},

            {'t': 'click', 'p': (586, 284), 'ec': True, 'desc': "1 upper left"},
            {'t': 'click', 'p': (634, 201), 'ec': True, 'wait-over': True, 'desc': "2 upper right"},

            {'t': 'exchange_and_click', 'p': (742, 342), 'ec': True, 'desc': "2 right"},
            {'t': 'click', 'p': (604, 456), 'wait-over': True, 'desc': "1 lower left"},

            {'t': 'exchange_and_click', 'p': (775, 374), 'ec': True, 'desc': "2 lower right"},
            {'t': 'click', 'p': (517, 577), 'desc': "1 lower left"},
        ]
    },
    '19-2-sss-present-task': {
        'start': {
            'pierce1': (824, 556),
            'mystic1': (371, 135),
        },
        'action': [
            {'t': 'click', 'p': (677, 395), 'ec': True, 'desc': "1 upper left"},
            {'t': 'click', 'p': (602, 381), 'ec': True, 'wait-over': True, 'desc': "2 lower right"},

            {'t': 'click', 'p': (478, 359), 'ec': True, 'desc': "1 upper left"},
            {'t': 'click', 'p': (628, 344), 'ec': True, 'wait-over': True, 'desc': "2 right"},

            {'t': 'choose_and_change', 'p': (512, 260), 'desc': "swap 1 2"},
            {'t': 'click', 'p': (610, 218), 'ec': True, 'desc': "1 upper right"},
            {'t': 'click', 'p': (511, 437), 'ec': True, 'wait-over': True, 'desc': "2 left"},

            {'t': 'exchange_and_click', 'p': (586, 569), 'ec': True, 'desc': "2 lower left"},
            {'t': 'click', 'p': (511, 291), 'wait-over': True, 'desc': "1 left"},

            {'t': 'exchange_and_click', 'p': (784, 572), 'ec': True, 'desc': "2 lower right"},
            {'t': 'click', 'p': (514, 215), 'desc': "1 upper left"},
        ]
    },
    '19-3-sss-present-task': {
        'start': {
            'pierce1': (763, 601),
            'mystic1': (400, 236),
            'pierce2': (583, 75),
        },
        'action': [
            {'t': 'click', 'p': (763, 416), 'ec': True, 'desc': "1 upper right"},
            {'t': 'click', 'p': (586, 239), 'ec': True, 'desc': "2 upper right"},
            {'t': 'click', 'p': (743, 273), 'ec': True, 'wait-over': True, 'desc': "3 right"},

            {'t': 'click', 'p': (694, 429), 'ec': True, 'desc': "1 upper right"},
            {'t': 'click', 'p': (631, 330), 'ec': True, 'desc': "2 right"},
            {'t': 'click', 'p': (545, 392), 'ec': True, 'wait-over': True, 'desc': "3 lower left"},

            {'t': 'click', 'p': (710, 280), 'ec': True, 'desc': "1 upper right"},
            {'t': ['exchange', 'choose_and_change'], 'p': (607, 381), 'desc': "swap 2 3"},
            {'t': 'click', 'p': (727, 380), 'ec': True, 'desc': "3 right"},
            {'t': 'click', 'p': (505, 315), 'wait-over': True, 'desc': "2 left"},

            {'t': 'click', 'p': (713, 353), 'ec': True, 'desc': "1 upper left"},
            {'t': 'click', 'p': (385, 342), 'ec': True, 'desc': "2 left"},
            {'t': 'click', 'p': (839, 342), 'ec': True, 'wait-over': True, 'desc': "3 upper right"},

            {'t': 'exchange_and_click', 'p': (436, 287), 'ec': True, 'desc': "2 upper left"},
            {'t': 'exchange_twice_and_click', 'p': (902, 404), 'ec': True, 'desc': "3 right"},
            {'t': 'choose_and_change', 'p': (787, 386), 'desc': "change 1 2"},
            {'t': 'click', 'p': (841, 315), 'desc': "1 upper right"},
        ]
    },
}
