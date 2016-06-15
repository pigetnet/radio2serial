| /do/radio2serial/check   |                                                       |
|:-------------------------|:------------------------------------------------------|
| Info                     | [beta] [radio] [433Mhz] [python]                      |
| Description              | Start radio2serial server in non-daemon mode          |
| Usage                    | /do/radio2serial/check                                |
| Modules                  | exec python -u /do/radio2serial/python/serialjson.py, |

| /do/radio2serial/install                                |                                                                                                                                                                                                                          |
|:--------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                                                    | [beta] [radio] [433Mhz] [arduino]                                                                                                                                                                                        |
| Description                                             | Install radio2serial                                                                                                                                                                                                     |
| Usage                                                   | /do/radio2serial/install                                                                                                                                                                                                 |
| Softwares                                               | supervisor,                                                                                                                                                                                                              |
| Modules                                                 | cp /do/radio2serial/conf/port /user/config/radio2serial, cp /do/radio2serial/conf/radio2serial.json /user/config/radio2serial, cp /do/radio2serial/conf/getRadio /user/scripts/getRadio, command=/do/radio2serial/check, |
| System                                                  | /system/makedir /user/config/radio2serial, /system/install supervisor,                                                                                                                                                   |
| 2. Type /do/radio2serial/uploadNano to setup an arduino |                                                                                                                                                                                                                          |

| /do/radio2serial/killSocket   |                                             |
|:------------------------------|:--------------------------------------------|
| Info                          | [beta] [radio] [433Mhz] [socket] [warning]  |
| Description                   | Kill radio socket                           |
| Usage                         | /do/radio2serial/killSocket                 |
| Variables                     | port=$(cat /user/config/radio2serial/port), |

| /do/radio2serial/listen   |                                             |
|:--------------------------|:--------------------------------------------|
| Info                      | [beta] [radio] [433Mhz] [socket]            |
| Description               | Listen until a radio message is received    |
| Usage                     | /do/radio2serial/listen                     |
| Variables                 | port=$(cat /user/config/radio2serial/port), |

| /do/radio2serial/log      |                                            |
|:--------------------------|:-------------------------------------------|
| Info                      | [beta] [radio] [433Mhz] [log] [supervisor] |
| Description               | Display radio2serial log                   |
| Usage                     | /do/radio2serial/log                       |
| 1. radio Status           |                                            |
| 1. PRESS [CTRL-C] to quit |                                            |
| 2. Supervisor status      |                                            |
| 2. radio log              |                                            |

| /do/radio2serial/restart   |                                               |
|:---------------------------|:----------------------------------------------|
| Info                       | [beta] [radio] [433Mhz] [serial] [supervisor] |
| Description                | Restart radio2serial                          |
| Usage                      | /do/radio2serial/restart                      |

| /do/radio2serial/send   |                                             |
|:------------------------|:--------------------------------------------|
| Info                    | [beta] [socket] [serial] [radio] [433Mhz]   |
| Description             | Send radiomessage using socket              |
| Usage                   | /do/radio2serial/send radiomessage          |
| Example                 | /radio/text/hello world                     |
| Variables               | port=$(cat /user/config/radio2serial/port), |

| /do/radio2serial/sendText   |                                                                                                                                    |
|:----------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| Info                        | [beta] [socket] [serial] [radio] [433Mhz] [string_manipulation] [iconv]                                                            |
| Description                 | Send text with radio using socket                                                                                                  |
| Usage                       | /do/radio2serial/sendText text                                                                                                     |
| Example                     | /do/radio2serial/sendText \You can type long text with strange accent\                                                             |
| Variables                   | string=$(echo $1 | iconv -f utf-8 -t us-ascii//TRANSLIT), len=${#string}, tmp=${string:0:59}, string=${string:59}, len=${#string}, |
| Modules                     | /do/radio2serial/send "/radio/text/$tmp", /do/radio2serial/send "/radio/text/$string",                                             |

| /do/radio2serial/settings   |                                   |
|:----------------------------|:----------------------------------|
| Info                        | [beta] [json] [serial] [nano]     |
| Description                 | Modify radio2serial configuration |
| Usage                       | /do/radio2serial/settings         |

| /do/radio2serial/start   |                                               |
|:-------------------------|:----------------------------------------------|
| Info                     | [beta] [radio] [433Mhz] [serial] [supervisor] |
| Description              | Start radio2serial                            |
| Usage                    | /do/radio2serial/start                        |

| /do/radio2serial/state   |                                                                                                                               |
|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| Info                     | [beta] [radio] [433Mhz] [serial] [socket] [arduino]                                                                           |
| Description              | Get arduino state                                                                                                             |
| Usage                    | /do/radio2serial/state                                                                                                        |
| Variables                | message=$("/do/radio2serial/listen"),                                                                                         |
| Modules                  | /do/radio2serial/send "/info", message=$("/do/radio2serial/listen"), python /do/radio2serial/python/radio2text.py "$message", |

| /do/radio2serial/stop   |                                               |
|:------------------------|:----------------------------------------------|
| Info                    | [beta] [radio] [433Mhz] [serial] [supervisor] |
| Description             | Stop radio2serial                             |
| Usage                   | /do/radio2serial/stop                         |

| /do/radio2serial/update   |                                                                                                                   |
|:--------------------------|:------------------------------------------------------------------------------------------------------------------|
| Info                      | [alpha] [git] [platformio] [arduino] [warning]                                                                    |
| Description               | Update radio2serial server and arduino                                                                            |
| Usage                     | /do/radio2serial/update                                                                                           |
| Modules                   | /do/radio2serial/stop, cd /do/radio2serial;git pull, /do/platformio/runNano radio2serial, /do/radio2serial/start, |

| /do/radio2serial/uploadNano   |                                                                                                                                                          |
|:------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                          | [alpha] [git] [platformio] [arduino] [warning]                                                                                                           |
| Description                   | Download and upload radio2serial server and arduino                                                                                                      |
| Usage                         | /do/radio2serial/uploadNano                                                                                                                              |
| Modules                       | /do/radio2serial/stop, if [ -d /do/platformio ];then, /do/platformio/download radio2serial, /do/platformio/runNano radio2serial, /do/radio2serial/start, |

