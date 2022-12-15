from django.urls import path

from .views import(
        OrderingByTime, OrderingByVotes, PostView, PublishPostView, PostUpView 
        , PostUnvoteView, CommentsCreation,
        
    ) 

urlpatterns = [
    path('<id>/', PostView, name ='detail'),
    path('publish/user/<slug>', PublishPostView, name ='publish_user'),
    path('publish/org/<slug>', PublishPostView, name ='publish_org'),
    path('comments/<id>/', CommentsCreation, name ='create_comments'),
    path('upvote/<id>/', PostUpView, name ='upvote'),
    path('unvote/<id>/', PostUnvoteView, name ='unvote'),
    path('order_by_time', OrderingByTime, name ='recent'),
    path('order_by_votes', OrderingByVotes, name ='mostvotes'),

]