def attendance(rollnum):
    roll_list = [2,4,7,9,10,13,17,15,12]
    if rollnum in roll_list:
        print("the student is present")
    else:
        print("the student is absent")
attendance(7)
attendance(5)