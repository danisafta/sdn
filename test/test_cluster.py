from data_structures.cluster import Cluster
from data_structures.datacenter import Datacenter
from main import get_data, URL
import unittest


class TestCluster(unittest.TestCase):
    data = get_data(URL)
    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    def test_init(self):
        for dc in self.datacenters:
            for cluster in dc.clusters:
                self.assertIsInstance(cluster, Cluster)
                self.assertIsInstance(cluster.security_level, int)
                self.assertIsInstance(cluster.name, str)
                self.assertIsInstance(cluster.networks, list)

    def test_remove(self):
        pass

    def test_networks(self):
        pass


if __name__ == "__main__":
    unittest.main()
