# Facebook_Scrapper

This application can scrap the first 5 pages of any public Facebook Page. 
It gives:
1) Link of the post
2) Links Contained inside the post(if any)
3) Image Url(if any).
4) Number of people commented on the post.
5) Number of people who reacted to the post.
6) Video Url(if any)
and stores all of them in a json file.

## Modules Used
1) facebook_scraper: It may be the only module present, that can be used to scrap facebook. Not very accurate, because sometimes it return 'None' even when it should not.
2) json: Used to create the json file. 
