"""
Clase Estudiante base para el Examen Convocatoria Ordinaria de la UD4
:author: Jaime Rabasco
Refactorización
Extrae una superclase con los campos
	nombre
	apellidos
	nif
"""


class Persona:
    def __init__(self):
        """

        """
        self.__nif = value
        self.__nombre = value
        self.__apellidos = value


class Estudiante(Persona):
    nif = "11111111Z";
    curso = "Primaria";
    nombre = "Nombre";
    apellidos = "Apellidos";

    def __init__(self, nif, curso, nombre, apellidos):
        """
        Constructor de la clase Estudiante, que deriva de persona
        :param nif: dni del alumno
        :param curso: curso del alumno
        :param nombre: nombre del alumno
        :param apellidos: apellidos del alumno
        """
        self.nif = nif;
        self.curso = curso;
        self.nombre = nombre;
        self.apellidos = apellidos;

    @property
    def nif(self):
        """
        devuelve nif
        :return:
        """
        return self.__nif

    @nif.setter
    def nif(self, value):
        """
        setter del nif
        :param value:
        """
        self.__nif = value

    @property
    def curso(self):
        """
        Devuelve el curso
        :return:
        """
        return self.__curso

    @curso.setter
    def curso(self, value):
        """
        Setter para curso
        :param value:
        """
        self.__curso = value

    @property
    def nombre(self):
        """
        devuelve nombre
        :return:
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        """
        setter del nombre
        :param value:
        """
        self.__nombre = value

    @property
    def apellidos(self):
        """
        devuelve apellidos
        :return:
        """
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        """
        setter de apellidos
        :param value:
        """
        self.__apellidos = value

