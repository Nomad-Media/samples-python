## Prerequisites

- Pip

> 📘 Note
> 
> You can download pip [here](https://pip.pypa.io/en/stable/installation/).

## Nomad SDK PIP

To learn how to download and setup the nomad sdk pip, go to [Nomad SDK PIP](https://github.com/Nomad-Media/nomad-sdk/tree/main/nomad-sdk-pip).

## Upload Asset

To upload a file, enter 1 when promted. Then enter the display name for your asset. If you leave it blank, it will default to the name of your file. Then, enter the upload overwrite option you want to select. Replace replaces an existing asset, continue continues the upload of an asset that is currently uploading, and cancel cancels the upload of an asset that is uploading. Then, enter the file path, related content id you want to add to the asset, and whether or not you want to use multi-thread upload.

![](images/upload-asset.png)

> 📘 Note
> 
> For more information about the API calls used go to [Asset Upload](https://developer.nomad-cms.com/docs/start-asset-upload)

## Upload Related Asset

To upload a file as a related asset, enter 2 when promted. Then enter the id of the asset you want to relate the file to in existing asset id. Then, if you want to update the related asset, enter the id of the related asset you want to update. Then, enter the asset metadata type, the file path, and optionally, the id of the language you want to use.

![](images/upload-related-asset.png)

> 📘 Note
>
> For more information about the API calls used go to [Related Asset Upload](https://developer.nomad-cms.com/docs/start-related-asset-upload)