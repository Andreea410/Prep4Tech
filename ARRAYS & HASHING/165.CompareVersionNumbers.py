class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 = version1.split(".")
        version2 = version2.split(".")

        iversion1 = 0
        iversion2 = 0
        while iversion1 < len(version1) and iversion2 < len(version2):
            if int(version1[iversion1]) < int(version2[iversion2]):
                return -1
            elif int(version1[iversion1]) > int(version2[iversion2]):
                return 1
            iversion1 += 1
            iversion2 += 1        

        while iversion1 < len(version1):
            if int(version1[iversion1]) != 0:
                return 1
            iversion1 += 1
            
        while iversion2 < len(version2):
            if int(version2[iversion2]) != 0:
                return -1
            iversion2 += 1
        return 0
