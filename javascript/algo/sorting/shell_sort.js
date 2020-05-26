const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
})

rl.on('line', function (line) {
  const array = line.split(' ').map(Number)
  shellSort(array)
  console.log(array.join(' '))
  process.exit(0)
})

function swap (array, i, j) {
  const tmp = array[i]
  array[i] = array[j]
  array[j] = tmp
}

function shellSort (array) {
  const n = array.length
  let h = 1
  while (h < n / 3) h = 3 * h + 1
  while (h >= 1) {
    for (let i = h; i < array.length; i++) {
      let j = i
      while (j >= h && array[j - h] > array[j]) {
        swap(array, j, j - h)
        j = j - h
      }
    }
    h = Math.floor(h / 3)
  }
}

module.exports = shellSort
