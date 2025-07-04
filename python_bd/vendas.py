from  conexao  import  conecta_db
from  menu     import  menu_resumido
from  datetime import  datetime

def menu_vendas():
    print("|------------------------------|")
    print("|        Menu -> Venda         |")
    print("|------------------------------|")
    print("|    1 - Consultar venda       |")
    print("|    2 - Inserir venda         |")
    print("|    3 - Sair                  |")
    print("|------------------------------|")

    conexao = conecta_db ()

    while True:

        opcao = input("Escolha uma opção:")

        if opcao == "1":
            consultar_vendas(conexao)
        elif opcao == "2":
            inserir_vendas(conexao)
        elif opcao == "3":
                break
        else:
            print ("Opção invalida, tente novamente.")

def consultar_vendas(conexao):
    print ("Não implementado")

def inserir_item_venda(conexao, item_venda):
    cursor = conexao.cursor()
    sql_insert_item = """
         insert into itens_venda(id_venda, id_produto, quantidade, valor_unitario, valor_total)
         values(%s, %s, %s, %s, %s)
    """
    cursor.execute(sql_insert_item,item_venda)
    conexao.commit()

def inserir_vendas(conexao):

    id_cliente   = input ("Digite o ID do cliente:")
    data_venda   = datetime.now()
    numero_venda = input ("Digite o número da venda:")
    valor_venda  = 0

    cursor = conexao.cursor()
    sql_insert_venda = """
        insert into venda (id_cliente, data_venda, numero_venda, valor_venda)
        values (%s, %s, %s, %s) returning id;
    """
    dados_vendas = (id_cliente, data_venda,numero_venda,valor_venda)
    cursor.execute(sql_insert_venda, dados_vendas)
    venda_id = cursor.fetchone()[0]
    conexao.commit()


    itens_venda = []
    while(True):
         
         id_produto = int(input("Digite o ID do produto:"))
         quantidade = float(input("Digite a quantidade:"))
         preco_unitario = float(input("Digite o preço unitario:"))
         valor_total = quantidade * preco_unitario 

         itens_venda.append({"id_produto": id_produto,
                             "quantidade": quantidade,
                             "preco_unitario": preco_unitario,
                             "valor_total": valor_total})
         
         continua = input("Deseja adicionar outro item? (S/N):")
         
         
         print(itens_venda)
         if continua == "N":
            break
         
    id_venda = venda_id
    for item in itens_venda:
        item_data = (id_venda, item['id_produto'], item['quantidade'],
                     item['preco_unitario'], item['valor_total'])
        inserir_item_venda(conexao,item_data)