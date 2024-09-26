from canvas_state import CanvasState

class History:
    def __init__(self):
        self.__prev_states: CanvasState = []

    def save_history_state(self, canvas_state):
        self.__prev_states.append(canvas_state)

    def undo(self):
        if self.__prev_states:
            return self.__prev_states.pop()
        else: 
            return None