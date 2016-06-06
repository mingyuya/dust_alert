## mingyulovesunmin ##
######################
## dust_alert
######################
import pdairp


region = "영등포구 신길동"

def get_near_station():
	stations = pdairp.StationInfo("gDbrBn8llIWjtyxuBOsXeV%2BZepaHh4hvBDAlxypLZaD%2FFavczDV69j9UJ0OvL%2FEKFGUa3TI6KuUjxEQ8wR8Stw%3D%3D")
	totalCount = 0

	while totalCount == 0 :
		region = input("관측 위치를 입력하세요. (예: 영등포구 신길동) : ")
		near_stations = stations.tmcode (region, page_no='1', num_of_rows='10') ## Get the locations of the stations near ROI
		totalCount = int(near_stations['totalCount'])
		if totalCount == 0 :
			print ("입력하신 위치에서 관측소가 발견되지 않았습니다.")
		else :
			tm_x = near_stations['0']['tmX']
			tm_y = near_stations['0']['tmY']
	
	#print ("가장 근접한 관측소의 이름은 <"+stations.nearby(tm_x, tm_y, page_no='1', num_of_rows='10')['0']['stationName']+"> 입니다.")
	nearest = stations.nearby(tm_x, tm_y, page_no='1', num_of_rows='10')['0']['stationName']

	return nearest

def get_grade_pm10 (pm10_val):
	## PM10 Grade
	## 0 ~ 30 : Good / 31 ~ 80 : Normal / 81 ~ 150 : Bad / 151 ~ : Danger
	if pm10_val < 31 :
		return 1
	elif pm10_val > 30 and pm10_val < 81 :
		return 2
	elif pm10_val > 80 and pm10_val < 151 :
		return 3
	else:
		return 4

def get_grade_pm25 (pm25_val):
	## PM2.5 Grade
	## 0 ~  15 : Good / 16 ~ 50 : Normal / 51 ~ 100 : Bad / 101 ~ : Danger
	if pm25_val < 31 :
		return 1
	elif pm25_val > 30 and pm25_val < 81 :
		return 2
	elif pm25_val > 80 and pm25_val < 151 :
		return 3
	else:
		return 4

pollution_dat = pdairp.PollutionData("gDbrBn8llIWjtyxuBOsXeV%2BZepaHh4hvBDAlxypLZaD%2FFavczDV69j9UJ0OvL%2FEKFGUa3TI6KuUjxEQ8wR8Stw%3D%3D")
## debug
#-print (pollution_dat.station("영등포로", "DAILY", page_no='1', num_of_rows='2', ver='1.2')['0']) ## '0' : latest data
##pm25_val = int(pollution_dat.station("영등포로", "DAILY", page_no='1', num_of_rows='2', ver='1.2')['0']['pm25Value']) ## '0' : latest data
##pm10_val = int(pollution_dat.station("영등포로", "DAILY", page_no='1', num_of_rows='2', ver='1.2')['0']['pm10Value'])
##pm25_grade = get_grade_pm25(pm25_val)
##pm10_grade = get_grade_pm10(pm10_val)

## debug
#-print("현재 미세먼지 농도는 %d 이고, 등급은 %d 입니다." %(pm10_val, pm10_grade))
#-print("현재 초미세먼지 농도는 %d 이고, 등급은 %d 입니다." %(pm25_val, pm25_grade))

get_near_station()