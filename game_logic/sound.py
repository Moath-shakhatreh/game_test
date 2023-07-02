import pygame
pygame.init()
pygame.mixer.init()
class Sound:
    def __init__(self):
        self.attack= pygame.mixer.Sound('assets/audio/attack.mp3')
        self.Background_Level1 = pygame.mixer.Sound("assets/audio/b_Level1.ogg")
        self.Background_Level2 = pygame.mixer.Sound("assets/audio/bg_L2.mp3")
        self.win = pygame.mixer.Sound("assets/audio/win_sound.mp3")
        self.loss = pygame.mixer.Sound("assets/audio/loss_sound.wav")
        self.End_Level = pygame.mixer.Sound("assets/audio/endoflevels.mp3")
        self.jump = pygame.mixer.Sound("assets/audio/Jump.mp3")
        self.Key = pygame.mixer.Sound("assets/audio/Key.wav")
        self.coins = pygame.mixer.Sound("assets/audio/coins.mp3")
        self.select = pygame.mixer.Sound("assets/audio/select.wav")
        self.resume = pygame.mixer.Sound("assets/audio/resume.ogg")
# set and controlling with sound's volume
    def set_volume(self, volume):
        self.volume = volume

# play sounds of game   
    def play_attack(self,volume=None):
        self.attack.set_volume(volume)
        sound = pygame.mixer.Sound.play(self.attack)
        while sound.get_busy():
         pygame.time.delay(100)
         
    def play_End_Level(self,volume=None):
        self.End_Level.set_volume(volume)
        sound = pygame.mixer.Sound.play(self.End_Level)
        while sound.get_busy():
         pygame.time.delay(100)

    def play_Background_Level1(self,volume=None):
        self.Background_Level1.set_volume(volume)
        sound = pygame.mixer.Sound.play(self.Background_Level1)
        while sound.get_busy():
         pygame.time.delay(100)
    
    def play_Background_Level2(self,volume=None):
        self.Background_Level2.set_volume(volume)
        sound = pygame.mixer.Sound.play(self.Background_Level2)
        while sound.get_busy():
         pygame.time.delay(100)
    
    def play_jump(self,volume=None):
        self.jump.set_volume(volume)
        pygame.mixer.Sound.play(self.jump)
        # while sound.get_busy():
        #  pygame.time.delay(100)

    def play_Key(self,volume=None):
        self.Key.set_volume(volume)
        sound = pygame.mixer.Sound.play(self.Key)
        while sound.get_busy():
         pygame.time.delay(100)

    def play_coins(self,volume=None):
        self.coins.set_volume(volume)
        sound = pygame.mixer.Sound.play(self.coins)
        while sound.get_busy():
         pygame.time.delay(100)

    def play_win(self,volume=None):
        self.win.set_volume(volume)
        sound = pygame.mixer.Sound.play(self.win)
        while sound.get_busy():
         pygame.time.delay(100)

    def play_loss(self,volume=None):
        self.loss.set_volume(volume)
        sound = pygame.mixer.Sound.play(self.loss)
        while sound.get_busy():
         pygame.time.delay(100)


    def play_select(self,volume=None):
        self.select.set_volume(volume)
        sound = pygame.mixer.Sound.play(self.select)
        while sound.get_busy():
         pygame.time.delay(100)

    def play_resume(self,volume=None):
        self.resume.set_volume(volume)
        sound= pygame.mixer.Sound.play(self.resume)
        while sound.get_busy():
         pygame.time.delay(100)
         
# stop -play Sound
    def stop_attack(self):
        self.attack.stop()

    def stop_End_Level(self):
        self.End_Level.stop()

    def stop_Background_Level1(self):
        self.Background_Level1.stop()

    def stop_Background_Level2(self):
        self.Background_Level2.stop()

    def stop_win(self):
        self.win.stop()
        
    def stop_loss(self):
        self.loss.stop()

    def stop_jump(self):
        self.jump.stop()

    def stop_Key(self):
        self.Key.stop()

    def stop_select(self):
        self.select.stop()

    def stop_coins(self):
        self.coins.stop()

    def stop_resume(self):
        self.resume.stop()

    
if __name__== "__main__":
    sound0 = Sound()
    sound0.play_loss()
    print("Audio")