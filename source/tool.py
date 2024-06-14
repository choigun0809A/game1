import pygame


class img_cutter:
    def __init__(self, big_img, amount, scale):
        pygame.init()
        length , height = big_img.get_size()
        self.return_list = []
        cutting_length= length//amount
        for i in range(amount):
            cutting_rect = pygame.Rect(cutting_length*i, 0, cutting_length, height)
            cutted_img = big_img.subsurface(cutting_rect)
            cutted_img = pygame.transform.scale(cutted_img, (scale, scale))
            self.return_list.append(cutted_img)

class timer:
    def __init__(self, cooldown_time):
        self.cooldown_time = cooldown_time
        self.starting_time = 0

    def running(self):
        time = ((pygame.time.get_ticks() - self.starting_time)//100)%10

        if time == self.cooldown_time:
            return True
