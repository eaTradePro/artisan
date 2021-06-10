import prettytable
import re
from PyQt5.QtWidgets import QApplication

def content():
    strlist = []
    helpstr = ''  #@UnusedVariable
    newline = '\n'  #@UnusedVariable
    strlist.append('<head><style> td, th {border: 1px solid #ddd;  padding: 6px;} th {padding-top: 6px;padding-bottom: 6px;text-align: left;background-color: #0C6AA6; color: white;} </style></head> <body>')
    strlist.append("<b>")
    strlist.append(QApplication.translate('HelpDlg','EVENT CUSTOM SLIDERS',None))
    strlist.append("</b>")
    tbl_Sliders = prettytable.PrettyTable()
    tbl_Sliders.field_names = [QApplication.translate('HelpDlg','Column',None),QApplication.translate('HelpDlg','Description',None)]
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Event',None),QApplication.translate('HelpDlg','Hide or show the corresponding slider.',None)])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Action',None),QApplication.translate('HelpDlg','Perform an action on the slider release.',None)])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Command',None),QApplication.translate('HelpDlg','Command to perform, depends on the Action type. (&#39;{}&#39; is replaced by the slider value*Factor + Offset)',None)])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Offset',None),QApplication.translate('HelpDlg','Offset to be added to the Slider value (after scaling by Factor).',None)])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Factor',None),QApplication.translate('HelpDlg','Scale factor, Slider value is multplied by this value.',None)])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Min',None),QApplication.translate('HelpDlg','Sets the minimum value for the range of the slider.',None)])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Max',None),QApplication.translate('HelpDlg','Sets the maximum value for the range of the slider.',None)])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Course',None),QApplication.translate('HelpDlg','When ticked the slider moves in steps of 10.',None)])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Temp',None),QApplication.translate('HelpDlg','Should be ticked when the slider&#39;s value is a temperature to allow Artisan to properly scale the value between Centigrade and Fahrenheit.',None)])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Unit',None),QApplication.translate('HelpDlg','Optional text used in annotations to the the units used for the slider value.',None)])
    strlist.append(tbl_Sliders.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    strlist.append("<br/><br/><b>")
    strlist.append(QApplication.translate('HelpDlg','COMMANDS',None))
    strlist.append("</b>")
    tbl_Commandstop = prettytable.PrettyTable()
    tbl_Commandstop.header = False
    tbl_Commandstop.add_row([QApplication.translate('HelpDlg','Note: "{}" can be used as a placeholder, it will be subsituted by (value*factor + offset). In all slider command actions, but for IO, VOUT, S7 and RC Commands, the bound value is converted from a float to an int.\n',None)+newline+QApplication.translate('HelpDlg','Note: The placeholders {ET}, {BT}, {time}, {ETB}, {BTB} will be substituted by the current ET, BT, time, ET background or BT background value in Serial/CallProgram/MODBUS/S7/WebSocket commands',None)+newline+QApplication.translate('HelpDlg','Note: commands can be sequenced, separated by semicolons like in “<cmd1>;<cmd2>;<cmd3>”\n',None)+newline+QApplication.translate('HelpDlg','Note: in PHIDGET commands, the optional parameter <sn> has the form <hub_serial>[:<hub_port>] allows to refer to a specific Phidget HUB by given its serial number, and optionally specifying the port number the addressed module is connected to.\n',None)+newline+QApplication.translate('HelpDlg','Note: in YOCTOPUCE commands, the optional parameters <sn> holds either the modules serial number or its name',None)])
    strlist.append(tbl_Commandstop.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    tbl_Commands = prettytable.PrettyTable()
    tbl_Commands.field_names = [QApplication.translate('HelpDlg','Action',None),QApplication.translate('HelpDlg','Command',None),QApplication.translate('HelpDlg','Description',None)]
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Serial Command',None),QApplication.translate('HelpDlg','ASCII serial command or binary a2b_uu(serial command)',None),'&#160;'])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Modbus Command',None),QApplication.translate('HelpDlg','_',None),QApplication.translate('HelpDlg','variable holding the last value read via MODBUS',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','sleep(<float>)',None),QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','button(<bool>)',None),QApplication.translate('HelpDlg','sets calling button to “pressed” if argument is 1 or True',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','read(slaveID,register)',None),QApplication.translate('HelpDlg','reads register from slave slaveID using function 3 (Read Multiple Holding Registers). The result is bound to the placeholder `_` and thus can be accessed in later commands.',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','write(slaveId,register,value) or write([slaveId,register,value],..,[slaveId,register,value])',None),QApplication.translate('HelpDlg','write register: MODBUS function 6 (int) or function 16 (float)',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','wcoil(slaveId,register,<bool>)',None),QApplication.translate('HelpDlg','write coil: MODBUS function 5',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','wcoils(slaveId,register,[<bool>,..,<bool>])',None),QApplication.translate('HelpDlg','write coils: MODBUS function 15',None)])
    tbl_Commands.add_row([QApplication.translate('HelpDlg',' ',None),QApplication.translate('HelpDlg','mwrite(slaveId,register,andMask,orMask) or mwrite(s,r,am,om,v)',None),QApplication.translate('HelpDlg','mask write register: MODBUS function 22 or simulates function 22 with function 6 and the given value v',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','writem(slaveId,register,value) or writem(slaveId,register,[<int>,..,<int>])',None),QApplication.translate('HelpDlg','write registers: MODBUS function 16',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','writeBCD(s,r,v) or writeBCD([s,r,v],..,[s,r,v])',None),QApplication.translate('HelpDlg','write 16bit BCD encoded value v to register r of slave s ',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','writeWord(slaveId,register,value) or writeWord([slaveId,register,value],..,[slaveId,register,value])',None),QApplication.translate('HelpDlg','write 32bit float to two 16bit int registers: MODBUS function 16',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','writeSingle(slaveId,register,value) or writeSingle([slaveId,register,value],..,[slaveId,register,value])',None),QApplication.translate('HelpDlg','write 16bit integer to a single 16bit register: MODBUS function 6 (int)',None)])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','DTA Command',None),QApplication.translate('HelpDlg','Insert Data address : value, ex. 4701:1000 and sv is 100. ',None),QApplication.translate('HelpDlg','Always multiply with 10 if value Unit: 0.1 / ex. 4719:0 stops heating',None)])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Call Program',None),QApplication.translate('HelpDlg','A program/script path (absolute or relative)',None),QApplication.translate('HelpDlg','start and external program',None)])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Hottop Heater',None),'&#160;',QApplication.translate('HelpDlg','sets heater to value',None)])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Hottop Fan',None),'&#160;',QApplication.translate('HelpDlg','sets fan to value',None)])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Hottop Command',None),QApplication.translate('HelpDlg','motor(n),solenoid(n),stirrer(n),heater(h),fan(f) ',None),QApplication.translate('HelpDlg','with n={0 ,1},h={0,..100},f={0,..10}',None)])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Fuji Command',None),QApplication.translate('HelpDlg','write(<unitId>,<register>,<value>)',None),'&#160;'])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','PWM Command',None),QApplication.translate('HelpDlg','out(<channel>,<value>[,<sn>])',None),QApplication.translate('HelpDlg','PHIDGET PWM Output: <value> in [0-100]',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','toggle(<channel>[,<sn>])',None),QApplication.translate('HelpDlg','PHIDGET PWM Output: toggles <channel>',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','pulse(<channel>,<millis>[,<sn>])',None),QApplication.translate('HelpDlg','PHIDGET PWM Output: turn <channel> on for <millis> milliseconds',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','outhub(<channel>,<value>[,<sn>])',None),QApplication.translate('HelpDlg','PHIDGET HUB PWM Output: <value> in [0-100]',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','togglehub(<channel>[,<sn>])',None),QApplication.translate('HelpDlg','PHIDGET HUB PWM Output: toggles <channel>',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','pulsehub(<channel>,<millis>[,<sn>])',None),QApplication.translate('HelpDlg','PHIDGET HUB PWM Output:  turn <channel> on for <millis> milliseconds',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','enabled(c,b[,sn])',None),QApplication.translate('HelpDlg','YOCTOPUCE PWM Output: PWM running state',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','freq(c,f[,sn])',None),QApplication.translate('HelpDlg','YOCTOPUCE PWM Output: set PWM frequency to f (Hz)',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','duty(c,d[,sn])',None),QApplication.translate('HelpDlg','YOCTOPUCE PWM Output: set PWM period with the duty cycle in % as a float [0.0-100.0]',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','move(c,d,t[,sn])',None),QApplication.translate('HelpDlg','YOCTOPUCE PWM Output: changes progressively the PWM to the specified value over the given time interval',None)])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','VOUT Command',None),QApplication.translate('HelpDlg','range(c,r[,sn])',None),QApplication.translate('HelpDlg','for PHIDGET OUTPUT modules: sets voltage voltage range (r=5 fo r5V and r=10 for 10V)',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','out(n,v[,sn])',None),QApplication.translate('HelpDlg','for PHIDGET OUTPUT modules: set analog output channel n to output voltage value v in V (eg. 5.5 for 5.5V)',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','vout(c,v[,sn])',None),QApplication.translate('HelpDlg','for YOCTOPUCE VOLTAGE OUT modules with c the channel (1 or 2),v the voltage as float [0.0-10.0]',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','cout(c[,sn])',None),QApplication.translate('HelpDlg','for YOCTOPUCE CURRENT OUT modules with c the current as float [3.0-21.0]',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','sleep(<float>)',None),QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds',None)])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','IO Command',None),QApplication.translate('HelpDlg','set(c,b[,sn])',None),QApplication.translate('HelpDlg','PHIDGET Binary Output: switches channel c off (b=0) and on (b=1)',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','toggle(c[,sn])',None),QApplication.translate('HelpDlg','PHIDGET Binary Output: toggles channel c',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','pulse(c,t[,sn])',None),QApplication.translate('HelpDlg','PHIDGET Binary Output: sets the output of channel c to on for time t in milliseconds',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','out(c,v[,sn])',None),QApplication.translate('HelpDlg','PHIDGET Voltage Output: sets voltage output of channel c to v (float)',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','accel(c,v[,sn])',None),QApplication.translate('HelpDlg','PHIDGET DCMotor: sets acceleration of channel c to v (float)',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','vel(c,v[,sn])',None),QApplication.translate('HelpDlg','PHIDGET DCMotor: sets target velocity of channel c to v (float)',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','on(c[,sn])',None),QApplication.translate('HelpDlg','YOCTOPUCE Relay Output: turn channel c of the relay module on',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','off(c[,sn])',None),QApplication.translate('HelpDlg','YOCTOPUCE Relay Output: turn channel c of the relay module off',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','flip(c[,sn])',None),QApplication.translate('HelpDlg','YOCTOPUCE Relay Output: toggle the state of channel c',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','pip(c,delay,duration[,sn])',None),QApplication.translate('HelpDlg','YOCTOPUCE Relay Output: pulse the channel c on after a delay of delay milliseconds for the duration of duration milliseconds',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','slider(c,v)',None),QApplication.translate('HelpDlg','move slider c to value v',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','button(i,c,b[,sn])',None),QApplication.translate('HelpDlg','switches channel c off (b=0) and on (b=1) and sets button i to pressed or normal depending on the value b',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','sleep(<float>)',None),QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds',None)])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','S7 Command',None),QApplication.translate('HelpDlg','_',None),QApplication.translate('HelpDlg','variable holding the last value read via S7',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','sleep(<float>)',None),QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','button(<bool>)',None),QApplication.translate('HelpDlg','sets calling button to “pressed” if argument evaluates to 1 or True',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','getDBbool(<dbnumber>,<start>,<index>)',None),QApplication.translate('HelpDlg','read bool from S7 DB',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','getDBint(<dbnumber>,<start>)',None),QApplication.translate('HelpDlg','read int from S7 DB',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','getDBfloat(<dbnumber>,<start>)',None),QApplication.translate('HelpDlg','read float from S7 DB',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','setDBbool(<dbnumber>,<start>,<index>,<value>)',None),QApplication.translate('HelpDlg','write bool to S7 DB',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','setDBint(<dbnumber>,<start>,<value>)',None),QApplication.translate('HelpDlg','write int to S7 DB',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','setDBfloat(<dbnumber>,<start>,<value>)',None),QApplication.translate('HelpDlg','write float to S7 DB',None)])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Aillio R1 Heater',None),'&#160;',QApplication.translate('HelpDlg','sets heater to value',None)])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Aillio R1 Fan',None),'&#160;',QApplication.translate('HelpDlg','sets fan to value',None)])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Aillio R1 Drum',None),'&#160;',QApplication.translate('HelpDlg','sets drum speed to value',None)])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Artisan Command',None),QApplication.translate('HelpDlg','alarms(<bool>)',None),QApplication.translate('HelpDlg','enables/disables alarms',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','autoCHARGE(<bool>)',None),QApplication.translate('HelpDlg','enables/disables autoCHARGE',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','autoDROP(<bool>)',None),QApplication.translate('HelpDlg','enables/disables autoDROP',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','sleep(<float>)',None),QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','tare(<int>)',None),QApplication.translate('HelpDlg','tare channel <int> with 1 => ET, 2 => BT, 3 => E1c1, 4: E1c2,..',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','PIDon',None),QApplication.translate('HelpDlg','turns PID on',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','PIDoff',None),QApplication.translate('HelpDlg','turns PID off',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','PIDtoggle',None),QApplication.translate('HelpDlg','toggles the PID state',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','pidmode(<int>)',None),QApplication.translate('HelpDlg','sets PID mode to 0: manual, 1: RS, 2: background follow',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','p-i-d(<p>,<i>,<d>)',None),QApplication.translate('HelpDlg','sets the p-i-d parameters of the PID',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','adjustSV(<int>)',None),QApplication.translate('HelpDlg','increases or decreases the current target SV value by <int>',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','pidSV(<int>)',None),QApplication.translate('HelpDlg','sets the PID target set value SV',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','pidRS(<rs>)',None),QApplication.translate('HelpDlg','activates the PID Ramp-Soak pattern number <rs> (1-based!) or the one labeled <rs>',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','pidSource(<int>)',None),QApplication.translate('HelpDlg','selects the PID input source with <n> 0: BT, 1: ET (Software PID); <n> in {0,..,3} (Arduino PID)',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','pidLookahead(<int>)',None),QApplication.translate('HelpDlg','sets the PID lookahead',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','popup(<msg>[,<int>])',None),QApplication.translate('HelpDlg','shows popup with message <msg> which optionally automatically closes after <int> seconds',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','message(<msg>)',None),QApplication.translate('HelpDlg','shows message <msg> in the message line',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','setCanvasColor(<color>)',None),QApplication.translate('HelpDlg','sets canvas color to the RGB-hex <color> like #27f1d3',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','resetCanvasColor',None),QApplication.translate('HelpDlg','resets canvas color',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','button(<name>)',None),QApplication.translate('HelpDlg','activates button <name> from { START, CHARGE, DRY, FCs, FCe, SCs, SCe, DROP, COOL, OFF } ',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','palette(<p>)',None),QApplication.translate('HelpDlg','activates palette <p> with <p> either a number 0-9 or a palette label',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','playbackmode(<int>)',None),QApplication.translate('HelpDlg','sets playback mode to 0: off, 1: time, 2: BT, 3: ET',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','openProperties',None),QApplication.translate('HelpDlg','opens the Roast Properties dialog',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','loadBackground(<filepath>)',None),QApplication.translate('HelpDlg','loads the .alog profile at the given filepath as background profile',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','clearBackground',None),QApplication.translate('HelpDlg','clears the current background profile',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','alarmset(<as>)',None),QApplication.translate('HelpDlg','activates the alarmset with the given number or label',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','moveBackground(<direction>,<int>)',None),QApplication.translate('HelpDlg','moves the background profile the indicated number of steps towards <direction>, with <direction> one of up, down, left, right',None)])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','RC Command',None),QApplication.translate('HelpDlg','pulse(ch,min,max[,sn])',None),QApplication.translate('HelpDlg','for PHIDGET RC modules: sets the min/max pulse width in microseconds',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','pos(ch,min,max[,sn])',None),QApplication.translate('HelpDlg','for PHIDGET RC modules: sets the min/max position',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','engaged(ch,b[,sn])',None),QApplication.translate('HelpDlg','for PHIDGET RC modules: engage (b=1) or disengage (b = 0)',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','ramp(ch,b[,sn])',None),QApplication.translate('HelpDlg','for PHIDGET RC modules: activates or deactivates the speed ramping state',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','volt(ch,v[,sn])',None),QApplication.translate('HelpDlg','for PHIDGET RC modules: set the voltage to one of 5, 6 or 7.4 in Volt',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','accel(ch,a[,sn])',None),QApplication.translate('HelpDlg','for PHIDGET RC modules: set the acceleration',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','veloc(ch,v[,sn])',None),QApplication.translate('HelpDlg','for PHIDGET RC modules: set the velocity',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','set(ch,pos[,sn])',None),QApplication.translate('HelpDlg','for PHIDGET RC modules: set the target position',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','enabled(c,b[,sn])',None),QApplication.translate('HelpDlg','for YOCTOPUCE RC modules: with c:int the channel, b a bool (eg. enabled(0,1) or enabled(0,True))',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','move(c,p[,t][,sn])',None),QApplication.translate('HelpDlg','for YOCTOPUCE RC modules: with c:int the channel, p:int the target position, the optional t the duration in ms',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','neutral(c,n[,sn])',None),QApplication.translate('HelpDlg','for YOCTOPUCE RC modules: with n an int [0..65000] in us',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','range(c,r[,sn])',None),QApplication.translate('HelpDlg','for YOCTOPUCE RC modules: with r an int in %',None)])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','WebSocket Command',None),QApplication.translate('HelpDlg','send(<json>)',None),QApplication.translate('HelpDlg','If {} substitutions are used, json brackets need to be duplicated to escape them like in send({{ “value”: {}}})',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','sleep(<float>)',None),QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','button(<bool>)',None),QApplication.translate('HelpDlg','sets calling button to “pressed” if argument evaluates to 1 or True',None)])
    tbl_Commands.add_row(['&#160;',QApplication.translate('HelpDlg','read(<json>)',None),QApplication.translate('HelpDlg','if the `<json>` text respects the JSON format it is send to the connected WebSocket server and the response is bound to the variable `_`',None)])
    strlist.append(tbl_Commands.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    strlist.append("</body>")
    helpstr = "".join(strlist)
    helpstr = re.sub(r"&amp;", r"&",helpstr)
    return helpstr