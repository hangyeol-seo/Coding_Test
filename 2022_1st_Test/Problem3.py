import math

def convert_time(time):
    temp=time.split(":")
    temp=list(map(int,temp))
    return temp[0]*60 + temp[1]

def calculate_fee(time,fees):
    base_time=fees[0]
    base_fee=fees[1]
    unit_time=fees[2]
    unit_fee=fees[3]
    
    if time<=base_time:
        return base_fee
    else:
        return base_fee+math.ceil((time-base_time)/unit_time)*unit_fee
    
def solution(fees, records):
    answer = []
    parkinglot={}
    car_time_dic={}
    
    for record in records:
        r=record.split()
        if r[1] not in car_time_dic:
            car_time_dic[r[1]]=0
        if r[2]=="IN":
            parkinglot[r[1]]=r[0]
            
        else:
            car_time_dic[r[1]]+=convert_time(r[0])-convert_time(parkinglot[r[1]])
            del parkinglot[r[1]]
    
    for car in parkinglot:
        car_time_dic[car]+=convert_time("23:59")-convert_time(parkinglot[car])
    print(car_time_dic)
    
    cars=sorted(car_time_dic.keys(),key=lambda x:int(x))

    for car in cars:
        answer.append(calculate_fee(car_time_dic[car],fees))
    
            
    return answer
