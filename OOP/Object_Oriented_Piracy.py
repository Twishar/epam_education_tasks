class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        one_piece = self.draft - self.crew * 1.5 > 20
        return one_piece
