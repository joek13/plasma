import sdl2
import sdl2.ext
import noise
import math

WIDTH = 50 # number of pixels horizontally.
HEIGHT = 50 # number of pixels vertically.
SCALE = 10 # resolution scale, for that good retro feel.
FRAMES = 25 # the number of frames corresponding to a unit on the simplex cube.

def main():
    window_size = (int(WIDTH * SCALE), int(HEIGHT * SCALE))
    window = sdl2.ext.Window("Hello SDL", window_size)
    window.show()

    renderer = sdl2.ext.Renderer(window.get_surface(), index=-1, flags=sdl2.SDL_RENDERER_ACCELERATED)
    renderer.scale = (SCALE, SCALE)

    frame = 0
    running = True
    while running:
        for ev in sdl2.ext.get_events():
            if ev.type == sdl2.SDL_QUIT:
                running = False
                break
        renderer.clear()
        for x in range(WIDTH):
            for y in range(HEIGHT):
                color = get_color(x, y, frame, freq=0.5)
                renderer.draw_point((x, y), color=color)
        window.refresh()
        frame += 1
def lerp(a, b, t):
    return (b - a) * t + a
def lerp_color(a, b, t):
    return (int(lerp(a[0], b[0], t)), int(lerp(a[1], b[1], t)), int(lerp(a[2], b[2], t)))

COLOR_1=[214, 61, 245]
COLOR_2=[119, 0, 193]
COLOR_3=[255, 50, 74]

def get_color(x, y, frame, freq = 1.0):
    val = noise.snoise3(float(x) / float(WIDTH), float(y) / float(HEIGHT), float(frame) / FRAMES, octaves=1, persistence=0.5, lacunarity=2.0)
    val = math.sin(val * freq)
    t = (val + 1) / 2.0
    if t < 0.5:
        return lerp_color(COLOR_1, COLOR_2, t * 2.0)
    else:
        return lerp_color(COLOR_2, COLOR_3, (t - 0.5) * 2.0)

if __name__ == "__main__":
    main()
