from ._anvil_designer import walletTemplate
from anvil import *
import anvil.server
from anvil.tables import app_tables

class wallet(walletTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # user_id = self.id.text
    # if user_id:
    #     # Query the database directly
    #     user_row = app_tables.users.get(user_id=id)
    #     if user_row is not None:
    #         balance = user_row['wallet_balance']
    #         self.label_4.text = f"Wallet Balance: {balance}"
    #     else:
    #         self.label_4.text = "User not found."  
    # Any code you write here will run before the form opens.
  def button_4_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    pass
  # Event handler for Button 1
  def button_1_click(self, **event_args):
      self.text_box_2.text = "1000"
  
  # Event handler for Button 2
  def button_2_click(self, **event_args):
      self.text_box_2.text = "3000"
  
  # Event handler for Button 3
  def button_3_click(self, **event_args):
      self.text_box_2.text = "5000"

  def back_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
  # def setup_user_data(self):
  #       # Get the current user
        
        
  #       if user is not None:
  #           # Retrieve the user's data from the Users table
  #           user_data = app_tables.users.get(user_id=user.get_id())
            
  #           if user_data is not None:
  #               # Retrieve the wallet_balance from the user's data
  #               wallet_balance = user_data['wallet_balance']
                
  #               # Set the value of textbox_1 to the wallet_balance
  #               self.text_box_1.text = str(wallet_balance)
  #           else:
  #               # If user_data is None, handle the case where user data is not found
  #               self.text_box_1.text = "User data not found"
  #       else:
  #           # If user is None, handle the case where no user is logged in
  #           self.text_box_1.text = "No user logged in"

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
  
    