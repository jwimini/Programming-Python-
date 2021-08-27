class GangwondowPackage:
    def __init__(self):
        self.palces = ['강릉 경포해수욕장', '속초 바다정원 카페']

    def __str__(self):
        return str(self.palces)

if __name__ == '__main__':
    gp = GangwondowPackage()
    print(gp)