import unittest

from app.actors.transform.theguardian_transformer import Transform


class TestTheGuardianTransform(unittest.TestCase):

    def setUp(self):
        self.return_dict_value = dict(
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

        self.row = dict(
            webUrl="webUrl",
            webPublicationDate="webPublicationDate",
            webTitle="webTitle",
            sectionName="sectionName",
            apiUrl="apiUrl",
            id="id",
            isHosted="isHosted",
            sectionId="sectionId",
            type="type",
            field1="field1",
            field2="field2",
            field3="field3",
            field4="field4",
        )
        self.pages = [[self.row, self.row], [self.row]]

    def test_with_correct_return(self):
        transformed_rows = Transform.run(self.pages)
        transformed_rows[0].pop("extractTime")

        self.assertEqual(len(transformed_rows), 3)
        self.assertDictEqual(self.return_dict_value, transformed_rows[0])
        self.assertTrue(True if "extractTime" in transformed_rows[1] else False)
