"""
Clase Gato.
:author: Jaime Rabasco Ronda.
"""
class Gato:

    def maullar(self):
        """
        Método por el cual el gato maulla
        """
        self.maulla = 'Miau'
        print(self.maulla);

g = Gato();
g.maullar();

#comentario