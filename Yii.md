# Yii2 starter kit API

## Articles
### Get Articles by slug
#### request
```
GET http://api.yii2-starter-kit.dev/v1/article/search?slug=id-voluptas-ipsum-non-mollitia-magni
```
### Create article
#### request
```
POST http://api.yii2-starter-kit.dev/v1/articles
```
```javascript
{
    "body": "Suscipit cum eos magnam ut. Adipisci doloribus tempore eligendi. Sit ratione expedita perferendis odit non.", 
    "title": "Miss", 
    "category_id": 1, 
    "id": 5, 
    "slug": "new-slug"
}
```
### Update article
#### request
```
PUT http://api.yii2-starter-kit.dev/v1/articles/11
```
```javascript
{
    "body": "Suscipit cum eos magnam ut. Adipisci doloribus tempore eligendi. Sit ratione expedita perferendis odit non.", 
    "category_id": 1, 
    "slug": "old-slug", 
    "title": "Miss"
}
```
### Delete Article
#### request
```
DELETE http://api.yii2-starter-kit.dev/v1/articles/11
```
### Get Article by ID
#### request
```
GET http://api.yii2-starter-kit.dev/v1/articles/6
```
### Get All Articles
#### request
```
GET http://api.yii2-starter-kit.dev/v1/articles
```
## Authorization
### Get OAuth 2.0 Password Credentials Grant
#### request
```
POST http://api.yii2-starter-kit.dev/v1/authorization/login
```
```javascript
{
    "username": "webmaster", 
    "client_secret": "client_secret", 
    "password": "webmaster", 
    "client_id": "client_name"
}
```
### Invalidate OAuth token
#### request
```
POST http://api.yii2-starter-kit.dev/v1/authorization/logout
```
```javascript
{
    "username": "webmaster", 
    "client_secret": "client_secret", 
    "password": "webmaster", 
    "client_id": "client_name"
}
```
## Pages
### Get Pages by slug
#### request
```
GET http://api.yii2-starter-kit.dev/v1/page/search?slug=id-voluptas-ipsum-non-mollitia-magni
```
### Create Page
#### request
```
POST http://api.yii2-starter-kit.dev/v1/pages
```
### Update page
#### request
```
PUT http://api.yii2-starter-kit.dev/v1/pages/11
```
### Delete page
#### request
```
DELETE http://api.yii2-starter-kit.dev/v1/pages/11
```
### Get page by ID
#### request
```
GET http://api.yii2-starter-kit.dev/v1/pages/6
```
### Get All pages
#### request
```
GET http://api.yii2-starter-kit.dev/v1/pages
```
## User
### Create User copy
#### request
```
POST http://api.yii2-starter-kit.dev/v1/users
```
```javascript
{
    "username": "2xAsa2aaaai2A", 
    "password": "PEPAEPiEEP", 
    "email": "sxx22A@iDDDA.coam", 
    "name": "ROMINA SUAREZ"
}
```
