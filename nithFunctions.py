import numpy as np
from udpFunctions import send_generic_udp_message


SENSORNAME = "NITHbeamWrapper"
SENSORVERSION = "0.1.0"
OPCODE_OPR = "OPR"
OPCODE_ERR = "ERR"


def send_data(
    head_pos_pitch,
    head_pos_yaw,
    head_pos_roll,
    gaze_x,
    gaze_y,
    head_presence,
    gaze_presence,
    verbose=False,
):
    message = (
        "$"
        + SENSORNAME
        + "-"
        + SENSORVERSION
        + "|"
        + OPCODE_OPR
        + "|"
        + "head_pos_pitch="
        + str(np.round(head_pos_pitch, 2))
        + "&head_pos_yaw="
        + str(np.round(head_pos_yaw, 2))
        + "&head_pos_roll="
        + str(np.round(head_pos_roll, 2))
        + "&gaze_x="
        + str(np.round(gaze_x, 5))
        + "&gaze_y="
        + str(np.round(gaze_y, 5))
        + "&head_presence="
        + str(head_presence)
        + "&gaze_presence="
        + str(gaze_presence)
        + "$"
    )

    if verbose:
        print(message)

    send_generic_udp_message(message)
