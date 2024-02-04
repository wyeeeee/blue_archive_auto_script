stage_data = {
    '23-1-sss-present-task': {
        'start': {
            'burst1': (398, 695),
            'pierce1': (688, 157),
        },
        'action': [
            {'t': 'click', 'p': (719, 507), 'ec': True, 'desc': "1 right"},
            {'t': 'click', 'p': (735, 360), 'ec': True, 'wait-over': True, 'desc': "2 lower right"},

            {'t': 'click', 'p': (723, 424), 'ec': True, 'desc': "1 upper right"},
            {'t': 'click', 'p': (768, 372), 'ec': True, 'wait-over': True, 'desc': "2 lower right"},

            {'t': ['exchange', 'click_and_teleport'], 'p': (885, 367), 'ec': True,'desc': "2 right and tp"},
            {'t': 'click', 'p': (626, 411), 'wait-over': True, 'desc': "1 upper right"},

            {'t': 'exchange_and_click', 'p': (698, 241), 'ec': True, 'desc': "2 upper left"},
            {'t': 'click', 'p': (560, 277), 'wait-over': True, 'desc': "1 upper right"},

            {'t': 'choose_and_change', 'p': (685, 288), 'desc': "swap 1 2"},
            {'t': 'click', 'p': (742, 205), 'ec': True, 'desc': "1 upper right"},
            {'t': 'click', 'p': (464, 283), 'ec': True, 'wait-over': True, 'desc': "2 upper left"},

            {'t': 'exchange_and_click', 'ec': True, 'p': (431, 385), 'desc': "2 left"},
            {'t': 'click', 'p': (841, 304), 'desc': "1 upper right"},
        ]
    },
    '23-2-sss-present-task': {
        'start': {
            'burst1': (458, 346),
            'pierce1': (921, 274),
        },
        'action': [
            {'t': 'click', 'p': (614, 403), 'ec': True, 'desc': "1 right"},
            {'t': 'click_and_teleport', 'p': (721, 442), 'ec': True, 'wait-over': True, 'desc': "2 lower right and tp"},

            {'t': 'exchange_and_click', 'p': (581, 208), 'ec': True, 'desc': "2 upper left"},
            {'t': 'click_and_teleport', 'p': (659, 358), 'wait-over': True, 'desc': "1 upper right and tp"},

            {'t': 'click', 'p': (607, 488), 'ec': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (417, 310), 'ec': True, 'wait-over': True, 'desc': "2 left"},

            {'t': 'exchange_and_click', 'p': (670, 297), 'ec': True, 'desc': "2 right"},
            {'t': 'click', 'p': (807, 558), 'wait-over': True,'desc': "1 lower right"},

            {'t': 'click', 'p': (667, 573), 'ec': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (461, 286), 'ec': True, 'wait-over': True, 'desc': "2 left"},

            {'t': 'exchange_and_click', 'p': (506, 209), 'ec': True, 'desc': "2 upper left"},
            {'t': 'click', 'p': (593, 495), 'desc': "1 left"},

        ]
    },
    '23-3-sss-present-task': {
        'start': {
            'burst1': (462, 304),
            'pierce1': (807, 411),
            'burst2': (710, 160),
        },
        'action': [
            {'t': 'click', 'p': (562, 503), 'ec': True, 'desc': "1 lower right"},
            {'t': 'click', 'p': (635, 454), 'ec': True, 'desc': "2 left"},
            {'t': 'click_and_teleport', 'p': (795, 274), 'ec': True, 'wait-over': True, 'desc': "3 right and tp"},

            {'t': 'choose_and_change', 'p': (704, 409), 'desc': "swap 1 2"},
            {'t': 'click', 'p': (823, 412), 'ec': True, 'desc': "1 right"},
            {'t': 'exchange_and_click', 'p': (620, 422), 'ec': True, 'desc': "3 right"},
            {'t': 'click', 'p': (566, 355), 'ec': True, 'wait-over': True, 'desc': "2 left"},

            {'t': ['exchange_twice','choose_and_change'], 'p': (497, 372), 'desc': "swap 1 3"},
            {'t': 'click', 'p': (443, 292), 'ec': True, 'desc': "3 upper left"},
            {'t': 'click', 'p': (846, 483), 'ec': True, 'desc': "1 lower right"},
            {'t': 'click_and_teleport', 'p': (383, 427), 'ec': True, 'wait-over': True, 'desc': "2 left and tp"},

            {'t': 'exchange_and_click', 'p': (631, 199), 'ec': True, 'desc': "2 upper left"},
            {'t': 'click', 'p': (670, 463), 'ec': True, 'desc': "1 lower right"},
            {'t': 'click', 'p': (616, 343), 'ec': True, 'wait-over': True, 'desc': "3 right"},

            {'t': 'exchange_and_click', 'p': (534, 193), 'ec': True, 'desc': "2 upper left"},
            {'t': 'exchange_twice_and_click', 'p': (596, 390), 'ec': True, 'desc': "3 upper right"},
            {'t': 'click', 'p': (668, 578), 'desc': "1 lower left"},

        ]
    },
}
