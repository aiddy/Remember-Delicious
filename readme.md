# Post Link

A little Python script to post links to [Del.icio.us](http://delicious.com). Simply does a POST to the [delicious API](https://github.com/SciDevs/delicious-api).

## Usage

	postlink URL Description Tags
		
		URL          The URL of the page to post to delicious
		Description  A string providing a description for the link
		Tags         A string providing a comma delimited list of tags for the link

## Dependencies 

* Uses [Requests](http://docs.python-requests.org/en/latest/) for HTTP stuff

