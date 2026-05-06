import pygame, math, time, os, random, ctypes
from pyvidplayer2 import Video

pygame.init()

pygame.display.set_caption("영상 출처: 유튜브 / ver.1.01")

w = 1600
h = w * (9/16)
screen = pygame.display.set_mode((w, h), pygame.SRCALPHA)
vid = Video("신같네.mp4")
vid.set_volume(0.5)

clock = pygame.time.Clock()

main = True
ingame = True

keys = [0, 0, 0, 0]
keyset = [0, 0, 0, 0]

maxframe = 170
fps = 0
score = 0
mutime = 93
precise_click = 0
click_all = 0

gst = time.time()
Time = time.time() - gst

ty = 0
tst = Time

t1 = []
t2 = []
t3 = []
t4 = []

def sum_note(n):
    if n == 1:
        ty = 0
        tst = Time + 2
        t1.append([ty, tst])
    if n == 2:
        ty = 0
        tst = Time + 2
        t2.append([ty, tst])
    if n == 3:
        ty = 0
        tst = Time + 2
        t3.append([ty, tst])
    if n == 4:
        ty = 0
        tst = Time + 2
        t4.append([ty, tst])
    if n == 5:
        ty = 0
        tst = Time + 2
        t4.append([ty, tst])
        t2.append([ty, tst])
    if n == 6:
        ty = 0
        tst = Time + 2
        t1.append([ty, tst])
        t3.append([ty, tst])
    if n == 8:
        ty = 0
        tst = Time + 2
        t1.append([ty, tst])
        t4.append([ty, tst])
    if n == 9:
        ty = 0
        tst = Time + 2
        t2.append([ty, tst])
        t3.append([ty, tst])

speed = 3

notesumt = 0

random_notes = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1, 7, 2, 7, 1, 7, 2, 7, 1, 7, 2, 7, 1, 7, 2, 7, 3, 7, 4, 7, 5, 7, 6, 7, 5, 7, 7, 4, 4, 4, 4, 7, 4, 7, 4, 7, 1, 7, 2, 7, 1, 7, 3, 7, 6, 7, 5, 7, 6, 7, 4, 3, 2, 1, 7, 5, 6, 7, 4, 7, 1, 3, 6, 5, 5, 7, 1, 4, 7, 5, 6, 7, 2, 7, 4, 4, 4, 4, 7, 4, 7, 4, 7, 7, 1, 1, 1, 1, 7, 1, 7, 1, 7, 4, 7, 4, 7, 1, 7, 1, 7, 2, 7, 4, 7, 6, 5, 6, 5, 7, 2, 7, 3, 7, 4, 7, 5, 7, 1, 7, 8, 7, 8, 7, 9, 9, 7, 7, 8, 7, 8, 7, 7, 7, 7, 4, 8, 4, 8, 7, 4, 7, 4, 7, 4, 9, 4, 9, 7, 4, 7, 4, 7, 1, 8, 1, 8, 7, 1, 7, 1, 7, 1, 9, 1, 9, 7, 1, 7, 1, 7, 4, 8, 4, 8, 7, 4, 7, 4, 7, 4, 9, 4, 9, 7, 4, 7, 4, 7, 7, 5, 7, 6, 7, 5, 7, 6, 7, 5, 6, 7, 7, 7, 9, 7, 8, 7, 1, 8, 1, 8, 7, 1, 7, 1, 7, 1, 9, 1, 9, 7, 1, 7, 1, 7, 4, 8, 4, 8, 7, 1, 7, 4, 7, 1, 8, 1, 8, 7, 1, 7, 1, 7, 8, 7, 9, 7, 8, 7, 8, 7, 5, 6, 5, 7, 7, 6, 6, 6, 7, 4, 7, 4, 4, 7, 6, 7, 1, 1, 1, 7, 7, 4, 4, 5, 7, 4, 4, 4, 4, 7, 5, 8, 9, 7, 1, 1, 7, 4, 4, 5, 7, 4, 4, 4, 4, 7, 5, 8, 9, 7, 1, 1, 7, 8, 9, 7, 1, 2, 7, 4, 7, 7, 7, 7, 1, 1, 1, 1, 1, 7, 4, 7, 4, 4, 5, 4, 6, 7, 7, 4, 5, 7, 6, 6, 7, 4, 4, 5, 7, 4, 4, 4, 4, 7, 5, 8, 9, 7, 1, 1, 7, 7, 1, 1, 5, 7, 1, 1, 1, 1, 7, 5, 8, 9, 7, 4, 4, 3, 2, 7, 1, 7, 2, 7, 3, 7, 5, 6, 8, 9, 7, 7, 7, 7, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 8, 8, 9, 9, 9, 7, 1, 2, 3, 4, 3, 2, 1, 7, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 4, 7, 7, 4, 7, 4, 4, 4, 4, 7, 4, 7, 4, 7, 4, 4, 4, 4, 7, 5, 8, 9, 7, 1, 1, 7, 7, 5, 8, 9, 7, 1, 1, 7, 8, 9, 7, 1, 2, 7, 4, 7, 7, 7, 7, 1, 1, 1, 1, 1, 7, 7, 5, 8, 9, 7, 4, 4, 7, 8, 9, 7, 4, 2, 7, 1, 7, 7, 7, 7, 4, 4, 4, 4, 4, 7, 1, 1, 7, 7, 1, 1, 5, 7, 1, 1, 1, 1, 7, 5, 8, 9, 7, 4, 4, 3, 2, 7, 1, 7, 2, 7, 3, 7, 5, 6, 8, 9, 7, 4, 4, 5, 7, 4, 4, 4, 4, 7, 5, 8, 9, 7, 4, 4, 3, 2, 7, 4, 7, 2, 7, 3, 7, 5, 6, 8, 9, 7, 7, 8, 7, 8, 7, 5, 6,]

a = 0
aa = 0

start_ticks = pygame.time.get_ticks()

while main:
    while ingame:

        if Time > 0.1 * notesumt:
            notesumt += 1
            sum_note(random_notes[a])
            a += 1
            if len(random_notes) == a:
                a = 43


        Time = time.time() - gst

        fps = clock.get_fps()

        if fps == 0:
            fps = maxframe

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vid.close()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    keyset[0] = 1
                    if len(t1) > 0:
                        if t1[0][0] > h / 2:
                          del t1[0]
                          score = score + 5
                          precise_click = precise_click + 1
                          click_all = click_all + 1
                        else:
                            score = score - 2
                            click_all = click_all + 1

                if event.key == pygame.K_f:
                    keyset[1] = 1
                    if len(t2) > 0:
                        if t2[0][0] > h / 2:
                          del t2[0]
                          score = score + 5
                          precise_click = precise_click + 1
                          click_all = click_all + 1
                        else:
                            score = score - 2
                            click_all = click_all + 1
                if event.key == pygame.K_j:
                    keyset[2] = 1
                    if len(t3) > 0:
                        if t3[0][0] > h / 2:
                          del t3[0]
                          score = score + 5
                          precise_click = precise_click + 1
                          click_all = click_all + 1
                        else:
                            score = score - 2
                            click_all = click_all + 1
                if event.key == pygame.K_k:
                    keyset[3] = 1
                    if len(t4) > 0:
                        if t4[0][0] > h / 2:
                          del t4[0]
                          score = score + 5
                          precise_click = precise_click + 1
                          click_all = click_all + 1
                        else:
                            score = score - 2
                            click_all = click_all + 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    keyset[0] = 0
                if event.key == pygame.K_f:
                    keyset[1] = 0
                if event.key == pygame.K_j:
                    keyset[2] = 0
                if event.key == pygame.K_k:
                    keyset[3] = 0

        #기어=============================================================================

        vid.draw(screen, (0, 0), force_draw=False)

        keys[0] += (keyset[0] - keys[0]) / (3 * (maxframe / fps))
        keys[1] += (keyset[1] - keys[1]) / (3 * (maxframe / fps))
        keys[2] += (keyset[2] - keys[2]) / (3 * (maxframe / fps))
        keys[3] += (keyset[3] - keys[3]) / (3 * (maxframe / fps))

        s = pygame.Surface((w / 4, h + int(w /50)), pygame.SRCALPHA)
        s.fill((0, 0, 0, 228))
        screen.blit(s, (w / 2 - w / 8, (w / -100)))
        
        #비주얼==============================================================================

        for i in range(4):
            i += 1
            pygame.draw.rect(screen, (204 - ((200 / 7) * i), 229 - ((200 / 7) * i), 255 - ((200 / 7) * i)), (w / 2 - w / 8 + w / 32 - (w / 32) * keys[0], (h / 12) * 9 - (h / 30) * keys[0] * i, w / 16 * keys[0], (h / 35) / i))
        for i in range(4):
            i += 1
            pygame.draw.rect(screen, (204 - ((200 / 7) * i), 255 - ((200 / 7) * i), 255 - ((200 / 7) * i)), (w / 2 - w / 16 + w / 32 - (w / 32) * keys[1], (h / 12) * 9 - (h / 30) * keys[1] * i, w / 16 * keys[1], (h / 35) / i))
        for i in range(4):
            i += 1
            pygame.draw.rect(screen, (255 - ((200 / 7) * i), 204 - ((200 / 7) * i), 255 - ((200 / 7) * i)), (w / 2 + w / 32 - (w / 32) * keys[2], (h / 12) * 9 - (h / 30) * keys[2] * i, w / 16 * keys[2], (h / 35) / i))
        for i in range(4):
            i += 1
            pygame.draw.rect(screen, (255 - ((200 / 7) * i), 204 - ((200 / 7) * i), 229 - ((200 / 7) * i)), (w / 2 + w / 16 + w / 32 - (w / 32) * keys[3], (h / 12) * 9 - (h / 30) * keys[3] * i, w / 16 * keys[3], (h / 35) / i))
            
        pygame.draw.rect(screen, (255, 255, 255), (w / 2 - w / 8, -int(w / 100), w / 4, h + int(w /50)), int(w /100))


        #노트=================================================================================
        for tile_data in t1:
            tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h / 900)
            pygame.draw.rect(screen, (204, 229, 255), (w / 2 - w / 8, tile_data[0] - h / 100, w /16, h / 50))
            if tile_data[0] > h - (h / 9):
                t1.remove(tile_data)
                score = score - 5
                click_all = click_all + 1

        for tile_data in t2:
            tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h / 900)
            pygame.draw.rect(screen, (204, 255, 255), (w / 2 - w / 16, tile_data[0] - h / 100, w /16, h / 50))
            if tile_data[0] > h - (h / 9):
                t2.remove(tile_data)
                score = score - 5
                click_all = click_all + 1

        for tile_data in t3:
            tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h / 900)
            pygame.draw.rect(screen, (255, 204, 255), (w / 2, tile_data[0] - h / 100, w /16, h / 50))
            if tile_data[0] > h - (h / 9):
                t3.remove(tile_data)
                score = score - 5
                click_all = click_all + 1

        for tile_data in t4:
            tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h / 900)
            pygame.draw.rect(screen, (255, 204, 229), (w / 2 + w / 16, tile_data[0] - h / 100, w /16, h / 50))
            if tile_data[0] > h - (h / 9):
                t4.remove(tile_data)
                score = score - 5
                click_all = click_all + 1


        #배경==============================================================================
        d = pygame.Surface((w / 4, h / 2), pygame.SRCALPHA)
        d.fill((0, 0, 0, 228))
        screen.blit(d, (w / 2 - w / 8, (h / 12) * 9))
        pygame.draw.rect(screen, (255, 255, 255), (w / 2 - w / 8, (h / 12) * 9, w / 4, h / 2), int(h /100))

        if click_all == 0:
            accuracy = 100
        else:
            accuracy = precise_click / click_all
            accuracy = accuracy * 100
            accuracy = int(accuracy)
        
        font = pygame.font.Font("Giants-Inline.ttf", 30)
        text1 = font.render("SCORE : {} / ACCURAY : {}%".format(score, accuracy), True, (255, 255, 255))
        screen.blit(text1, (1100, 9))
        
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

        text2 = font.render(str(int(mutime - elapsed_time)) + " :sec", True, (255, 204, 255))
        screen.blit(text2, (20, 9))
        
        
        
        if int(mutime - elapsed_time) == 0:
            vid.close()
            pygame.quit()
            ctypes.windll.user32.MessageBoxW(0, "SCORE : {} / ACCURAY : {}%".format(score, accuracy), "DJ PY RESPECT", 48)
            


        pygame.display.flip()
        
        clock.tick(maxframe)