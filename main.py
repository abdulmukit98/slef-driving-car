import pygame
pygame.init()

track = pygame.image.load('track6.png')
window = pygame.display.set_mode((1200, 400))
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30,60))

car_x = 155
car_y = 300
cam_x_ofset = 0
cam_y_ofset = 0
focal_dist = 25
direction = 'up'
drive = True
clock = pygame.time.Clock()
while drive:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False

    #detect road
    cam_x = car_x + cam_x_ofset + 15
    cam_y = car_y + cam_y_ofset + 15
    up_px = window.get_at((cam_x, cam_y - focal_dist)) [0]
    down_px = window.get_at((cam_x, cam_y + focal_dist)) [0]
    right_px = window.get_at((cam_x + focal_dist, cam_y)) [0]
    print(up_px, right_px, down_px)

    #direction
    if direction=='up' and up_px!=255 and right_px == 255:
        direction = 'right'
        cam_x_ofset = 30
        car = pygame.transform.rotate(car, -90)

    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car = pygame.transform.rotate(car, -90)
        car_x = car_x + 30
        cam_x_ofset = 0
        cam_y_ofset = 30
    elif direction == 'down' and down_px!=255 and right_px == 255:
        direction = 'right'
        car = pygame.transform.rotate(car, 90)
        car_y = car_y + 30
        cam_x_ofset = 30
        cam_y_ofset = 0
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car = pygame.transform.rotate(car, 90)
        car_x = car_x + 30
        cam_x_ofset = 0

    #drive
    if direction=='up' and up_px == 255:
        car_y = car_y -1
    elif direction == 'right' and right_px == 255:
        car_x = car_x +1
    elif direction == 'down' and down_px == 255:
        car_y = car_y + 1

    window.blit(track, (0,0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)

    pygame.display.update()
