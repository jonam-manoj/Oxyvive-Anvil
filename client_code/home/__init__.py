from ._anvil_designer import homeTemplate
from anvil import *
import anvil.server

class home(homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("home")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("login")

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("signup")

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""

  def button_5_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.label_64.visible=True
    self.label_63.visible=False
    self.label_65.visible=False
    self.label_66.visible=False
    self.label_67.visible=False
    self.label_68.visible=False
    self.label_69.visible=False
  

  def link_9_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.label_64.visible=False
    self.label_63.visible=True
    self.label_65.visible=False
    self.label_66.visible=False
    self.label_67.visible=False
    self.label_68.visible=False
    self.label_69.visible=False


  def link_10_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.label_64.visible=False
    self.label_63.visible=False
    self.label_65.visible=True
    self.label_66.visible=False
    self.label_67.visible=False
    self.label_68.visible=False
    self.label_69.visible=False
  

  def link_11_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.label_64.visible=False
    self.label_63.visible=False
    self.label_65.visible=False
    self.label_66.visible=True
    self.label_67.visible=False
    self.label_68.visible=False
    self.label_69.visible=False
  

  def link_12_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.label_64.visible=False
    self.label_63.visible=False
    self.label_65.visible=False
    self.label_66.visible=False
    self.label_67.visible=True
    self.label_68.visible=False
    self.label_69.visible=False
   

  def link_13_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.label_64.visible=False
    self.label_63.visible=False
    self.label_65.visible=False
    self.label_66.visible=False
    self.label_67.visible=False
    self.label_68.visible=True
    self.label_69.visible=False
    

  def link_14_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.label_64.visible=False
    self.label_63.visible=False
    self.label_65.visible=False
    self.label_66.visible=False
    self.label_67.visible=False
    self.label_68.visible=False
    self.label_69.visible=True
    


  