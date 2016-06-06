## mingyulovesunmin ##
######################
## dust_alert
######################
import pdairp

region = "영등포구 신길동"

### Get the tmX and tmY of nearest station ###
#stations = pdairp.StationInfo("gDbrBn8llIWjtyxuBOsXeV%2BZepaHh4hvBDAlxypLZaD%2FFavczDV69j9UJ0OvL%2FEKFGUa3TI6KuUjxEQ8wR8Stw%3D%3D")
#near_stations = stations.tmcode(region, page_no='1', num_of_rows='10') ## Get the locations of the stations near ROI
#print(near_stations)
# print(near_stations['totalCount'])
#tm_x = near_stations['1']['tmX']
#tm_y = near_stations['1']['tmY']
#print ("TM_X = %s, TM_Y = %s" %(tm_x, tm_y))  ## for debug
#print (stations.nearby(tm_x_1, tm_y_1, page_no='1', num_of_rows='10'))

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
#print (pollution_dat.station("영등포로", "DAILY", page_no='1', num_of_rows='2', ver='1.2')['0']) ## '0' : latest data
pm25_val = int(pollution_dat.station("영등포로", "DAILY", page_no='1', num_of_rows='2', ver='1.2')['0']['pm25Value']) ## '0' : latest data
pm10_val = int(pollution_dat.station("영등포로", "DAILY", page_no='1', num_of_rows='2', ver='1.2')['0']['pm10Value'])

pm10_grade = get_grade_pm10(pm10_val)
pm25_grade = get_grade_pm25(pm25_val)
print("현재 미세먼지 농도는 %d 이고, 등급은 %d 입니다." %(pm10_val, pm10_grade))
print("현재 초미세먼지 농도는 %d 이고, 등급은 %d 입니다." %(pm25_val, pm25_grade))