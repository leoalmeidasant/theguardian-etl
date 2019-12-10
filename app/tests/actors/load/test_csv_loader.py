import os
import glob
import pandas as pd
import unittest

from app.actors.load.csv_loader import Load


class TestTheGuardianLoad(unittest.TestCase):
    def setUp(self):
        self.row = dict(
            webUrl="webUrl",
            webPublicationDate="webPublicationDate",
            webTitle="webTitle",
            sectionName="sectionName",
            apiUrl="apiUrl",
            id="id",
            isHosted="isHosted",
            sectionId="sectionId",
            type="type"
        )
        self.rows = [self.row, self.row, self.row, self.row]
        self.output_dir = os.path.dirname(os.path.abspath(__file__))

    def tearDown(self):
        files = glob.glob(os.path.join(self.output_dir, "*.csv"))
        for file in files:
            os.remove(file)

    def test_writing_files_and_count(self):
        Load.run(self.rows, self.output_dir)

        df = pd.concat(map(pd.read_csv, glob.glob(os.path.join(self.output_dir, "*.csv"))))
        self.assertEqual(df.shape[0], 4) # assert that dataframe has 3 rows plus header