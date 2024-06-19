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
    # Initially hide the payment options panel
    self.payment_options_panel.visible = False


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

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('wallet_homepage.bank_accounts')

  def link_1_click(self, **event_args):
      # Show the payment options panel when the link is clicked
      self.payment_options_panel.visible = True

  # def button_3_click(self, **event_args):
  #   """This method is called when the button is clicked"""
  #   # Get the selected payment method
  #   selected_payment_method = self.radio_button_group_1.selected_value
  #   if selected_payment_method:        
  #     # Hide the payment options panel        
  #     self.payment_options_panel.visible = False
  #     # Show the selected payment method in a notification (or handle it as needed)    
  #     Notification(f"Selected Payment Method: {selected_payment_method}", timeout=3).show()

      
  # def button_3_click(self, **event_args):
  #       # Get the selected payment method from the RadioButtonGroup
  #       selected_payment_method = self.radio_button_group_1.selected_value

  #       if selected_payment_method:
  #           # Hide the payment options panel
  #           self.payment_options_panel.visible = False

  #           # Show the selected payment method in a notification (or handle it as needed)
  #           Notification(f"Selected Payment Method: {selected_payment_method}", timeout=3).show()
  #       else:
  #           alert("Please select a payment method.")

  def button_3_click(self, **event_args):
        # Get the selected payment method from the RadioButtons
        selected_payment_method = None
        if self.radio_button_1.selected:
            selected_payment_method = self.radio_button_1.text
        elif self.radio_button_2.selected:
            selected_payment_method = self.radio_button_2.text
        elif self.radio_button_3.selected:
            selected_payment_method = self.radio_button_3.text
        

        if selected_payment_method:
            # Hide the payment options panel
            self.payment_options_panel.visible = False

            # Show the selected payment method in a notification (or handle it as needed)
            Notification(f"Selected Payment Method: {selected_payment_method}", timeout=3).show()
        else:
            alert("Please select a payment method.")

  
  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form4')     

  def add_record_with_unique_account_id(self, account_id, other_data):
        # Check if the account_id already exists in the table
        existing_record = app_tables.oxi_wallet_history.get(account_id=account_id)
        
        if existing_record:
            alert(f"Account ID {account_id} already exists. Please use a unique Account ID.")
            return
        
        # Add new record with unique account_id
        app_tables.oxi_wallet_history.add_row(account_id=account_id, other_column=other_data)
        Notification(f"Record with Account ID {account_id} added successfully!", timeout=3).show()

  def update_record_with_unique_account_id(record_id, new_account_id, other_data):
    # Retrieve the record by its primary key (id)
    record_to_update = app_tables.oxi_wallet_history.get_by_id(record_id)
    if record_to_update:
        # Check if the new account_id already exists in other records
        existing_record = app_tables.oxi_wallet_history.get(account_id=new_account_id)
        
        if existing_record and existing_record.get_id() != record_id:
            alert(f"Account ID {new_account_id} already exists. Please use a unique Account ID.")
            return
        
        # Update the record
        record_to_update['account_id'] = new_account_id
        record_to_update['other_column'] = other_data
        Notification(f"Record with ID {record_id} updated successfully!", timeout=3).show()
    else:
        alert(f"No record found with ID {record_id}")


