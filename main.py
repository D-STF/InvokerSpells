import pygame
import spells
import logic
import graphics

pygame.init()
window = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
render = graphics.GameRenderer(window)
pygame.display.set_caption("Invoker Game")
pygame.display.set_icon(pygame.image.load("assets/icons/icon.png"))

status =  True
gaming = False
clock = pygame.time.Clock()

while status:
    render.update_layout()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            status = False

        elif gaming == False:
            if e.type == pygame.MOUSEBUTTONDOWN:
                select_mode = render.get_clicked_mode(e.pos)
                if select_mode != None:
                    invoker = logic.InvokerSpells(select_mode)

    if gaming == False:
        render.draw_menu()

    else:

        render.draw(invoker)








