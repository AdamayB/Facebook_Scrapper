from facebook_scraper import get_posts
import json

link=[]
post1=[]
no_comments=[]
img_URL=[]
like_count=[]
video=[]

n=input('Enter user handle of a public FaceBook page:')
for post in get_posts(n, pages=5):
  link.append(post['link'])
  post1.append(post['post_url'])
  no_comments.append(post['comments'])
  img_URL.append(post['images'])
  like_count.append(post['likes'])
  video.append(post['video'])


l2=[]
for i in range(len(post1)):
  d={}
  d['Post Link']=post1[i]
  d['Link']=link[i]
  d['No of Comments']=no_comments[i]
  d['Image']=img_URL[i]
  d['Likes and Reactions']=like_count[i]
  d['Video']=video[i]
  l2.append(d)


c=n+'.json'
with open(c, 'w+') as f:
  json.dump(l2, f, indent=4)
