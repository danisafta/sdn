from data_structures.cluster import Cluster
from data_structures.datacenter import Datacenter
from main import get_data, URL
import unittest


class TestDatacenter(unittest.TestCase):
    data = get_data(URL)
    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    def test_init(self):
        for dc in self.datacenters:
            self.assertIsInstance(dc, Datacenter)
            self.assertIsInstance(dc.name, str)
            self.assertIsInstance(dc.clusters, list)
            self.assertIsInstance(dc.clusters[0], Cluster)

    def test_remove(self):
        pass


if __name__ == "__main__":
    unittest.main()
