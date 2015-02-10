class URLShortener:

    def __init__(self):
        self.id_counter = 0
        self.links = {}

    def getURL(self, short_id):
        return self.links.get(short_id)

    def shorten(self, url):
        short_id = self.getNextId()
        self.links.update({short_id: url})
        return short_id

    def getNextId(self):
        self.id_counter += 1
        # Id got from a URL is type str anyway so it is easiest to just use
        # type str everywhere after this point.
        return str(self.id_counter)
