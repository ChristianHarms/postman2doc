
#

simple script to generate an API document from the Postman collection json file.

## todo

* we read post-body allways from request.raw attribute as json
* pretty print response-body for json / xml

## get all tools

for getting an postman collection

* install postman
* install postman interceptor as chrome plugin
* for generating the html file from md:
```
> brew install pandoc
```


## Build API data

* start postman interceptor + activate
* start postman + sync interceptor
* capture request in postman history
* take your requests to a collection (organize it in subfolder=
* save response data on every request separate (in postman)
* export collection als postman-collection 2.0 json file

## Generate documentation

```
> ./postman2md.py myservice.json myservice.md
```

## Convert MD into HTML

```
> pandoc --toc -c <uritocss> myservice.md  -o myservice.html
```

You can use for *uritocss* an public uri like https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css