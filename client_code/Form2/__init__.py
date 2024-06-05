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

  def button_6_click(self, **event_args):
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
