from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True

def handle_events():
    global running # 이녀석을 지우면 esc가 작동하지 않음. 왜냐? 밖에 있는 running을 갖다 쓰지 않고 지역에서 running을 새로 만들기 때문

    events = get_events() # 이벤트들이 담긴 리스트가 넘어옴.
    for event in events: # 이벤트를 하나씩 꺼내서 확인.
        if event.type == SDL_QUIT: # sdl 라이브러리에 키 코드가 정해져 있음, 얘는 윈도우 종료
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

frame = 0
for x in range(0, 800, 5):

    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    if not running:
        break

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()
