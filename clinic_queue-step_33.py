# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: ClinicQueue
import copy

class UndoStack:
    def __init__(self):
        self._history = []
        self._max_depth = 10

    def snapshot(self, obj):
        self._history.append(copy.deepcopy(obj))
        if len(self._history) > self._max_depth:
            del self._history[0]

    def undo(self):
        if not self._history:
            return None
        return self._history.pop()
