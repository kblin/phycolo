from unittest import TestCase

from os import path
from helperlibs.bio import seqio

from phycolo.utils import (
    count_codons,
    calculate_percentages,
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
        codons, count = count_codons(self.record)
        self.assertEqual(4432, count)
        self.assertEqual(249, codons['GCC'])
        self.assertEqual(0, codons['TAA'])


    def test_calculate_percentages(self):
        '''Test utils.calculate_precentages()'''
        codons = {'ATG': 5, 'TGA': 3, 'TAG': 2}
        count = 10
        percentages = calculate_percentages(codons, count)
        self.assertAlmostEqual(50, percentages['ATG_percent'])
        self.assertAlmostEqual(30, percentages['TGA_percent'])
        self.assertAlmostEqual(20, percentages['TAG_percent'])
