import pygame
import virtualPet as vp
#import menus

# Initialize Pygame
pygame.init()

#set
width = 500
height = 500
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Virtual Leni Turtle")
fps = 60
#timer = pygame.time.Clock()
main_menu = False
font = pygame.font.Font('freesansbold.ttf', 24)
menu_command = 0

# Create and configure the virtual pet
pet = vp.VirtualLeniTurtle([r"BESTturtle_idle.png", r"BESTturtle_idle2.png"], 200, 150)
clock = pygame.time.Clock()

class Button:
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40))
    
    def draw(self):
        pygame.draw.rect(screen, 'light grey', self.button, 0, 5)
        pygame.draw.rect(screen, 'dark grey', self.button, 5, 5)
        text = font.render(self.text, True, 'black')
        screen.blit(text, (self.pos[0] + 15, self.pos[1] +7))
    
    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else: 
            return False

class ImgButton:
    def __init__(self, img_path, pos):
        self.image = pygame.image.load(img_path)
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (self.image.get_width(), self.image.get_height()))

    def draw(self):
        screen.blit(self.image, (self.pos[0], self.pos[1]))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

def draw_menu():
    command = 0
    pygame.draw.rect(screen, 'black', [100, 100, 300, 300])

    # exit menu button
    menu_btn = Button('Exit Menu', (120, 350))
    btn1 = Button('Button 1', (120, 180))
    btn2 = Button('Button 2', (120, 240))
    btn3 = Button('Button 3', (120, 300))

    menu_btn.draw()
    btn1.draw()
    btn2.draw()
    btn3.draw()
    if menu_btn.check_clicked():
        command = 1
    if btn1.check_clicked():
        command = 2
    if btn2.check_clicked():
        command = 3
    if btn3.check_clicked():
        command = 4

    return command

def draw_game():
    button = ImgButton('menu_btn.png', (370,440))
    button.draw()
    return button.check_clicked()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pet.update()
    #screen.fill((0, 206, 209))
    screen.blit(pet.get_current_frame(), (pet.x, pet.y))
    pygame.display.flip()

    screen.fill('light blue')
    clock.tick(fps)
    if main_menu:
        menu_command = draw_menu()
        if menu_command > 0:
            main_menu = False
    else:
        main_menu = draw_game()
        if menu_command > 1:
            text = font.render(f'Button {menu_command - 1} was clicked!', True, 'black')
            screen.blit(text, (100,200))

    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            run = False

    screen.fill((0, 206, 209))
    screen.blit(pet.get_current_frame(), (pet.x, pet.y))
    pygame.display.flip()
    clock.tick(10)  # Adjust the frame rate as needed

pygame.quit()
