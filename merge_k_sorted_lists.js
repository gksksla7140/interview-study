var merge = function (list1, list2) {
    let dummy = new ListNode(0);
    let cur = dummy;
    while (list1 != null && list2 != null) {
        if (list1.val > list2.val) {
            cur.next = list2;
            list2 = list2.next;
        } else {
            cur.next = list1;
            list1 = list1.next;
        }
        cur = cur.next;
    }
    if (list1 !== null) {
        cur.next = list1;
    }
    if (list2 !== null) {
        cur.next = list2;
    }
    return dummy.next;
}


var mergeKLists = function (lists) {
    if (lists === null || lists.length === 0) {
        return lists;
    }
    // 两两merge
    while (lists.length > 1) {
        lists.push(merge(lists.pop(), lists.shift()));
    }
    return lists[0];
};