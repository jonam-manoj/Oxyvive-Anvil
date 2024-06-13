from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # Call the method to display wallet balance
    self.display_wallet_balance()

  def display_wallet_balance(self):
          # Assuming there is only one record in the wallet_balance table
          wallet_balance_record = app_tables.oxi_wallet.search()
          if wallet_balance_record:
              # Assuming wallet_balance column is a number
              balance = wallet_balance_record[0]['wallet_balance']
              # Set the text of label_5 to the wallet balance
              self.label_5.text = str(balance)
          else:
              self.label_5.text = "No balance found"
            