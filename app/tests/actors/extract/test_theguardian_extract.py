import unittest
from unittest.mock import patch, Mock
from app.actors.extract.theguardian_extract import Extract


class TestTheGuardianExtract(unittest.TestCase):

    @patch.object(Extract, "run")
    def test_simple_return(self, mock_method):
        mock_method.return_value([dict(response={"foo": "bar"})])

        uri = "http://testuri.com/search"
        payload = dict(foo="bar")

        response = Extract.run(uri=uri, payload=payload)

        mock_method.assert_called_with(uri=uri, payload=payload)
        self.assertEqual(mock_method.return_value, response)