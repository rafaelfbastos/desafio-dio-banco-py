from peewee import *


db = SqliteDatabase('banco.db')



class Cliente(Model):
    nome = CharField()
    cpf = CharField(max_length=11)  

    class Meta:
        database = db  

class Conta(Model):
    numero = IntegerField(null=True)
    senha = CharField()
    saldo = FloatField()
    cliente = ForeignKeyField(Cliente, backref='cliente')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor >= self.saldo:
            return False , 'Saldo Insuficiente'
        elif valor > 500:
            return False, 'Valor Extrapola limite por transação'
        else:
            self.saldo-=valor
            return True , ''


    class Meta:
       database = db  

    
class Movimentacao(Model):
    conta = ForeignKeyField(Conta, backref='conta')
    valor = FloatField()
    tipo = CharField(choices=[('D', 'Deposito'), ('S', 'Saque'), ])
    data = DateField()


    class Meta:
        database = db  


if __name__ == '__main__':
    db.connect()
    db.create_tables([Cliente,Conta,Movimentacao]) 