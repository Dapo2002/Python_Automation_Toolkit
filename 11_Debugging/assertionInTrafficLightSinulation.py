# A state-machine simulation using assertions to enforce safety invariants, ensuring
# that at least one 'red' value persists across dictionary transitions.

market_2nd = {'ns': 'green', 'ew': 'red'}


def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red!' + str(stoplight)


switchLights(market_2nd)
