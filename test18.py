car_weight = float(input('ป้อนน้ำหนักรถ: '))
car_number = input('ป้อนทะเบียนรถ: ')                        
print('---------------------------')
if car_weight > 1000 :
    print(f'รถทะเบียน {car_number} น้ำหนักรถ {car_weight} ไม่ผ่านเกณฑ์' )
else :
    print(f'รถทะเบียน {car_number} น้ำหนักรถ {car_weight} ผ่านเกณฑ์' )