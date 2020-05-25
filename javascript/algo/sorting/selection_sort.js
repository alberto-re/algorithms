const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
})

rl.on('line', function (line) {
  const array = line.split(' ').map(Number)
  selectionSort(array)
  console.log(array.join(' '))
  process.exit(0)
})

function swap (array, i, j) {
  const tmp = array[i]
  array[i] = array[j]
  array[j] = tmp
}

function selectionSort (array) {
  for (let i = 0; i < array.length; i++) {
    let minIdx = i
    for (let j = i + 1; j < array.length; j++) {
      if (array[minIdx] > array[j]) {
        minIdx = j
      }
    }
    if (minIdx !== i) {
      swap(array, i, minIdx)
    }
  }
}

module.exports = selectionSort
