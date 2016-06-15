| /do/radio2serial/check   |                                                       |
|:-------------------------|:------------------------------------------------------|
| Info                     | [alpha] [undocumented]                                |
| Modules                  | exec python -u /do/radio2serial/python/serialjson.py, |

| /do/radio2serial/install   |                                 |
|:---------------------------|:--------------------------------|
| Info                       | [alpha] [undocumented]          |
| Softwares                  | supervisor,                     |
| Modules                    | command=/do/radio2serial/check, |
| System                     | /system/install supervisor,     |

| /do/radio2serial/killSocket   |                                             |
|:------------------------------|:--------------------------------------------|
| Info                          | [alpha] [undocumented]                      |
| Variables                     | port=$(cat /user/config/radio2serial/port), |

| /do/radio2serial/listen   |                                             |
|:--------------------------|:--------------------------------------------|
| Info                      | [alpha] [undocumented]                      |
| Variables                 | port=$(cat /user/config/radio2serial/port), |

| /do/radio2serial/log      |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |
| 1. radio Status           |                        |
| 1. PRESS [CTRL-C] to quit |                        |
| 2. Supervisor status      |                        |
| 2. radio log              |                        |

| /do/radio2serial/restart   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |

| /do/radio2serial/send   |                                             |
|:------------------------|:--------------------------------------------|
| Info                    | [alpha] [undocumented]                      |
| Variables               | port=$(cat /user/config/radio2serial/port), |

| /do/radio2serial/sendText   |                                                                                                                                    |
|:----------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| Info                        | [alpha] [undocumented]                                                                                                             |
| Variables                   | string=$(echo $1 | iconv -f utf-8 -t us-ascii//TRANSLIT), len=${#string}, tmp=${string:0:59}, string=${string:59}, len=${#string}, |
| Modules                     | /do/radio2serial/send "/radio/text/$tmp", /do/radio2serial/send "/radio/text/$string",                                             |

| /do/radio2serial/settings   |                        |
|:----------------------------|:-----------------------|
| Info                        | [alpha] [undocumented] |

| /do/radio2serial/start   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |

| /do/radio2serial/state   |                                                                                                                               |
|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| Info                     | [alpha] [undocumented]                                                                                                        |
| Variables                | message=$("/do/radio2serial/listen"),                                                                                         |
| Modules                  | /do/radio2serial/send "/info", message=$("/do/radio2serial/listen"), python /do/radio2serial/python/radio2text.py "$message", |

| /do/radio2serial/stop   |                        |
|:------------------------|:-----------------------|
| Info                    | [alpha] [undocumented] |

| /do/radio2serial/update   |                               |
|:--------------------------|:------------------------------|
| Info                      | [alpha] [undocumented]        |
| Modules                   | cd /do/radio2serial;git pull, |

| /do/radio2serial/uploadNano   |                                                                                                                           |
|:------------------------------|:--------------------------------------------------------------------------------------------------------------------------|
| Info                          | [alpha] [undocumented]                                                                                                    |
| Modules                       | /do/radio2serial/stop, /do/platformio/download radio2serial, /do/platformio/runNano radio2serial, /do/radio2serial/start, |

