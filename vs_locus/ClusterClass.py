from __future__ import print_function
'''
Cluster: A class to hold information and methods associated with a unique cluster
Sequence: A class to hold information and methods associated with each hit to a cluster
'''

import pandas as pd
from Messages import Messages

msg = Messages()

class ClusterSummary:
    def __init__(self):
        self.clusters = {}
    def load_table(self, filename):
        msg.info("Loading {}...".format(filename))
        try:
            header_names = ['type', 'cluster_number', 'length', 'percent', 'orientation', 'skip1', 'skip2', 'cigar', 'seq_label', 'centroid_label']
            self.tab = pd.read_table(filename, header = None, names = header_names)
            msg.success('Finished loading table from {}.'.format(filename))
            msg.info('Loaded {} lines.'.format( self.tab.shape[0]))
        except:
            msg.fail('Could not load {}'.format(filename))
            raise IOError
    def add_centroids(self):
        self.tab_centroids = self.tab[self.tab.type == 'C']
        self.loci = {}
        for row in self.tab_centroids.itertuples():
            self.loci[row.seq_label] = {}
            self.loci[row.seq_label]['size'] = row.length
            self.loci[row.seq_label]['id'] = row.cluster_number
            self.loci[row.seq_label]['locus_ref_id'] = row.seq_label
            self.loci[row.seq_label]['hits'] = {}
        msg.info('Loaded {} centroids.'.format(len(self.loci)))
    def add_hits(self):
        self.tab_hits = self.tab[self.tab.type == 'H']
        for locus in self.loci:
            msg.info("Going over locus {}.".format(locus))
            id_number = self.loci[locus]['id']
            tmp = self.tab_hits[self.tab_hits.cluster_number == id_number]
            msg.info('Found {} sequences associated with {}, with {} alleles.'.format(tmp.shape[0], locus, self.loci[locus]["size"]))
            tmp = tmp[tmp.cigar == '50M']
            msg.info('Found {} sequences associated with {} with match along all bases, with {} alleles.'.format(tmp.shape[0], locus, self.loci[locus]["size"]))
            p_ids = []
            inds = []
            for row in tmp.itertuples():
                self.loci[locus]['hits'][row.seq_label]  = {}
                self.loci[locus]['hits'][row.seq_label]['p_id'] = row.percent
                self.loci[locus]['hits'][row.seq_label]['ind'] = row.seq_label.split(';')[0].split('.')[0]
                p_ids.append(self.loci[locus]['hits'][row.seq_label]['p_id'] )
                inds.append(self.loci[locus]['hits'][row.seq_label]['ind'])
            msg.info("Found this locus across {} individuals".format(len(set(inds))))
class Cluster:
    def __init__(self, cluster_id, cluster_centroid):
        '''
        the --uc table has 10 columns in version XX of vsearch.

        1. Record type: S (centroid sequence), H (hit to centroid), or C (centroid summary).
        2. Cluster number (0-based).
        3. Centroid length (S), query length (H), or cluster size (C).
        4. Percentage of similarity with the centroid sequence (H), or set to "*" (S, C).
        5. Match orientation + or - (H), or set to "*" (S, C).
        6. Not used, always set to "*" (S, C) or to zero (H).
        7. Not used, always set to "*" (S, C) or to zero (H).
        8. Compact representation of the pairwise alignment using the  CIGAR  format  (Compact
            Idiosyncratic  Gapped Alignment Report): M (match), D (deletion) and I (insertion).
            The equal sign "=" indicates that the query is identical to the centroid sequence.
        9. Label of the query sequence (H), or of the centroid sequence (S, C).
        10. Label of the centroid sequence (H), or set to "*" (S, C).
        '''
        self.id = cluster_id
        self.centroid = cluster_centroid
        pass

class Sequence:
    def __init__(self, seq_id):
        self.id = seq_id
