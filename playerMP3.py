import pygame

pygame.init()

print(pygame.mixer.music.get_busy())

pygame.mixer.music.load('midia/Um_abrigo.mp3')
pygame.mixer.music.play(loops=5)

print(pygame.mixer.music.get_volume())
print(pygame.mixer.music.get_busy())

pygame.event.wait()
