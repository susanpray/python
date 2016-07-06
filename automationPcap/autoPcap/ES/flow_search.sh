#!/bin/bash

curl -XPOST 'http://192.168.24.81:9200/flow/_search?pretty=true' -d '{
	"query": {
		"bool": {
			"must": [
				{"term": {"sp": "'$1'"}},
				{"term": {"dp": "'$2'"}}
			]
		}
	},
	"_source": {
		"includes": ["receiveoctet","sendoctet","receivepacket","sendpacket"]
	},
	"sort": [{"startts": {"order": "desc"}}],
	"from": 0,"size": 1
}'
