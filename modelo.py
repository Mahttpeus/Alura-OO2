# a vantagem de usar herença: evitar duplicação de código, pontos de falha e o compartilhamento de codigo com subclasses
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()  # o title pega a primeira letra de cada palavra e coloca em maiúsculo.
        self.ano = ano
        self._likes = 0

    @property  # Os properties são importantes, pois quem depende da classe não precisa mudar.
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    def __str__(self):
        return f'{self.nome}, {self.ano}, {self.likes}'


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome}, {self.ano}, {self.duracao} Min , {self.likes} Likes'


class Serie(Programa):

    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'{self.nome}, {self.ano}, {self.temporada} Temporadas, {self.likes} Likes'


class Playlist:
    def __init__(self, nome, programas):
        self.nome= nome
        self._programas = programas

    def __getitem__(self, item): # representa um comportamento iteravel
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

#####################
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
druk = Filme('druk - another round', 2020, 140)
sopranos = Serie('the sopranos', 2000, 8)
thebear = Serie('the bear', 2022, 1)


vingadores.dar_like()
sopranos.dar_like()
sopranos.dar_like()
sopranos.dar_like()
druk.dar_like()
druk.dar_like()
druk.dar_like()
thebear.dar_like()
thebear.dar_like()


filmes_e_series = [vingadores, thebear, druk, sopranos]
playlist_top = Playlist('Chillzinho', filmes_e_series)

print(f'Itens na playlist: {len(playlist_top)}')

for programa in playlist_top:
    print(programa)

