import homehabit_manager.msg
from std_msgs.msg import String
import homehabit_manager.msg
import json
import rospy
from stt_watson.SttWatsonAbstractListener import SttWatsonAbstractListener


class HomeHabbitListener(SttWatsonAbstractListener):
    def __init__(self, watsonDialogClient, watsonTts):
        self.watsonDialogClient = watsonDialogClient
        self.watsonTts = watsonTts
        self.lock = False
        self.pubPayload = rospy.Publisher("/homehabit/watson_stt/payload", String, queue_size=10)
        self.pubGeneralPurposeCmd = rospy.Publisher("/homehabit/general_purpose_cmd", homehabit_manager.msg.GeneralPurposeCmd, queue_size=10)
        self.pubInterimHypothesis = rospy.Publisher("/homehabit/watson_stt/hypothesis/interim", String, queue_size=10)
        self.pubFinalHypothesis = rospy.Publisher("/homehabit/watson_stt/hypothesis/final", String, queue_size=10)

    def listenHypothesis(self, hypothesis):
        hypothesisStr = json.dumps(hypothesis)
        self.pubFinalHypothesis.publish(hypothesisStr)
        if self.lock:
            return
        print "Hypothesis: {0}".format(hypothesis)
        self.lock = True
        resp = self.watsonDialogClient.converse(hypothesis[0]['transcript'])
        print "Your profile:"
        dataReceive = self.watsonDialogClient.get_profile().get_data()
        for name, value in dataReceive.iteritems():
            print "\t" + name + ": " + value
        place = "bedroom"
        actionValue = ""
        if "place" in dataReceive:
            place = dataReceive['place']
        if "actionValue" in dataReceive
            actionValue = dataReceive["actionValue"]

        instructions = None

        if ("device" in dataReceive) and ("action" in dataReceive):
            instructions = [{
                'device': dataReceive['device'],
                'action': dataReceive['action'],
                'value': actionValue
            }]
        if instructions is not None:
            self.pubGeneralPurposeCmd.publish(homehabit_manager.msg.GeneralPurposeCmd(
                Person="unknown", 
                Instruction=json.dumps(instructions), 
                Location=place, 
                Type="user", 
                Date=rospy.Time.now()
            ))
        self.watsonTts.play(resp.response)
        self.lock = False

    def listenPayload(self, payload):
        payloadStr = json.dumps(payload)
        self.pubPayload.publish(payloadStr)
        

    def listenInterimHypothesis(self, interimHypothesis):
        interimHypothesisStr = json.dumps(interimHypothesis)
        self.pubInterimHypothesis.publish(interimHypothesisStr)
