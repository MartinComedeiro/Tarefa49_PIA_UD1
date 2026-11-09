class LunhException(Exception):
    def __init__(self,valor):
        self.valor = valor
    def __str__(self):
        return f"Non se pode usar o número {self.valor} como num de tarxeta"

class Usuario:
    @staticmethod
    def lunh(numTarxeta):
        numTarxeta = str(numTarxeta).replace(" ", "")

        if numTarxeta.isalnum() :
            numTarxetaLista = list(numTarxeta)[::-1]

            for num in range(1, len(numTarxetaLista), 2):
                numTarxetaLista[num] = int(numTarxetaLista[num]) * 2
                if numTarxetaLista[num] > 9:
                    numTarxetaLista[num] = numTarxetaLista[num] - 9

            suma = 0
            for num in numTarxetaLista:
                suma += int(num)

            if suma % 10 == 0:
                return True
            else:
                return False
        else:
            return False

    def __init__(self, nome, nomeUser, password, numTarxeta = None):
        self.nome = nome
        self.nomeUser = nomeUser
        self.password = password

        if numTarxeta == None:
            self._numTarxeta = numTarxeta
        else:
            numTarxeta = str(numTarxeta).replace(" ", "")

            if Usuario.lunh(numTarxeta):
                self._numTarxeta = numTarxeta
            else:
                self._numTarxeta = None
                raise LunhException(numTarxeta)

    def get_numTarxeta(self):
        return self._numTarxeta
    
    def set_numTarxeta(self, numTarxeta):
        if Usuario.lunh(numTarxeta):
            self._numTarxeta = numTarxeta
        else:
            raise LunhException(numTarxeta)

    numTarxeta = property(get_numTarxeta,set_numTarxeta)

    

if __name__ == "__main__":
    
        user1 = Usuario("Martin", "Martin", "Martin", "4539 3195 0343 6467")
        print (user1.get_numTarxeta())
        user1.set_numTarxeta("8273 1232 7352 0569")
        print (user1.numTarxeta)
    