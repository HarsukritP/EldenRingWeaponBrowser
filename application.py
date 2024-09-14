import csv
from weapon import *
from collection import *

def parse_damage_stats(line):
    statList = [0, 0, 0, 0, 0, 0, 0]
    for stat in range(len(statList)):
        if line[stat + 2] != '-':
            statList[stat] = int(line[stat + 2])
        else:
            statList[stat] = 0
    return statList[0], statList[1], statList[2], statList[3], statList[4], statList[5], statList[6]
def parse_scale_stats(line):
    scaleDict = {'-': 1.0, 'S': 7.0, 'A': 5.5, 'B': 4.5, 'C': 3.5, 'D': 2.5, 'E': 1.5}
    statList = []
    for stat in line[9:14]:
        statList.append(scaleDict[stat])
    return statList[0], statList[1], statList[2], statList[3], statList[4]
def parse_weight(line):
    if line[22] != '-':
        return float(line[22])
    else:
        return 0.0
def createAllWeapons(filename, collection):
    with open(filename, 'r', encoding='utf-8') as file_in:
        file_in.readline()
        reader = csv.reader(file_in)
        for line in reader:
            name = line[0]
            weaponTYPE = line[1]
            phyDMG, magDMG, firDMG, litDMG, holDMG, criDMG, staDMG = parse_damage_stats(line)
            strSCL,dexSCL,intSCL,faiSCL,arcSCL = parse_scale_stats(line)
            weight = parse_weight(line)
            upgrade_type = line[23]
            weapon = Weapon(name, weaponTYPE, phyDMG, magDMG, firDMG, litDMG, holDMG, criDMG, staDMG, strSCL,dexSCL,intSCL,faiSCL,arcSCL,weight,upgrade_type)
            collection.add_object(weapon, weaponTYPE)
def writeTestCases(filename):
    pointer = open(filename, 'w', encoding='utf-8')
    weapon1 = Weapon("Bloodhound's Fang", 'Curved Greatsword', 345, 0, 0, 0, 0, 100, 122, 3.5, 4.5, 1, 1, 1, 11.5,'Somber Smithing Stones',9)
    weapon2 = Weapon('Nagakiba','Katana',281,0,0,0,0,100,90,2.5,4.5,1,1,1,7.0,'Smithing Stones', 1, 40, 29, 15, 15, 15)
    #weapon3 = Weapon("Morgott's Cursed Sword", "Curved Greatsword",294,0,0,0,0,110,116,2.5,4.5,1,1,2.5,7.5,'Somber Smithing Stone', 10, 19, 55, 9, 12 ,30)


    """
    These weapons have different attribute values due to their vast physical differences and due to them not only being different scaling 
    types (upgradeTYPE), levels and player stat effects, I deem them to represent the anomalous nature of each weapon in the dataset.
    """
    call_all_tests(pointer, weapon1, weapon2)
    pointer.close()
def call_all_tests(pointer, obj1, obj2):
    test_case_one(pointer, obj1, obj2)
    test_case_two(pointer, obj1, obj2)
    test_case_three(pointer, obj1, obj2)
    test_case_four(pointer, obj1, obj2)
    test_case_five(pointer, obj1, obj2)
    test_case_six(pointer, obj1, obj2)
    test_case_seven(pointer, obj1, obj2)
    test_case_eight(pointer, obj1, obj2)
    test_case_nine(pointer, obj1, obj2)
    test_case_ten(pointer, obj1, obj2)
def test_case_one(file_pointer, obj1, obj2):
    file_pointer.write(f'{"-"*90}\nTest 1: Testing For String Representations of Weapon Objects\n{"-"*90}\n')

    isSuccess = str(str(obj1) == "Bloodhound's Fang [Type: Curved Greatsword | Rating %: 71.2% | Weight: 11.5 | Level: 9]") + '\n'
    file_pointer.write("Expected Value: Bloodhound's Fang [Type: Curved Greatsword | Rating %: 71.2% | Weight: 11.5 | Level: 9]\n")
    file_pointer.write(f"Actual Value Matches Expected Value: {isSuccess}\n")


    isSuccess = str(str(obj2) == "Nagakiba [Type: Katana | Rating %: 73.6% | Weight: 7.0 | Level: 1]") + '\n'
    file_pointer.write("Expected Value: Nagakiba [Type: Katana | Rating %: 73.6% | Weight: 7.0 | Level: 1]\n")
    file_pointer.write(f"Actual Value Matches Expected Value: {isSuccess}\n")
def test_case_two(file_pointer, obj1, obj2):
    file_pointer.write(f'{"-" * 90}\nTest 2: Testing For repr() Representations of Weapon Objects\n{"-" * 90}\n')
    expected = ("--------------------\nNAME: Bloodhound's Fang\nTYPE: Curved Greatsword\nPHYSICAL DAMAGE: 345\nMAGIC DAMAGE: 0\nFIRE DAMAGE: 0\nLIGHT DAMAGE: 0\nHOLY DAMAGE: 0\nCRITICAL DAMAGE: 100\nSTAMINA DAMAGE: 122\nSTRENGTH SCALING: 3.5\nDEXTERITY SCALING: 4.5\nINTELLIGENCE SCALING: 1\nFAITH SCALING: 1\nARCANE SCALING: 1\nWEIGHT: 11.5\nUPGRADE TYPE: Somber Smithing Stones\nRATING: 71.2\nLEVEL: 9\n--------------------\n")
    file_pointer.write('Expected Value for Object 1:\n')
    file_pointer.write(expected)
    isSuccess = str(repr(obj1) == expected)
    file_pointer.write(f'Actual Value of Object 1 Matches Expected Value Of Object 1: {isSuccess}\n\n')

    expected = ("--------------------\nNAME: Nagakiba\nTYPE: Katana\nPHYSICAL DAMAGE: 281\nMAGIC DAMAGE: 0\nFIRE DAMAGE: 0\nLIGHT DAMAGE: 0\nHOLY DAMAGE: 0\nCRITICAL DAMAGE: 100\nSTAMINA DAMAGE: 90\nSTRENGTH SCALING: 2.5\nDEXTERITY SCALING: 4.5\nINTELLIGENCE SCALING: 1\nFAITH SCALING: 1\nARCANE SCALING: 1\nWEIGHT: 7.0\nUPGRADE TYPE: Smithing Stones\nRATING: 73.6\nLEVEL: 1\n--------------------\n")
    file_pointer.write('Expected Value for Object 2:\n')
    file_pointer.write(expected)
    isSuccess = str(repr(obj2) == expected)
    file_pointer.write(f'Actual Value of Object 2 Matches Expected Value Of Object 2: {isSuccess}\n\n')
def test_case_three(file_pointer, obj1, obj2):
    file_pointer.write(f'{"-"*90}\nTest 3: Testing For (In)Equality Between Objects\n{"-"*90}\n')

    isSuccess = str((obj1 == obj2) == False)+'\n'
    file_pointer.write(f'Object 1 is not equal to Object 2 (Using "=="): {isSuccess}\n')

    isSuccess = str((obj1 != obj2)) + '\n'
    file_pointer.write(f'Object 1 is not equal to Object 2 (Using "!="): {isSuccess}\n')
def test_case_four(file_pointer, obj1, obj2):
    file_pointer.write(f'{"-"*90}\nTest 4: Testing For Comparisons Between Objects\n{"-"*90}\n')

    isSuccess = str(obj1 < obj2) + '\n'
    file_pointer.write(f"Object 1's value is lesser than Object 2's value (Testing '<'): {isSuccess}\n")

    isSuccess = str(obj2 > obj1) + '\n'
    file_pointer.write(f"Object 2's value is greater than Object 1's value (Testing '>'): {isSuccess}\n")
def test_case_five(file_pointer, obj1, obj2):
    file_pointer.write(f'{"-"*90}\nTest 5: Testing for Weapon .value() Result\n{"-"*90}\n')

    isSuccess = str(obj1.value() == 71.22631620542509) + '\n'
    file_pointer.write(f"Object 1's value is equal to 71.2: {isSuccess}\n")

    isSuccess = str(obj2.value() == 73.58328200692796) + '\n'
    file_pointer.write(f"Object 2's value is equal to 73.6: {isSuccess}\n")

    isSuccess = str(obj1.value() < 72) + '\n'
    file_pointer.write(f"Object 1's value is lesser than 72: {isSuccess}\n")

    isSuccess = str(obj2.value() > 73) + '\n'
    file_pointer.write(f"Object 1's value is greater than 73: {isSuccess}\n")
def test_case_six(file_pointer, obj1, obj2):

    file_pointer.write(f'{"-"*90}\nTest 6: Testing For Object Addition\n{"-"*90}\n')

    try:
        actual = obj1 + obj2
        expected = 71.22631620542509 + 73.58328200692796
        isSuccess = actual == expected
    except TypeError: isSuccess = False
    file_pointer.write(f"Object 1 + Object 2 is equal to {expected}: {isSuccess}\n\n")
def test_case_seven(file_pointer, obj1, obj2):
    file_pointer.write(f'{"-" * 90}\nTest 7: Testing For Object Subtraction\n{"-" * 90}\n')

    actual = obj1 - obj2
    expected = 71.22631620542509 - 73.58328200692796
    isSuccess = actual == expected

    file_pointer.write(f"Object 1 - Object 2 is equal to {expected:.1f}: {isSuccess}\n\n")

    actual = obj2 - obj1
    expected = 73.58328200692796 - 71.22631620542509
    isSuccess = actual == expected

    file_pointer.write(f"Object 2 - Object 1 is equal to {expected:.1f}: {isSuccess}\n\n")
def test_case_eight(file_pointer, obj1, obj2):
    file_pointer.write(f'{"-" * 90}\nTest 8: Testing For Object Multiplication\n{"-" * 90}\n')

    actual = obj1 * obj2
    expected = 71.22631620542509 * 73.58328200692796
    isSuccess = actual == expected

    file_pointer.write(f"Object 1 * Object 2 is equal to {expected}: {isSuccess}\n\n")
def test_case_nine(file_pointer, obj1, obj2):
    file_pointer.write(f'{"-" * 90}\nTest 9: Testing For Object Division\n{"-" * 90}\n')

    actual = obj1 / obj2
    expected = 71.22631620542509 / 73.58328200692796
    isSuccess = actual == expected

    file_pointer.write(f"Object 1 / Object 2 is equal to {expected:}: {isSuccess}\n\n")
def test_case_ten(file_pointer, obj1, obj2):
    file_pointer.write(f'{"-" * 90}\nTest 10: Testing For Length (Raw Value) Output\n{"-" * 90}\n')
    expected = 123
    isSuccess = len(obj1) == expected
    file_pointer.write(f'The len() of Object 1 is equal to {expected}: {isSuccess}\n\n')

    expected = 281
    isSuccess = len(obj2) == expected
    file_pointer.write(f'The len() of Object 2 is equal to {expected}: {isSuccess}\n')


def main():
    dataset = 'elden_ring_weapon.csv'
    test_report = 'testCases.txt'
    collection = CollectionObjects()
    createAllWeapons(dataset, collection)
    writeTestCases(test_report)

main()


