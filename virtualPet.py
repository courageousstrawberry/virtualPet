import pygame

class VirtualLeniTurtle:
    def __init__(self, image_paths, x, y):
        self.images = [pygame.image.load(path) for path in image_paths]
        self.x = x
        self.y = y
        self.current_frame = 0
        self.frame_duration = 1000  # Adjust frame duration as needed (milliseconds)
        self.last_frame_change = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_change >= self.frame_duration:
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.last_frame_change = current_time

    def get_current_frame(self):
        return self.images[self.current_frame]


def run():

    width = 500
    height = 500
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption("Virtual Leni Turtle")
    fps = 60
    #timer = pygame.time.Clock()
    # Create and configure the virtual pet
    pet = VirtualLeniTurtle([r"BESTturtle_idle.png", r"BESTturtle_idle2.png"], 200, 150)
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pet.update()
        #screen.fill((0, 206, 209))
        screen.blit(pet.get_current_frame(), (pet.x, pet.y))
        pygame.display.flip()

        #screen.fill('light blue')
        clock.tick(fps)
        
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                running = False

        screen.fill((0, 206, 209))
        screen.blit(pet.get_current_frame(), (pet.x, pet.y))
        pygame.display.flip()
        clock.tick(10)  # Adjust the frame rate as needed
    
    pygame.quit()
