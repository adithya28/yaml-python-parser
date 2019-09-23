from Constants import *
from CommonRoutines import *
from commonUtils import *

class ActiveEventListScreen:
	def __init__(self):
		self.active_event_list_window = find_component(self.__class__.__name__, "active_event_list_window")
		self.active_event_list_element = find_component(self.__class__.__name__, "active_event_list_element")
