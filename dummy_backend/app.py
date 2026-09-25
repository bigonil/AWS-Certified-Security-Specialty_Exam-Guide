import time


class Item:
    def __init__(self, id):
        self.id = id


class ItemDetail:
    def __init__(self, item_id, data):
        self.item_id = item_id
        self.data = data


class MockDB:
    def __init__(self):
        self._delay = 0.01  # Simulating a 10ms database round trip
        self.details_table = {
            i: ItemDetail(i, f"Detail for item {i}") for i in range(1, 1001)
        }

    def query(self, model):
        self.current_model = model
        return self

    def filter(self, **kwargs):
        # Simulate network/DB latency for a query
        time.sleep(self._delay)

        if "item_id" in kwargs:
            item_id = kwargs["item_id"]
            return self.details_table.get(item_id)

        if "item_id__in" in kwargs:
            item_ids = kwargs["item_id__in"]
            return [
                self.details_table.get(i)
                for i in item_ids
                if i in self.details_table
            ]

        return []


db = MockDB()
items = [Item(i) for i in range(1, 101)]


def process_items(items, db):
    if not items:
        return []

    # Optimized: Fetch all details in a single query
    item_ids = [item.id for item in items]
    all_details = db.query(ItemDetail).filter(item_id__in=item_ids)

    # Map them in memory to preserve order and structure
    details_map = {detail.item_id: detail for detail in all_details}

    result = []
    for item in items:
        # Gracefully handle missing records if any
        result.append(details_map.get(item.id))

    return result


if __name__ == "__main__":
    start = time.time()
    results = process_items(items, db)
    end = time.time()
    print(f"Processed {len(items)} items in {end - start:.4f} seconds")
    print(f"Sample result: {results[0].data if results else 'None'}")
