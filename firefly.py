# THis is the firefly class that wraps all the methods to be called on our firefly drone
import dronekit as dk
connection_string = '/dev/tty0'
class FireFly:
  
  def __init__():
    self.vehicle = connect(connection_string, wait_ready=True)
   
  def __del__():
    self.vehicle.close()
  
  def report():
    print('Hello, I am a firefly drone')
    print (f'My GPS location is{vehicle.gps_0}')
