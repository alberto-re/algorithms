const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
})

rl.on('line', function (line) {
  const array = line.split(' ').map(Number)
  cocktailSort(array)
  console.log(array.join(' '))
  process.exit(0)
})

function swap (array, i, j) {
  const tmp = array[i]
  array[i] = array[j]
  array[j] = tmp
}

function cocktailSort (array) {
  while (true) {
    let swapped = false
    for (let i = 0; i < array.length - 1; i++) {
      if (array[i] > array[i + 1]) {
        swap(array, i, i + 1)
        swapped = true
      }
    }
    if (!swapped) break
    for (let i = array.length - 1; i > 0; i--) {
      if (array[i - 1] > array[i]) {
        swap(array, i - 1, i)
        swapped = true
      }
    }
    if (!swapped) break
  }
}

module.exports = cocktailSort
