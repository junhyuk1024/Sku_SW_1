import time
import math

class GPS: #GPS 모듈
    def get_current_location(self):
        # 임의의 현재 위치 (위도, 경도)
        return (37.5665, 126.9780)  # 서울시청 위도 경도도

class MapService: #지도 서비스스
    def calculate_route(self, start, destination):
        # 두 지점 간의 거리 계산
        distance = math.sqrt((destination[0] - start[0])**2 + (destination[1] - start[1])**2)
        steps = 5 # 경로의 포인트 구간
        route = []
        for i in range(1, steps + 1):
            lat = start[0] + (destination[0] - start[0]) * i / steps #위도
            lon = start[1] + (destination[1] - start[1]) * i / steps #경도도
            route.append((lat, lon))
        return route

class NavigationSystem: # 네비게이션 시스템템
    def __init__(self):
        self.gps = GPS()
        self.map_service = MapService()

    def start_navigation(self, destination):
        print("📍 현재 위치 확인 중...")
        current_location = self.gps.get_current_location()
        print(f"현재 위치: {current_location}")

        print("🗺️ 경로 계산 중...")
        route = self.map_service.calculate_route(current_location, destination)
        print("경로 안내 시작!\n")

        for i, point in enumerate(route):
            print(f"➡️ {i+1}단계: 다음 지점으로 이동 중... {point}")
            time.sleep(1)

        print("\n🎉 목적지에 도착했습니다!")

def get_destination_from_user(): #사용자 인터페이스
    print("🚗 목적지를 입력하세요.")
    lat = float(input("목적지 위도: "))
    lon = float(input("목적지 경도: "))
    return (lat, lon)

if __name__ == "__main__":
    nav_system = NavigationSystem()
    destination = get_destination_from_user()
    nav_system.start_navigation(destination)
