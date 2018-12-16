# import time
# import autoit
#
# autoit.run("notepad.exe")
# time.sleep(2)
# autoit.win_activate("无标题 - 记事本")
# time.sleep(1000)
# autoit.send("{LSHIFT}")
# time.sleep(2)
# autoit.send("#Process finished with exit code 0.",1)
# time.sleep(2)
# autoit.win_close("无标题 - 记事本")
# autoit.win_activate("记事本")
# time.sleep(2)
# autoit.control_click("记事本","保存(&S)")
# time.sleep(2)
# autoit.win_activate("另存为")
# autoit.control_set_text("另存为","[CLASS:Edit; INSTANCE:1]","myTest.py")
# time.sleep(2)
# autoit.control_click("另存为","保存(&S)")

from datetime import datetime
t=datetime.now().strftime('%Y%m%d%H%M%S')
print(t)