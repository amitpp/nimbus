
A simple Python, Flask web application using python client for Github "PyGithub". It exposes a public GET api which accepts username of Github user as URL parameter and returns a JSON dictionary with basic details of User as well as Top 3 languages used by the user based on number of repositories created.

A sample CURL request will look like this: curl http://localhost:5000/amitpp

And here is the response for above request: { "Basic Profile Information": { "company": "Jamia Hamdard ( my college)", "id": 7340309, "last_modified": "Mon, 13 Aug 2018 03:08:33 GMT", "location": "New Delhi", "name": "Amit Prakash Pandey", "public_repos": 37 }, "Number Of Contributions In Last Three Months": 0, "Top Languages": [ "Python" ] }
