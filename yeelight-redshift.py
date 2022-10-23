import subprocess
from time import sleep

old_temp = 0

def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def display_temp():
    try:
        result = int(subprocess.run(["redshift", "-p"],capture_output=True).stdout.split()[-4])
    except:
        result = 6500
    return result

        
def lamp_temp(temp):
    global old_temp
    if old_temp !=temp:
        subprocess.run(["/home/pablo/yeelight-shell-scripts/yeelight-colortemp.sh", "0", str(temp)])
        old_temp = temp


while True:
    sleep(60)
    new_temp = map_range(display_temp(), 4500,6500,4000,5500)
    lamp_temp(new_temp)
