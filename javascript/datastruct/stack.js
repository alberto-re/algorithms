/**
 * Stack ADT (Abstract Data Structure) implementations in JavaScript.
 * 
 * Here two implementations are provided:
 * - LinkedListStack, based on a singly-linked list.
 * - DynamicArrayStack, based on the JavaScript array type.
 * 
 * Both provides the same interface exposing those methods:
 *
 * - push: adds an item to the top of the stack.
 * - pop: removes the last inserted item from the top of the stack.
 * - peek: returns the item at the top of the stack without removing it.
 * - isEmpty: returns true if stack is empty, else false.
 * 
 * All methods run in O(1) time (or amortized O(1) in the dynamic array
 * implementations of push/pop).
 */
class Node {

    constructor (value) {
        this.value = value
        this.child = null
    }
    
    addChild (child) {
        this.child = child
    }
}
    
class LinkedListStack {
    
    constructor () {
        this.top = null
        this.size = 0
    }
    
    push (value) {
        const tmp = this.top
        this.top = new Node(value)
        this.top.addChild(tmp)
        this.size++
    }
    
    pop () {
        if (this.top === null) {
            return null
        } else {
            const retVal = this.top.value
            this.top = this.top.child
            this.size--
            return retVal
        }
    }
    
    peek () {
        return this.top === null ? this.top : this.top.value
    }
    
    size () {
        return this.size
    }
    
    isEmpty () {
        return this.size === 0
    }
}
    
class DinamicArrayStack {
    
    constructor () {
        this.elements = []
    }
    
    push (value) {
        this.elements.push(value)
    }
    
    pop () {
        this.elements.pop()
    }
    
    peek () {
        return this.elements[this.elements.length - 1]
    }
    
    size () {
        return this.elements.length
    }
    
    isEmpty () {
        return this.elements.isEmpty()
    }
}
    
module.exports = {
    LinkedListStack,
    DinamicArrayStack
}
    