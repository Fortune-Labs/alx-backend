import csv
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Range of the page

    Args:
        page: Current page
        page_size: Total size of the page

    Return:
        tuple with the range start and end size page
    """

    final_size: int = page * page_size
    start_size: int = final_size - page_size

    return (start_size, final_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # excluding header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0, "Page should be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size should be a positive integer"

        dataset = self.dataset()
        total_rows = len(dataset)

        start, end = index_range(page, page_size)

        if start >= total_rows:
            return []  # Return empty list if the start index exceeds dataset size
        else:
            return dataset[start:end]


# Test cases
server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print("AssertionError raised with 0")

try:
    should_err = server.get_page(2, 'Bob')
except AssertionError:
    print("AssertionError raised when page and/or page_size are not ints")

print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))
