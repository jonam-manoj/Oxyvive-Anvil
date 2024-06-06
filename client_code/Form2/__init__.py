from ._anvil_designer import Form2Template
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.set_button_date()

  def set_button_date(self):
        current_date = datetime.now()
        for i in range(1, 5):  # Assuming you have 4 buttons named button_1, button_2, ..., button_4
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            date_for_button = current_date + timedelta(days=i-1)
            # Format the date as "Day" (e.g., "Tue") and day number (e.g., "17")
            formatted_date = date_for_button.strftime("%a %d")
            button.text = formatted_date

  def button_1_click(self, **event_args):
      self.primary_color_1.visible=True
      current_time = datetime.now().time()
      times = ["09:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
      for i in range(5, 11):  # Assuming you have buttons named button_5 to button_11
          button_name = f'button_{i}'
          button = getattr(self, button_name)
          # Assuming times list is predefined
          button.text = times[i - 5] if i - 5 < len(times) else "No Time"  # Display time if available, otherwise display "No Time"
          button_time = datetime.strptime(button.text, "%I:%M %p").time()
          if current_time > button_time:
              button.enabled = False  
      for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.visible = True

  def button_2_click(self, **event_args):
      self.primary_color_1.visible=True
      current_time = datetime.now().time()
      times = ["09:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
      for i in range(5, 11):  # Assuming you have buttons named button_5 to button_11
          button_name = f'button_{i}'
          button = getattr(self, button_name)
          # Assuming times list is predefined
          button.text = times[i - 5] if i - 5 < len(times) else "No Time"  # Display time if available, otherwise display "No Time"
          button_time = datetime.strptime(button.text, "%I:%M %p").time()
          if current_time > button_time:
              button.enabled = False  
      for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.visible = True

  

  def button_3_click(self, **event_args):
      self.button_4.visible = False
      # self.button_4.visible=True
      current_time = datetime.now().time()
      times = ["09:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
      for i in range(5, 11):  # Assuming you have buttons named button_5 to button_11
          button_name = f'button_{i}'
          button = getattr(self, button_name)
          # Assuming times list is predefined
          button.text = times[i - 5] if i - 5 < len(times) else "No Time"  # Display time if available, otherwise display "No Time"
          button_time = datetime.strptime(button.text, "%I:%M %p").time()
          if current_time > button_time:
              button.enabled = False  
      for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.visible = True

  def button_4_click(self, **event_args):
      self.primary_color_1.visible=True
      current_time = datetime.now().time()
      times = ["09:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
      for i in range(5, 11):  # Assuming you have buttons named button_5 to button_11
          button_name = f'button_{i}'
          button = getattr(self, button_name)
          # Assuming times list is predefined
          button.text = times[i - 5] if i - 5 < len(times) else "No Time"  # Display time if available, otherwise display "No Time"
          button_time = datetime.strptime(button.text, "%I:%M %p").time()
          if current_time > button_time:
              button.enabled = False  
      for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.visible = True
  def button_5_click(self, **event_args):
      """This method is called when the button is clicked"""
      pass
  
 