class LunhException(Exception):
    def __init__(self,valor):
        self.valor = valor
    def __str__(self):
        return f"Non se pode usar o número {self.valor} como num de tarxeta por non cumplir co algoritmo de Lunh"

class Usuario:
    def __init__(self, nome, nomeUser, password, numTarxeta = None):
        self.nome = nome
        self.nomeUser = nomeUser
        self.password = password

        if numTarxeta == None:
            self.numTarxeta = numTarxeta
        else:

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
                    self.numTarxeta = numTarxeta
                else:
                    raise LunhException(numTarxeta)

            else:
                raise ValueError("El número de tarjeta solo puede tener números")

        


if __name__ == "__main__":
    try:
        user1 = Usuario("Martin", "Martin", "Martin", "4539 3195 0343 6467")
        print (user1.numTarxeta)
    except Exception as e:
        print(e)