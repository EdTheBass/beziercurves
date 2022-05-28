import pygame as game
import numpy as np

game.init()

WIDTH = 500
HEIGHT = 500

screen = game.display.set_mode((WIDTH, HEIGHT))

game.display.set_caption("Bezier Curves")

bezier_points = [[100, 100], [50, 200], [200, 200]]

def lerp(p0, p1, t):
    dt = 1-t
    x1 = p0[0]
    x2 = p1[0]
    y1 = p0[1]
    y2 = p1[1]
    return [dt * x1 + t * x2, dt * y1 + t * y2]
def lerp_points(_points, _t):
    first_lerps = []
    
    for _x in range(len(_points)-1):
        p0 = _points[_x]
        p1 = _points[_x+1]
        first_lerps.append(lerp(p0, p1, _t))

    if len(first_lerps) > 1:
        return lerp_points(first_lerps, _t)
    else:
        return first_lerps[0]


dragging = False
dragged_point = -1
running = True
while running:
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
        elif event.type == game.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = game.mouse.get_pos()
                
                for points in range(len(bezier_points)):
                    offset = 10
                    point = bezier_points[points]
                    x1 = pos[0]
                    y1 = pos[1]
                    x2 = point[0]
                    y2 = point[1]
                    if (x2-offset) <= x1 <= (x2+offset) and (y2-offset) <= y1 <= (y2+offset):
                        dragging = True
                        dragged_point = points

        elif event.type == game.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
                dragged_point = -1

        elif event.type == game.KEYDOWN:
            if event.key == game.K_SPACE:
                bezier_points.append(game.mouse.get_pos())

            
    screen.fill((0, 0, 0))

    if dragging:
        bezier_points[dragged_point] = game.mouse.get_pos()

    for x in bezier_points:
        game.draw.circle(screen, (255, 255, 255), (x[0], x[1]), 5, width=2)

    scale = 1000
    for x in range(0, scale):
        pos = lerp_points(bezier_points, x / scale)
        screen.set_at((int(pos[0]), int(pos[1])), (255,255,255))

    game.display.update()