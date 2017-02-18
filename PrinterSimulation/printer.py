class Printer:

    def __init__(self, ppm):
        self.ppm = ppm
        self.current_task = None
        self.remaining_time = 0
    
    def tick(self):
        if self.current_task != None:
            self.remaining_time = self.remaining_time -1
            if self.remaining_time <= 0:
                self.current_task = None
    
    def busy(self):
        return self.current_task != None

    def start_next(self, new_task):
        self.current_task = new_task
        self.remaining_time = new_task.getPages() * 60 / self.ppm
    

