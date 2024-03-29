## Prerequisites

- Pip

> 📘 Note
> 
> You can download pip [here](https://pip.pypa.io/en/stable/installation/).

## Nomad SDK PIP

To learn how to download and setup the nomad sdk pip, go to [Nomad SDK PIP](https://github.com/Nomad-Media/nomad-sdk/tree/main/nomad-sdk-pip).

## Create and Update Event Instance

To create or update an event, enter 1 when prompted. Then first select whether you want to create or update an event. Then enter the name you want to assign the event, the start and end date-time of the event, and any additional properties.

![](images/create-and-update-event-instance.png)

> 📘 Note
> 
> For more information about the API calls used go to [Create and Update an Event](https://developer.nomad-cms.com/docs/create-and-update-an-event)

## Add Live Schedule To Event

To add a live schedule to an event, enter 2 when prompted. Then enter the id of the event you want to add the live schedule to. Next, fill out the rest of the information. Either the Primary Livestream Input, or the Primary Livesteam Input URL is required.

![](images/add-live-schedule-to-event.png)

> 📘 Note
> 
> For more information about the API calls used go to [Adds Live Schedule to Event](https://developer.nomad-cms.com/docs/add-live-schedule-to-event)

## Extend Live Schedule

To extend a Live Schedule, enter 3 when prompted. Then enter the id of the event with the live schedule, the days you want to extend it to, and the number of weeks you want to extend the live schedule to. Optionally, you can include the datetime in which you want to end the extension.

![](images/extend-live-schedule.png)

> 📘 Note
> 
> For more information about the API calls used go to [Extend Live Schedule](https://developer.nomad-cms.com/docs/extent-live-schedule)

## Get Live Schedule

To get a live schedule of an event, you need to enter the id of the event.

![](images/get-live-schedule.png)

> 📘 Note
> 
> For more information about the API calls used go to [Get Live Schedule](https://developer.nomad-cms.com/docs/get-live-schedule)

## Start Live Schedule

To start a live schedule of an event, you need to enter the id of the event.

![](images/start-live-schedule.png)

> 📘 Note
> 
> For more information about the API calls used go to [Starts Live Schedule](https://developer.nomad-cms.com/docs/start-live-schedule)

## Stop Live Schedule

To stop a live schedule of an event, you need to enter the id of the event.

![](images/stop-live-schedule.png)

> 📘 Note
> 
> For more information about the API calls used go to [Stop Live Schedule](https://developer.nomad-cms.com/docs/stop-live-schedule)

## Deleting Event Instance

To delete an instance, you need the content id, and the content definition id.

![](images/delete-event-instance.png)

> 📘 Note
> 
> For more information about the API calls used go to [Delete Event](https://developer.nomad-cms.com/docs/delete-event)