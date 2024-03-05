class Asignatura:

    def _init_(self, nombre, salon = "remoto"):
        self._nombre = nombre
        self._salon = salon

    def _str_(self):
        return self._nombre+" "+self._salon
