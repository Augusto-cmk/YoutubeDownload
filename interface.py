from download import *

class interface:
    def __init__(self):
        self.video = None
        while True:
            op = self.menu()
            if op == 2:
                sys.exit(0)
            else:
                modo = self.escolherModo()
                if modo != 3:
                    modos = [playlist,video]
                    while self.executar(modos[modo-1]) == False:
                        if self.continuar() == False:
                            sys.exit(0)
                    print("Vídeo(s) baixado(s) com sucesso! O(s) vídeo(s) baixado(s) se encontra(m) na paste videos do seu computador :)")
                


    def escolherModo(self):
        print("\n--------------------------------------------\n")
        print("***** Escolha o modo de download *****")
        print("1- Playlist")
        print("2- Link Unico")
        print("3- Voltar")
        print("\n--------------------------------------------\n")
        op = input("op:: ")
        if op == '1' or op == '2' or op == '3':
            return int(op)
        else:
            print("\n:::::::::: Opção inválida ::::::::::\n")
            return self.escolherModo()       

    def executar(self,type):
        op = self.get_config(type)
        if op:
            print("Baixando vídeo(s)...")
            verdadeiro,qtd = self.video.baixar(op)
            if verdadeiro == True or verdadeiro == False:
                return verdadeiro
            
            elif verdadeiro > 0 and verdadeiro < qtd:
                print(f"ATENÇÃO ********** {verdadeiro} dos {qtd} vídeos foram baixados *************")
                return self.continuar(exit=True)
            else:
                return False
        else:
            return False
    
    def continuar(self,exit=False):
        if exit:
            op = input("Parece que algo deu errado! Deseja continuar ? (s/n)").upper()
            if op == 'S':
                return True
            elif op == 'N':
                sys.exit(0)
            else:
                print("\n:::::::::: Opção inválida ::::::::::\n")
                return self.continuar()
        else:
            op = input("Parece que algo deu errado! Deseja continuar ? (s/n)").upper()
            if op == 'S':
                return True
            elif op == 'N':
                return False
            else:
                print("\n:::::::::: Opção inválida ::::::::::\n")
                return self.continuar()

    def get_config(self,type):
        self.video = type(self.lancarLink())
        try:
            print("Obtendo as resoluções possiveis...")
            op = self.escolherResolucao(self.video.resolutions())
            return op
        except Exception:
            print("[ON FUNCTION get_congig] --> Erro ao tentar acessar o link")
            return None

    def lancarLink(self):
        print("\n--------------------------------------------\n")
        link = input("Entre com o link: ")
        print("\n--------------------------------------------\n")
        return link
    
    def escolherResolucao(self,qualidades):
        print("\n--------------------------------------------\n")
        print("***** Escolha a resuloção de download *****")
        for i in range(1,len(qualidades)+1):
            print(f"{i} - {qualidades[i-1]}")

        print("\n--------------------------------------------\n")
        op = int(input("op:: "))
        opcoesPossiveis = [pos for pos in range(1,len(qualidades)+1)]
        if op in opcoesPossiveis:
            return qualidades[op-1]
        else:
            print("\n:::::::::: Opção inválida ::::::::::\n")
            return self.escolherResolucao(qualidades)

    def menu(self):
        print("\n\t********* menu **********")
        print("\t1 - Iniciar")
        print("\t2 - Sair")
        print("\t-----------------------------")
        op = input("op:: ")
        if op == '1' or op == '2':
            return int(op)
        else:
            print("\n:::::::::: Opção inválida ::::::::::\n")
            return self.menu()


interface()