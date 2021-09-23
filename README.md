# Chartmetric---Webpage-Challenge
Challenge for a startup to create a webpage that processes a database or a webserver that can return a database in 24 hours.

I created a server that both displays a website and has a backend.

Live server here: https://protected-ocean-96638.herokuapp.com/

## DOCUMENTATION:

Start up the server - run runserver.py

Home - (what users see):
http://protected-ocean-96638.herokuapp.com/

Posts of a user – 
http://protected-ocean-96638.herokuapp.com/[USERNAME]/recentposts

Stats of a user-
http://protected-ocean-96638.herokuapp.com/[USERNAME]/stats


## BACKEND

Entire content of a user can be retrieved by going to 
http://protected-ocean-96638.herokuapp.com/api/[USERNAME]/

Or 

http://protected-ocean-96638.herokuapp.com/api/[USERID]/


## Specifics of a user that can be retrieved:

Report_Info: http://protected-ocean-96638.herokuapp.com/api/[USERID/USERNAME]/reportinfo/

User_Profile: http://protected-ocean-96638.herokuapp.com/api/[USERID/USERNAME]/userprofile/

Audience_Likers: http://protected-ocean-96638.herokuapp.com/api/[USERID/USERNAME]/audiencelikers/

Audience_Followers: http://protected-ocean-96638.herokuapp.com/api/[USERID/USERNAME]/audiencefollowers/

Audience_Commenters: http://protected-ocean-96638.herokuapp.com/api/[USERID/USERNAME]/audiencecommenters/


## Extra: http://protected-ocean-96638.herokuapp.com/api/[USERID/USERNAME]/extra/ \

Example command to retrieve JSON data of a user's report_info: \

curl http://protected-ocean-96638.herokuapp.com/api/55165562/reportinfo/
