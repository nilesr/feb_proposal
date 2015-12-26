#!/usr/bin/env python3
from PIL import Image, ImageFont, ImageDraw
font = ImageFont.truetype("font.ttf", 50)
n, s, e, w = 0, 1, 2, 3 # Poor man's enum
mazea = [   [["E"],[s],    [s],    [s],    [],  [s]],
            [[e],  [w, n], [n, s], [n, s], [s], [n, s]],
            [[e],  [w, s], [n, s], [n, s], [n], [n, s]],
            [[e],  [w, n], [n],    [n],    [],  [n]],
            [[],   [s],    [s],    [],     [s], [s]],
            [[],   [n],    [n],    [],     [n], [n, "S"]]
        ]
mazea_solved = [[["E"],   [s,"1"],    [s,"2"],     [s,"3"],    ["4"],   [s,"5"]],
                [[e,"1"], [w, n,"8"], [n, s,"7"],  [n, s,"6"], [s,"5"], [n, s,"6"]],
                [[e,"2"], [w, s,"9"], [n, s,"10"], [n, s,"11"],[n,"10"],[n, s,"11"]],
                [[e,"3"], [w, n,"6"], [n,"7"],     [n,"8"],    ["9"],   [n,"10"]],
                [["4"],   [s,"5"],    [s,"6"],     ["7"],      [s, "8"],[s, "9"]],
                [["5"],   [n,"6"],    [n,"7"],     ["8"],      [n,"9"], [n, "S"]]
        ]

mazes = [
      [mazea, "1.png"]
    , [mazea_solved, "1_solved.png"]
    ]
for maze_struct in mazes:
    f = Image.new("RGB",(600, 600),(255,255,255))
    draw = ImageDraw.Draw(f)
    for x in range(600):
        for y in range(600):
            for j in range(len(maze_struct[0])):
                for i in range(len(maze_struct[0][0])):
                    for wall in maze_struct[0][i][j]:
                        if type(wall) == int:
                            if 100*i < x < 100*i+100 and 100*j < y < 100*j+100 and ((x%100 < 3 and wall == n) or (100-(x%100) < 3 and wall == s) or (y%100 < 3 and wall == w) or (100-(y%100) < 3 and wall == e)):
                                f.putpixel((y,x),(0,0,0))
                        elif x == i+50 and y == j+50:
                            k = len(wall)
                            p, q = j*100+35-((-35/2)*(1-k)), i*100+25
                            draw.text((p, q),wall,(0,0,0),font=font)
            if (x % 100 < 3 or y % 100 < 3) and f.getpixel((x, y)) == (255,255,255):
                f.putpixel((x,y),(220,220,220))
    f.save(maze_struct[1], subsampling=0, quality=100)
