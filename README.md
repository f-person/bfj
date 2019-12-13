# bson from json
bjf - bson from json for go structs.

This little script automatically adds bson tags (usually used with [mongo-go-driver](https://github.com/mongodb/mongo-go-driver)) to a Go struct based on existing json tags.

## Usage
`python bjf.py <filename>`
<br>
it can also from stdio:
<br>
`cat <filename> | python bjf.py` 

For example the following input:
```
type OsmPlace struct {
	PlaceID        string    `json:"place_id"`
	OsmID          string    `json:"osm_id"`
	OsmType        string    `json:"osm_type"`
	Licence        string    `json:"licence"`
	Lat            string    `json:"lat"`
	Lon            string    `json:"lon"`
	Boundingbox    []string  `json:"boundingbox"`
	Class          string    `json:"class"`
	Type           string    `json:"type"`
	DisplayName    string    `json:"display_name"`
	DisplayPlace   string    `json:"display_place"`
	DisplayAddress string    `json:"display_address"`
	Address        OsmPlaceAddress `json:"address"`
}

type OsmPlaceAddress struct {
	Name        string `json:"name"`
	City        string `json:"city"`
	State       string `json:"state"`
	Country     string `json:"country"`
	CountryCode string `json:"country_code"`
}
```

will output the following:
```
type OsmPlace struct {
	PlaceID        string    `json:"place_id" bson:"place_id"`
	OsmID          string    `json:"osm_id" bson:"osm_id"`
	OsmType        string    `json:"osm_type" bson:"osm_type"`
	Licence        string    `json:"licence" bson:"licence"`
	Lat            string    `json:"lat" bson:"lat"`
	Lon            string    `json:"lon" bson:"lon"`
	Boundingbox    []string  `json:"boundingbox" bson:"boundingbox"`
	Class          string    `json:"class" bson:"class"`
	Type           string    `json:"type" bson:"type"`
	DisplayName    string    `json:"display_name" bson:"display_name"`
	DisplayPlace   string    `json:"display_place" bson:"display_place"`
	DisplayAddress string    `json:"display_address" bson:"display_address"`
	Address        OsmPlaceAddress `json:"address" bson:"address"`
}

type OsmPlaceAddress struct {
	Name        string `json:"name" bson:"name"`
	City        string `json:"city" bson:"city"`
	State       string `json:"state" bson:"state"`
	Country     string `json:"country" bson:"country"`
	CountryCode string `json:"country_code" bson:"country_code"`
}
```
