const chai = require('chai')
const { describe, it } = require('mocha')
const selectionSort = require('../algo/sorting/selection_sort')

chai.should()

describe('selection sort', () => {
  describe('a random unordered array', () => {
    it('should be ordered in place', () => {
      for (let i = 10; i < 1000; i = i + 100) {
        const array = Array(i).fill().map(() => Math.round(Math.random() * i))
        const expected = JSON.parse(JSON.stringify(array))
        expected.sort((a, b) => a - b)
        selectionSort(array)
        array.should.be.deep.equal(expected)
      }
    })
  })
})
