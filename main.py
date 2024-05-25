import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
clock = pygame.time.Clock()

pygame.display.set_caption("All hail potato")

potato = pygame.image.load("potato.png")

song = 'song.mp3'

pygame.mixer.init()
pygame.mixer.music.load(song)
pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.blit(potato, (0, 0))

    pygame.display.update()
    clock.tick(60)