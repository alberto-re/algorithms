const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
})

rl.on('line', function (line) {
  const array = line.split(' ').map(Number)
  insertionSort(array)
  console.log(array.join(' '))
  process.exit(0)
})

function swap (array, i, j) {
  const tmp = array[i]
  array[i] = array[j]
  array[j] = tmp
}

function insertionSort (array) {
  for (let i = 1; i < array.length; i++) {
    let j = i
    while (j > 0 && array[j - 1] > array[j]) {
      swap(array, j, j - 1)
      j--
    }
  }
}

module.exports = insertionSort
