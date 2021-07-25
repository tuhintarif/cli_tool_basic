
from app.application import main
from app.formating_excel import FormatingExcel
from click.testing import CliRunner
import unittest

class TestCases(unittest.TestCase):

  def test_proccess_string_with_success(self):
    runner = CliRunner()
    result = runner.invoke(main, input='hello world')
    self.assertEqual(result.exit_code, 0)
  
  def test_proccess_string_with_error(self):
    runner = CliRunner()
    string = FormatingExcel('hello world')
    result = string.format_excel()
    self.assertEqual(result, 'CSV created!')

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
