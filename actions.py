from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class UserInfo(FormAction):
    def name(self) -> Text:
        return "user_info"

    @staticmethod
    def required_slots(tracker):
        return ["name", "email", "age", "phone", "location"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "name": [
                self.from_entity(entity="name"),
                self.from_intent(intent="deny", value="None"),
            ],
            "phone": [
                self.from_entity(entity="phone"),
                self.from_intent(intent="deny", value="None"),
            ],
            "age": [self.from_entity(entity="age"), self.from_intent(intent="deny", value="None")],
            "location": [
                self.from_entity(entity="location"),
                self.from_intent(intent="deny", value="None"),
            ],
            "email": [
                self.from_entity(entity="email"),
                self.from_intent(intent="deny", value="None"),
            ],
        }