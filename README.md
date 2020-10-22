# pyxmp
A Python XMP metadata injection tool based on py3exiv2

## Installation

```
python -m pip install pyxmp
```

## Usage

To inject XMP metadata to the image, the input metadata should be a list of dict following the format below, with `provider`, `name` and `value` as keys.

```
[
    {
        "provider": "InfoSnapshot",
        "name": "Brand",
        "value": "My Service"
    },
    {
        "provider": "InfoSnapshot",
        "name": "Current GPS Accuracy",
        "value": "14.589"
    },
    {
        "provider": "InfoSnapshot",
        "name": "Current GPS Latitude",
        "value": "25.045234"
    },
    {
        "provider": "InfoSnapshot",
        "name": "Current GPS Longitude",
        "value": "121.530795"
    },
    {
        "provider": "InfoSnapshot",
        "name": "Current GPS Timestamp",
        "value": "2020-09-15T13:50:25.143Z"
    },
    {
        "provider":"InfoSnapshot",
        "name":"Timestamp",
        "value":"2020-09-15T13:50:30.203Z"
    }
]
```

Then the metadata could be injected like the following example:


```
import pyxmp

metadata = {...} # Prepare the metadata like the above example

xmp_injected_image = pyxmp.inject(
    original_image_bytes,
    metadata,
    'http://numbersprotocol.io/xmp/',
    'examplePrefix'
)
```

To read the XMP metadata into a dict:

```
import pyxmp

metadata_dict = pyxmp.read(xmp_injected_image)
```

Example injected XMP metadata dict:

```
{
    'Xmp.examplePrefix.infoSnapshot.brand': 'My Service',
    'Xmp.examplePrefix.infoSnapshot.currentGPSAccuracy': '14.589',
    'Xmp.examplePrefix.infoSnapshot.currentGPSLatitude': '25.045234',
    'Xmp.examplePrefix.infoSnapshot.currentGPSLongitude': '121.530795',
    'Xmp.examplePrefix.infoSnapshot.currentGPSTimestamp': '2020-09-15T13:50:25.143Z',
    'Xmp.examplePrefix.infoSnapshot.timestamp': '2020-09-15T13:50:30.203Z'
}
```
