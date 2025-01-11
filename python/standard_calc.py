def bound_to_180(angle):
    # mod operator
    angle_new = angle % 360
    if (angle_new >= 180):
        return float(angle_new - 360)
    else:
        return float(angle_new)

    # if (-180 <= angle < 180):
    #     return float(angle)
    # elif (180 <= angle <= 360):
    #     return float(angle - 360)
    # elif (angle > 360):
    #     return float(angle - (angle // 360) * 360)
    # else:
    #     return float(360 + angle)


def is_angle_between(first_angle, middle_angle, second_angle):

    if (second_angle - first_angle > 180):
        temp_second_angle = second_angle
        second_angle = first_angle
        first_angle = temp_second_angle - 360

    if (first_angle <= middle_angle <= second_angle):
        return True
    else:
        return False
