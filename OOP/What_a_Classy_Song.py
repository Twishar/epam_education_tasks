class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.chart_analytics = set()

    def how_many(self, args):
        unique = 0
        for arg in args:
            arg = arg.lower()
            if not arg in self.chart_analytics:
                self.chart_analytics.add(arg)
                unique += 1
        return unique
