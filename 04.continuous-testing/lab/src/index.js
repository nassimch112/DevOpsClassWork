const express = require('express')
const userRouter = require('./routes/user')
const bodyParser = require('body-parser')

const app = express()
const port = process.env.PORT || 3000

// Setup Express Swagger Generator
const expressSwagger = require('express-swagger-generator')(app);

let options = {
    swaggerDefinition: {
        info: {
            title: 'User API',
            version: '1.0.0',
            description: 'API documentation for User management',
        },
        host: `localhost:${port}`,
        basePath: '/',
        produces: [
            "application/json",
            "text/plain"
        ],
        schemes: ['http'],
    },
    basedir: __dirname, //app absolute path
    files: ['./routes/**/*.js', './app.js'], //Path to the API handle folder
};
expressSwagger(options)

const db = require('./dbClient')
db.on("error", (err) => {
  console.error(err)
})

app.use(bodyParser.urlencoded({
  extended: false
}))
app.use(bodyParser.json())

app.get('/', (req, res) => res.send('Hello World!'))

app.use('/user', userRouter)

const server = app.listen(port, (err) => {
  if (err) throw err
  console.log("Server listening the port " + port)
})

module.exports = server