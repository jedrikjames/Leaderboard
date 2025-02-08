init python:
    class Variables():
        def __init__(self,):
            self._points = 0
            self._mistakes = 0
            self.retry_option = False
            self.continue_anyway = False

        @property
        def points(self):
            return self._points
        @points.setter
        def points(self, value):
            if value < self._points:
                self.mistakes += 1
            else:
                self._points = value
        
        @property
        def mistakes(self):
            return self._mistakes
        @mistakes.setter
        def mistakes(self, value):
            self._mistakes = value
            if self._mistakes > 2:
                self.retry_option = True


#        @property
#        def playerpoints(self):
#            return self.points
#        
#        @playerpoints.setter
#        def playerpoints(self, value):  # Corrected setter name
#            self.points = value
#            if self.correct_choice:  # Added self reference
#                self.points += 5
    

#        def correct_choice(self, is_true):
#        if is_true:
#            self.points += 5
#        else:
#            self.points -= 1
#        @property
#        def playermistakes(self):
#            return self.mistakes
        
#        @playermistakes.setter
#        def playermistakes(self, value): #           self.mistakes = value
#           if self.incorrect_choice:  # Added self reference
#                self.mistakes += 1
        
#        @property
#        def mistakeschecker(self):
#            return self.mistakes_check
        
#        @mistakeschecker.setter
#        def mistakeschecker(self, value):  # Added value parameter
#            self.mistakes_check = value
#            if self.mistakes >= 2:
#                self.retry_option = True
#            else:
#                self.retry_option = False


