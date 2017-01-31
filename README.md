
#

simple script to generate an API document from the Postman collection json file.

## get all tools

for getting an postman collection

* install postman
* install postman interceptor as chrome plugin
* for generating the html file:
    ```
    > brew install pandoc
    ```



## Generate documentation

```
> postman2doc myservice.json myservice.md
```

## Convert MD into HTML

```
> pandoc --toc -c uritocss myservice.md  -o myservice.html
```
