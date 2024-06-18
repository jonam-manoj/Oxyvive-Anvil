from ._anvil_designer import Form4Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form4(Form4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
        # Get the value from the text box
        new_balance = self.text_box_1.text
        
        # Convert the value to a number
        try:
            new_balance = float(new_balance)
        except ValueError:
            alert("Please enter a valid number.")
            return
        
        # Update the wallet_balance in the oxi_wallet table
        wallet_record = app_tables.oxi_wallet.get()  # Adjust this if you need to filter specific records
        if wallet_record:
            # Retrieve the current balance and add the new value
            current_balance = wallet_record['wallet_balance']
            updated_balance = current_balance + new_balance
            
            # Update the wallet_balance in the database
            wallet_record['wallet_balance'] = updated_balance
            Notification("Wallet balance updated successfully!", timeout=3).show()
            open_form('Form3')
        else:
            alert("No wallet record found to update.")
            