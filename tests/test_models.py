from unittest import TestCase
from phycolo.models import Fingerprint


class TestFingerprint(TestCase):
    '''Test the phycolo Fingerprint object mapper'''

    def test_init(self):
        '''Test Fingerprint initialization'''
        fingerprint = Fingerprint('foo', ATG=5)
        self.assertTrue(isinstance(fingerprint, Fingerprint))


    def test_init_no_valid_codons(self):
        '''Test Fingerprint initalization without valid codons'''
        self.assertRaises(ValueError, Fingerprint, 'foo')
        self.assertRaises(ValueError, Fingerprint, 'foo', NNN=4)


    def test_total_count(self):
        '''Test Fingerprint total count'''
        fingerprint = Fingerprint('foo', ATG=5, TGA=3, TAG=2)
        self.assertEqual(10, fingerprint.total_count)


    def test_case_insensitivity(self):
        '''Test Fingerprint counts work for upper and lower case'''
        fingerprint = Fingerprint('foo', ATG=3, atg=2)
        self.assertEqual(5, fingerprint.ATG_count)


    def test_percentages(self):
        '''Test Fingerprint percentages'''
        fingerprint = Fingerprint('foo', ATG=5, TGA=3, TAG=2)
        self.assertAlmostEqual(50.0, fingerprint.ATG)
        self.assertAlmostEqual(30.0, fingerprint.TGA)
        self.assertAlmostEqual(20.0, fingerprint.TAG)
        self.assertAlmostEqual(0.0, fingerprint.TAA)
