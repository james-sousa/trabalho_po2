import abc
import random
from datetime import datetime, time
#import psycopg2


class Funcionario():
    """
    Representa um funcionário com credenciais de login.

    Atributos:
        _usuario (str): Nome de usuário do funcionário.
        _senha (str): Senha do funcionário.
    """

    def __init__(self, usuario, senha):
        self._usuario = usuario
        self._senha = senha


class Autenticacao(abc.ABC):
    """
    Interface para autenticação de usuários.

    Métodos abstratos:
        login(usuario, senha): Verifica as credenciais do usuário.
    """

    @abc.abstractmethod
    def login(self, usuario, senha):
        pass


class AutenticacaoSimples:
    """
    Implementação simples de autenticação usando credenciais padrão.

    Atributos:
        usuario_padrao (str): Nome de usuário padrão.
        senha_padrao (str): Senha padrão.
    """

    def __init__(self):
        self.usuario_padrao = "admin"
        self.senha_padrao = "admin"

    def login(self, funcionario: Funcionario):
        """
        Realiza a autenticação do funcionário.

        Args:
            funcionario (Funcionario): Objeto contendo credenciais do funcionário.

        Returns:
            bool: True se as credenciais forem válidas, False caso contrário.
        """
        if funcionario._usuario == self.usuario_padrao and funcionario._senha == self.senha_padrao:
            return True
        else:
            return False


Autenticacao.register(AutenticacaoSimples)


def obter_credenciais():
    """
    Solicita ao usuário as credenciais de login.

    Returns:
        Funcionario: Objeto contendo as credenciais fornecidas.
    """
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    return Funcionario(usuario, senha)


def autenticar_usuario(autenticacao: Autenticacao):
    """
    Autentica o usuário utilizando a interface de autenticação.

    Args:
        autenticacao (Autenticacao): Instância da classe de autenticação.

    Returns:
        bool: True se a autenticação for bem-sucedida, False caso contrário.
    """
    funcionario = obter_credenciais()
    if autenticacao.login(funcionario):
        print("Login bem-sucedido!")
        return True
    else:
        print("Usuário ou senha incorretos. Tente novamente.")
        return False


def autenticacao():
    """
    Gerencia o processo de autenticação com limite de tentativas.
    """
    autenticacao = AutenticacaoSimples()
    tentativas = 3

    while tentativas > 0:
        if autenticar_usuario(autenticacao):
            # menu_historico()
            break
        else:
            tentativas -= 1
            print(f"Tentativas restantes: {tentativas}")

        if tentativas == 0:
            print("Número máximo de tentativas alcançado!")
            continue


class Produto(abc.ABC):
    """
    Classe abstrata representando um produto.

    Atributos:
        _nome (str): Nome do produto.
        _preco (float): Preço do produto.
        _unidade (str): Unidade de medida do produto.

    Métodos abstratos:
        calcular_preco(quantidade): Calcula o preço com base na quantidade.
        editar(): Edita os atributos do produto.
    """

    def __init__(self, nome, preco, unidade):
        self._nome = nome
        self._preco = preco
        self._unidade = unidade

    @abc.abstractmethod
    def calcular_preco(self, quantidade):
        pass

    @abc.abstractmethod
    def editar(self):
        pass


class Bebidas(Produto):
    """
    Representa o produto Bebidas.

    Métodos:
        calcular_preco(quantidade): Calcula o preço com base na quantidade.
        editar(): Permite editar o nome e preço da bebida.
    """
    def __init__(self, nome, preco, unidade="UNI"):
        super().__init__(nome, preco, unidade)

    def calcular_preco(self, quantidade):
        return self._preco * quantidade

    def editar(self):
        try:
            self._nome = input("DIGITE O NOVO NOME DA BEBIDA: ").upper()
            self._preco = float(input("DIGITE O NOVO PREÇO DA BEBIDA: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico para o preço.")

# Classes adicionais como Pastel, Acai, Sorvete, Cuzcuz seguem a mesma estrutura,
# com métodos para calcular preço e editar atributos.


class Pedido:
    """
    Representa um pedido realizado por um cliente.

    Atributos:
        _cliente (str): Nome do cliente.
        _produtos (list): Lista de produtos no pedido.
        _id_pedido (int): ID único do pedido.
        _data (int): Data do pedido (formato juliano).
        _hora (time): Hora do pedido.
        _status (str): Status do pedido.

    Métodos:
        adicionar_produto(produto, quantidade, tipo_produto): Adiciona um produto ao pedido.
        calcular_total(): Calcula o valor total do pedido.
        imprimir_nota(): Imprime a nota fiscal detalhada.
    """
    def __init__(self, cliente, id_pedido):
        self._cliente = cliente
        self._produtos = []
        self._id_pedido = id_pedido
        now = datetime.now()
        self._data = now.toordinal()  # Convertendo para data Juliana
        self._hora = now.time()  # Armazenando a hora
        self._status = "ABERTO"

    def adicionar_produto(self, produto, quantidade, tipo_produto):
        self._produtos.append((produto, quantidade, tipo_produto))

    def calcular_total(self):
        total = 0
        for produto, quantidade, tipo_produto in self._produtos:
            total += produto.calcular_preco(quantidade)
        return total

    def imprimir_nota(self):
        data_gregoriana = datetime.fromordinal(self._data)  # Convertendo de volta para data Gregoriana
        print("\n")
        print("╔══════════════════════════════════════════════════════════════════════════════════╗")
        print("║                                    NOTA FISCAL                                   ║")
        print("╠══════════════════════════════════════════════════════════════════════════════════╣")
        print(f"║ ID DO PEDIDO: {self._id_pedido:<65}  ║")
        print(f"║ NOME DO CLIENTE: {self._cliente:<62}  ║")
        print(f"║ DATA DO PEDIDO: {data_gregoriana.strftime('%d/%m/%Y'):<63}  ║")
        print(f"║ HORA DO PEDIDO: {self._hora.strftime('%H:%M:%S'):<63}  ║")
        print("╠══════════════════════════════════════════════════════════════════════════════════╣")
        for produto, quantidade, tipo_produto in self._produtos:
            if tipo_produto == "AÇAI" or tipo_produto == "SORVETE":
                print(f"║ {tipo_produto:<7} {produto._nome:50} PESO: {quantidade:<4}g  {produto.calcular_preco(quantidade):>5.2f} R$ ║")
            else:
                print(f"║ {tipo_produto:<7} {produto._nome:50} QUANT: {quantidade:<4}  {produto.calcular_preco(quantidade):>5.2f} R$ ║")
        print("╠══════════════════════════════════════════════════════════════════════════════════╣")
        print(f"║ TOTAL: {self.calcular_total():>70.2f} R$ ║")
        print("╚══════════════════════════════════════════════════════════════════════════════════╝\n")

# Caixa e suas funções de banco de dados seguem com documentação semelhante.

class Caixa:
    """
    Classe responsável por gerenciar as operações relacionadas ao banco de dados e os produtos no sistema.

    Atributos:
        postgres_config (dict): Configurações para conexão com o banco de dados PostgreSQL.
    """

    def __init__(self):
        """
        Inicializa uma nova instância da classe Caixa com as configurações do banco de dados.
        """
        self.postgres_config = {
            "host": "localhost",  # Endereço do servidor do banco de dados.
            "port": 5410,  # Porta padrão ou configurada para o PostgreSQL.
            "database": "employee",  # Nome do banco de dados.
            "user": "postgres",  # Usuário do banco de dados.
            "password": "2512",  # Senha do banco de dados.
        }

    def conectar_bd(self):
        """
        Estabelece uma conexão com o banco de dados PostgreSQL.

        Returns:
            conn (psycopg2.extensions.connection): Objeto de conexão com o banco de dados, ou None em caso de falha.
        """
        try:
            conn = psycopg2.connect(**self.postgres_config)
            print("Conexão ao banco de dados estabelecida.")
            return conn
        except psycopg2.OperationalError as e:
            print(f"Erro de operação: {e}")
        except psycopg2.DatabaseError as e:
            print(f"Erro no banco de dados: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")
        return None

    def adicionar_produto(self, produto):
        """
        Adiciona um produto ao banco de dados, verificando a validade do preço.

        Args:
            produto (object): Objeto que representa o produto a ser adicionado.
        """
        if produto._preco <= 0:
            print("PREÇO INVÁLIDO! PRODUTO NÃO CADASTRADO!")
            return

        conn = self.conectar_bd()
        if conn:
            try:
                with conn.cursor() as cursor:
                    query = """
                        INSERT INTO produtos (tipo, nome, preco, unidade)
                        VALUES (%s, %s, %s, %s)
                    """
                    cursor.execute(query, (produto.__class__.__name__.upper(), produto._nome, produto._preco, "uni"))
                    conn.commit()
                    print(f"Produto '{produto._nome}' adicionado ao banco de dados.")
            except Exception as e:
                print(f"Erro ao adicionar produto ao banco de dados: {e}")
            finally:
                conn.close()

    def editar_produto(self, nome_produto):
        """
        Permite editar os detalhes de um produto existente.

        Args:
            nome_produto (str): Nome do produto a ser editado.
        """
        try:
            for tipo, conteudo in self._produtos.items():
                if isinstance(conteudo, list):
                    for produto in conteudo:
                        if produto._nome == nome_produto:
                            print("╔═════════════════════════════════════════════════╗")
                            print("║              NOME            ║ PREÇO  ║ UNIDADE ║")
                            print("╠═════════════════════════════════════════════════╣")
                            print(f"║ {produto._nome:28} ║ {produto._preco:6.2f} ║ {produto._unidade:7} ║")
                            print("╚═════════════════════════════════════════════════╝\n")
                            print("\n1 - EDITAR")
                            print("0 - CANCELAR")
                            try:
                                op = int(input("DIGITE A OPÇÃO DESEJADA: "))
                                if op == 0:
                                    return
                                elif op == 1:
                                    produto.editar()
                                    print(f"{tipo} EDITADO COM SUCESSO!")
                                    return
                                else:
                                    print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
                                    continue
                            except ValueError:
                                print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
                                continue

            print("PRODUTO NÃO ENCONTRADO!")
        except Exception as e:
            print(f"Erro: {str(e)}")

    def remover_produto(self, nome_produto):
        """
        Remove um produto do sistema, exceto produtos específicos (como 'AÇAÍ' e 'SORVETE').

        Args:
            nome_produto (str): Nome do produto a ser removido.
        """
        try:
            for tipo, lista_produtos in self._produtos.items():
                for produto in lista_produtos:
                    if produto._nome == nome_produto:
                        if tipo == "AÇAI" or tipo == "SORVETE":
                            print("NÃO É POSSÍVEL REMOVER AÇAÍ OU SORVETE!")
                            return
                        print("╔═════════════════════════════════════════════════╗")
                        print("║              NOME            ║ PREÇO  ║ UNIDADE ║")
                        print("╠═════════════════════════════════════════════════╣")
                        print(f"║ {produto._nome:28} ║ {produto._preco:6.2f} ║ {produto._unidade:7} ║")
                        print("╚═════════════════════════════════════════════════╝\n")
                        print("\n1 - REMOVER")
                        print("0 - CANCELAR")
                        try:
                            op = int(input("DIGITE A OPÇÃO DESEJADA: "))
                            if op == 0:
                                return
                            elif op == 1:
                                lista_produtos.remove(produto)
                                print(f"{tipo} REMOVIDO COM SUCESSO!")
                                return
                            else:
                                print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
                                continue
                        except ValueError:
                            print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
                            continue

            print("PRODUTO NÃO ENCONTRADO!")
        except Exception as e:
            print(f"PRODUTO NÃO ENCONTRADO!")




