const { expect } = require('chai')
const userController = require('../src/controllers/user')
const db = require('../src/dbClient')

describe('User', () => {
  
  beforeEach(() => {
    // Clean DB before each test
    db.flushdb()
  })

  describe('Create', () => {

    it('create a new user', (done) => {
      const user = {
        username: 'sergkudinov',
        firstname: 'Sergei',
        lastname: 'Kudinov'
      }
      userController.create(user, (err, result) => {
        expect(err).to.be.equal(null)
        expect(result).to.be.equal('OK')
        done()
      })
    })

    it('passing wrong user parameters', (done) => {
      const user = {
        firstname: 'Sergei',
        lastname: 'Kudinov'
      }
      userController.create(user, (err, result) => {
        expect(err).to.not.be.equal(null)
        expect(result).to.be.equal(null)
        done()
      })
    })
  })

  describe('Get', () => {
    
    it('get a user by username', (done) => {
      const user = {
        username: 'sergkudinov',
        firstname: 'Sergei',
        lastname: 'Kudinov'
      }
      // Create a user to make this unit test independent from the others
      userController.create(user, (err, result) => {
        expect(err).to.be.equal(null)
        
        // Check if the result of the get method is correct
        userController.get(user.username, (err, res) => {
          expect(err).to.be.equal(null)
          expect(res).to.be.a('object')
          expect(res.firstname).to.be.equal('Sergei')
          expect(res.lastname).to.be.equal('Kudinov')
          done()
        })
      })
    })

    it('cannot get a user when it does not exist', (done) => {
      // Check with any invalid user
      userController.get('invaliduser', (err, res) => {
        expect(err).to.not.be.equal(null)
        expect(res).to.be.equal(null)
        done()
      })
    })

  })
})