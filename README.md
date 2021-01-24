


# smartcity_eg  
### 부산 스마트시티 - 라즈베리 파이를 이용한 (RPi 4) 이더넷 게이트웨이 구현.  
***  
### 실행 설명  
**디렉토리(라즈베리파이 내부)** 
/home/pi/servers/smartcity_eg/

### 실행
 1. start.sh [SITEID] [SIGNALID]  
 2. process_check_ever.sh [SITEID]
    [SIGNALID]
    
#### 사용법(실행)     
 1. 크론탭 생성(crontab -e) 후    
 2. @reboot sleep 60; bash /home/pi/servers/smartcity_eg/process_check_ever.sh [SITEID] [SIGNALID]  
  
### 중지
1. stop.sh   
#### 사용법(중지)  
cmd에서 stop.sh 실행 (bash /home/pi/servers/smartcity_eg/stop.sh)  

### 로그 파일  
* log.py : 로그 포맷 지정 파일  
* del_log.sh : 생성된 지 30일이 지난 로그 파일 삭제  
* zip_log.sh : 생성된 지 10일이 지난 로그 파일 압축(10개의 파일 압축)  

### 모니터링
* ssh 접속을 위해서는 vpn 연결이 선행되어야 함. (icent 에서 지급한 vpn 사용. )

**![](https://lh4.googleusercontent.com/_3BtOtDd5Wu9SMNwMvX4v5vwHTYcY0YkekhPCT7HxOSsnrZ7b0qDK5Pb-9qgxFoCTbDKs_ez9RtxzUICa2jNblXEvj6gYPPsTMUf98NxBCbnOIK1z2xfjkucR0OervoruSgh9WN3)**
1. ssh 접속 (eg-02, eg-06 제외한 eg-01 ~ eg-16 각각 매칭되는 ip 입력.)
2. 프로세스 체크 --> alias 로 pspy 저장되어 있음
3. 프로세스 체크 --> ps -ef | grep process_check_ever
4. 로그 체크 --> tail -10f eg.log

**![](https://lh3.googleusercontent.com/vtBu8loMkWPQ2koEYMe9PaKOBy3m4WgrVpbeva2X_FaQKtp-KOpoa7SLqGOh70blEvLPGhchKA3cOTr1b90ItT2nFYfRQm_o9zbIeQ1vH9P5XkO2yPBekaL0Q65nJdD0I12sJPj8)**
***  
### 코드 별 구현 기능  
* **start.sh**: 2개의 인수를 받아 이더넷 게이트웨이 기능(start_gateway.py) 시작.
	(ex.  start.sh [SITEID] [SIGNALID])
* **stop.sh**: start_gateway.py 기능 중지.
	(ex.  ./stop.sh)
* **process_check_ever.sh**:start_gateway.py가 돌고 있는지 1초마다 체크하면서 만약 프로세스 종료 시 자동으로 재시작.
	(ex. ./process_check_ever.sh [SITEID] [SIGNALID])
* **encode.py**: json 데이타를 m00ff00ff(m+hex4자리+hex4자리) 로 인코딩  
* **publish.py**: json 데이타 publish 코드(임시 서버역할)  
* **senduart.py**: uart 통신으로 비콘에 정보(eg. m00ff00ff\r\n ) 전달  
* **start_gateway.py**: 인수를 받아 게이트웨이 기능 진행.  
	(ex. start_gateway.py [siteId] [signalId])  
* **subs.py**: mqtt 프로토콜 이용하여 데이터 subscribe 한 데이터(JSON) 넘겨줌
* **eg.yaml**: isaver 서버 정보, uart 통신(라즈베리파이<->비콘) 관련 정보, log 관련 정보, iot endpoint 에 대한 정보

***
### AWS CloudWatch 로 로그 확인하기
1. AWS 클라우드워치 로그인 (authy 인증 필요.)
2. 로그 그룹 클릭
3. /SmartCity/home/pi/servers/smartcity_eg/logs 검색
4. 로그 스트림 확인

**![](https://lh4.googleusercontent.com/f6tbdcFhW55IZtbnNRz2Y-Wx_8jN3jQZuu-8v-6qVMWzguSVRkPsHSHmXFPA6zSpvLFI9bdksWhCX44av670RiU3xYHUWsGb5JLEU3d5fTJl6OsV5X9mEMqG2CtsBS9H7Doos-3C)**
**![](https://lh3.googleusercontent.com/NfXISlPcMvc9pinyoqyJYmNClPDk9BB9mTFs4yVz3TdgN2NTL9QVowdGJVLzJlqjB4IFAJXDIKrCHtYN9LOvdDvsFD2T_kvOXMbwhO8InkAJxryq78ICRsuUiV8k7Lq2artvqzQI)**

***

### AWS SSM 활용하여 여러대의 기기의 코드수정 하기
1. AWS SSM 로그인
2. Run Command 클릭
3. 명령 기록 확인
4. 명령 클릭 후 copy to new
5. run command 실행

**![](https://lh6.googleusercontent.com/gx36jEdwkGA7QNmffNqQBEwWsENl9VKJwWVSlEP5rc_9zu66RmkG4kXG8nkbO0oJBkDtvQTbqHo83RdwFingxTPgkj122Pa85dlnuScfJ0yAD5RjeBy12LE_rcIbYHyYXdpcLkub)**

# algorithm
