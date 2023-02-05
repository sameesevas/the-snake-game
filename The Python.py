# import lib
import pygame
import time
import random

speed = 15

window_x = 720
window_y = 480

# colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

#
pygame.init()

pygame.display.set_caption("The Python")
window = pygame.display.set_mode((window_x, window_y))
score = 0
snake_position = [100, 60]
snake_body = [[100, 60], [90, 60], [80, 60], [70, 60]]


# generate random food position
def generate_random_food_position():
    return [
        random.randrange(1, (window_x // 10) * 10),
        random.randrange(1, (window_y // 10) * 10)
        
    ]


food_position = generate_random_food_position()

direction = 'RIGHT'




def show_score(choice, color, font, size):
    s_font = pygame.font.SysFont(font, size)
    s_surface = s_font.render("SCORE : " + str(score), True, color)
    s_rect = s_surface.get_rect()
    window.blit(s_surface, s_rect)
   

def game_over():
    font = pygame.font.SysFont("Roboto", 50)
    go_surface = font.render("YOUR SCORE IS " + str(score), True, blue)
    go_rect = go_surface.get_rect()
    go_rect.midtop = (window_x / 2, window_y / 4)
    window.blit(go_surface, go_rect)

    pygame.display.flip()
    time.sleep(2)
    pygame.quit()

    quit()


fps = pygame.time.Clock()
font = pygame.font.SysFont("Roboto", 70)
go_surface = font.render("Level - 1 ", True, blue)
go_rect = go_surface.get_rect()
go_rect.midtop = (window_x / 2, window_y / 2)
window.blit(go_surface, go_rect)

pygame.display.flip()
time.sleep(1)
while True:
    # events handle karne honge
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction != 'DOWN':
                    direction = 'UP'
            if event.key == pygame.K_DOWN:
                if direction != 'UP':
                    direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                if direction != 'RIGHT':
                    direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                if direction != 'LEFT':
                    direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] = snake_position[1] - 10
    if direction == 'DOWN':
        snake_position[1] = snake_position[1] + 10
    if direction == 'LEFT':
        snake_position[0] = snake_position[0] - 10
    if direction == "RIGHT":
        snake_position[0] = snake_position[0] + 10

    # body grow
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1] or pygame.Rect(food_position[0],food_position[1],20,20).collidepoint(snake_position[0],snake_position[1]) :
        score += 10
        food_position = generate_random_food_position()
    else:
        snake_body.pop()

    window.fill(black)

    for sb in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(sb[0], sb[1], 10, 10))

    pygame.draw.rect(window, white, pygame.Rect(food_position[0], food_position[1], 10, 10))

    # game over
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    show_score(1, white, "Robot", 40)
    if score>=30:
        break
    pygame.display.update()

    fps.tick(speed)

font = pygame.font.SysFont("Roboto", 70)
go_surface = font.render("Level - 2 ", True, blue)
go_rect = go_surface.get_rect()
go_rect.midtop = (window_x / 2, window_y / 2)
window.blit(go_surface, go_rect)

pygame.display.flip()
time.sleep(1)
brick = [[window_x/2, window_y/2-40], [(window_x/2)-10, window_y/2-40], [(window_x/2)-20, window_y/2-40], [(window_x/2)-30, window_y/2-40],[(window_x/2)-40, window_y/2-40],[(window_x/2)-50, window_y/2-40],[(window_x/2)-60, window_y/2-40],[(window_x/2)-70, window_y/2-40],[(window_x/2)-80, window_y/2-40],[(window_x/2)-90, window_y/2-40]]
brick2 = [[window_x/2, window_y/2+40], [(window_x/2)-10, window_y/2+40], [(window_x/2)-20, window_y/2+40], [(window_x/2)-30, window_y/2+40],[(window_x/2)-40, window_y/2+40],[(window_x/2)-50, window_y/2+40],[(window_x/2)-60, window_y/2+40],[(window_x/2)-70, window_y/2+40],[(window_x/2)-80, window_y/2+40],[(window_x/2)-90, window_y/2+40]]
while True:
# events handle karne honge
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction != 'DOWN':
                    direction = 'UP'
            if event.key == pygame.K_DOWN:
                if direction != 'UP':
                    direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                if direction != 'RIGHT':
                    direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                if direction != 'LEFT':
                    direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] = snake_position[1] - 10
    if direction == 'DOWN':
        snake_position[1] = snake_position[1] + 10
    if direction == 'LEFT':
        snake_position[0] = snake_position[0] - 10
    if direction == "RIGHT":
        snake_position[0] = snake_position[0] + 10

    # body grow
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1] or pygame.Rect(food_position[0],food_position[1],20,20).collidepoint(snake_position[0],snake_position[1]) :
        score += 20
        food_position = generate_random_food_position()
    else:
        snake_body.pop()

    window.fill(black)

    for sb in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(sb[0], sb[1], 10, 10))
    
    pygame.draw.rect(window, white, pygame.Rect(food_position[0], food_position[1], 10, 10))
    for sb in brick:
        pygame.draw.rect(window, red, pygame.Rect(sb[0], sb[1], 15, 15))
    for sb in brick:
        if snake_position[0] == sb[0] and snake_position[1] == sb[1] or pygame.Rect(sb[0],sb[1],15,15).collidepoint(snake_position[0],snake_position[1]) :
            game_over()



    for sb in brick2:
        pygame.draw.rect(window, red, pygame.Rect(sb[0], sb[1], 15, 15))
    for sb in brick2:
        if snake_position[0] == sb[0] and snake_position[1] == sb[1] or pygame.Rect(sb[0],sb[1],15,15).collidepoint(snake_position[0],snake_position[1]) :
            game_over()



    # game over
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()
    # for sb in snake_body:
    #     if pygame.Rect(sb[0],sb[1],15,15).collidepoint(snake_position[0],snake_position[1]) :
    #         game_over()

    show_score(1, white, "Robot", 40)
    if score>=80:
        break
    pygame.display.update()

    fps.tick(speed)



font = pygame.font.SysFont("Roboto", 70)
go_surface = font.render("Level - 3 ", True, blue)
go_rect = go_surface.get_rect()
go_rect.midtop = (window_x / 2, window_y / 2)
window.blit(go_surface, go_rect)

pygame.display.flip()
time.sleep(1)
brick = [[window_x/2, window_y/2-40], [(window_x/2)-10, window_y/2-40], [(window_x/2)-20, window_y/2-40], [(window_x/2)-30, window_y/2-40],[(window_x/2)-40, window_y/2-40],[(window_x/2)-50, window_y/2-40],[(window_x/2)-60, window_y/2-40],[(window_x/2)-70, window_y/2-40],[(window_x/2)-80, window_y/2-40],[(window_x/2)-90, window_y/2-40]]
brick2 = [[window_x/2, window_y/2+40], [(window_x/2)-10, window_y/2+40], [(window_x/2)-20, window_y/2+40], [(window_x/2)-30, window_y/2+40],[(window_x/2)-40, window_y/2+40],[(window_x/2)-50, window_y/2+40],[(window_x/2)-60, window_y/2+40],[(window_x/2)-70, window_y/2+40],[(window_x/2)-80, window_y/2+40],[(window_x/2)-90, window_y/2+40]]
brick3= [[window_x/4-100, window_y/2-10], [window_x/4-100, window_y/2-20],[window_x/4-100, window_y/2-30],[window_x/4-100, window_y/2-40],[window_x/4-100, window_y/2-50],[window_x/4-100, window_y/2-60],[window_x/4-100, window_y/2-70],[window_x/4-100, window_y/2-80],[window_x/4-100, window_y/2-90],[window_x/4-100, window_y/2-100],[window_x/4-100, window_y/2+10],[window_x/4-100, window_y/2+20],[window_x/4-100, window_y/2+30],[window_x/4-100, window_y/2+40],[window_x/4-100, window_y/2+50],[window_x/4-100, window_y/2+60],[window_x/4-100, window_y/2+70],[window_x/4-100, window_y/2+80],[window_x/4-100, window_y/2],[window_x/4-100, window_y/2+90],[window_x/4-100, window_y/2+100]]
brick4 = [[window_x/4+450, window_y/2-10], [window_x/4+450, window_y/2-20],[window_x/4+450, window_y/2-30],[window_x/4+450, window_y/2-40],[window_x/4+450, window_y/2-50],[window_x/4+450, window_y/2-60],[window_x/4+450, window_y/2-70],[window_x/4+450, window_y/2-80],[window_x/4+450, window_y/2-90],[window_x/4+450, window_y/2-100],[window_x/4+450, window_y/2+10],[window_x/4+450, window_y/2+20],[window_x/4+450, window_y/2+30],[window_x/4+450, window_y/2+40],[window_x/4+450, window_y/2+50],[window_x/4+450, window_y/2+60],[window_x/4+450, window_y/2+70],[window_x/4+450, window_y/2+80],[window_x/4+450, window_y/2],[window_x/4+450, window_y/2+90],[window_x/4+450, window_y/2+100]]
while True:
# events handle karne honge
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction != 'DOWN':
                    direction = 'UP'
            if event.key == pygame.K_DOWN:
                if direction != 'UP':
                    direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                if direction != 'RIGHT':
                    direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                if direction != 'LEFT':
                    direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] = snake_position[1] - 10
    if direction == 'DOWN':
        snake_position[1] = snake_position[1] + 10
    if direction == 'LEFT':
        snake_position[0] = snake_position[0] - 10
    if direction == "RIGHT":
        snake_position[0] = snake_position[0] + 10

    # body grow
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1] or pygame.Rect(food_position[0],food_position[1],20,20).collidepoint(snake_position[0],snake_position[1]) :
        score += 40
        food_position = generate_random_food_position()
    else:
        snake_body.pop()

    window.fill(black)

    for sb in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(sb[0], sb[1], 10, 10))
    
    pygame.draw.rect(window, white, pygame.Rect(food_position[0], food_position[1], 10, 10))
    for sb in brick:
        pygame.draw.rect(window, red, pygame.Rect(sb[0], sb[1], 15, 15))
    for sb in brick:
        if snake_position[0] == sb[0] and snake_position[1] == sb[1] or pygame.Rect(sb[0],sb[1],15,15).collidepoint(snake_position[0],snake_position[1]) :
            game_over()



    for sb in brick2:
        pygame.draw.rect(window, red, pygame.Rect(sb[0], sb[1], 15, 15))
    for sb in brick2:
        if snake_position[0] == sb[0] and snake_position[1] == sb[1] or pygame.Rect(sb[0],sb[1],15,15).collidepoint(snake_position[0],snake_position[1]) :
            game_over()

    for sb in brick3:
        pygame.draw.rect(window, red, pygame.Rect(sb[0], sb[1], 15, 15))
    for sb in brick3:
        if snake_position[0] == sb[0] and snake_position[1] == sb[1] or pygame.Rect(sb[0],sb[1],15,15).collidepoint(snake_position[0],snake_position[1]) :
            game_over()


    for sb in brick4:
        pygame.draw.rect(window, red, pygame.Rect(sb[0], sb[1], 15, 15))
    for sb in brick4:
        if snake_position[0] == sb[0] and snake_position[1] == sb[1] or pygame.Rect(sb[0],sb[1],15,15).collidepoint(snake_position[0],snake_position[1]) :
            game_over()

    # game over
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()
    # for sb in snake_body:
    #     if pygame.Rect(sb[0],sb[1],15,15).collidepoint(snake_position[0],snake_position[1]) :
    #         game_over()

    show_score(1, white, "Robot", 40)
   
    pygame.display.update()

    fps.tick(speed)
