def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if not valid_period(permanence_period):
        return None
    if target_time is None:
        return None
    cont = 0
    for period in permanence_period:
        if target_time >= int(period[0]) and target_time <= int(period[1]):
            cont += 1
    return cont


def valid_period(periods):
    for period in periods:
        if period[0] is None or period[1] is None:
            return False
        if (isinstance(period[0], str)) or (isinstance(period[1], str)):
            return False
        if (period[1] - period[0]) < 0:
            return False
    return True
