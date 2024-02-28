## Prerequisites

- Pip

> 📘 Note
> 
> You can download pip [here](https://pip.pypa.io/en/stable/installation/).

## Sample Code

You can find the sample code [here](https://github.com/Nomad-Media/samples-python).

## Nomad SDK PIP

To learn how to download and setup the nomad sdk pip, go to [Nomad SDK PIP](https://github.com/Nomad-Media/nomad-sdk/tree/main/nomad-sdk-pip).

## Setup

To run the sample code, you need to add a `config.py` file in the root directory of the sample code. The `config.py` file should contain the following code:

```python
config = {
    "username": "username",
    "password": "password",
    "serviceApiUrl": "serviceApiUrl",
    "apiType": "admin",
    "debugMode": False
}
```

## Sample Code Structure
| Title | Description | Link |
| ----- | ----------- | ---- |
| Account Authenticateion | Shows how to authenticate a user and generate a token. | [Account Authentication](https://github.com/Nomad-Media/samples-python/tree/main/account_authentication)
| Account Registration | Shows how to register a user. | [Account Registration](https://github.com/Nomad-Media/samples-python/tree/main/account_registration)
| Account Updates | Shows how to update a user's account. | [Account Updates](https://github.com/Nomad-Media/samples-python/tree/main/account_updates)
| Asset | show how to use all of the endpoints related to assets (not including uploading). | [Asset](https://github.com/Nomad-Media/samples-python/tree/main/asset)
| Asset Upload | Shows how to upload an asset. | [Asset Upload](https://github.com/Nomad-Media/samples-python/tree/main/assets_upload)
| Audit | Shows how to get audit logs. | [Audit](https://github.com/Nomad-Media/samples-python/tree/main/audit)
| Config | Shows how to use all of the endpoints related to config. | [Config](https://github.com/Nomad-Media/samples-python/tree/main/config)
| Content | Shows how to create, delete, get and update content (including getting user tracking). | [Content](https://github.com/Nomad-Media/samples-python/tree/main/content)
| Content Admin | Shows how to manipulate asset metadata | [Content Admin](https://github.com/Nomad-Media/samples-python/tree/main/content_admin)
| Content Groups | Shows how to create, delete, and manipulate content groups. | [Content Groups](https://github.com/Nomad-Media/samples-python/tree/main/content_groups)
| Event Scheduler | Shows how to create, delete, and update and event and add and extend a live schedule to an event. | [Event Scheduler](https://github.com/Nomad-Media/samples-python/tree/main/event_scheduler)
| Live Channel | Shows how to use live channels, live inputs, live outputs, schedule events, and live operators. | [Live Channel](https://github.com/Nomad-Media/samples-python/tree/main/live_channel)
| Media | Shows how to use all of the endpoints related to media. | [Media](https://github.com/Nomad-Media/samples-python/tree/main/media)
| Movies | Shows how to use content admin, content groups, and content to create a movie. | [Movies](https://github.com/Nomad-Media/samples-python/tree/main/movies)
| Ping | Shows how to ping an application and/or a user session. | [Ping](https://github.com/Nomad-Media/samples-python/tree/main/ping)
| Saved Search | Shows how to use saved searches and search saves. | [Saved Search](https://github.com/Nomad-Media/samples-python/tree/main/saved_search)
| Schedule | Shows how to set up and use intelligent playlists, intellignet schedules, and playlists. | [Schedule](https://github.com/Nomad-Media/samples-python/tree/main/schedule)
| Search | Shows how to use search and all of the parameters that can be used with search. | [Search](https://github.com/Nomad-Media/samples-python/tree/main/search)
| Sync | Shows how to set up CRUD operations for a content definition (in this case, a movie). | [Sync](https://github.com/Nomad-Media/samples-python/tree/main/sync)
| User | Shows how to delete various user data. | [User](https://github.com/Nomad-Media/samples-python/tree/main/user)
| User Session | Shows how to change a user session status. | [User Session](https://github.com/Nomad-Media/samples-python/tree/main/user_session)
| Video Tracking | Shows the different ways to track video. | [Video Tracking](https://github.com/Nomad-Media/samples-python/tree/main/video_tracking)