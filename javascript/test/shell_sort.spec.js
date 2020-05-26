const chai = require('chai')
const { describe, it } = require('mocha')
const shellSort = require('../algo/sorting/shell_sort')

chai.should()

describe('shell sort', () => {
  describe('a random unordered array', () => {
    it('should be ordered in place', () => {
      for (let i = 10; i < 1000; i = i + 100) {
        const array = Array(i).fill().map(() => Math.round(Math.random() * i))
        const expected = JSON.parse(JSON.stringify(array))
        expected.sort((a, b) => a - b)
        shellSort(array)
        array.should.be.deep.equal(expected)
      }
    })
  })
})
