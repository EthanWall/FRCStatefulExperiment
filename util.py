def deadband(value: float, deadband: float) -> float:
    """
    Require a "deadband" to be surpassed in order to return the given value.

    :param value: The value to be tested
    :param deadband: The number that the value must surpass
    :return: The deadbanded value
    """

    return value if abs(value) > abs(deadband) else 0
