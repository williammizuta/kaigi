from models.kaigi import Kaigi

class KaigiDAO:
    def insert(self, kaigi):
        Kaigi.put(kaigi)
