import os
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')
import datetime

from flask import Flask, request, url_for, current_app
from twilio.twiml.messaging_response import MessagingResponse
from CameraApi import TwilioCamera

# define flask app
app = Flask(__name__)

current_time = datetime.datetime.now().isoformat()


image_name = 'default_photo_name'

@app.route("/sms", methods=['POST', 'GET'])
def handle_reply():
	''' main sms reply handler '''
	body = request.values.get('Body', None)
	from_number = request.values.get('From', None)
	    
	resp = MessagingResponse()
	
	print('Message from {}: {}'.format(from_number, body))
	msg = resp.message('\n ... sent from my Pi')
	
	if 'photo' in body.lower():
		print('taking a photo ...')
		image_path = TwilioCamera.take_photo(image_name)
		print('retrieving image from {}'.format(image_path))
		msg.media(url_for('static', filename='default_photo_name.jpg'))
		
	return str(resp)
	
	
@app.route("/debug", methods=['GET'])
def debug_route():
	''' simple route to assure server is running '''
	#return 'Bringo! If you see this the server is running!'
	return current_app.send_static_file('index.html')
	
	
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

