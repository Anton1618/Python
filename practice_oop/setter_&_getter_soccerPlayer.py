'''Класс SoccerPlayer с простыми пользовательскими сеттером и геттером
    score - сеттер, который устанавливает количество голов
    make_assists - сеттер, который устанавливает количество передач
    statistics - геттер, который возвращает информацию о игроке
    '''
class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goal = 0
        self.assists = 0
    def score(self, value=1):
        self.goal += value
    def make_assists(self, value=1):
        self.assists += value
    def statistics(self):
        return f'{self.surname} {self.name} - голы: {self.goal}, передачи: {self.assists}'

if __name__ == '__main__':
    leo = SoccerPlayer('Leo', 'Messi')
    leo.score(700)
    leo.make_assists(500)
    print(leo.statistics())
