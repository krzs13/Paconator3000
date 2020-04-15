from random import randrange

from bird import Bird
from bone import Bone
from game_over import GameOver
from get_key import ClearConsole, GetKey, Wait, WindowSize
from laser import Laser
from map import Map
from paco import Paco
from saver import Saver
from start import Start

if __name__ == '__main__':
    map = Map(133, 33, '#')
    start = Start(133, 33)
    finish = GameOver(133, 33)
    paconator = Paco(1, 15, 133, 33)
    getKey = GetKey()
    save = Saver()
    pigeons = []
    lasers = []
    bones = []
    play_game = False
    game_over = False
    ammo = 20
    points = 0
    x = save.load()
    record = int(x)
    WindowSize()

# ====== START SCREEN ======
    while True:
        key = getKey()
        for y in range(11):
            ClearConsole()
            if y < 10:
                for x in range(87):
                    map.set_point(start.screen[y][x].x, start.screen[y][x].y, start.screen[y][x].character)
                    map.set_point(start.screen[y + 12][x].x, start.screen[y + 12][x].y, start.screen[y + 12][x].character)
            else:
                for x in range(87):
                    map.set_point(start.screen[24][x].x, start.screen[24][x].y, start.screen[24][x].character)
            map.printer()
            print(f'--- MOVE: ARROWS --- FIRE: SPACE --- COLLECT BONES TO ADD AMMO {72 * "-"}')
            Wait()
        if key == 13:
            play_game = True
        if play_game:
            break

# ====== GAME WINDOW ======
    while True:
        # ====== INITIAL STUFF ======
        ammo_str = ('0' * (1 - (ammo // 10))) + f'{ammo}'  # makes 09 from 9 etc.
        points_str = ''
        if points < 10:
            points_str = f'00{points}'
        if 10 <= points < 100:
            points_str = f'0{points}'
        if points >= 100:
            points_str = f'{points}'
        record_str = ''
        if record < 10:
            record_str = f'00{record}'
        if 10 <= record < 100:
            record_str = f'0{record}'
        if record >= 100:
            record_str = f'{record}'
        probability = randrange(1000)  # for randomly generating pigeons and bones
        # ------ clears game map ------
        ClearConsole()
        map.cleaner()
        # ------ gets key from user ------
        key = getKey()
        if key == 27:
            #save.save(record)
            break
        elif key == 299:  # left arrow
            paconator.direction.x = -3
            paconator.direction.y = 0
        elif key == 301:  # right arrow
            paconator.direction.x = 3
            paconator.direction.y = 0
        elif key == 296:  # up arrow
            paconator.direction.x = 0
            paconator.direction.y = -2
        elif key == 304:  # down arrow
            paconator.direction.x = 0
            paconator.direction.y = 2

        # ====== PACONATOR ======
        # ------ moves Paco on a map ------
        paconator.move()
        paconator.direction.x = 0
        paconator.direction.y = 0
        # ------ prints Paco ------
        for y in range(5):
            for x in range(15):
                map.set_point(paconator.sprite[y][x].x, paconator.sprite[y][x].y, paconator.sprite[y][x].character)

        # ====== LASERS ======
        # ------ shoots laser if 'space' pressed ------
        if key == 32 and ammo > 0:
            paconator.sprite[1][8].character = 'X'
            laser = Laser(paconator.sprite[1][6].x, paconator.sprite[1][6].y, 133, 33)
            lasers.append(laser)
            ammo -= 1
        else:
            paconator.sprite[1][8].character = '@'
        for index in range(len(lasers)):
            lasers[index].direction.x = 3
            lasers[index].move()
        for index in range(len(lasers)):
            for x in range(5):
                map.set_point(lasers[index].sprite[0][x].x, lasers[index].sprite[0][x].y,
                              lasers[index].sprite[0][x].character)
        # ------ destroys laser if it hits map border ------
        for index in range(len(lasers)):
            if lasers[index].sprite[0][4].x == 131:
                del lasers[index]
                break

        # ====== PIGEONS ======
        # ------ randomly adds pigeons to pigeons ------
        if probability < 50 + (20 * (points // 10)):
            pigeon = Bird(124, randrange(1, 28), 133, 33)
            pigeons.append(pigeon)
        # ------ destroys pigeon hit by laser ------
        lasers_delete = set()  # set of lasers and pigeons to delete from original lists
        pigeons_delete = set()
        for index_l in range(len(lasers)):
            for index_p in range(len(pigeons)):
                for y in range(5):
                    for x in range(7):
                        if lasers[index_l].sprite[0][4].x == pigeons[index_p].sprite[y][x].x \
                                and lasers[index_l].sprite[0][4].y == pigeons[index_p].sprite[y][x].y:
                            lasers_delete.add(lasers[index_l])
                            pigeons_delete.add(pigeons[index_p])
                            points += 1
        lasers = [laser for laser in lasers if laser not in lasers_delete]
        pigeons = [pigeon for pigeon in pigeons if pigeon not in pigeons_delete]
        # ------ destroys pigeon if it hits map border ------
        for index in range(len(pigeons)):
            if pigeons[index].sprite[0][0].x == 1:
                del pigeons[index]
                break
        # ------ game over if pigeon hits Paconator ------
        for pigeon in pigeons:
            for y in range(5):
                for x in range(7):
                    for y_p in range(5):
                        for x_p in range(15):
                            if pigeon.sprite[y][x].x == paconator.sprite[y_p][x_p].x \
                                    and pigeon.sprite[y][x].y == paconator.sprite[y_p][x_p].y \
                                    and paconator.sprite[y_p][x_p].character != ' ':
                                game_over = True
        # ------ moves pigeon on a map ------
        for index in range(len(pigeons)):
            pigeons[index].direction.x = -3
            pigeons[index].move()
        # ------ prints pigeons ------
        for index in range(len(pigeons)):
            for y in range(5):
                for x in range(7):
                    map.set_point(pigeons[index].sprite[y][x].x, pigeons[index].sprite[y][x].y,
                                  pigeons[index].sprite[y][x].character)

        # ====== BONES ======
        # ------ randomly adds bone to bones ------
        if probability < 10 + (2 * (points // 10)):
            bone = Bone(124, randrange(1, 33), 133, 33)
            bones.append(bone)
        # ------ destroys bone if it hits map border ------
        for index in range(len(bones)):
            if bones[index].sprite[0][0].x == 1:
                del bones[index]
                break
        for index in range(len(bones)):
            bones[index].direction.x = -3
            bones[index].move()
        # ------ prints bones ------
        for index in range(len(bones)):
            for x in range(5):
                map.set_point(bones[index].sprite[0][x].x, bones[index].sprite[0][x].y,
                              bones[index].sprite[0][x].character)
        # ------ adds ammo if bone eaten ------
        bones_delete = set()
        for y in range(5):
            for x in range(15):
                for index in range(len(bones)):
                    if bones[index].sprite[0][0].x == paconator.sprite[y][x].x \
                            and bones[index].sprite[0][0].y == paconator.sprite[y][x].y:
                        bones_delete.add(bones[index])
                        if ammo < 100:  # max ammo = 99
                            ammo += 10
        bones = [bone for bone in bones if bone not in bones_delete]

        # ====== MAP ======
        # ------ prints map ------
        map.printer()
        print(f'--- POINTS: {points_str} --- AMMO: {f"{ammo_str} ------------------" if ammo > 0 else "NO AMMO, EAT A BONE! "}'
              f'{72 * "-"} RECORD: {record_str} ---')
        if points > record:
            record = points
            save.save(record)
        Wait()

# ====== GAME OVER WINDOW ======
        if game_over:
            map.cleaner()
            while True:
                key = getKey()
                ClearConsole()
                for y in range(11):
                    ClearConsole()
                    if y < 10:
                        for x in range(43):
                            map.set_point(finish.screen[y][x].x, finish.screen[y][x].y, finish.screen[y][x].character)
                            map.set_point(finish.screen[y + 12][x].x, finish.screen[y + 12][x].y,
                                          finish.screen[y + 12][x].character)
                    else:
                        for x in range(43):
                            map.set_point(finish.screen[24][x].x, finish.screen[24][x].y, finish.screen[24][x].character)
                    map.printer()
                    Wait()
                break
            break
