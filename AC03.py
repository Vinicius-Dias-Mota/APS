from unittest import TestCase, main
import abc

class OperacaoFabrica(object):

    def criar(self, operador):
        if operador == 'operacao_soma':
            return operacao_soma()
        elif operador == 'operacao_divisao':
            return operacao_divisao()
        elif operador == 'operacao_subtracao':
            return operacao_subtracao()
        elif operador == 'operacao_multiplicacao':
            return operacao_multiplicacao()

class Calculadora(object):
    def calcular(self, valor1, valor2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if operacao == None:
            return 0
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado


class Operacao(metaclass=abc.ABCMeta):

    def executar(self, valor1, valor2):
        pass

class operacao_soma(Operacao):
    def executar(self, valor1, valor2):
        return valor1 + valor2

class operacao_divisao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado

class operacao_subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado

class operacao_multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado


class ClasseTeste(TestCase):

    def test_operacao_divisao(self):
        dividindo = Calculadora()
        self.assertEqual(dividindo.calcular(10, 5, 'operacao_divisao'), 2)

    def test_operacao_soma(self):
        operacao_somando = Calculadora()
        self.assertEqual(operacao_somando.calcular(5, 5, 'operacao_soma'), 10)

    def test_operacao_subtracao(self):
        calcular = Calculadora()
        self.assertEqual(calcular.calcular(5, 6, 'operacao_subtracao'), -1)
    
    def test_operacao_multiplicacao(self):
        calcular = Calculadora()
        self.assertEqual(calcular.calcular(5, 5, 'operacao_multiplicacao'), 25)

        

duvida = Calculadora()
x = duvida.calcular(5, 5, 'operacao_soma')


if __name__ == '__main__':
    main()
