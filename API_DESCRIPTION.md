### Webserver

#### Routes

#### User

##### /user/new



#### Chat

##### /chat/create

This is a POST Endpoint.
You can send this payload:

```
{
    user_id: "<user id from /user/new endpoint>",
    lat: float,
    long: float
    
}
```

on success it will return a HTTP Statuscode 200 and

```
{
    "id": <server generated chat uuid>
}
```


on failure it will return a HTTP Statuscode 500 and no payload.


##### /chat/<chat_hash>

This is a GET Endpoint.
You can send call it with the <chat_hash>.

You need to send the user hash as http header:
x-mapchat-user=<user_id>


On success it will return a HTTP Statuscode 200 and a list of the chats:
```
[
    {
    "id":"<message_id>",
    "create_at":"",
    "user_id":"",
    "message":""
    },
    // More stuff ...
]

```

On failure it will return a HTTP Statuscode 500 and no payload.

#### Messages

##### /message/create

This is a POST Endpoint.
You can send this payload:

```
{
  "user_id":"",
  "message":""   
}
```

The message may not exceed 255 characters.
The user must be a uuid you have acquired by calling /users/new.
on success it will return a HTTP Statuscode 200 and no payload.
on failure it will return a HTTP Statuscode 500 and no payload.