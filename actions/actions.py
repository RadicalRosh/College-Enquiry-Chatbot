# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"


#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionScholarshipDetails(Action):
    def name(self) -> Text:
        return "action_redirect_to_scholarship"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Send a message to the user
        dispatcher.utter_message(text="Redirecting to site for more information on scholarships...")
        
        # Custom payload to trigger frontend redirection
        dispatcher.utter_custom_json({
            "redirect": "https://www.aldel.in/scholarship.html"
        })
        
        dispatcher.utter_message(text="Need anything more?")
        return []

class ActionApplyNow(Action):
    def name(self) -> Text:
        return "action_redirect_to_apply_now"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Send a message to the user
        dispatcher.utter_message(text="Here is where you can apply for jobs. Redirecting to site for more information...")
        
        # Custom payload to trigger frontend redirection
        dispatcher.utter_custom_json({
            "redirect": "https://www.aldel.in/applynow.php"
        })
        
        dispatcher.utter_message(text="Need anything more?")
        return []
    
class ActionAttendance(Action):
    def name(self) -> Text:
        return "action_redirect_to_attendance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Send a message to the user
        dispatcher.utter_message(text="Here is where you can check your attendance . Redirecting to site...")
        
        # Custom payload to trigger frontend redirection
        dispatcher.utter_custom_json({
            "redirect": "http://report.aldel.org"
        })
        
        dispatcher.utter_message(text="Need anything more?")
        return []
    
class ActionCampus(Action):
    def name(self) -> Text:
        return "action_redirect_to_campus"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Send a message to the user
        dispatcher.utter_message(text="Here is where you can check campus of St John's College of Engineering and Management. Redirecting to the site...")
        
        # Custom payload to trigger frontend redirection
        dispatcher.utter_custom_json({
            "redirect": "https://www.aldel.in/campus-facilities.html"
        })
        
        dispatcher.utter_message(text="Need anything more?")
        return []
    
class ActionAdmission(Action):
    def name(self) -> Text:
        return "action_redirect_to_admission"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Send a message to the user
        dispatcher.utter_message(text="Here is where you can fill the form of admission or check the list of documents required for admission for St John's College of Engineering and Management. Redirecting to the site...")
        
        # Custom payload to trigger frontend redirection
        dispatcher.utter_custom_json({
            "redirect": "https://www.sjcem.edu.in/first-year-engineering-degree-admission-form/"
        })
        
        dispatcher.utter_message(text="Need anything more?")
        return []
    
class ActionCurriculum(Action):
    def name(self) -> Text:
        return "action_redirect_to_curriculum"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Send a message to the user
        dispatcher.utter_message(text="Here is where you can check the curriculum of St John's College of Engineering and Management. Redirecting to the site...")
        
        # Custom payload to trigger frontend redirection
        dispatcher.utter_custom_json({
            "redirect": "https://www.sjcem.edu.in/engdeg/wp-content/uploads/sites/2/2021/03/ilovepdf_merged-1.pdf"
        })
        
        dispatcher.utter_message(text="Need anything more?")
        return []
    
class ActionResults(Action):
    def name(self) -> Text:
        return "action_redirect_to_exam_results"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Send a message to the user
        dispatcher.utter_message(text="Here is where you can check the results of St John's College of Engineering and Management. Redirecting to the site...")
        
        # Custom payload to trigger frontend redirection
        dispatcher.utter_custom_json({
            "redirect": "http://moodle.aldel.org/course/index.php?categoryid=2"
        })
        
        dispatcher.utter_message(text="Need anything more?")
        return []
    
class ActionExams(Action):
    def name(self) -> Text:
        return "action_redirect_to_exams"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Send a message to the user
        dispatcher.utter_message(text="Here is where you can check the exams held in St John's College of Engineering and Management. Redirecting to the site...")
        
        # Custom payload to trigger frontend redirection
        dispatcher.utter_custom_json({
            "redirect": "https://www.sjcem.edu.in/engdeg/examinations/#"
        })
        
        dispatcher.utter_message(text="Need anything more?")
        return []
    
class ActionFacultyLogin(Action):
    def name(self) -> Text:
        return "action_redirect_to_faculty_login"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Send a message to the user
        dispatcher.utter_message(text="Redirecting to the faculty login site...")
        
        # Custom payload to trigger frontend redirection
        dispatcher.utter_custom_json({
            "redirect": "http://moodle.aldel.org/login/index.php"
        })
        
        dispatcher.utter_message(text="Need anything more?")
        return []
    
class ActionPlacements(Action):
    def name(self) -> Text:
        return "action_redirect_to_placements"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Send a message to the user
        dispatcher.utter_message(text="Redirecting to the Placements site...")
        
        # Custom payload to trigger frontend redirection
        dispatcher.utter_custom_json({
            "redirect": "https://www.sjcem.edu.in/engdeg/recruiters/"
        })
        
        dispatcher.utter_message(text="Need anything more?")
        return []
    
class ActionFeeStructure(Action):
    def name(self) -> Text:
        return "action_redirect_to_fees_structure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Send a message to the user
        dispatcher.utter_message(text="Redirecting to the Fees Structure site...")
        
        # Custom payload to trigger frontend redirection
        dispatcher.utter_custom_json({
            "redirect": "https://www.sjcem.edu.in/engdeg/fee-structure/"
        })
        
        dispatcher.utter_message(text="Need anything more?")
        return []
    
class ActionFeedbackForm(Action):

    def name(self) -> Text:
        return "action_feedback_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Send a message to the user
        dispatcher.utter_message(text="Redirecting to the Feedback site...")
        
        # Custom payload to trigger frontend redirection
        dispatcher.utter_custom_json({
            "redirect": "https://docs.google.com/forms/d/e/1FAIpQLSeGtf69xY05FBI0w8eVb9rjsLk9mQN1QzWbPZgAKfqxAyIgMw/viewform"
        })
        return []
    
class ActionGetImage(Action):

    def name(self) -> Text:
        return "action_cat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # # Send a message to the user
        # dispatcher.utter_message(text="Redirecting to the Feedback site...")
        
        # Custom payload to trigger frontend redirection
        dispatcher.utter_custom_json({
            "redirect": "https://imgflip.com/i/6grgcv"
        })
        return []