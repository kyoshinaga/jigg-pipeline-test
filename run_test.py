#!/usr/bin/python

import unittest
import subprocess
import sys
import xml.etree.ElementTree as ET
import json

import comp_modules as cm

cmd = 'java -cp "$HOME/IdeaProjects/jigg/bin/*" jigg.pipeline.Pipeline'

class TestSequenceFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.reporter = lambda x: sys.stdout.write(x + '\n')

        # XML -> XML
        #subprocess.call(cmd + ' -props ./props/english_corenlp_tokenize_ssplit_xml.properties', shell = True)
        #subprocess.call(cmd + ' -props ./props/english_corenlp_pos_gold_xml.properties', shell=True)
        #subprocess.call(cmd + ' -props ./props/english_corenlp_pos_test_xml.properties', shell=True)
        #subprocess.call(cmd + ' -props ./props/english_corenlp_lemma_gold_xml.properties', shell=True)
        #subprocess.call(cmd + ' -props ./props/english_corenlp_lemma_test_xml.properties', shell=True)
        #subprocess.call(cmd + ' -props ./props/english_corenlp_ner_gold_xml.properties', shell=True)
        #subprocess.call(cmd + ' -props ./props/english_corenlp_ner_test_xml.properties', shell=True)
        #subprocess.call(cmd + ' -props ./props/english_corenlp_parse_gold_xml.properties', shell=True)
        #subprocess.call(cmd + ' -props ./props/english_corenlp_parse_test_xml.properties', shell=True)
        #subprocess.call(cmd + ' -props ./props/english_corenlp_depparse_test_xml.properties', shell=True)
        #subprocess.call(cmd + ' -props ./props/english_corenlp_depparse_gold_xml.properties', shell=True)

        # JSON -> JSON
        subprocess.call(cmd + ' -props ./props/english_corenlp_tokenize_ssplit_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_pos_gold_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_pos_test_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_lemma_gold_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_lemma_test_json.properties', shell = True)

        # XML -> JSON
        subprocess.call(cmd + ' -props ./props/english_corenlp_pos_test_xml_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_lemma_test_xml_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_ner_test_xml_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_parse_test_xml_json.properties', shell = True)
        subprocess.call(cmd + ' -props ./props/english_corenlp_depparse_test_xml_json.properties', shell = True)

        # JSON -> XML
        subprocess.call(cmd + ' -props ./props/english_corenlp_pos_test_json_xml.properties', shell = True)


    def test_1_corenlp_1_pos(self):
        testRoot = ET.parse('./xml/english_corenlp_pos_test.xml').getroot()
        testJsonRoot = ET.parse('./xml/english_corenlp_pos_test_json.xml').getroot()
        goldRoot = ET.parse('./xml/english_corenlp_pos_gold.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.xml_compare(goldRoot, testJsonRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_corenlp_pos_gold.json', \
            './json/english_corenlp_pos_test_xml.json'))
        self.assertTrue(cm.json_comp('./json/english_corenlp_pos_gold.json', \
            './json/english_corenlp_pos_test.json'))

    def test_1_corenlp_2_lemma(self):
        testRoot = ET.parse('./xml/english_corenlp_lemma_test.xml').getroot()
        goldRoot = ET.parse('./xml/english_corenlp_lemma_gold.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))
        self.assertTrue(cm.json_comp('./json/english_corenlp_lemma_gold.json', \
            './json/english_corenlp_lemma_test.json'))

    def test_1_corenlp_3_ner(self):
        testRoot = ET.parse('./xml/english_corenlp_ner_test.xml').getroot()
        goldRoot = ET.parse('./xml/english_corenlp_ner_gold.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))

    def test_1_corenlp_4_parse(self):
        testRoot = ET.parse('./xml/english_corenlp_parse_test.xml').getroot()
        goldRoot = ET.parse('./xml/english_corenlp_parse_gold.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))

    def test_1_corenlp_5_depparse(self):
        testRoot = ET.parse('./xml/english_corenlp_depparse_test.xml').getroot()
        goldRoot = ET.parse('./xml/english_corenlp_depparse_gold.xml').getroot()
        self.assertTrue(cm.xml_compare(goldRoot, testRoot, self.reporter))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=3).run(suite)
