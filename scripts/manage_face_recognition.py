#!/usr/bin/env python
import rospy
import face_recognition.msg
import homehabit_manager.msg
import rospy
import json
from std_msgs.msg import Int32
class ManageRecognition:
    LOCATION = "bedroom"
    def __init__(self):
        self.default_location = self.LOCATION
        self.nb_persons = 0
        self.persons = []
        self.previous_persons = []
        self.previous_nb_persons = 0
        self.pub = rospy.Publisher("/homehabit/general_purpose_cmd", homehabit_manager.msg.GeneralPurposeCmd, queue_size=10)
    
    def filtering(self):
        if not self.previous_persons:
            return
        for person in self.previous_persons:
            if self.find_person(person['name']):
                continue
            if person['state'] == 'disappear' and person['time'] >= 10:
                continue
            person['state'] = 'disappear'
            person['time'] += 1
            self.persons.append(person)

    def find_person(self, name):
        for person in self.persons:
            if person['name'] == name:
                return True
        return False

    def update(self, event):
        i = 0
        self.filtering()
        for person in self.persons:
            instances = [{
                'action': person['state']
            }]
            self.pub.publish(homehabit_manager.msg.GeneralPurposeCmd(Person=person['name'], Instruction=json.dumps(instances), Location=self.default_location, Type="user", Date=rospy.Time.now()))
            i += 1
        nb_persons_remaining = self.nb_persons - i
        for x in range(0, nb_persons_remaining):
            self.pub.publish(homehabit_manager.msg.GeneralPurposeCmd(Person="anonymous", Instruction="[]", Location=self.default_location, Type="user", Date=rospy.Time.now()))
        self.previous_persons = self.persons
        self.previous_nb_persons = self.nb_persons
        self.nb_persons = 0
        self.persons = []

    def get_message_recognition(self, data):
        feedback = data.feedback
        if len(feedback.names) > self.nb_persons:
            self.nb_persons = len(feedback.names)

        for name in feedback.names:
            self.persons.append({
                'name': name,
                'state': 'appear',
                'time': 0
            })

    def get_nb_faces(self, data):
        if data.data > self.nb_persons:
            self.nb_persons = data.data

    def get_nb_pedestrians(self, data):
        if data.data > self.nb_persons:
            self.nb_persons = data.data

def listen():
    manageRecognition = ManageRecognition()
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/face_recognition/feedback", face_recognition.msg.FaceRecognitionActionFeedback, manageRecognition.get_message_recognition)
    rospy.Subscriber("/person_detection/nb_faces", Int32, manageRecognition.get_nb_faces)
    rospy.Subscriber("/person_detection/nb_pedestrians", Int32, manageRecognition.get_nb_pedestrians)

    rospy.Timer(rospy.Duration(1), manageRecognition.update)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listen()
