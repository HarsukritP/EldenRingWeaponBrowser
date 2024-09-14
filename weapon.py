import math
class Weapon:
    def __init__(self, name, type, physical_dmg, magic_dmg, fire_dmg, light_dmg, holy_dmg, crit_dmg, stamina_dmg, str_scale, dex_scale, int_scale, faith_scale, arc_scale, weight, upgrade_type, level=1, str=10, dex=10, int=10, fai=10, arc=10):
        self._name = name
        self._type = type
        self._physicalDMG = physical_dmg
        self._magicDMG = magic_dmg
        self._fireDMG = fire_dmg
        self._lightDMG = light_dmg
        self._holyDMG = holy_dmg
        self._critDMG = crit_dmg
        self._staminaDMG = stamina_dmg
        self._strSCALE = str_scale
        self._dexSCALE = dex_scale
        self._intSCALE = int_scale
        self._faiSCALE = faith_scale
        self._arcSCALE = arc_scale
        self._weight = weight
        self._upgradeTYPE = upgrade_type

        self._level = level
        self._playerSTR = str
        self._playerDEX = dex
        self._playerINT = int
        self._playerFAI = fai
        self._playerARC = arc

    # Getter functions that return attribute values.
    def name(self):
        return self._name
    def type(self):
        return self._type
    def physical_damage(self):
        return self._physicalDMG
    def magic_damage(self):
        return self._magicDMG
    def fire_damage(self):
        return self._fireDMG
    def light_damage(self):
        return self._lightDMG
    def holy_damage(self):
        return self._holyDMG
    def crit_damage(self):
        return self._critDMG
    def stamina_damage(self):
        return self._staminaDMG
    def strength_scaling(self):
        return self._strSCALE
    def dexterity_scaling(self):
        return self._dexSCALE
    def intelligence_scaling(self):
        return self._intSCALE
    def faith_scaling(self):
        return self._faiSCALE
    def arcane_scaling(self):
        return self._arcSCALE
    def weight(self):
        return self._weight
    def upgrade_stone(self):
        return self._upgradeTYPE

    #Value Calculations
    def _average_player_scaling_damage(self):
        return (self._playerSTR * self._strSCALE) + (self._playerDEX * self._dexSCALE) + (self._playerINT * self._intSCALE) + (self._playerFAI * self._faiSCALE) + (self._playerARC * self._arcSCALE)
    def _average_weapon_scaling_damage(self):
        if self._upgradeTYPE == 'Somber Smithing Stones':
            rate = 1.08
            #avglevel = 5
        else:
            rate = 1.02
            #avglevel = 13

        return rate * self._level
    def _max_value(self):
        return (161 / 40) + (1.02 * self._level) + ((self._playerSTR * 3.5) + (self._playerDEX * 3.5) + (self._playerINT * 3.5) + (self._playerFAI * 4.5) + (self._playerARC * 1))
    def _raw_value(self):

        damage_sum = (self._physicalDMG + self._magicDMG + self._fireDMG + self._lightDMG + self._holyDMG + self._critDMG)/self._staminaDMG
        raw_value = damage_sum + self._average_player_scaling_damage() + self._average_weapon_scaling_damage()

        return raw_value
    def value(self):
        average_rating = (float((self._raw_value()/self._max_value())*100))

        return average_rating

    #Setter Functions
    def set_level(self, level):
        self._level = level
    def set_player_strength(self, stat):
        self._playerSTR = stat
    def set_player_dexterity(self, stat):
        self._playerDEX = stat
    def set_player_intelligence(self, stat):
        self._playerINT = stat
    def set_player_faith(self, stat):
        self._playerFAI = stat
    def set_player_arcane(self, stat):
        self._playerARC = stat

    #Magic Methods
    def __repr__(self):
        return (f'{"-"*20}\nNAME: {self._name}\nTYPE: {self._type}\nPHYSICAL DAMAGE: {self._physicalDMG}\nMAGIC DAMAGE: {self._magicDMG}\nFIRE DAMAGE: {self._fireDMG}\nLIGHT DAMAGE: {self._lightDMG}\nHOLY DAMAGE: {self._holyDMG}\nCRITICAL DAMAGE: {self._critDMG}\nSTAMINA DAMAGE: {self._staminaDMG}\nSTRENGTH SCALING: {self._strSCALE}\nDEXTERITY SCALING: {self._dexSCALE}\nINTELLIGENCE SCALING: {self._intSCALE}\nFAITH SCALING: {self._faiSCALE}\nARCANE SCALING: {self._arcSCALE}\nWEIGHT: {self._weight}\nUPGRADE TYPE: {self._upgradeTYPE}\nRATING: {round(self.value(),1)}\nLEVEL: {self._level}\n{"-"*20}\n')
    def __str__(self):
        return (f'{self._name} [Type: {self._type} | Rating %: {round(self.value(),1)}% | Weight: {self._weight} | Level: {self._level}]')
    def __len__(self):
        return math.floor(self._raw_value())
    def __lt__(self, other_weapon):
        return self.value() < other_weapon.value()
    def __gt__(self, other_weapon):
        return self.value() > other_weapon.value()
    def __eq__(self, other_weapon):
        return self.value() == other_weapon.value()
    def __ge__(self, other_weapon):
        return self.value() >= other_weapon.value()
    def __le__(self, other_weapon):
        return self.value() <= other_weapon.value()
    def __ne__(self, other_weapon):
        return self.value() != other_weapon.value()
    def __add__(self, other_weapon):
        try:
            ans = self.value() + other_weapon.value()
        except TypeError:
            ans = 0
        return ans
    def __sub__(self, other_weapon):
        try:
            ans = self.value() - other_weapon.value()
        except TypeError:
            ans = 0
        return ans
    def __mul__(self, other_weapon):
        try:
            ans = self.value() * other_weapon.value()
        except TypeError:
            ans = 0
        return ans
    def __truediv__(self, other_weapon):
        try:
            ans = self.value() / other_weapon.value()
        except TypeError or ZeroDivisionError:
            ans = 0
        return ans
