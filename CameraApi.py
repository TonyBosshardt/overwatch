from picamera import PiCamera
from time import sleep


ROOT_PATH = 'home/pi/overwatch/static'
STILL_PHOTO_SLEEP_TIME = 2


class TwilioCamera():
	
	@staticmethod
	def take_photo(image_name, image_format='jpg'):	
	
		constructed_path = '/{}/{}.{}'.format(ROOT_PATH, image_name, image_format)
		print('taking photo, saving to {}'.format(constructed_path))
		
		camera = PiCamera()

		camera.start_preview()
		sleep(STILL_PHOTO_SLEEP_TIME)
		camera.capture('/{}'.format(constructed_path))
		camera.stop_preview()
		camera.close()
		
		return constructed_path
