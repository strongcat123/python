import pygame, math, time, os, random, ctypes


pygame.init()

pygame.display.set_caption("DJ PY RESPECT ver1.2")

w = 1600
h = w * (9/16)
screen = pygame.display.set_mode((w, h))

clock = pygame.time.Clock()

main = True
ingame = True

keys = [0, 0, 0, 0]
keyset = [0, 0, 0, 0]

maxframe = 170
fps = 0
score = 0
mutime = 90
precise_click = 0
click_all = 0
combo = 0

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
    if n == 10:
        ty = 0
        tst = Time + 2
        t1.append([ty, tst])
        t2.append([ty, tst])
    if n == 11:
        ty = 0
        tst = Time + 2
        t3.append([ty, tst])
        t4.append([ty, tst])

speed = 3.5

notesumt = 0

start_notes = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 3, 2, 3, 2, 7, 1, 7, 7, 7, 7, 4, 7, 4, 7, 7, 7, 1, 7, 7, 3, 2, 3, 2, 7, 1, 7, 7, 2, 3, 4, 1, 4, 7, 4, 7, 1, 7, 7, 4, 3, 4, 4, 7, 9, 9, 9, 9, 9, 9, 7, 7, 7, 7, 7, 4, 2, 4, 4, 4, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 7, 7, 3, 1, 3, 3, 7, 7, 1, 2, 4, 4, 9, 9, 9, 9, 9, 3, 2, 3, 2, 7, 7, 7, 3, 1, 3, 3, 3, 4, 3, 2, 1, 2, 3, 4, 7, 5, 2, 3, 3, 1, 1, 1, 2, 3, 8, 10, 9, 1, 10, 7, 11, 10, 11, 10, 11, 10, 9, 1, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 9, 4, 10, 11, 10, 11, 10, 11, 10, 11, 9, 1, 11, 10, 11, 10, 11, 10, 11, 10, 5, 5, 6, 6, 6, 5, 6, 5, 6, 5, 6, 6, 6, 5, 5, 5, 6, 5, 6, 5, 6, 5, 5, 5, 6, 6, 6, 5, 6, 5, 6, 5, 6, 6, 6, 5, 5, 6, 6, 6, 8, 4, 3, 6, 5, 4, 3, 6, 8, 4, 3, 8, 9, 3, 2, 10, 6, 3, 3, 8, 9, 3, 2, 10, 4, 4, 2, 2, 3, 3, 1, 1, 11, 11, 8, 1, 1, 5, 6, 1, 2, 5, 8, 1, 1, 5, 9, 2, 3, 3, 5, 2, 2, 8, 6, 1, 2, 9, 1, 1, 4, 2, 9, 6, 1, 4, 2, 9, 8, 8, 8, 8, 1, 2, 5, 3, 1, 3, 2, 3, 2, 3, 8, 3, 2, 3, 4, 2, 4, 2, 6, 2, 3, 2, 4, 1, 4, 1, 9, 9, 4, 2, 4, 2, 6, 2, 3, 2, 4, 1, 4, 1, 9, 1, 3, 1, 4, 2, 3, 2, 6, 2, 3, 2, 4, 1, 4, 1, 9, 9, 2, 2, 4, 4, 6, 1, 3, 3, 2, 2, 4, 4, 6, 1, 3, 3, 2, 2, 4, 4, 6, 1, 9, 3, 2, 2, 4, 4, 10, 10, 4, 4, 2, 2, 6, 3, 1, 1, 4, 4, 3, 3, 5, 2, 1, 1, 3, 3, 2, 2, 8, 4, 1, 1, 3, 3, 2, 2, 3, 3, 9, 9, 7, 1, 4, 3, 4, 4, 7, 6, 1, 3, 1, 3, 1, 11, 1, 9, 1, 5, 5, 4, 1, 2, 3, 10, 2, 4, 8, 2, 8, 2, 8, 2, 4, 1, 4, 1, 3, 3, 8, 8, 1, 4, 8, 4, 4, 4, 7, 6, 1, 3, 1, 3, 11, 1, 9, 1, 5, 5,]
a = 0
aa = 0

start_ticks = pygame.time.get_ticks()

pygame.mixer.music.load("blackcat1.mp3")
pygame.mixer.music.play(-1)

while main:
    while ingame:

        if Time > 0.19 * notesumt:
            notesumt += 1
            sum_note(start_notes[a])
            a += 1
            if len(start_notes) == a:
                a = 0


        Time = time.time() - gst

        fps = clock.get_fps()

        if fps == 0:
            fps = maxframe

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
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
                          combo = combo + 1
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
                          combo = combo + 1
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
                          combo = combo + 1
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
                          combo = combo + 1
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

        screen.fill((0, 0, 0))

        keys[0] += (keyset[0] - keys[0]) / (3 * (maxframe / fps))
        keys[1] += (keyset[1] - keys[1]) / (3 * (maxframe / fps))
        keys[2] += (keyset[2] - keys[2]) / (3 * (maxframe / fps))
        keys[3] += (keyset[3] - keys[3]) / (3 * (maxframe / fps))

        pygame.draw.rect(screen, (0, 0, 0), (w / 2 - w / 8, -int(w / 100), w / 4, h + int(w /50)))

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
                score = score - 3
                combo = 0
                

        for tile_data in t2:
            tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h / 900)
            pygame.draw.rect(screen, (204, 255, 255), (w / 2 - w / 16, tile_data[0] - h / 100, w /16, h / 50))
            if tile_data[0] > h - (h / 9):
                t2.remove(tile_data)
                score = score - 3
                combo = 0
                

        for tile_data in t3:
            tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h / 900)
            pygame.draw.rect(screen, (255, 204, 255), (w / 2, tile_data[0] - h / 100, w /16, h / 50))
            if tile_data[0] > h - (h / 9):
                t3.remove(tile_data)
                score = score - 3
                combo = 0
            

        for tile_data in t4:
            tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h / 900)
            pygame.draw.rect(screen, (255, 204, 229), (w / 2 + w / 16, tile_data[0] - h / 100, w /16, h / 50))
            if tile_data[0] > h - (h / 9):
                t4.remove(tile_data)
                score = score - 3
                combo = 0
                


        #배경==============================================================================
        pygame.draw.rect(screen, (0, 0, 0), (w / 2 - w / 8, (h / 12) * 9, w / 4, h / 2))
        pygame.draw.rect(screen, (255, 255, 255), (w / 2 - w / 8, (h / 12) * 9, w / 4, h / 2), int(h /100))

        if click_all == 0:
            accuracy = 100
        else:
            accuracy = precise_click / click_all
            accuracy = accuracy * 100
            accuracy = int(accuracy)
        
        font = pygame.font.Font("Giants-Inline.ttf", 30)
        text1 = font.render("SCORE : {} / ACCURAY : {}%".format(score, accuracy), True, (255, 255, 255))
        screen.blit(text1, (1090, 9))
        
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

        pygame.draw.rect(screen, (0, 255, 140), (0, 0, 18 * int(mutime - elapsed_time), 5))

        font2 = pygame.font.Font("Giants-Inline.ttf", 40)
        text3 = font2.render("{}".format(combo), True, (204, 204, 204))
        if combo>0 and combo<10:
            screen.blit(text3, (785, 50))
        if combo>9 and combo<100:
            screen.blit(text3, (775, 50))
        if combo>99 and combo<1000:
            screen.blit(text3, (755, 50))
        text4 = font.render("COMBO", True, (204, 204, 204))
        if combo>0 and combo<10:
            screen.blit(text4, (740, 100))
        if combo>9 and combo<100:
            screen.blit(text4, (740, 100))
        if combo>99 and combo<1000:
            screen.blit(text4, (740, 100))
    
    
        
        
        if int(mutime - elapsed_time) == 0:
            pygame.mixer.music.stop()
            pygame.quit()
            if combo == 565:
                ctypes.windll.user32.MessageBoxW(0, "ACCURAY : {} / FULL COMBO!!".format(accuracy), "DJ PY RESPECT", 48)
            else:
                ctypes.windll.user32.MessageBoxW(0, "SCORE : {} / ACCURAY : {}%".format(score, accuracy), "DJ PY RESPECT", 48)
            


        pygame.display.flip()
        
        clock.tick(maxframe)