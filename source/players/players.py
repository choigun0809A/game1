import pygame
import source.tool as tool
class deploy:
    def __init__(self, screen):
        self.timer_box = tool.timer(2)
        self.player_speed = 10
        self.waling_animation = tool.img_cutter(pygame.image.load('source/imgs/walkin_slime.png'), 2, 60).return_list
        self.main_player = self.waling_animation[0]
        self.player_rect = self.main_player.get_rect(x = 10, y = 10)
        self.player_moved = False
        self.facing = 'right'
        self.img_number = 0

        

        pygame.mouse.set_visible(False)


        self.click_animation = tool.img_cutter(pygame.image.load('source/imgs/cursor.png'), 2, 40).return_list
        self.main_cursor = self.click_animation[0]
        self.cursor_rect = self.main_cursor.get_rect()
        self.cursor_mask = pygame.mask.from_surface(self.click_animation[1])



        self.left_button = tool.img_cutter(pygame.image.load('source/imgs/right_left_button.png'), 1, 120).return_list[0]
        screen_width, screen_height = screen.get_size()
        self.left_button_rect = self.left_button.get_rect(center = (screen_width // 2, screen_height // 2))
        self.left_button_rect.x = 20
        self.left_button_rect.y += 100
        self.left_button_mask = pygame.mask.from_surface(self.left_button)

        self.right_button = pygame.transform.flip(self.left_button, True, False)
        self.right_button_rect = self.left_button_rect.copy()
        self.right_button_rect.x = screen.get_size()[0]-10-self.left_button.get_size()[0]
        self.right_button_mask = pygame.mask.from_surface(self.right_button)

    def run(self, screen):
        self.move_button(screen)
        self.mouse_transform(screen)
        self.animation(screen)

    
    
    def move_button(self, screen):
        screen.blit(self.left_button, self.left_button_rect)

        screen.blit(self.right_button, self.right_button_rect)

    def mouse_transform(self, screen):
        key = pygame.mouse.get_pressed()
        self.cursor_rect.center = pygame.mouse.get_pos()
        self.cursor_mask = pygame.mask.from_surface(self.main_cursor)
        self.player_moved = False
        if key[0]:
            self.main_cursor = self.click_animation[1]
            
            if self.cursor_mask.overlap(self.right_button_mask, (self.right_button_rect.x - self.cursor_rect.x , self.right_button_rect.y - self.cursor_rect.y)):
                self.player_rect.x += self.player_speed
                self.player_moved = True
                self.facing = 'right'
            elif self.cursor_mask.overlap(self.left_button_mask, (self.left_button_rect.x - self.cursor_rect.x, self.left_button_rect.y - self.cursor_rect.y)):
                self.player_rect.x -= self.player_speed
                self.player_moved = True
                self.facing = 'left'
        else:
            self.main_cursor = self.click_animation[0]
        screen.blit(self.main_cursor, self.cursor_rect)

    def animation(self, screen):
        if self.player_moved:
            if self.timer_box.running():
                self.timer_box.starting_time = pygame.time.get_ticks()
                for i in range(len(self.waling_animation)):
                    if self.img_number == len(self.waling_animation)-1:
                        self.main_player = self.waling_animation[0]
                        self.img_number = 0
                        break
                    elif self.img_number == i:
                        self.main_player = self.waling_animation[i+1]
                        self.img_number += 1
                        break
        else:
            self.main_player = self.waling_animation[0]
            self.img_number = 0
            self.timer_box.starting_time = pygame.time.get_ticks()

        if self.facing == 'left':
            temp_player = pygame.transform.flip(self.main_player, True, False)
            screen.blit(temp_player, self.player_rect)
        else:
            screen.blit(self.main_player, self.player_rect)

        

    
        