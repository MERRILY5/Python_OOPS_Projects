# Thermal-power-plant-efficiency-calcuator
def design():
    print("\n")
    print("_"*30+"THERMAL POWER PLANT EFFICIENCY CALCULATOR"+"_"*30)
    print("NOTE: All masses must be in Kg\nEnthalopy must be in kJ/Kg\nBrake output must be in KJ/Kg")
design()

from boiler import plant


def ans():
    ch=int(input("Enter the choice Rankine cycle[1],Boiler[2],Turbine[3],Generator[4],Overall[5]: "))
    if ch==1:
        print("\n\tη of RANKINE CYCLE:",plant.cycle(),"KJ/Kg")
    if ch==2:
        print("\tη of BOILER:",plant.boiler(),"KJ/Kg")
    if ch==3:
        print("\tη of TURBINE:",plant.turbine(),"KJ/Kg")
    if ch==4:
        print("\tη of GENERATOR:",plant.generator(),"KJ/Kg")
    if ch==5:
        plant.overall()

ans()

X=True
while(X):
    ag=str(input("\n\nDo you want to try again(n/y): "))
    if ag=='n':
        print("_"*120)
        break
    if ag=='y':
        ans()
    if ag!='n' or ag!='y':
        print("Try again")
        X=True