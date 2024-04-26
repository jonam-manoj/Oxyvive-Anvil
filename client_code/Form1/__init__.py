from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import string


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_1.text = self.generate_random_code()

    # Any code you write here will run before the


  # Define the function inside your Anvil form
  def generate_random_code(self):
      prefix = "SP"
      random_numbers = ''.join(random.choice(string.digits) for _ in range(5))
      code = prefix + random_numbers
      return code


