# Sku_SW_1
개인과제1

샘플코드 : Navigation_system

시퀀스 다이어그램 : sequenceDiagram


자동차 네비게이션 소프트웨어 사용 사례를 가지고 시퀀스 다이어그램 작성/샘플 코드 작성을 하였습니다.

시퀀스 다이어그램에서의 개체와 매칭되는 샘플코드의 클래스와 함수에 주석을 달아두었습니다.


모듈평가

GPS 모듈 , 네비게이션 시스템모듈 , 지도 서비스모듈 , 사용자 인터페이스모듈


응집도 평가

1.GPS 모듈 - 현재 위치를 반환해주는 기능만을 수행합니다.

2.지도 서비스 모듈 - 현재 위치에서 목적지까지의 거리를 계산해주는 기능만을 수행합니다.

3.네비게이션 시스템 모듈 - 음성 및 시각 안내의 기능만을 수행합니다.

4.사용자 인터페이스 모듈 - 사용자에게 인터페이스를 제공하는 기능만을 수행합니다.

=> 네가지 모듈들이 하나의 책임만을 맡고 있기에 응집도가 높다고 평가할 수 있습니다.


결합도 평가

네비게이션 시스템모듈 -> GPS 모듈 / 네비게이션 시스템모듈 -> 지도 서비스모듈

=> 두가지 경우 모두 '클래스 객체 전달'을 하고 있으므로 스탬프 결합도에 해당합니다. 결합도가 낮다고 평가할 수 있습니다.
