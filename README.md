
#

simple script to generate an API document from the Postman collectionv2 json file.

## todo

* we read post-body allways from request.body.raw attribute as json
```
"body": {
          "mode": "raw",
          "raw": "{\"pin\":\"1111\"}"
      }
```
* pretty print response-body for json / xml
* hard-coded Header list for export
* no Cookies export - feel free to add it

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
* save requests to a collection (organize it in subfolder)
* re-run and save response data on every request separate (in postman)
* export collection als postman-collection v2.0 json file

## Generate documentation

```
> ./postman2md.py myservice.json myservice.md
```

## Convert MD into HTML

```
> pandoc --toc -c <uritocss> myservice.md  -o myservice.html
```

You can use for *uritocss* an public uri like https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css