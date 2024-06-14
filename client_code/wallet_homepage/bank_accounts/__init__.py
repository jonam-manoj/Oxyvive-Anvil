from ._anvil_designer import bank_accountsTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class bank_accounts(bank_accountsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    account_holder_name=self.text_box_1.text
    account_number=int(self.text_box_2.text)
    bank_name=self.text_box_4.text
    branch_name=self.text_box_5.text
    ifsc_code=int(self.text_box_6.text)
    account_type=self.text_box_7.text
    app_tables.oxi_bank_accounts.add_row(account_holder_name=account_holder_name, account_number=account_number, bank_name=bank_name, branch_name=branch_name, ifsc_code=ifsc_code, account_type=account_type)
    self.text_box_1.text = ''
    self.text_box_2.text = ''
    self.text_box_3.text = ''
    self.text_box_4.text = ''
    self.text_box_5.text = ''
    self.text_box_6.text = ''
    self.text_box_7.text = ''
    alert("Bank account added successfully!", title="Success")