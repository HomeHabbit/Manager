# Manager

## Requirements

### Always needed
- **Python 2.7**
- **Pip**
- Ros indigo (maybe can be used on new version of ros but this is not tested)

### Needed for face recognition

- [face_recognition](http://wiki.ros.org/face_recognition)
- (optional if you want better detection and prediction): [hog_haar_person_detection](https://github.com/HomeHabbit/hog_haar_person_detection)

### Voice control/recognition
- **portaudio**, can be installed with `brew install portaudio` (mac) or `apt-get install portaudio19-dev`(linux)

## Basic installation

1. Clone into your catkin worskpace src folder (e.g: `~/catkin_ws/src`) by doing: `git clone https://github.com/HomeHabbit/Manager.git homehabit_manager`
2. go to catkin worskpace (e.g: `~/catkin_ws`) and run `catkin_make`

## Installation to use watson voice recognition

1. Clone into your catkin worskpace src folder (e.g: `~/catkin_ws/src`) by doing: `git clone https://github.com/HomeHabbit/Manager.git homehabit_manager`
2. Create an account on bluemix: https://console.ng.bluemix.net/ (this is free for 30 days)
3. Create an access on *speech to text* service from bluemix
4. Create an access on *text to speech* service from bluemix
5. Create an access on *dialogs* service from bluemix
6. Update the `config.sample.yml` with your credentials previously created on watson and rename it `config.yml`
7. run `pip install -r requirements.txt` inside `your_catkin_workspace/src/homehabit_manager`
8. go to catkin worskpace (e.g: `~/catkin_ws`) and run `catkin_make`

## Messages

Messages format are available in [/msg folder](/msg).

Messages list:

- Basic messages:
 - Topic `/homehabit/general_purpose_cmd` use [GeneralPurposeCmd.msg](/msg/GeneralPurposeCmd.msg), give informations to create interaction from multiple sources
- Watson messages:
 - Topic `/homehabit/watson_stt/payload` is a std_msgs.String, give a json about payload given by speech to text with watson
 - Topic `/homehabit/watson_stt/hypothesis/interim` is a std_msgs.String, give a json about interim hypothsesis given by speech to text with watson (interim hypothesis mean when your sentence is not finished)
 - Topic `/homehabit/watson_stt/hypothesis/final` is a std_msgs.String, give a json about final hypothsesis given by speech to text with watson (interim hypothesis mean when your sentence is finished)

## Usage:

To use face recognition from video stream:

- Follow tutorial from: face_recognition](http://wiki.ros.org/face_recognition)
- Run `rosrun homehabit_manager scripts/manage_face_recognition.py` 

To use voice control/recognition with watson:

- Run `rosrun homehabit_manager scripts/manage_dialog_watson.py` 

## Available sources:

- From camera stream by detecting peoples around the place
- From voice recognition using watson

