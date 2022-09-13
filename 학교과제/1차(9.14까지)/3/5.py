car_in_out = car_in_out = ['07:30 1234 IN', 
              '07:35 2580 IN',
              '08:15 0328 IN',
              '08:45 2580 OUT',
              '08:55 9876 IN',
              '11:00 1597 IN',
              '15:15 1234 OUT',
              '21:00 0328 OUT',
              '23:45 9876 OUT']
car_parking_log = dict()

for i in car_in_out:
    getTime, carNum, state = i.split() 

    if (state == "IN"):
        car_parking_log[carNum] = {state : getTime}
    elif (state == "OUT"):
        fee = 0
        car_parking_log[carNum].update({state : getTime})
        startHour, startMinutes = car_parking_log[carNum]["IN"].split(':')
        processedMinutes_s = int(startHour) * 60 + int(startMinutes)
        finishHour, finishMinutes = car_parking_log[carNum]["OUT"].split(':')
        processedMinutes_f = int(finishHour) * 60 + int(finishMinutes)
        parking_duration = abs(processedMinutes_s - processedMinutes_f)
        car_parking_log[carNum].update({'parking_duration' : parking_duration})

        if (30 < parking_duration < 790): # 기본 30분, 그게 아니면 무료 출차
            parking_duration -= 30
            fee += 2000

            tensFee = parking_duration // 10
            unitsFee = parking_duration % 10
            fee += 500 * tensFee

            if (unitsFee == 5):
                fee += 500
        else:
            fee = 40000
        car_parking_log[carNum].update({'parking_fee' : fee})

print(car_parking_log)