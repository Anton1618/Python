import time
import itertools
colors = ['🔴', '🟢', '🟡']

def traffic_light():
    '''Имитация работы светофора на паттерне стейт-машины'''
    states = itertools.cycle(['red', 'green', 'yellow'])
    traffic_light.state = next(states)

    def light(color, duration):
        stop_time = time.time() + duration

        while time.time() < stop_time:
            remaining_time = stop_time - time.time()
            if remaining_time < 5:  # Если осталось меньше 5 секунд, смена индикации
                print(f'===|{" ":3}|=', end='\r')
                time.sleep(1)
                print(f'===|{color:2}|=', end='\r')
            else:  # Основная индикация
                print(f'===|{color:2}|=', end='\r')
            time.sleep(1)

        traffic_light.state = next(states)  # Переключение на следующее состояние


    while True :
        if traffic_light.state == "red":
            light(colors[0], 10)
        elif traffic_light.state == "green":
            light(colors[1], 15)
        elif traffic_light.state == "yellow":
            light(colors[2], 8)




if __name__ == '__main__':
    traffic_light()
