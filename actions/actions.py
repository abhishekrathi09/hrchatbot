from typing import Dict, Text, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted
from rasa_sdk.types import DomainDict

from fuzzywuzzy import process

# subject_map = {'children education advance':'CHEA','training need assesssment':'TNA','multi-purpose advance':'MPA'}

class ActionSubjectCheck(Action):
    """Validating our form input using
    multiple choice answers from Harvard
    Dialect Study"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "action_subject_check"

    # # validate user answers
    # @staticmethod
    # def subject_db() -> Dict[str, List]:
    #     """Database of multiple choice answers"""
    #     return {
    #         "subject": ["children education advance", "training need assessment", "multi-purpose advance","tna"],
    #         "subject_short": ['chea','tna','mpa']
    #     }


    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
        ) -> Dict[Text, Any]:
        """Validate user input."""
        slot_value = tracker.get_slot('subject')
        if slot_value.lower() not in domain['slots']['subject_cat']['values']:
            # find the closest answer by some measure (edit distance?)
            choices = domain['slots']['subject_cat']['values']
            answer = process.extractOne(slot_value.lower(), choices)
            # check to see if distnace is greater than some threshold
            if answer[1] < 50:
                # if so, set slot to "other"
                dispatcher.utter_message("please reframe your query")
                return [SlotSet("subject_cat",None)]
            else:
                return [SlotSet("subject_cat", answer[0])]
        else:
            return [SlotSet("subject_cat",slot_value.lower())]



    # create validation functions for each of our questions
    # validate_subject = create_validation_function(name_of_slot="subject")
    
# class FAQProcessResponse(Action):
#     """Detect the users dialect"""

#     def name(self) -> Text:
#         """Unique identifier of the action"""

#         return "FAQ_process_response"

#     def run(self, dispatcher, tracker, domain):
#         """get dialect classification """
#         # let user know the analysis is running
#         # dispatcher.utter_message(template="utter_working_on_it")

#         # get information from the form & format it
#         # for encoding
#         if tracker.get_slot("subject")=="CHEA":
#             print("CHEA")
#         else:
#             print("Not CHEA")

class ActionSlotReset(Action): 	
    def name(self): 		
        return 'action_slot_reset' 	
    def run(self, dispatcher, tracker, domain): 		
        return[AllSlotsReset()]

# class ActionRestarted(Action): 	
#     def name(self): 		
#         return 'action_restarted' 	
#     def run(self, dispatcher, tracker, domain): 
#         return[Restarted()] 

subject2_map = ["accomodation charges"]

class ActionSubject2Check(Action):
    """Validating our form input using
    multiple choice answers from Harvard
    Dialect Study"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "action_subject2_check"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
        ) -> Dict[Text, Any]:
        """Validate user input."""
        slot_value = tracker.get_slot('subject2')
        print(slot_value)
        print(subject2_map)
        if slot_value.lower() not in subject2_map:
            # find the closest answer by some measure (edit distance?)
            answer = process.extractOne(slot_value.lower(),subject2_map)
            print(answer)
            # check to see if distnace is greater than some threshold
            if answer[1] < 60:
                # if so, set slot to "other"
                dispatcher.utter_message("please reframe your query")
                return [SlotSet("subject2",None)]
            else:
                return [SlotSet("subject2", answer[0])]
        else:
            return [SlotSet("subject2",slot_value.lower())]

class ActionLevelCheck(Action):
    """Validating our form input using
    multiple choice answers from Harvard
    Dialect Study"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "action_level_check"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
        ) -> Dict[Text, Any]:
        """Validate user input."""
        slot_value = tracker.get_slot('level')
        if slot_value.lower() not in domain['slots']['level_cat']['values']:
            # find the closest answer by some measure (edit distance?)
            choices = domain['slots']['level_cat']['values']
            answer = process.extractOne(slot_value.lower(), choices)
            # check to see if distnace is greater than some threshold
            if answer[1] < 70:
                # if so, set slot to "other"
                dispatcher.utter_message("please reframe your query")
                return [SlotSet("level_cat",None)]
            else:
                return [SlotSet("level_cat", answer[0])]
        else:
            return [SlotSet("level_cat",slot_value.lower())]

tables = {'accomodation charges':{'CMD & Functional Directors': {'Principal Cities and State/UT capitals': 'Boarding & Lodging as per actual',
  'Other Principal Cities': 'Boarding & Lodging as per actual',
  'Oridnary Cities': 'Boarding & Lodging as per actual'},
 'E9': {'Principal Cities and State/UT capitals': '14000',
  'Other Principal Cities': '11000',
  'Oridnary Cities': '8800'},
 'E8': {'Principal Cities and State/UT capitals': '9800',
  'Other Principal Cities': '7700',
  'Oridnary Cities': '6160'},
 'E7': {'Principal Cities and State/UT capitals': '5600',
  'Other Principal Cities': '4400',
  'Oridnary Cities': '3520'},
 'E6': {'Principal Cities and State/UT capitals': '5600',
  'Other Principal Cities': '4400',
  'Oridnary Cities': '3520'},
 'E5': {'Principal Cities and State/UT capitals': '4200',
  'Other Principal Cities': '3300',
  'Oridnary Cities': '2640'},
 'E4': {'Principal Cities and State/UT capitals': '4200',
  'Other Principal Cities': '3300',
  'Oridnary Cities': '2640'},
 'E3': {'Principal Cities and State/UT capitals': '3150',
  'Other Principal Cities': '2475',
  'Oridnary Cities': '1980'},
 'E2': {'Principal Cities and State/UT capitals': '3150',
  'Other Principal Cities': '2475',
  'Oridnary Cities': '1980'},
 'W8/S1 and above but below E2': {'Principal Cities and State/UT capitals': '2000',
  'Other Principal Cities': '1600',
  'Oridnary Cities': '1200'},
 'W4, W5, W6 & W7': {'Principal Cities and State/UT capitals': '1500',
  'Other Principal Cities': '1200',
  'Oridnary Cities': '900'},
 'W3 and below': {'Principal Cities and State/UT capitals': '1000',
  'Other Principal Cities': '800',
  'Oridnary Cities': '600'},
 'Executive Trainee': {'Principal Cities and State/UT capitals': '1500',
  'Other Principal Cities': '1200',
  'Oridnary Cities': '900'},
 'Non-Excutive Trainee': {'Principal Cities and State/UT capitals': '1000',
  'Other Principal Cities': '800',
  'Oridnary Cities': '600'}}}

class ActionTables(Action):
    """Validating our form input using
    multiple choice answers from Harvard
    Dialect Study"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "action_tables"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
        ) -> Dict[Text, Any]:
        """Validate user input."""
        slot_value1 = tracker.get_slot('grade')
        print(slot_value1)
        slot_value2 = tracker.get_slot('subject2')
        print(slot_value2)
        dispatcher.utter_message('\n'.join("{}: {}".format(k, v) for k, v in tables[slot_value2][slot_value1].items()))
        return []


