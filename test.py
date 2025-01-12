import pygame
import math

if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 300, 300
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    pygame.display.set_caption('Шарики')

    running = True
    circles = []
    speed = []
    clock = pygame.time.Clock()
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                speed.append([-1, -1])
                circles.append(list(event.pos))
        screen.fill('black')

        for i in circles:
            pygame.draw.circle(screen, 'white', i, 10)

        for i in range(len(circles)):
            if circles[i][0] <= 7:
                speed[i] = [1, -1]

            if circles[i][1] <= 7:
                speed[i] = [1, 1]

            if circles[i][0] >= width - 7:
                speed[i] = [-1, 1]

            if circles[i][1] >= height - 7:
                speed[i] = [-1, -1]

            if speed[i] == [1, -1]:
                circles[i][0] += math.sqrt(2) / 2
                circles[i][1] -= math.sqrt(2) / 2

            if speed[i] == [1, 1]:
                circles[i][0] += math.sqrt(2) / 2
                circles[i][1] += math.sqrt(2) / 2

            if speed[i] == [-1, -1]:
                circles[i][0] -= math.sqrt(2) / 2
                circles[i][1] -= math.sqrt(2) / 2

            if speed[i] == [-1, 1]:
                circles[i][0] -= math.sqrt(2) / 2
                circles[i][1] += math.sqrt(2) / 2


        # отрисовка и изменение свойств объектов
        clock.tick(100)

        # обновление экрана
        pygame.display.flip()
    # завершение работы:
    pygame.quit()
