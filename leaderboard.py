def show_top10(screen, file_name):
    bx = 480  # x-size of box
    by = 400  # y-size of box
    
    file = open(file_name, 'r')
    lines=file.readlines()
       
    all_score = []
    for line in lines:
        sep = line.index(',')
        name = line[:sep]
        score = int(line[sep+1:-1])
        all_score.append((score, name))
    file.close
    all_score.sort(reverse=True)  # sort from largest to smallest
    best = all_score[:10]  # top 10 values

    # make the presentation box
    box = pygame.surface.Surface((bx, by)) 
    box.fill(GREY)
    pygame.draw.rect(box, WHITE, (50, 12, bx-100, 35), 0)
    pygame.draw.rect(box, WHITE, (50, by-60, bx-100, 42), 0)
    pygame.draw.rect(box, BLACK, (0, 0, bx, by), 1)
    txt_surf = font.render("HIGHSCORE", True, BLACK)  
    txt_rect = txt_surf.get_rect(center=(bx//2, 30))
    box.blit(txt_surf, txt_rect)
    txt_surf = font.render("Press ENTER to continue", True, BLACK)  
    txt_rect = txt_surf.get_rect(center=(bx//2, 360))
    box.blit(txt_surf, txt_rect)

    # write the top-10 data to the box
    for i, entry in enumerate(best):
        txt_surf = font.render(entry[1] + "  " + str(entry[0]), True, BLACK)
        txt_rect = txt_surf.get_rect(center=(bx//2, 30*i+60))
        box.blit(txt_surf, txt_rect)
    
    screen.blit(box, (0, 0))
    pygame.display.flip()
    
    while True:  # wait for user 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                return
        pygame.time.wait(20)

		
		





import pygame, sys
pygame.init()

GREY = (150, 150, 150)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont("Arial", 16)


def read_from_file_and_find_highscore(file_name):
    file = open(file_name, 'r')
    lines=file.readlines()
    file.close
       
    high_score = 0
    
    for line in lines:
        name, score = line.strip().split(",")
        score = int(score)

        if score > high_score:
            high_score = score
            high_name = name

    return high_name, high_score


def write_to_file(file_name, your_name, points):
    score_file = open(file_name, 'a')
    print (your_name+",", points, file=score_file)
    score_file.close()
    

def show_top10(screen, file_name):
    bx = 480  # x-size of box
    by = 400  # y-size of box
    
    file = open(file_name, 'r')
    lines=file.readlines()
       
    all_score = []
    for line in lines:
        sep = line.index(',')
        name = line[:sep]
        score = int(line[sep+1:-1])
        all_score.append((score, name))
    file.close
    all_score.sort(reverse=True)  # sort from largest to smallest
    best = all_score[:10]  # top 10 values

    # make the presentation box
    box = pygame.surface.Surface((bx, by)) 
    box.fill(GREY)
    pygame.draw.rect(box, WHITE, (50, 12, bx-100, 35), 0)
    pygame.draw.rect(box, WHITE, (50, by-60, bx-100, 42), 0)
    pygame.draw.rect(box, BLACK, (0, 0, bx, by), 1)
    txt_surf = font.render("HIGHSCORE", True, BLACK)  
    txt_rect = txt_surf.get_rect(center=(bx//2, 30))
    box.blit(txt_surf, txt_rect)
    txt_surf = font.render("Press ENTER to continue", True, BLACK)  
    txt_rect = txt_surf.get_rect(center=(bx//2, 360))
    box.blit(txt_surf, txt_rect)

    # write the top-10 data to the box
    for i, entry in enumerate(best):
        txt_surf = font.render(entry[1] + "  " + str(entry[0]), True, BLACK)
        txt_rect = txt_surf.get_rect(center=(bx//2, 30*i+60))
        box.blit(txt_surf, txt_rect)
    
    screen.blit(box, (0, 0))
    pygame.display.flip()
    
    while True:  # wait for user 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                return
        pygame.time.wait(20)
    

def enterbox(screen, txt):

    def blink(screen):
        for color in [GREY, WHITE]:
            pygame.draw.circle(box, color, (bx//2, int(by*0.7)), 7, 0)
            screen.blit(box, (0, by//2))
            pygame.display.flip()
            pygame.time.wait(300)

    def show_name(screen, name):
        pygame.draw.rect(box, WHITE, (50, 60, bx-100, 20), 0)
        txt_surf = font.render(name, True, BLACK)
        txt_rect = txt_surf.get_rect(center=(bx//2, int(by*0.7)))
        box.blit(txt_surf, txt_rect)
        screen.blit(box, (0, by//2))
        pygame.display.flip()
        
    bx = 480
    by = 100

    # make box
    box = pygame.surface.Surface((bx, by))
    box.fill(GREY)
    pygame.draw.rect(box, BLACK, (0, 0, bx, by), 1)
    txt_surf = font.render(txt, True, BLACK)
    txt_rect = txt_surf.get_rect(center=(bx//2, int(by*0.3)))
    box.blit(txt_surf, txt_rect)

    name = ""
    show_name(screen, name)

    # the input-loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                inkey = event.key
                if inkey in [13, 271]:  # enter/return key
                    return name
                elif inkey == 8:  # backspace key
                    name = name[:-1]
                elif inkey <= 300:
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT and 122 >= inkey >= 97:
                        inkey -= 32  # handles CAPITAL input
                    name += chr(inkey)

        if name == "":
            blink(screen)
        show_name(screen, name)


def highscore(screen, file_name, your_points, player_name):
    high_name, high_score = read_from_file_and_find_highscore(file_name)

    if your_points > high_score:
        your_name = enterbox(screen, "YOU HAVE BEATEN THE HIGHSCORE - What is your surname?")
    
    elif your_points == high_score:
        your_name = enterbox(screen, "YOU HAVE SAME AS HIGHSCORE - What is your surname?")
    
    elif your_points < high_score:
        st1 = "Highscore is "
        st2 = " made by "
        st3 = "   What is your surname?"
        txt = st1+str(high_score)+st2+high_name+st3
        your_name = enterbox(screen, txt)
        your_name = player_name + ' ' + your_name

    if your_name == None or len(your_name) == 0:
        return  # do not update the file unless a name is given

    write_to_file(file_name, your_name, your_points)
    show_top10(screen, file_name)
    return
		
		
		
		
		
		

def ShowScore(score,player_name):
    import pygame
    #from High_Score_Module import highscore
    #pygame.init()

    X = 480
    Y = 400
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    font = pygame.font.SysFont("Arial", 16)
    screen = pygame.display.set_mode((X, Y))
    screen.fill(WHITE)

    my_score = score

    highscore(screen, 'score_file.txt', my_score, player_name)

    txt_surf = font.render("Ready to continue...", True, BLACK)
    txt_rect = txt_surf.get_rect(center=(X//2, Y//2))
    screen.blit(txt_surf, txt_rect)
    pygame.display.flip()

#ShowScore(155,'hemanth')
