/** Node: node for a singly linked list. */

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

/** LinkedList: chained together nodes. */

class LinkedList {
  constructor(vals = []) {
    this.head = null;
    this.tail = null;
    this.length = 0;

    for (let val of vals) this.push(val);
  }

  _get(idx) {
    let cur = this.head
    let count = 0

    while (cur !== null & count != idx) {
      count += 1
      cur = cur.next
    }
    return cur;
  }

  /** push(val): add new value to end of list. */


  push(val) {
    // we take the val of the "new Node"
    let newNode = new Node(val);
    // if there is no head
    if (!this.head) {
      // we make the new NewNode the head and the tail
      this.head = newNode
      this.tail = newNode
      // else
    } else {
      // we make the newNode the ____.next -> then the newNode becomes the tail
      this.tail.next = newNode
      this.tail = newNode
    }

    this.length += 1
  }

  /** unshift(val): add new value to start of list. */

  unshift(val) {
    let newNode = new Node(val);
    // if there is no head
    if (this.head === null) {
      this.head = newNode;
      // else
    } else {
      // the next newNode will now be the head
      newNode.next = this.head
      this.head = newNode;
    }
    // if the length is 0 then this.tail is this.head
    if (this.length === 0) this.tail = this.head;

    // increment this.length by 1
    this.length += 1
  }

  /** pop(): return & remove last item. */

  pop() {
    // remove the last element 
    return this.removeAt(this.length - 1)
  }

  /** shift(): return & remove first item. */

  shift() {
    // remove the first element
    return this.removeAt(0)
  }

  /** getAt(idx): get val at idx. */

  getAt(idx) {
    // if idx is greater than or equal to this.length OR less than 0
    // throw new Error: invalid index
    if (idx >= this.length || idx < 0) {
      throw new Error("Invalid index")
    }
    return this._get(idx).val
  }

  /** setAt(idx, val): set val at idx to val */

  setAt(idx, val) {
    // if idx is less than or equal to this.length OR less than 0
    // throw new Error: invalid index
    if (idx >= this.length || idx < 0) {
      throw new Error("Invalid index")
    }
    // create a variable named cur and set it equal to the index at this._get
    // current value equals value
    let cur = this._get(idx)
    cur.val = val;
  }

  /** insertAt(idx, val): add node w/val before idx. */

  insertAt(idx, val) {
    // if idx is less than or equal to this.length OR less than 0
    // throw new Error: invalid index
    if (idx >= this.length || idx < 0) {
      throw new Error("Invalid index")
    }
    // if idx is 0 unshift val and return
    if (idx === 0) return this.unshift(val)
    // if idc equals this.length push val and return
  if (idx === this.length) return this.push(val)

  // create a variable "previous" and retrieve the "previous" index before this
  let prev  = this._get(idx -1)

  // create a newNode variable
  let newNode = new Node(val);
  // set the next newNode to equal the prev next
  newNode.next = prev.next
  // the previous next now becomes the newNode
  prev.next = newNode
  }

  /** removeAt(idx): return & remove item at idx, */

  removeAt(idx) {
    // if idx is less than or equal to this.length OR less than 0
    // throw new Error: invalid index
    if (idx >= this.length || idx < 0) {
      throw new Error("Invalid index")
    }

    // remove first item

    // if idx is 0
    if (idx === 0) {
      // create a variable "val" and set it to be the val of the head
      let val = this.head.val;
      // the head should equal the next head
      this.head = this.head.next
      // decrement the length by 1
      this.length -= 1
      // if the length is less than 2 the tail is the head
      if (this.length < 2) this.tail = this.head
      // return val
      return val
    }

    // get the index before this one
    let prev = this._get(idx - 1)

    // remove tail
    
    // if idx is the last idx
    if (idx === this.length - 1) {
      // create a val variable and set it to the prev next val
      let val = prev.next.val
      // set prev.next to be empty
      prev.next = null;
      // this.tial = prev
      this.tail = prev
      // decrement this.length
      this.length -= 1
      // return val
      return val
    }

    // remove in the middle

      // create a val variable and set it to the prev next val
      let val = prev.next.val
      // set the prev.next to equal the prev next next
      prev.next = prev.next.next
      // decrement this.length
      this.length -= 1
      // return val
      return val
  }

  /** average(): return an average of all values in the list */

  average() {
    // if the length is 0 return 0
    if (this.length === 0) return 0

    // create an empty total variable 
    let total = 0
    // create a variable "current" and set it equal to the head
    let current = this.head

    // while there is a head
    while (currrent) {
      // add and update current val to total
      total += current.val
      // set current to equal the next
      current = current.next
    }
    // return total divided by th length
    return total / this.length
  }
}

module.exports = LinkedList;
