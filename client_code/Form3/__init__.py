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
        # Get the selected payment method from the RadioButtonGroup
        selected_payment_method = self.radio_button_group_1.selected_value
        

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