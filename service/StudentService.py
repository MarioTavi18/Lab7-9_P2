from domeniu.student import Student
from domeniu.DTO import StudentSub5, StudentNumaiGrup
from repository import FisierStudentrepository, FisierProblemerepository
from repository.problemeRepository import ProblemaRepository
from repository.studentRepository import StudentRepository

class StudentService:
    def __init__(self, studentRepository: StudentRepository, problemaRepository:ProblemaRepository, fisierS: FisierStudentrepository, fisierP: FisierProblemerepository):
        self.__studentRepository = studentRepository
        self.__problemaRepository = problemaRepository
        self.__fisierS = fisierS
        self.__fisierP = fisierP

    def getALLStudenti(self, tip):
        """
        returneaza lista de studenti
        :return: o lista de obiecte de tipul Student
        """
        if tip == "memorie":
            return self.__studentRepository.getAll()
        else:
            return self.__fisierS.getAll()

    def adaugaStudent (self, studentID, nume, grup,lucrare,nota,tip):
        """
        adauga un student
        :param studentID: string
        :param nume: string
        :param grup: int
        :return:
        """
        student = Student(studentID, nume, grup, lucrare, nota)
        if tip == "memorie":
            if self.__problemaRepository.getByNr(lucrare) is None and lucrare != "-":
                raise KeyError("Nu exista o problema cu nr-ul dat!")
            if lucrare == "-" and nota != 0:
                raise KeyError("Studentul nu are o problema care poate fi notata!")
            self.__studentRepository.adaugaStudent(student)

        else:
            if self.__fisierP.getByNr(lucrare) is None and lucrare != "-":
                raise KeyError("Nu exista o problema cu nr-ul dat!")
            if lucrare == "-" and nota != 0:
                raise KeyError("Studentul nu are o problema care poate fi notata!")
            self.__fisierS.adauga(student)


    def modificaStudent(self, studentID, numeNou, grupNou, lucrareNou, notaNou, tip):
        """
        modifica un student dupa id
        :param studentID: string
        :param numeNou: string
        :param grupNou: int
        :return:
        """
        studentNou = Student(studentID, numeNou, grupNou, lucrareNou, notaNou)
        if tip == "memorie":
            if self.__problemaRepository.getByNr(lucrareNou) is None and lucrareNou !="-":
                raise KeyError("Nu exista o problema cu nr-ul dat!")
            if lucrareNou =="-" and notaNou !=0:
                raise KeyError("Studentul nu are o problema care poate fi notata!")
            self.__studentRepository.modificaStudent(studentNou)
        else:
            if self.__fisierP.getByNr(lucrareNou) is None and lucrareNou !="-":
                raise KeyError("Nu exista o problema cu nr-ul dat!")
            if lucrareNou =="-" and notaNou !=0:
                raise KeyError("Studentul nu are o problema care poate fi notata!")
            self.__fisierS.modifica(studentNou)

    def stergeStudent(self, studentID, tip):
        """
        sterge un student dupa ID
        :param studentID: string
        :return:
        """
        if tip == "memorie":
            self.__studentRepository.stergeStudent(studentID)
        else:
            self.__fisierS.sterge(studentID)

    def cautareStudent(self, id, tip):
        """
        cauta un  student dupa ID
        :param id: string
        :return:
        """
        if tip == "memorie":
            if self.__studentRepository.getById(id) is None:
                raise KeyError("Nu exista niciun student cu ID-ul dat!")
            student = self.__studentRepository.cautareStudent(id)
            return student
        else:
            self.__fisierS.cautare(id)

    def Asignare(self,id,nr, tip):
        """
        asigneaza o problema la studentul dat
        :param id:
        :param nr:
        :return:
        """
        if tip == "memorie":
            if self.__studentRepository.getById(id) is None:
                raise KeyError ("Nu exista niciun student cu ID-ul dat!")
            if self.__problemaRepository.getByNr(nr) is None:
                raise KeyError ("Nu exista nicio problema cu nr-ul dat!")
            studentNou = self.__studentRepository.getById(id)
            if studentNou.getLucrare() != "-":
                raise KeyError ("Studentul are deja o problema!")
            stud = Student(id,studentNou.getNume(),studentNou.getGrup(),nr,studentNou.getNota())
            self.__studentRepository.modificaStudent(stud)
        else:
            if self.__fisierS.getById(id) is None:
                raise KeyError ("Nu exista niciun student cu ID-ul dat!")
            if self.__fisierP.getByNr(nr) is None:
                raise KeyError ("Nu exista nicio problema cu nr-ul dat!")
            studentNou = self.__fisierS.getById(id)
            if studentNou.getLucrare() != "-":
                raise KeyError ("Studentul are deja o problema!")
            stud = Student(id,studentNou.getNume(),studentNou.getGrup(),nr,studentNou.getNota())
            self.__fisierS.modifica(stud)

    def Notare(self,id,nota,tip):
        """
        noteaza un student dat
        :param id: string
        :param nota: float
        :return:
        """
        if tip == "memorie":
            if self.__studentRepository.getById(id) is None:
                raise KeyError("Nu exista niciun student cu ID-ul dat!")
            stud = self.__studentRepository.getById(id)
            if stud.getLucrare() == "-":
                raise KeyError("Studentul nu are o problema data!")
            if stud.getNota() != 0:
                raise KeyError("Studentul este deja notat!")
            stud = Student(id, stud.getNume(), stud.getGrup(), stud.getLucrare(), nota)
            self.__studentRepository.modificaStudent(stud)
        else:
            if self.__fisierS.getById(id) is None:
                raise KeyError("Nu exista niciun student cu ID-ul dat!")
            stud = self.__fisierS.getById(id)
            if stud.getLucrare() == "-":
                raise KeyError("Studentul nu are o problema data!")
            if stud.getNota() != 0:
                raise KeyError("Studentul este deja notat!")
            stud = Student(id, stud.getNume(), stud.getGrup(), stud.getLucrare(), nota)
            self.__fisierS.modifica(stud)

    def ordonareAlf(self,tip):
        """
        returneaza o lista de studenti ordonata alfabetic
        :return:
        """
        if tip == "memorie":
            sir = self.__studentRepository.getAll()
        else:
            sir = self.__fisierS.getAll()
        ok = 1
        while ok == 1:
            ok = 0
            for i in range(len(sir) - 1):
                nume1 = str(sir[i].getNume())
                nume2 = str(sir[i + 1].getNume())
                if nume1 > nume2:
                    cop = sir[i]
                    sir[i] = sir[i + 1]
                    sir[i + 1] = cop
                    ok = 1
                elif nume1 == nume2:
                    if sir[i].getNota() > sir[i + 1].getNota():
                        cop = sir[i]
                        sir[i] = sir[i + 1]
                        sir[i + 1] = cop
                        ok = 1
        return sir

    def ordonareNota(self,tip):
        """
        returneaza o lista de studenti ordonata dupa nota
        :return:
        """
        if tip == "memorie":
            sir = self.__studentRepository.getAll()
        else:
            sir = self.__fisierS.getAll()
        ok = 1
        while ok == 1:
            ok = 0
            for i in range(len(sir) - 1):
                if sir[i].getNota() > sir[i + 1].getNota():
                    cop = sir[i]
                    sir[i] = sir[i + 1]
                    sir[i + 1] = cop
                    ok = 1
        return sir

    def Sub5(self,tip):
        """
        returneaza o lista de studenti ordonata dupa note sub 5
        :return:
        """
        sir = self.ordonareNota(tip)
        lista = []
        for student in sir:
            if student.getNota() < 5 and student.getLucrare() != "-":
                student = StudentSub5(student.getNume(), student.getNota())
                lista.append(student)
        return lista

    def NumaiGrup(self,tip):
        """
        returneaza o lista de studenti ordonata (nume si grupa numai)
        :return:
        """
        sir = self.ordonareAlf(tip)
        lista = []
        for student in sir:
            student = StudentNumaiGrup(student.getNume(), student.getGrup())
            lista.append(student)
        return lista