from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('sprite.png')


def handle_events():
    global running
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1 # 이게 정말 쩌는 군
            elif event.key == SDLK_LEFT:
                dir -= 1 # 생각해 본 적이 없어
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key  == SDLK_LEFT:
                dir += 1


dir = 0
running = True
frameX = 0
frameY = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2


while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frameX * 80, 355, 80, 43, x, y)

    update_canvas()
    handle_events()
    frameX = (frameX + 1) % 4
    delay(0.1)

close_canvas()




