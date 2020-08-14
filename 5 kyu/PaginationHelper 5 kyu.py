class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collections = collection
        self.items_per_page = items_per_page
        self.total_pages = len(self.collections)
        n = self.total_pages
        self.book = []
        while n > 0:
            self.book.append(self.items_per_page)
            n -= self.items_per_page
            if n < self.items_per_page:
                self.book.append(n)
                break

    # returns the number of items within the entire collection
    def item_count(self):
        if not self.collections:
            return -1
        return self.total_pages

    # returns the number of pages
    def page_count(self):
        return len(self.book)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        try:
            return self.book[page_index]
        except:
            return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index >= self.total_pages:
            return -1
        else:
            return item_index // self.items_per_page

