class Context:
    def __init__(self, screen):
        self.screen = screen

    def screen_width(self):        
        return self.screen.get_width()
    
    def screen_height(self):        
        return self.screen.get_height()