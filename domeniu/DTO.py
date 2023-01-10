class StudentSub5:
    def __init__(self, nume, nota):
        self.__nume = nume
        self.__nota = nota

    def getNume(self):
        return self.__nume

    def getNota(self):
        return self.__nota

    def setNume(self, nume):
        self.__nume = nume

    def setNota(self, nota):
        self.__nota = nota

    def __str__(self):
        return f"nume: {self.__nume}, nota: {self.__nota}"

class StudentNumaiGrup:
    def __init__(self, nume, grup):
        self.__nume = nume
        self.__grup = grup

    def getNume(self):
        return self.__nume

    def getGrup(self):
        return self.__grup

    def setNume(self, nume):
        self.__nume = nume

    def setGrup(self, grup):
        self.__grup = grup

    def __str__(self):
        return f"nume: {self.__nume}, grup: {self.__grup}"
