const express = require('express')
const userController = require('../controllers/user')

const userRouter = express.Router()

/**
 * @typedef User
 * @property {string} username.required - User username
 * @property {string} firstname - First name
 * @property {string} lastname - Last name
 */

/**
 * @route POST /user
 * @group User - Operations about user
 * @param {User.model} user.body - User object
 * @returns {object} 201 - Success response
 * @returns {Error} 400 - Wrong user parameters
 */
userRouter
  .post('/', (req, resp) => {
    userController.create(req.body, (err, res) => {
      let respObj
      if(err) {
        respObj = {
          status: "error",
          msg: err.message
        }
        return resp.status(400).json(respObj)
      }
      respObj = {
        status: "success",
        msg: res
      }
      resp.status(201).json(respObj)
    })
  })

/**
 * @route GET /user/{username}
 * @group User - Operations about user
 * @param {string} username.path.required - username of the user
 * @returns {object} 200 - Success response with user object
 * @returns {Error} 404 - User not found
 */
  .get('/:username', (req, resp, next) => {
    const username = req.params.username
    userController.get(username, (err, res) => {
      let respObj
      if (err) {
        respObj = {
          status: "error",
          msg: err.message
        }
        return resp.status(404).json(respObj)
      }
      respObj = {
        status: "success",
        data: res
      }
      resp.status(200).json(respObj)
    })
  })
  
module.exports = userRouter