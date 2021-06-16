# Making game using level design
import pygame

level = []

with open("level.txt") as level1:
    for row in level1:
        level.append(list(row))
level1.close()

for i in level:
    print(i)

width, height = 1366, 768
cell_size = 50
fps = 120
start_x, start_y = 0, 0
velocity_x = 10
velocity_y = 10
frame = 0
jump_dur = 0

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Platformer")
# win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
win = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.init()

sky = pygame.transform.scale(pygame.image.load("sprites/sky.png"), (cell_size, cell_size))
ground_bellow = pygame.transform.scale(pygame.image.load("sprites/ground/slice_451.png"), (cell_size, cell_size))
ground_grass_center = pygame.transform.scale(pygame.image.load("sprites/ground/slice_426.png"),
                                             (cell_size, cell_size))
player_idle = pygame.transform.scale(pygame.image.load("sprites/mario/mario_1.png"), (cell_size, cell_size))
player_jump = pygame.transform.scale(pygame.image.load("sprites/mario/jump.png"), (cell_size, cell_size))
player_run = [pygame.transform.scale(pygame.image.load("sprites/mario/mario_2.png"), (cell_size, cell_size)),
              pygame.transform.scale(pygame.image.load("sprites/mario/mario_3.png"), (cell_size, cell_size)),
              pygame.transform.scale(pygame.image.load("sprites/mario/mario_4.png"), (cell_size, cell_size))]
player_run_flipped = [
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("sprites/mario/mario_2.png"),
                                                 (cell_size, cell_size)), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("sprites/mario/mario_3.png"),
                                                 (cell_size, cell_size)), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("sprites/mario/mario_4.png"),
                                                 (cell_size, cell_size)), True, False)]

cloud1 = pygame.transform.scale(pygame.image.load("sprites/clouds/cloud_1.png"), (cell_size, cell_size))
cloud2 = pygame.transform.scale(pygame.image.load("sprites/clouds/cloud_2.png"), (cell_size, cell_size))
cloud3 = pygame.transform.scale(pygame.image.load("sprites/clouds/cloud_3.png"), (cell_size, cell_size))
cloud4 = pygame.transform.scale(pygame.image.load("sprites/clouds/cloud_4.png"), (cell_size, cell_size))
cloud5 = pygame.transform.scale(pygame.image.load("sprites/clouds/cloud_5.png"), (cell_size, cell_size))
cloud6 = pygame.transform.scale(pygame.image.load("sprites/clouds/cloud_6.png"), (cell_size, cell_size))

isRunning = True


def loadLevel():
    global win, ground_bellow, width, sky, ground_grass_center, cell_size, height, start_x, jump_dur
    r = len(level)
    c = len(level[0])

    frame_x = -start_x // cell_size
    frame_y = 0

    for i in range(15):
        if jump_dur > 0:
            jump_dur = jump_dur - 1
            frame_y = -1
        for j in range(28):
            _sp = sky

            if level[i + frame_y][j + frame_x] == "1":
                _sp = ground_bellow
            elif level[i + frame_y][j + frame_x] == "2":
                _sp = ground_grass_center
            elif level[i + frame_y][j + frame_x] == "a":
                _sp = cloud1
            elif level[i + frame_y][j + frame_x] == "b":
                _sp = cloud2
            elif level[i + frame_y][j + frame_x] == "c":
                _sp = cloud3
            elif level[i + frame_y][j + frame_x] == "d":
                _sp = cloud4
            elif level[i + frame_y][j + frame_x] == "e":
                _sp = cloud5
            elif level[i + frame_y][j + frame_x] == "f":
                _sp = cloud6

            else:
                _sp = sky
            win.blit(_sp, (j * cell_size, i * cell_size))


i = 0


def movePlayer(action):
    global player_idle, player_run, player_run_flipped, i, player_jump
    player_x, player_y = 4, 11
    _sp = ""

    if i >= 6:
        i = 0

    if action == "right":
        _sp = player_run[i // 2]
        pass
    elif action == "left":
        _sp = player_run_flipped[i // 2]
        pass
    else:  # action == "idle"
        _sp = player_idle
        pass
    if action == "jump":
        _sp = player_jump
        pass

    i = i + 1
    win.blit(_sp, (player_x * cell_size, player_y * cell_size))


def handleKeys():
    global start_x, start_y, velocity_x, velocity_y, jump_dur
    keys = pygame.key.get_pressed()
    isJump = False

    if keys[pygame.K_SPACE]:
        # JUMP HERE
        isJump = True
        movePlayer("jump")

        jump_dur = 5
    if keys[pygame.K_LEFT]:
        # move left
        isRun = True
        start_x = start_x + 1 * velocity_x
        movePlayer("left")

    elif keys[pygame.K_RIGHT]:
        # move right
        isRun = True
        start_x = start_x - 1 * velocity_x
        movePlayer("right")
    else:
        # stay Calm
        movePlayer("idle")


while isRunning:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    loadLevel()
    handleKeys()

    # settupPlayer()

    pygame.display.update()
