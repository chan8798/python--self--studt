while True:
    try:
        x=int(input("가격을 입력하시오:"))

        if(x<=12000000):
            print(x*0.06,"원을 내십시오.")
        elif(12000000<x<=46000000):
            print(int(12000000*0.06+(x%12000000)*0.15),"원을 내십시오.")
        elif(46000000<x<=88000000):
            print(int(582+(x%46000000)*0.24),"원을 내십시오")
        elif(88000000<x<=150000000):
            print(int(1590+(x%88000000)*0.35),"원을 내십시오")
        elif(150000000<x<=300000000):
            print(int(3760+(x%150000000)*0.38),"원을 내십시오")
        elif(300000000<x<=500000000):
            print(int(9460+(x%300000000)*0.4),"원을 내십시오")
        elif(x>500000000):
            print(int(17460+(x%500000000)*0.42),"원을 내십시오")
            
        
    except ValueError:
        print("가격을 다시 입력하시오:")
        
