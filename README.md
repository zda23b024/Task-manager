# Flask API Projects

This repository contains Two Flask-based APIs:

1. Student Information API (`port 5002`) – Provides details of DSAI students.
2. Weather API (`port 5001`) – Provides current weather and 3-day forecast for selected cities.

Student Information API

Endpoints:

* Get Student Details

```
GET /api/student?id=<roll_number>
```

Range of Roll_Num : {ZDA23001,ZDA23002,ZDA23003,ZDA23004,ZDA23005}
API:
```
http://127.0.0.1:5002/api/student?id=ZDA23001
```

* Get Total Students

```
GET /api/students/count
```
API:
```
http://127.0.0.1:5002/api/students/count
```

---

# Weather API
Endpoints:

* Current Weather

```
GET /api/weather/current?city=<city_name>
```

Cities in Lists : {Paris,zanzibar,London,New-york,Tokyo}
```
http://127.0.0.1:5001/api/weather/current?city=Zanzibar
```

* Weather Forecast
```
GET /api/weather/forecast?city=<city_name>&days=<number_of_days>
```

maximum day = 3 

```
http://127.0.0.1:5001/api/weather/forecast?city=London&days=2
```

### Running

```bash
python weather_api.py   # Weather API
python student_api.py   # Student API
```
