# Requirement:
#     + Dau vao cho mot mang cac chuoi cung kich thuoc, duoc sap xep bat ki
# Results:
#     + Dau ra yeu cau kiem tra xem mang ma cac phan tu hon kem nhau 1 ki tu khong

from itertools import permutations

def stringsRearrangement(inputArray):
    # Sap xep tat car cac phan tu co trong mang inpuArray (n! truong hop)
    for inputRearrangementsArray in permutations(inputArray):
        # check neu co bat ki truong hop nao thoa man sap xep duoc theo yeu cau
        if (compareStringToArray(inputRearrangementsArray)): return True
        
    # Neu khong co truong hop nao thoa man
    return False

# sap xep 1 truong hop cua mang xem co thoa man khong
def compareStringToArray(inputArray):
    for idx, checkString in enumerate(inputArray):
        # check xem phan tu co phai phan tu cuoi cung khong
        if (idx != len(inputArray) - 1):
            # kiem tra 2 phan tu lien tiep co khac nhau 1 ki tu khong
            if (not compareTwoString(checkString, inputArray[idx + 1])): return False
        
        
    return True
    

# kiem tra 2 phan tu lien tiep co khac nhau 1 ki tu khong
def compareTwoString(checkString, desString):
    checkStringArray = list(checkString)
    desStringArray = list(desString)
    checkEqual = 0;
    
    for idx, char in enumerate(checkStringArray):
        if (char == desStringArray[idx]):
            checkEqual += 1;
            
    if (checkEqual == len(checkStringArray) - 1): return True
    
    return False
