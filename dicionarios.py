usuarios={}

def perguntar():
    resposta = input("o que deseja realizar? \n" + "<I> iNSERIR \n" + "<P> pesquisar\n" + "<E> excluir\n" + "<L> Listar\n").upper()
    return resposta

def Inserir(dicionario):
    chave = input("Digite a chave: ").upper()
    dicionario[chave] = [input("Digite o nome: ").upper(), 
                         input("Digite a data: ").upper(),
                         input("Digite a estação: ").upper()
                         ]

def pesquisar(dicionario, chave):
    
   lista = dicionario.get(chave)
   if lista != None:
       print("Nome....: " + lista [0] + "data....: " + lista [1] + "etação....: " + lista [2])

def remove(dicionario, chave):
    if dicionario.get(chave)!= None:
        del dicionario[chave]
    print("objeto deletado com sucesso")
        
def listar(dicionario):
    for chave, valor in dicionario.items():
        print("obejtos: ")
        print("Login: ", chave)
        print("Dados: ", valor)
    
      
       
    
op = perguntar()
while op == "I" or op == "P" or op == "E" or op == "L":
    if (op == "I"):
        Inserir(usuarios)
    if (op == "P"):
        pesquisar(usuarios, input("digite a chave de pesquisa:"))
    if (op == "E"):
        remove(usuarios, input("digite a chave de deseja remover:"))
    if (op == "L"):
        listar(usuarios)
        
    op = perguntar()
        
        
    
        
