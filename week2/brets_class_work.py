class ScubaGear:
    def __init__(self, user, air_tanks, mask, flippers, harpoon, bcd, regulator):
        self.user = user
        self.air_tanks = air_tanks
        self.mask = mask
        self.flippers = flippers
        self.harpoon = harpoon
        self.bcd = bcd
        self.regulator = regulator
        self.diver_certified = False
        self.dives_completed = 0

    def display_info(self):
        print(self.user)
        print(self.air_tanks)
        print(self.mask)
        print(self.flippers)
        print(self.harpoon)
        print(self.bcd)
        print(self.regulator)

    def dives(self):
        self.dives_completed += 1
        print(f"You have completed a dive {self.dives_completed}")
        return self

    def certification_comlete(self):
        self.diver_certified = True
        print(f"You have completed your certification {self.diver_certified}")
        
diver_1 = ScubaGear("bret", "Scuba", "Aqua Lung", "flipped", "harpoon", "Oceanic", "Cressi")
diver_1.display_info()
diver_1.dives()
diver_1.dives()
diver_1.dives()
diver_1.dives()
diver_1.certification_comlete

#print(diver_1.user)