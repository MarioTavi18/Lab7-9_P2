from repository import FisierStudentrepository, FisierProblemerepository
from service.ProblemeService import ProblemeService
from service.StudentService import StudentService

class Consola:
    def __init__(self, studentService: StudentService, problemaService: ProblemeService, fisierS:FisierStudentrepository,  fisierP:FisierProblemerepository):
        self.__studentService = studentService
        self.__problemaService = problemaService
        self.__fisierS = fisierS
        self.__fisierP = fisierP

    def adaugaStudent(self,tip):
        try:
            studentID = input("Dati ID-ul studentului: ")
            nume = input("Dati numele studentului: ")
            grup = int(input("Dati grupul studentului: "))
            lucrare = input("Dati problema studentului: ")
            nota = float(input("Dati nota studentului: "))
            self.__studentService.adaugaStudent(studentID, nume, grup, lucrare, nota,tip)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def adaugaProblema(self,tip):
        try:
            NrProb = input("Dati Nr-ul problemei: ")
            Descriere = input("Dati descrierea problemei: ")
            Deadline = input("Dati deadline-ul problemei: ")
            self.__problemaService.adaugaProblema(NrProb, Descriere, Deadline,tip)
        except KeyError as e:
            print(e)

    def modificaStudent(self, tip):
        try:
            studentID = input("Dati ID-ul studentului care sa fie modificat: ")
            numeNou = str(input("Dati noul nume al studentului: "))
            grupNou = int(input("Dati noul grup al studentului: "))
            lucrareNou = input ("Dati noua problema a studentului: ")
            notaNou = float(input("Dati noua nota studentului: "))
            self.__studentService.modificaStudent(studentID, numeNou, grupNou, lucrareNou, notaNou, tip)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modificaProblema(self,tip):
        try:
            NrProb = input("Dati Nr-ul problemei care sa fie modificata: ")
            DescriereNou = input("Dati noua descriere a problemei: ")
            DeadlineNou = input("Dati noul deadline al problemei: ")
            self.__problemaService.modificaProblema(NrProb, DescriereNou,DeadlineNou, tip)
        except KeyError as e:
            print(e)

    def stergeStudent(self,tip):
        try:
            studentID = input("Dati ID-ul studentului care sa fie sters: ")
            self.__studentService.stergeStudent(studentID, tip)
        except KeyError as e:
            print(e)

    def stergeProblema(self,tip):
        try:
            NrProb = input("Dati Nr-ul problemei care sa fie stearsa: ")
            self.__problemaService.stergeProblema(NrProb, tip)
        except KeyError as e:
            print(e)
        except ValueError as a:
            print(a)

    def cautareStudent(self, tip):
        try:
            id = input("Dati id-ul studentului cautat: ")
            print(self.__studentService.cautareStudent(id, tip))

        except KeyError as e:
            print (e)

    def cautareProblema(self, tip):
        try:
            NrProb = input("Dati nr-ul problemei cautate: ")
            print(self.__problemaService.cautareProblema(NrProb, tip))
        except KeyError as e:
            print (e)

    def asignare(self, tip):
        try:
            id = input("Dati id-ul studentului care sa primeasca problema: ")
            nr = input("Dati nr-ul problemei pe care s-o primeasca: ")
            self.__studentService.Asignare(id, nr, tip)
        except KeyError as e:
            print(e)

    def notare(self, tip):
        try:
            id = input("Dati id-ul studentului care sa fie notat: ")
            nota = float(input(("Dati nota studentului: ")))
            self.__studentService.Notare(id,nota, tip)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def afiseaza(self,entitati):
    #   with open('probleme.txt', 'r') as f:
    #        for line in f:
    #            print(line,end='')

        if len(entitati) == 0:
            print("Nu exista niciun element!")
        else:
            for entitate in entitati:
                print(entitate)

    def afiseazaNumeNota(self,entitati):
        if len(entitati) == 0:
            print("Nu exista niciun element!")
        else:
            for entitate in entitati:
                print("Nume: "+entitate.getNume()+", Nota: "+str(entitate.getNota()))

    def adaugaFisier(self):
        self.__fisierS.adauga()

    def printMeniu(self,tip):
        print('\n'+"-----------------------------------")
        print("Se lucreaza cu: "+tip)
        print("-----------------------------------")
        print("1a. Adauga student")
        print("1b. Adauga problema")
        print("2a. Modifica student")
        print("2b. Modifica problema")
        print("3a. Sterge student")
        print("3b. Sterge problema")
        print("4a. Cautare student")
        print("4b. Cautare problema")
        print("5. Asignare problema")
        print("6. Notare problema")
        print("7. Ordonare studenti dupa nume")
        print("8. Ordonare studenti dupa nota")
        print("9. Toti studentii cu nota sub 5")
        print("10. Toti studentii cu grupe")
        print("a. Afiseaza toti studentii")
        print("b. Afiseaza toate problemele")
        print("x. Iesire")
        print("-----------------------------------")
        if tip != "memorie":
            print("M. Sa se lucreze cu memoria")
        else:
            print("F. Sa se lucreze cu fisierul")
        print("-----------------------------------")

    def meniu(self):
        tip ="memorie"
        while True:
            self.printMeniu(tip)
            tasta = input("Dati optiunea: ")
            if tasta == "1a":
                self.adaugaStudent(tip)
            elif tasta == "1b":
                self.adaugaProblema(tip)
            elif tasta == "2a":
                self.modificaStudent(tip)
            elif tasta == "2b":
                self.modificaProblema(tip)
            elif tasta == "3a":
                self.stergeStudent(tip)
            elif tasta == "3b":
                self.stergeProblema(tip)
            elif tasta == "4a":
                self.cautareStudent(tip)
            elif tasta == "4b":
                self.cautareProblema(tip)
            elif tasta == "5":
                self.asignare(tip)
            elif tasta == "6":
                self.notare(tip)
            elif tasta == "7":
                self.afiseaza(self.__studentService.ordonareAlf(tip))
            elif tasta == "8":
                self.afiseaza(self.__studentService.ordonareNota(tip))
            elif tasta == "9":
                self.afiseaza(self.__studentService.Sub5(tip))
            elif tasta == "10":
                self.afiseaza(self.__studentService.NumaiGrup(tip))
            elif tasta == "test":
                self.__problemaService.adaugaProblema("Lab1", "Suma", "Maine", tip)
                self.__problemaService.adaugaProblema("Lab2", "Produs", "Azi", tip)
                self.__studentService.adaugaStudent("1", "Vlad", 315, "Lab1", 4.0, tip)
                self.__studentService.adaugaStudent("2", "Ana", 315, "Lab2", 9.0, tip)
                self.__studentService.adaugaStudent("3", "Ana", 315, "Lab1", 3.0, tip)
            elif tasta == "a":
                self.afiseaza(self.__studentService.getALLStudenti(tip))
            elif tasta == "b":
                self.afiseaza(self.__problemaService.getALLProbleme(tip))
            elif tasta == "F":
                tip = "fisier"
            elif tasta == "M":
                tip = "memorie"
            elif tasta == "fisier":
                self.adaugaFisier()
            elif tasta == "afisare":
                self.__fisierS.afis()
            elif tasta == "x":
                break
            else:
                print("Optiune gresita")