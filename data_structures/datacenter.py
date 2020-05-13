from data_structures.cluster import Cluster
import re

class Datacenter:
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """
        self.name = name
        self.clusters = [Cluster(name, values['networks'], values['security_level'])
                         for name, values in cluster_dict.items()]

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """
        first3_upper = self.name[:3].upper()
        pattern = '^' + first3_upper +'-\d{1,3}$'
        c_pattern = re.compile(pattern)
        valid_clusters = []
        for cluster in self.clusters:
            if c_pattern.match(cluster.name):
                valid_clusters.append(cluster)
        self.clusters = valid_clusters