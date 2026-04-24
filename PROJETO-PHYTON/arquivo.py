
ARQ_USUARIOS = "usuarios.txt"
ARQ_VIDEOS = "videos.txt"
ARQ_FAVORITOS = "favoritos.txt"



def cadastroUser():
    usuario = input("Digite o nome do usuário: ").strip()
    senha = input("Digite sua senha: ").strip()

    arquivo = open(ARQ_USUARIOS, "a")
    arquivo.write(usuario + ";" + senha + "\n")
    arquivo.close()

    print("Usuário cadastrado com sucesso!")



def login():
    usuario = input("Digite seu usuário: ").strip()
    senha = input("Digite sua senha: ").strip()

    open(ARQ_USUARIOS, "a").close()

    arquivo = open(ARQ_USUARIOS, "r")
    linhas = arquivo.readlines()
    arquivo.close()

    for linha in linhas:
        linha = linha.strip()
        partes = linha.split(";")

        if len(partes) >= 2:
            u = partes[0].strip()
            s = partes[1].strip()

            if u == usuario and s == senha:
                print("Login realizado com sucesso!")
                return usuario

    print("Usuário não encontrado.")
    return None



def inicializar_videos():
    open(ARQ_VIDEOS, "a").close()

    arquivo = open(ARQ_VIDEOS, "r")
    conteudo = arquivo.read()
    arquivo.close()

    if conteudo == "":
        arquivo = open(ARQ_VIDEOS, "w")
        arquivo.write("CHIPAZINNI BANANINI;0\n")
        arquivo.write("O RETORNO DO CAFÉ;0\n")
        arquivo.write("A GUERRA DO PÃO;0\n")
        arquivo.close()


def buscar_video():
    nome = input("Digite o nome do vídeo: ").lower()

    arquivo = open(ARQ_VIDEOS, "r")
    videos = arquivo.readlines()
    arquivo.close()

    for v in videos:
        if nome in v.lower():
            titulo, likes = v.strip().split(";")
            print(f"{titulo} - Curtidas: {likes}")


def listar_videos():
    arquivo = open(ARQ_VIDEOS, "r")
    videos = arquivo.readlines()
    arquivo.close()

    for v in videos:
        titulo, likes = v.strip().split(";")
        print(f"{titulo} - Curtidas: {likes}")


def curtir_video():
    nome = input("Qual vídeo deseja curtir: ")

    arquivo = open(ARQ_VIDEOS, "r")
    videos = arquivo.readlines()
    arquivo.close()

    novos = []

    for v in videos:
        titulo, likes = v.strip().split(";")

        if titulo == nome:
            likes = str(int(likes) + 1)

        novos.append(titulo + ";" + likes)

    arquivo = open(ARQ_VIDEOS, "w")
    for v in novos:
        arquivo.write(v + "\n")
    arquivo.close()

    print("Curtido!")


def descurtir_video():
    nome = input("Qual vídeo deseja descurtir: ")

    arquivo = open(ARQ_VIDEOS, "r")
    videos = arquivo.readlines()
    arquivo.close()

    novos = []

    for v in videos:
        titulo, likes = v.strip().split(";")

        if titulo == nome and int(likes) > 0:
            likes = str(int(likes) - 1)

        novos.append(titulo + ";" + likes)

    arquivo = open(ARQ_VIDEOS, "w")
    for v in novos:
        arquivo.write(v + "\n")
    arquivo.close()

    print("Descurtido!")



def adicionar_favorito(usuario):
    video = input("Nome do vídeo: ")

    arquivo = open(ARQ_FAVORITOS, "a")
    arquivo.write(usuario + ";" + video + "\n")
    arquivo.close()

    print("Adicionado aos favoritos!")


def ver_favoritos(usuario):
    open(ARQ_FAVORITOS, "a").close()

    arquivo = open(ARQ_FAVORITOS, "r")
    linhas = arquivo.readlines()
    arquivo.close()

    print("Seus favoritos:")

    for l in linhas:
        u, v = l.strip().split(";")
        if u == usuario:
            print(v)


def remover_favorito(usuario):
    video = input("Qual vídeo remover: ")

    arquivo = open(ARQ_FAVORITOS, "r")
    linhas = arquivo.readlines()
    arquivo.close()

    novos = []

    for l in linhas:
        u, v = l.strip().split(";")
        if not (u == usuario and v == video):
            novos.append(l.strip())

    arquivo = open(ARQ_FAVORITOS, "w")
    for l in novos:
        arquivo.write(l + "\n")
    arquivo.close()

    print("Removido!")



def menu(usuario):
    while True:
        print("\n=== MENU FEI-TV ===")
        print("1 - Listar vídeos")
        print("2 - Buscar vídeo")
        print("3 - Curtir vídeo")
        print("4 - Descurtir vídeo")
        print("5 - Adicionar aos favoritos")
        print("6 - Ver favoritos")
        print("7 - Remover favorito")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            listar_videos()

        elif op == "2":
            buscar_video()

        elif op == "3":
            curtir_video()

        elif op == "4":
            descurtir_video()

        elif op == "5":
            adicionar_favorito(usuario)

        elif op == "6":
            ver_favoritos(usuario)

        elif op == "7":
            remover_favorito(usuario)

        elif op == "0":
            break



def main():
    inicializar_videos()

    print("SEJA BEM-VINDO AO FEI-TV!")

    usuario = login()

    if not usuario:
        print("Você precisa se cadastrar primeiro.")
        cadastroUser()

        print("Agora faça login novamente:")
        usuario = login()

    if usuario:
        menu(usuario)


main()
