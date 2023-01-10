class Student:
    def __init__(self, studentID, nume, grup, lucrare, nota):
        self.__studentID = studentID
        self.__nume = nume
        self.__grup = grup
        self.__lucrare = lucrare
        self.__nota = nota

    def getStudentID(self):
        return self.__studentID

    def getNume(self):
        return self.__nume

    def getGrup(self):
        return self.__grup

    def getLucrare(self):
        return self.__lucrare

    def getNota(self):
        return self.__nota

    def setStudentID(self, studentID):
        self.__studentID = studentID

    def setNume(self, nume):
        self.__nume = nume

    def setGrup(self, grup):
        self.__grup = grup

    def setLucrare(self, lucrare):
        self.__lucrare = lucrare

    def setNota(self, nota):
        self.__nota = nota

    def __str__(self):
        return f"id: {self.__studentID}, nume: {self.__nume}, grup: {self.__grup}, lucrare: {self.__lucrare}, nota: {self.__nota}"

