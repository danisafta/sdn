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
        for dc in self.datacenters:
            clusters_before = dc.clusters
            dc.remove_invalid_clusters()
            clusters_after = dc.clusters
            self.assertGreaterEqual(len(clusters_before), len(clusters_after))
        for dc in self.datacenters:
            for cluster in dc.clusters:
                self.assertEqual(dc.name[:3].upper(),cluster.name[:3])

if __name__ == "__main__":
    unittest.main()
