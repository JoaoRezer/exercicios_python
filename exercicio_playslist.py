# Requisitos:
# Variáveis para armazenar informações da playlist (nome, músicas, etc.).
# Controle de fluxo (if, while, for) para gerenciar ações do usuário.
# Funções para adicionar, remover, listar e reproduzir músicas.
# Coleções (listas ou dicionários) para armazenar as músicas.
# Classe Playlist para encapsular os métodos.

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        musica = musica.lower()
        if musica in self.musicas:
            print('Essa música já está na playlist.')
        else:
            self.musicas.append(musica)
            print(f'Música: {musica} adicionada à playlist.')

    def listar_musicas(self):
        if self.musicas:
            print(f"\nPlaylist: {self.nome}")
            for i, musica in enumerate(self.musicas, 1):
                print(f"{i}. {musica}")
        else:
            print("A playlist está vazia.")

    def remover_musica(self):
        if not self.musicas:
            print("Não há músicas na playlist.")
            return False

        self.listar_musicas()

        while True:
            try:
                escolha = int(input("Digite o número da música que deseja remover: "))
                if 1 <= escolha <= len(self.musicas):
                    break
                else:
                    print("Número inválido! Por favor, escolha um número da lista.")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número.")

        musica_removida = self.musicas.pop(escolha - 1)
        print(f"A música '{musica_removida}' foi removida com sucesso.")
        return True

    def reproduzir_musica(self, musica):
        if musica in self.musicas:
            print(f'🎶 Tocando agora: {musica} 🎶')
        else:
            print(f"A música '{musica}' não está na playlist.")

def criar_playlist():
    nome_playlist = input('Digite o nome da sua playlist: ')
    return Playlist(nome_playlist)

def menu():
    playlist_atual = None  

    while True:
        print("\n=== Sistema de Gerenciamento de Playlist ===")
        print("1. Criar playlist")
        print("2. Adicionar música")
        print("3. Listar músicas")
        print("4. Remover música")
        print("5. Reproduzir música")  
        print("6. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            playlist_atual = criar_playlist()
            print(f"Playlist '{playlist_atual.nome}' criada com sucesso.")
        elif opcao == "2":
            if playlist_atual:
                musica = input('Digite a música que quer adicionar à playlist: ')
                playlist_atual.adicionar_musica(musica)
            else:
                print("Crie uma playlist primeiro.")
        elif opcao == "3":
            if playlist_atual:
                playlist_atual.listar_musicas()
            else:
                print("Crie uma playlist primeiro.")
        elif opcao == "4":
            if playlist_atual:
                playlist_atual.remover_musica()
            else:
                print("Crie uma playlist primeiro.")
        elif opcao == "5":  
            if playlist_atual:
                musica = input('Digite a música que quer reproduzir: ')
                playlist_atual.reproduzir_musica(musica.lower())
            else:
                print("Crie uma playlist primeiro.")
        elif opcao == "6":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
