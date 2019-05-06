class SensorID:
    HOST = "主机"
    SLAVE_1 = "从机1"
    SLAVE_2 = "从机2"
    SLAVE_3 = "从机3"

    AXIS_X = 0
    AXIS_Y = 1
    AXIS_Z = 2

    DATA_ACCELERATOR = 1
    DATA_ORIENTATION = 2

    int_to_ID_dict = {
        1: HOST,
        2: SLAVE_1,
        3: SLAVE_2,
        4: SLAVE_3
    }
