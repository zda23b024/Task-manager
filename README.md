# Flask API Projects

This repository contains **Two Flask-based APIs**:

1. **Student Information API** (`port 5002`) – Provides details of DSAI students.  
2. **Weather API** (`port 5001`) – Provides current weather and 3-day forecast for selected cities.

---

## Student Information API

**Endpoints:**

- **Get Student Details**
```http
GET /api/student?id=<roll_number>
````

* **Range of Roll_Num:** {ZDA23001, ZDA23002, ZDA23003, ZDA23004, ZDA23005}
* **API Example:**

```
http://127.0.0.1:5002/api/student?id=ZDA23001
```

* **Get Total Students**

```http
GET /api/students/count
```

* **API Example:**

```
http://127.0.0.1:5002/api/students/count
```

---

## Weather API

**Endpoints:**
* **Current Weather**

```http
GET /api/weather/current?city=<city_name>
```
* **Cities in List:** {Paris, Zanzibar, London, New-York, Tokyo}
* **API Example:**

```
http://127.0.0.1:5001/api/weather/current?city=Zanzibar
```
* **Weather Forecast**

```http
GET /api/weather/forecast?city=<city_name>&days=<number_of_days>
```

* **Maximum days:** 3
* **API Example:**

```
http://127.0.0.1:5001/api/weather/forecast?city=London&days=2
```
---
### Running
```bash
python weather_api.py   # Weather API
python student_api.py   # Student API
```
