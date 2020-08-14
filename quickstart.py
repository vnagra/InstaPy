# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'ryd_den'
insta_password = 'V220856s'

comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  multi_logs=True)

with smart_run(session):
  """ Activity flow """		
  # general settings		
  session.set_dont_include(["friend1", "friend2", "friend3"])		
  
  # activity
  session.like_by_tags(["motorcycle"], amount=10)
  session.follow_user_followers(["plexaudio"],amount=10, randomize=False)
  session.follow_by_tags(["motorcycle"], amount=2)
  session.set_do_like(enabled=True, percentage=100)
  session.set_delimit_commenting(enabled=False, max=10, min=0)
  session.set_do_follow(enabled=True, percentage=100, times=2)
  session.set_do_comment(False, percentage=20)
  session.set_relationship_bounds(enabled=True,
  delimit_by_numbers=True,
  max_followers=1000,
  max_following=900,
  min_followers=20,
  min_following=10)
 
