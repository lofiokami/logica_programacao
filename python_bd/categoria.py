from  conexao  import  conecta_db
from  menu     import  menu_resumido

def menu_categoria(titulo):
    menu_resumido(titulo)

    while True: 

        opcao   = input ("Escolha uma opção:")
        conexao = conecta_db()

        if opcao == "1":
            listar_categoria(conexao)
            menu_resumido(titulo)

        elif opcao == "2":
            listar_categoria(conexao)
            consultar_categoria_por_id(conexao)
            menu_resumido(titulo)

        elif opcao == "3":
            inserir_categoria(conexao)
            listar_categoria(conexao)
            menu_categoria(titulo)

        elif opcao == "4":
            listar_categoria(conexao)
            atualizar_categoria(conexao)
            listar_categoria(conexao)
            menu_resumido(titulo)

        elif opcao == "5":
            listar_categoria(conexao)
            delete_categoria(conexao)
            listar_categoria(conexao)
            menu_resumido(titulo)

        elif opcao == "6":
            print ("Sair")
            break

        else:
            print ("Opção invalida, tente novamente")

def listar_categoria(conexao):
    cursor = conexao.cursor()
    # Execução do select no banco de dados
    cursor.execute("select id,nome from categoria order by id asc")
    # recuperar todos registros
    registros = cursor.fetchall()
    print ("|-------------------------------------------------------------------|")
    for registro in registros:
        print (f"| ID: {registro[0]}  - Nome: {registro[1]} ")
    print ("|-------------------------------------------------------------------|")

def consultar_categoria_por_id(conexao):
    id = input ("Digite o ID: ")
    cursor = conexao.cursor()
    cursor.execute("select id,cliente from categoria where id = " + id)
    registro = cursor.fetchone()
    
    if registro is None:
        print ("Categoria não encontrada:")
    else:
        print (" |------------------------------------|")
        print (f"| ID ..     : {registro[0]}          |")
        print (f"| Categoria : {registro[1]}          |")
        print (" |------------------------------------|")

def inserir_categoria(conexao):
    print ("Inserindo a Categoria ..: ")

    cursor = conexao.cursor()
    nome   = input ("Nome :")
    sql_insert = "insert into categoria (nome) values ('" + nome + "')"
    cursor.execute(sql_insert)
    conexao.commit()

def atualizar_categoria(conexao):
    print ("Alterando dados das Categorias")
    cursor = conexao.cursor()

    id   = input ("Digite o ID:")
    nome = input ("Nome : ")
     
    sql_update = "update categoria set nome = '" + nome + "' where id = "+ id 
    cursor.execute(sql_update)
    conexao.commit()

def delete_categoria(conexao):
    print ("Deletar Categoria")
    cursor = conexao.cursor()

    id         = input ("Digite o ID:")
    sql_delete = "delete from categoria where id =" + id

    cursor.execute(sql_delete)
    conexao.commit()