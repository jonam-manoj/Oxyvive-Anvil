from ._anvil_designer import slot_bookTemplate
from anvil import *
import anvil.server
# Import the datetime module
from datetime import datetime
class slot_book(slot_bookTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    button_2_click()
   

# Define a function to set the text of the button to the current date and day name

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    current_date = datetime.now()
    # Format the date as "Day Name, Month Day, Year" (e.g., "Wednesday, April 15, 2024")
    formatted_date = current_date.strftime("%A, %B %d, %Y")
    
    # Set the text of button_2 to the formatted date
    self.button_2.text = formatted_date
    
    
