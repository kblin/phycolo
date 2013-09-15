from unittest import TestCase

from os import path
from helperlibs.bio import seqio

from phycolo.utils import (
    count_codons,
)

def get_file_path(name):
    '''Get the path of a test file'''
    dirname = path.dirname(__file__)
    return path.join(dirname, name)

class TestPhycoloUtils(TestCase):
    '''Test the phycolo utility functions'''

    def setUp(self):
        self.record = seqio.read(get_file_path('melanin.gbk'))

    def test_count_codons(self):
        '''Test utils.count_codons()'''
        codons = count_codons(self.record)
        self.assertEqual(144, codons['GCC'])
        self.assertEqual(0, codons['TAA'])
