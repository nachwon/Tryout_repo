## Tryout Repository

this repository contains a simple django application for practicing some techs with django.

python version: 3.6.4
django version: 2.0.4
database: MyQSL 5.7.22

- - -

### mysql_redis

This app contains a simple Post model. A post contains id, title and content.

`addpost` command will add dummy posts for test as many as you want.

For example, following command will add 1000 dummy posts to database.

```
./manage.py addpost 1000
```

Once some dummy posts are created, you can retrieve the entire list of posts by accessing 'posts/' endpoint.

Django will retrieve the data from database and save it to redis database.

Once the data is saved in redis database, it will be served from redis whenever the same data is requested.

If there is any change happens to the post list data, such as creating new post or deleting existing one, django will erase the cache data from redis server and save newly updated data.

In this way, django doesn't have to access database every time when data are requested but instead, data can be retrieved from redis server which is In-Memory database.

- - -

### drf_router

This app is to learn how routers work in django rest framework.

This app is an API app so it has a serializer for post model.

The goal is to create endpoints for CRUD of post model and a custom create action which is activated by a POST request.

To achieve this goal, I've created a ModelViewSet which contains methods for all of CRUD actions.

This is the PostViewSet that I've wrote to use with routers.

```
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

Once this ModelViewSet is connected with routers, the endpoints for all CRUD actions will automatically created.

In this case, following endpoints are created.

- GET `drf_router/`: The api root endpoint. This page will list all the available endpoints that start with 'drf_router/'.
- GET `drf_router/posts/`: List of all the posts.
- POST `drf_router/posts/`: Create a post.
- GET `drf_router/posts/pk/`: Detail of pk post.
- PUT `drf_router/posts/pk/`: Update pk post.
- PATCH `drf_router/posts/pk/`: Partial Update pk post.
- DELETE `drf_router/posts/pk/`: Delete pk post.

But sometimes we might want to create a special action that doesn't exactly fit any of CRUD actions.

A custom action can be created using actions decorator.

Just define a method that does what it needs to do and decorate it with actions decorator.

```

class PostViewSet(ModelViewSet):
    ...
    @actions(methods=['post'], detail=True)
    def custom_action(self, request, *args, **kwargs):
        do somthing
        return result
```

The actions decorator basically takes two arguments, `methods` and `detail`.

`methods` determines which Http request method it will respond to.

`detail` determines whether this action will be executed for one particular post instance or for entire posts.

If detail is `True`, the custom_action method will be given a pk value of a model instance. Nothing will be given otherwise.

And also, endpoints created by router will differ according to the value of detail and methods.

If detail is `True` and methods is `post`, this endpoint will be created.

```
POST drf_router/posts/pk/custom_action/
```

If detail is `False` and methods is `post`,

```
POST drf_router/posts/custom_action/
```

will be created.

- - -

