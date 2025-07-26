function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

var addTwoNumbers = function( l1, l2) {
    let p1 = l1;
    let p2 = l2;
    let sum = 0;
    let carry = 0;
    const node_list = [];
    while (p1 || p2 || carry) {
        let val1 = p1 ? p1.val: 0;
        let val2 = p2 ? p2.val: 0;
        sum = val1 + val2 + carry;
        carry = Math.floor(sum / 10);
        const new_node = new ListNode( sum % 10);
        node_list.push(new_node);
        p1 = p1 ? p1.next : null;
        p2 = p2 ? p2.next : null;
    }
    for (let i = 0; i < node_list.length - 1; i++) {
        node_list[i].next = node_list[i+1];
    }
    return node_list[0] || null;
}

function arrayToLinkedList(arr) {
    const dummy = new ListNode(0);
    let current = dummy;
    for (let num of arr) {
        current.next = new ListNode(num);
        current = current.next;
    }
    return dummy.next;
}

function linkedListToArray(l1) {
    const node_list = [];
    let current = l1;
    while (current) {
        node_list.push(current.val);
        current = current.next;
    }
    return node_list;
}

const l1 = arrayToLinkedList([1,2,6]);
const l2 = arrayToLinkedList([2,3,4]);

result = linkedListToArray(addTwoNumbers(l1, l2));

console.log(result);
