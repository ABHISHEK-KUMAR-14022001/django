https://pypi.org/project/uv/
https://pypi.org/project/uv/0.1.39/

python -m venv .venv
or 
uv venv

.venv\Scripts\activate
uv pip install Django
django-admin startproject chaiaurDjango
python manage.py runserver

![alt text](image.png)
![alt text](image-2.png)
![alt text](image-1.png)

python --version
pip --version
uv --version


Use venv Instead of pipenv (Recommended for Simplicity)

cd ~/Desktop/python
python -m venv .venv
source myenv/Scripts/activate  # On Git Bash
pip install django

django-admin startproject storefront .




Running MongoDB on Docker and Connecting to Django
Step 1: Run MongoDB in Docker
docker run -d \
 --name mongodb \
 -p 27017:27017 \
 -e MONGO_INITDB_ROOT_USERNAME=admin \
 -e MONGO_INITDB_ROOT_PASSWORD=adminpassword \
 mongo

Explanation:
- -d: Run in detached mode.
- --name mongodb: Container name.
- -p 27017:27017: Expose MongoDB port.
- -e MONGO_INITDB_ROOT_USERNAME=admin: Set MongoDB admin username.
- -e MONGO_INITDB_ROOT_PASSWORD=adminpassword: Set password.
- mongo: Official MongoDB image.

Step 2: (Optional) Check MongoDB is Running
docker ps

Step 3: (Optional) Access MongoDB CLI in the container
docker exec -it mongodb mongosh -u admin -p adminpassword

Step 4: Connect MongoDB to Django

Step 4.1: Install MongoDB support in Django
pip install djongo

Step 4.2: Update settings.py in Django
DATABASES = {
 'default': {
 'ENGINE': 'djongo',
 'NAME': 'mydatabase',
 'ENFORCE_SCHEMA': False,
 'CLIENT': {
 'host': 'mongodb://admin:adminpassword@localhost:27017/',
 'authSource': 'admin',
 }
 }
}

Notes:
- NAME: Name of your MongoDB database (it will be created automatically).
- host: MongoDB URI format.
- authSource: Must be 'admin' since we are authenticating with root credentials.

Step 5: Run Your Django App
python manage.py runserver

Optional: Docker Compose (For Production or Multi-Container Setup)
docker-compose.yml
version: "3.8"
services:
 mongodb:
 image: mongo
 container_name: mongodb
 ports:
 - "27017:27017"
 environment:
 MONGO_INITDB_ROOT_USERNAME: admin
 MONGO_INITDB_ROOT_PASSWORD: adminpassword
 django:
 build: .
 command: python manage.py runserver 0.0.0.0:8000
 volumes:
 - .:/code
 ports:
 - "8000:8000"
 depends_on:
 - mongodb
 environment:
 - DB_HOST=mongodb




mongosh "mongodb://admin:adminpassword@localhost:27017/mydatabase?authSource=admin"
docker exec -it mongodb mongosh -u admin -p adminpassword

show dbs
show collections
use admin or use school

db.createCollection("students")
db.dropDatabase()

db.students.insertOne({name:"Abhishek",age:24,gpa:7.9})
db.students.find()

View all documents:
db.students.find().pretty()


db.students.insertMany([{name:"Akshay",age:24,gpa:7.9},{name:"Amit",age:24,gpa:7.9},{name:"Ayush",age:24,gpa:7.9}])

✅ MongoDB Data Types from Your Example

1.
db.students.insertOne({
  name: "Larry",                           // String
  age: 32,                                 // Number (Integer)
  gpa: 2.8,                                // Number (Float)
  fullTime: false,                         // Boolean
  registerDate: new Date(),               // Date
  graduationDate: null,                   // Null
  courses: ["Biology", "Chemistry", "Calculus"],  // Array of Strings
  address: {                               // Embedded Document (Object)
    street: "123 Fake St.",
    city: "Bikini Bottom",
    zip: 12345                             // Number
  }
});

2.
db.allTypes.insertOne({
  name: "All Types Example",                 // String
  id: ObjectId(),                            // ObjectId (unique identifier)
  highPrecision: NumberDecimal("99.999"),    // Decimal128 (for money, accuracy)
  binary: BinData(0, "SGVsbG8gV29ybGQ="),     // Binary Data (Base64 encoded)
  regex: /test/i,                            // Regular Expression (case-insensitive match)
  createdAt: new Date(),                     // Date (current timestamp)
  ts: Timestamp(),                           // Timestamp (used internally by MongoDB)
  nullable: null,                            // Null value
  active: true,                              // Boolean
  min: MinKey(),                             // MinKey (used to compare as lowest possible value)
  max: MaxKey(),                             // MaxKey (used to compare as highest possible value)
  numbers: [                                 // Array containing:
    1,                                       // Integer
    2.5,                                     // Double
    NumberDecimal("3.14")                    // Decimal128
  ],
  nested: {                                  // Embedded Document (sub-object)
    message: "Hello",                        // String
    count: 5                                 // Integer
  }
})


db.students.find().sort({ field: 1 })   // Ascending
db.students.find().sort({ field: -1 })  // Descending

db.students.find().sort({ field: 1 }).limit(n)
db.students.find().sort({ gpa: -1 }).limit(3).pretty()

1 = ascending
-1 = descending
n = number of documents to return


db.students.find({ name: "Abhishek" })

db.students.find({ fullTime:false})
db.students.find({ fullTime:false, gpa:4})


find(query, projection)
db.collection.find(<query>, <projection>)

query → filter condition
projection → specify which fields to include (or exclude)

✅ 1. Example with query only:
db.students.find({ fullTime: false, gpa: 4 })

✅ 2. Example with query + projection:
db.students.find(
  { fullTime: false, gpa: 4 },      // query
  { name: 1, age: 1, _id: 0 }        // projection: include only name & age, exclude _id
)

db.students.find(
  { field1: value1, field2: value2 },  // query
  { fieldA: 1, fieldB: 0 }             // projection
)


db.students.find( {}, { name: true } )
db.students.find( {}, {_id:false, name: true } )

1 means include the field
0 means exclude the field
You must either include or exclude, not both (except _id, which is optional to exclude)


db.students.updateOne(filter,update)

db.students.updateOne( {name:"Abhishek"}, {$set:{fulltime:true}})
db.students.updateOne( {_id: ObjectId('686d482732a2b9c43a964033')}, {$set:{fulltime:false}})

db.students.find({_id: ObjectId('686d482732a2b9c43a964033')})

db.students.updateMany( {}, {$set:{fulltime:false}})


db.students.updateOne( {name:"Abhishek"}, {$unset:{fulltime:true}})



exit 
cls