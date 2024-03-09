## Prerequisites

- Pip

> 📘 Note
> 
> You can download pip [here](https://pip.pypa.io/en/stable/installation/).

## Nomad SDK PIP

To learn how to download and setup the nomad sdk pip, go to [Nomad SDK PIP](https://github.com/Nomad-Media/nomad-sdk/tree/main/nomad-sdk-pip).

## Get Live Channels

To get all live channels, enter get channels into the prompt.

![](images/get-live-channels.png)

> 📘 Note
> 
> For more information about the API call used go to [Gets live channels.](ref:getlivechannels)

## Get Live Channel

To get a live channel enter get channel into the prompt. Then enter the id of the channel you want to get.

![](images/get-live-channel.png)

> 📘 Note
> 
> For more information about the API call used go to [Gets a live channel.](ref:getlivechannel)

## Live Channel Refresh

To refresh all live channels enter channel refresh when prompted.

![](images/live-channel-refresh.png)

> 📘 Note
> 
> For more information about the API call used go to [Refresh Live Channels](ref:livechannelrefresh)

## Create Live Channel

To create a live channel, enter create channel into the prompt. Then enter the name, folder archive id, high availability, live clipping, secure output, output screenshots, and channel type.

![](images/create-live-channel.png)

> 📘 Note
> 
> For more information about the API call used go to [Creates a live channel.](ref:createlivechannel)

## Clip Live Channel

To clip a live channel enter clip channel into the prompt. Then enter the id of the channel you want to clip and the rest of the data you want to set for the clip.

![](images/clip-live-channel.png)

> 📘 Note
> 
> For more information about the API call used go to [Clips a live channel.](ref:cliplivechannel)

## Next Event

To get the next event of a channel, enter get next into the prompt. Then enter the id of the event you want to get the next event of.

![](images/next-event.png)

> 📘 Note
> 
> For more information about the API call used go to [Gets the next event.](ref:nextevent)

## Start Output Tracking

To start output tracking, enter start tracking into the prompt, Then enter the id of the channel you want to start the output tracking of.

![](images/start-output-tracking.png)

> 📘 Note
> 
> For more information about the API call used go to [Starts output tracking.](ref:startoutputtracking)

## Update Live Channel

To update a live channel, enter update channel into the prompt. Then enter the id of the channel of the channel you want to update. Then enter the name, folder archive id, high availability, live clipping, secure output, output screenshots, and channel type you want to update.

![](images/update-live-channel.png)

> 📘 Note
> 
> For more information about the API call used go to [Updates a live channel.](ref:updatelivechannel)

## Start Live Channel

To start a live channel, enter start channel into the prompt. Then enter the id of the channel you want to start.

![](images/start-live-channel.png)

> 📘 Note
> 
> For more information about the API call used go to [Starts a live channel.](ref:startlivechannel)

## Stop Live Channel

To stop a live channel, enter stop channel into the prompt. Then enter the id of the channel you want to stop.

![](images/stop-live-channel.png)

> 📘 Note
> 
> For more information about the API call used go to [Stops a live channel.](ref:stoplivechannel)

## Delete Live Channel

To delete a live channel, enter delete channel when prompted. Then enter the channel id and if you want to delete the live inputs attached to the live channel.

![](images/delete-live-channel.png)

> 📘 Note
> 
> For more information about the API call used go to [Deletes a live channel.](ref:deletelivechannel)

## Add Asset Schedule Event

To add an asset schedule event to a channel, enter add event into the prompt. Then enter the id of the channel you want to add the asset schedule event to and the id of the asset you want to add to the channel.

![](images/add-asset-schedule-event.png)

> 📘 Note
> 
> For more information about the API call used go to [Adds an asset schedule event.](ref:addassetscheduleevent)

## Get Asset Schedule Event

To get an asset schedule event, enter get event into the prompt. Then enter the id of the channel that the asset schedule event is in and the id of the asset schedule event.

![](images/get-asset-schedule-event.png)

> 📘 Note
> 
> For more information about the API call used go to [Gets an asset schedule event.](ref:getassetscheduleevent)

## Update Asset Schedule Event

To update an asset schedule event, enter update event when prompted. Then enter the id of the channel that the asset schedule event is in and the id of the asset schedule event. Then enter the data you want to update.

![](images/update-asset-schedule-event.png)

> 📘 Note
> 
> For more information about the API call used go to [Updates an asset schedule event.](ref:updateassetscheduleevent)

## Remove Asset Schedule Event

To remove an asset schedule event, enter remove event into the prompt. Then enter the id of the channel you want to remove the asset channel from and the id of the asset schedule event you want to remove from the channel.

![](images/remove-asset-schedule-event.png)

> 📘 Note
> 
> For more information about the API call used go to [Removes an asset schedule event.](ref:removeassetscheduleevent)

## Move Schedule Event

![](images/move-schedule-event.png)

> 📘 Note
> 
> For more information about the API call used go to [Moves a schedule event.](ref:movescheduleevent)

## Get Live Inputs

To get all live input, enter get inputs into the prompt.

![](images/get-live-inputs.png)

> 📘 Note
> 
> For more information about the API call used go to [Gets live inputs.](ref:getliveinputs)

## Get Live Input

To get a live input, enter get input into the prompt. Then enter the id of the input you want to get.

![](images/get-live-input.png)

> 📘 Note
> 
> For more information about the API call used go to [Gets a live input.](ref:getliveinput)

## Create Live Input

To create a live input, enter create input when prompted. Then enter the name you want to assign the input and the input type. If the input type is RTMP_PULL, RTP_PUSH, or URL_PULL, you will be asked for a source. If the input type is RTMP_PUSH, you will be asked for a source cidr.

![](images/create-live-input.png)

> 📘 Note
> 
> For more information about the API call used go to [Creates a live input.](ref:createliveinput)

## Updating Live Input

To update a live input enter update input into the prompt. Then enter the id of the input you want to update, the updated name, and the updated type. If the input type is RTMP_PULL, RTP_PUSH, or URL_PULL, you will be asked for a source. If the input type is RTMP_PUSH, you will be asked for a source cidr. If you don't want to update a parameter, leave it blank and press enter on the prompt.

![](images/update-live-input.png)

> 📘 Note
> 
> For more information about the API call used go to [Updates a live input.](ref:updateliveinput)

## Add Live Input Schedule Event

To add a live input to a live channel, enter add input into the prompt. Then enter the channel id you want to add the input to, the input id, and if you want to have a fixed on air time, the on air time in UTC.

![](images/add-live-input-schedule-event.png)

> 📘 Note
> 
> For more information about the API call used go to [Adds an input schedule event.](ref:addinputscheduleevent)

## Get Live Input Schedule Event

To get a live input schedule event, enter get input event when prompted. Then enter the id of the channel the input schedule event is in and the id of the input schedule event.

![](images/get-live-input-schedule-event.png)

> 📘 Note
> 
> For more information about the API call used go to  [Gets an input schedule event.](ref:getinputscheduleevent)

## Update Live Input Schedule Event

To update a live input schedule event, enter update input event when prompted. Then enter the id of the channel the input schedule event is in and the id of the input schedule event. Then enter the data you want to update.

![](images/update-live-input-schedule-event.png)

> 📘 Note
> 
> For more information about the API call used go to [Updates an input schedule event.](ref:updateinputscheduleevent)

## Remove Live Input Schedule Event

To remove a live input schedule event, enter remove input when prompted. Then enter the id of the channel the input schedule event is in and the id of the input schedule event.

![](images/remove-live-input-schedule-event.png)

> 📘 Note
> 
> For more information about the API call used go to [Removes an input schedule event.](ref:removeinputscheduleevent)

## Delete Live Input

To delete a live input, enter delete input when prompted. Then enter the id of the input you want to delete.

![](images/delete-live-input.png)

> 📘 Note
> 
> For more information about the API call used go to [Deletes a live input.](ref:deleteliveinput)

## Get Live Output Profiles

To get all live output profiles, enter get outputs into the prompt.

![](images/get-live-outputs.png)

> 📘 Note
>
> For more information about the API call used go to [Gets live outputs.](ref:getliveoutputs)

## Get Live Output Profile

To get a live output profile, enter get output into the prompt. Then enter the id of the output you want to get.

![](images/get-live-output.png)

> 📘 Note
>
> For more information about the API call used go to [Gets a live output.](ref:getliveoutput)

## Get Live Output Types

To get all live output types, enter get output types into the prompt.

![](images/get-live-output-types.png)

> 📘 Note
>
> For more information about the API call used go to [Gets live output types.](ref:getliveoutputtypes)

## Create Live Output Profile

To create a live output profile, enter create output when prompted. Then enter the name of the output, choose an output type, and select if the output is active or not. Then, optionally, enter the rest of the information you want to add when prompted.

![](images/create-live-output.png)

> 📘 Note
>
> For more information about the API call used go to [Creates a live output.](ref:createliveoutput)

## Update Live Output Profile

To udpate a live output profile, enter update output when prompted. Then fill in the rest of the information you want to update.

![](images/update-live-output.png)

> 📘 Note
>
> For more information about the API call used go to [Updates a live output.](ref:updateliveoutput)

## Delete Live Output Profile

To delete a live output profile, enter delete output when prompted. Then enter the id of the output you want to delete.

![](images/delete-live-output.png)

> 📘 Note
>
> For more information about the API call used go to [Deletes a live output.](ref:deleteliveoutput)

## Get Live Output Profile Groups

To get all live output profile groups, enter get output groups into the prompt.

![](images/get-live-output-groups.png)

> 📘 Note
>
> For more information about the API call used go to [Gets live output groups.](ref:getliveoutputgroups)

## Get Live Output Profile Group

To get a live output profile group, enter get output group when prompted. Then enter the id of the output group you want to get.

![](images/get-live-output-group.png)

> 📘 Note
>
> For more information about the API call used go to [Gets a live output group.](ref:getliveoutputgroup)

## Create Live Output Profile Group

To create a live output profile group, enter create output group when prompted. Then enter the name of the output group, whether or not to enable the group, the manifest type, whether or not to make the group the default group, optionally, the archive live output profile id, and the output ids you want to add to the group.

![](images/create-live-output-group.png)

> 📘 Note
>
> For more information about the API call used go to [Creates a live output group.](ref:createliveoutputgroup)

## Update Live Output Profile Group

To update a live output profile group, enter update output group when prompted. Then enter the id of the output group you want to update and the rest of the information you want to update.

![](images/update-live-output-group.png)

> 📘 Note
>
> For more information about the API call used go to [Updates a live output group.](ref:updateliveoutputgroup)

## Delete Live Output Profile Group

To delete a live output profile group, enter delete output group when prompted. Then enter the id of the output group you want to delete.

![](images/delete-live-output-group.png)

> 📘 Note
>
> For more information about the API call used go to [Deletes a live output group.](ref:deleteliveoutputgroup)

## Get Live Operators

To get all live operators, enter get operators into the prompt.

![](images/get-live-operators.png)

> 📘 Note
> 
> For more information about the API call used go to [Gets live operators.](ref:getliveoperators)

## Get Live Operator

To get a specific live operator, enter get operator into the prompt. Then enter the id of the channel you want to get the live operator of.

![](images/get-live-operator.png)

> 📘 Note
> 
> For more information about the API call used go to [Gets a live operator.](ref:getliveoperator)

## Start Broadcast

To start a broadcast, enter start broadcast when prompted. Then enter the id of the channel you want to use for the broadcast. Then enter the preroll and postroll asset id, live input id, related content ids, and tag ids if you want to add them.

![](images/start-broadcast.png)

> 📘 Note
> 
> For more information about the API call used go to [Starts a broadcast.](ref:startbroadcast)

## Cancel Broadcast

To cancel a broadcast, enter cancel broadcast when prompted. Then enter the id of the channel associated with the broadcast.

![](images/cancel-broadcast.png)

> 📘 Note
> 
> For more information about the API call used go to [Cancels a Broadcast](ref:post_admin-liveoperator-liveoperatorid-cancel)

## Stop Broadcast

To stop a broadcast, enter stop broadcast when prompted. Then enter the id of the channel associated with the broadcast.

![](images/stop-broadcast.png)

> 📘 Note
> 
> For more information about the API call used go to [Stops a Broadcast](ref:post_admin-liveoperator-liveoperatorid-stop)

## Get Completed Segments

To get all completed segments, enter get segments when prompted. Then enter the id of the channel associated with the broadcast the segments are in. 

![](images/get-completed-segments.png)

> 📘 Note
> 
> For more information about the API call used go to [Gets complete segments.](ref:getcompletesegments)

## Start Segment

To start a segment, enter start segment when prompted. Then enter the id of the channel associated with the broadcast that you want to start the segment in.

![](images/start-segment.png)

> 📘 Note
> 
> For more information about the API call used go to [Starts a segment.](ref:startsegment)

## Cancel Segment

To cancel a segment, enter cancel segment when prompted. Then enter the id of the channel associated with the broadcast that you want to cancel the segment from.

![](images/cancel-segment.png)

> 📘 Note
> 
> For more information about the API call used go to [Cancels a segment.](ref:cancelsegment)

## Complete Segment

To complete a segment, enter complete segment when prompted. Then enter the ids of the related contents and tags you want to add to the segment.

![](images/complete-segment.png)

> 📘 Note
> 
> For more information about the API call used go to [Completes a segment.](ref:completesegment)