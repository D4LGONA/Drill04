from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('sprite.png')


def handle_events():
    global running, dirX, dirY, state, frameX
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX += 1
            elif event.key == SDLK_LEFT:
                dirX -= 1
            elif event.key == SDLK_UP:
                dirY += 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
            elif event.key  == SDLK_LEFT:
                dirX += 1
            elif event.key == SDLK_UP:
                dirY -= 1
            elif event.key == SDLK_DOWN:
                dirY += 1

state = 'idle'
dirX = 0
dirY = 0
running = True
frameX = 0
frameY = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
count = 0

while running:
    clear_canvas()

    if dirX == 1:
        if dirY != 0:
            state = 'dizzy'
            count = 0
        else:
            state = 'right'
    elif dirX == -1:
        if dirY != 0:
            state = 'dizzy'
            count = 0
        else:
            state = 'left'
    elif dirY == 1:
        if dirX != 0:
            state = 'dizzy'
            count = 0
        else:
            state = 'up'
    elif dirY == -1:
        if dirX != 0:
            state = 'dizzy'
            count = 0
        else:
            state = 'down'
    else:
        state = 'idle'

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if state == 'idle':
        character.clip_draw(frameX * 80, 356, 80, 42, x, y)
    elif state == 'right':
        character.clip_draw(frameX * 108, 356 - 42, 104, 42, x, y)
    elif state == 'left':
        character.clip_draw(frameX * 108, 356 - 42, 104, 42, x, y)
    elif state == 'up':
        character.clip_draw(frameX * 50, 356 - 42 - 73, 50, 72, x, y)


    update_canvas()
    handle_events()
    frameX = (frameX + 1) % 4
    if state != 'dizzy':
        x += dirX * 5
        y += dirY * 5
    delay(0.1)

close_canvas()




