// Input: [
//     [1, 3],
//     [2, 6],
//     [8, 10],
//     [15, 18]
// ]
// Output: [
//     [1, 6],
//     [8, 10],
//     [15, 18]
// ]
// Explanation: Since intervals[1, 3] and[2, 6] overlaps, merge them into[1, 6].
// answer############
var merge = function (intervals) {
    let result = [];
    let sorted = intervals.sort((a, b) => a.start - b.start);
    for (let i = 0; i < sorted.length - 1; i++) {
        if (sorted[i].end >= sorted[i + 1].start) {
            sorted[i + 1].start = Math.min(sorted[i].start, sorted[i + 1].start);
            sorted[i + 1].end = Math.max(sorted[i].end, sorted[i + 1].end);
            sorted = sorted.slice(0, i).concat(sorted.slice(i + 1));
            i--;
        }
    }
    return sorted;
};

// 3 % fast

var merge = function (intervals) {
    let i = 0
    let size = intervals.length
    let result = []
    while (i < size) {
        let item = intervals[i]
        if (item) {
            let j = i + 1
            let lastMerged
            // console.log('item', item, intervals)
            while (j < size) {
                let next = intervals[j]
                // console.log('next', next)
                if (next) {
                    if (item.start >= next.start && next.end >= item.start) {
                        // Swap
                        let tmp = item
                        item = next
                        next = tmp
                    }
                    if (item.end >= next.start && item.start <= next.start) {
                        // overlap found, merge
                        if (next.end > item.end) {
                            item.end = next.end
                        }
                        // set merged j to null
                        intervals[j] = null
                        lastMerged = j
                    }
                }
                j++
            }
            if (lastMerged) {
                // Put merged item back to the original array in case the next i could
                // merge with it.
                intervals[lastMerged] = item
            } else {
                result.push(item)
            }
        }
        i++
    }

    return result
};
