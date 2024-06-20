class Power():
    def __init__(self):
        self.fuel=int(input("\nEnter the no.of fuel(coal[1],natural gas[2],methane[3]): "))
        if self.fuel == 1:
            self.cv = 30000
        elif self.fuel == 2:
            self.cv = 53600
        else:
            self.cv = 55600
        self.h2=float(input("Enter the enthalopy of steam to the boiler(h2): "))
        self.h3=float(input("Enter the enthalopy of steam from the boiler(h3): "))
        self.h4=float(input("Enter the enthalopy of steam from the turbine(h4): "))
        self.hs=self.h3-self.h4
        self.mf=float(input("Enter the mass of the fuel: "))
        self.ms=float(input("Enter the mass of the steam: "))
        self.brake_output = float(input("Enter the brake output or losses in turbine: "))

    def cycle(self):
        efficiency_of_cycle = self.hs /(self.h3-self.h2)
        return efficiency_of_cycle *100

    def boiler(self):
        efficiency_of_boiler = self.hs /(self.mf*self.cv)
        return efficiency_of_boiler *100
    
    def turbine(self):
        efficieny_of_turbine = self.brake_output/(self.hs*self.ms)
        return efficieny_of_turbine *100

    def generator(self):
        efficiency_of_generator = 3600/self.brake_output
        return efficiency_of_generator *100
    
    def overall(self):
        overall_efficiency = 3600/(self.mf*self.cv)
        return overall_efficiency *100
    
plant=Power()


def overall():
        print("\n\tη of RANKINE CYCLE:",plant.cycle(),"KJ/Kg")
        print("\tη of BOILER:",plant.boiler(),"KJ/Kg")
        print("\tη of TURBINE:",plant.turbine(),"KJ/Kg")
        print("\tη of GENERATOR:",plant.generator(),"KJ/Kg")
        print("\tη of THERMAL POWER PLANT:",plant.overall(),"KJ/Kg")