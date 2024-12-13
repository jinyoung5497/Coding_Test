import math

def solution(fees, records):
    cars = []
    default_min, default_price, per_minute, per_price = fees
    for i in records:
        a,b,c = i.split()
        cars.append(b)

    cars = sorted(set(cars))
    answer = []
    for car in cars:
        calc_time = []
        for i in records:
            a, b, c = i.split()
            hour, minute = a.split(':')
            time = (int(hour) * 60) + int(minute)
            if b == car:
                calc_time.append(time)
        if len(calc_time) % 2 != 0:
            calc_time.append(1439)

        calc = 0
        for i in range(len(calc_time)):
            if (i + 1) % 2 == 0:
                calc += calc_time[i] - calc_time[i-1]

        if calc > default_min:
            parking_price = default_price + math.ceil((calc - default_min) / per_minute) * per_price
            answer.append(parking_price)
        else:
            answer.append(default_price)

    return answer