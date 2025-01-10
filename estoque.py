import json 
import os 

arquivo = os.path.join(os.path.dirname(__file__), 'database', 'estoque.json')

def carregar_produtos():
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as file:
            return json.load(file)
    else:
        return []
    
def salvar_produtos(produtos):
    os.makedirs(os.path.dirname(arquivo), exist_ok=True)
    with open(arquivo, 'w') as file:
        json.dump(produtos, file, indent=4, ensure_ascii=False)

def gerar_id(produtos):
    if produtos:
        return max(produto["id"] for produto in produtos) + 1
    return 1

def exibir_menu_produtos():
    os.system("cls")
    print("SISTEMA DE ESTOQUE:"     )
    print("1 - CADASTRAR UM PRODUTO")
    print("2 - EXIBIR PRODUTOS"     )
    print("3 - ATUALIZAR PRODUTO"   )
    print("4 - EXCLUIR PRODUTO"     )
    print("5 - EXIBIR APENAS UM PRODUTO")

def cadastrar_produtos(): 
    produtos = carregar_produtos()

    nome_do_produto       =      input ("DIGITE O NOME DO PRODUTO: ")
    categoria_do_produto  =      input ("DIGITE A CATEGORIA DO PRODUTO (ELETRÔNICO, CAPINHAS, ACESSÓRIOS): ")
    quantidade_em_estoque =      input ("DIGITE A QUANTIDADE DE PRODUTOS QUE SERÃO CADASTRADOS: ")
    valor_do_produto      =      input ("QUAL SERÁ O VALOR DO PRODUTO? ")
    
    id_do_produto         =      gerar_id(produtos)

    produtos.append({"id": id_do_produto, "nome_do_produto": nome_do_produto, "categoria_do_produto": categoria_do_produto, "quantidade_em_estoque": quantidade_em_estoque, "valor_do_produto": valor_do_produto})
    
    salvar_produtos(produtos)
    print(f"PRODUTO CADASTRADO COM SUCESSO. ")

def listar_produtos():
    os.system('cls' if os.name == 'nt' else 'clear')
    produtos = carregar_produtos()

    if produtos:
        print(f"LISTA DOS PRODUTOS EM ESTOQUE")
        for produto in produtos:
             print(f"ID: {produto['id']} | NOME: {produto['nome_do_produto']} | CATEGORIA: {produto['categoria_do_produto']} | QUANTIDADE: {produto['quantidade_em_estoque']} | VALOR: R${produto['valor_do_produto']}")
    else:
        print("NENHUM PRODUTO ENCONTRADO.")

def atualizar_produto():
    produtos = carregar_produtos()
    if not produtos:
        print("NENHUM PRODUTO CADASTRADO.")
        return
   
    try: 
        id_do_produto = int(input("DIGITE O ID DO PRODUTO QUE DESEJA ATUALIZAR:"))
        produto = next((p for p in produtos if p['id'] == id_do_produto), None)

        if produto:
            print("O QUE VOCÊ DESEJA ATUALIZAR?")
            print("1 - NOME")
            print("2 - CATEGORIA")
            print("3 - QUANTIDADE")
            print("4 - VALOR")

            opcao = int(input("OPÇÃO: "))
            if opcao == 1:
                produto['nome_do_produto'] = input("DIGITE O NOVO NOME: ")
            elif opcao == 2:
                produto['categoria_do_produto'] = input("DIGITE A NOVA CATEGORIA: ")
            elif opcao == 3:
                produto['quantidade_em_estoque'] = int(input("DIGITE A NOVA QUANTIDADE DO EM ESTOQUE:"))
            elif opcao == 4:
                produto['valor_do_produto'] = float(input("DIGITE O NOVO VALOR DO PRODUTO: "))
            else:
                print(" OPÇÃO INVÁLIDA.")

            salvar_produtos(produtos)
            print("PRODUTO ATUALIZADO COM SUCESSO.")
        else:
            print("PRODUTO NÃO ENCONTRADO.")
    except ValueError:
        print("ENTRADA VÁLIDA")
        
def excluir_produto():
    produtos = carregar_produtos()
    if not produtos:
        print("NENHUM PRODUTO CADASTRADO.")
        return

    try:
        id_do_produto = int(input("DIGITE O ID DO PRODUTO QUE DESEJA EXCLUIR:"))
        produto = next((p for p in produtos if p['id'] == id_do_produto), None)

        if produto:
            produtos.remove(produto)
            salvar_produtos(produtos)
            print("PRODUTO EXCLUÍDO.")
        else:
            print("PRODUTO NÃO ENCONTRADO.")
    except ValueError:
        print("ENTRADA INVÁLIDA.")

def listar_um_produto():
    produtos = carregar_produtos()
    produto_id = input("DIGITE O NOME OU ID DO PRODUTO:")

    produto_encontrado  = None
    if produto_id.isdigit():
        produto_id = int(produto_encontrado)
        produto_encontrado = next((p for p in produtos if p['nome_do_produto'].lower() == produto_id.lower()), None)

        if produto_encontrado:
            print(f"ID: {produto_encontrado['id']} | NOME: {produto_encontrado['nome_do_produto']} | CATEGORIA: {produto_encontrado['categoria_do_produto']} | QUANTIDADE: {produto_encontrado['quantidade_em_estoque']} | VALOR: R${produto_encontrado['valor_do_produto']}")
        else:
            print("PRODUTO NÃO ENCONTRADO.")

def main():
    while True:
        exibir_menu_produtos()
        try:
            opcao = int(input("ESCOLHA UMA OPÇÃO:"))
            if opcao == 0:
                print("SAINDO DO SISTEMA...")
                break
            elif opcao == 1:
                cadastrar_produtos()
            elif opcao == 2:
                listar_produtos()
            elif opcao == 3:
                atualizar_produto()
            elif opcao == 4:
                excluir_produto()
            elif opcao == 5:
                listar_um_produto()
            else:
                    print("OPÇÃO INVÁLIDA.")
        except ValueError:
            print("ENTRADA INVÁLIDA.")

        input("PRESSIONE ENTER PARA CONTINUAR...")

if __name__ == '__main__':
    main()


    