class MinHeap {
    elements = []
    constructor(collection = null) {
        if(collection) {
            // this.elements = collection;
            this.elements.unshift(0);
            this.buildHead(collection);
        }

    }

    buildHead(collection) {
        // for(let i = this.elements.length-1; i > 1; i--) {
        //     this.siftUp(i);
        // }
        for(let item of collection) {
            this.add(item)
        }
    }

    siftUp(i) {
        let minIndex = i
        while(minIndex > 1 && this.elements[minIndex] < this.elements[this.parent(minIndex)]) {
            const parentIndex = this.parent(minIndex)
            this.swap(minIndex, parentIndex)
            minIndex = parentIndex
        }
    }

    swap(a, b) {
        const tmp = this.elements[a]
        this.elements[a] = this.elements[b]
        this.elements[b] = tmp
    }
    parent(i) {
        return Math.floor(i/2)
    }
    leftChild(i) {
        return Math.floor(i/2)
    }
    rightChild(i) {
        return Math.floor(i/2)+1
    }

    add(item) {
        this.elements.push(item)
        this.siftUp(this.elements.length-1)
    }

    print() {
        if(this.elements.length > 1) {
            for(let i=1; i < this.elements.length/2; i++) {
                console.log(this.elements[i])
                let lChild = this.leftChild(i)
                let rChild = this.rightChild(i)

                lChild = lChild < this.elements.length ? this.elements[lChild] : null
                rChild = rChild < this.elements.length ? this.elements[rChild] : null
                console.log(lChild, rChild)
            }
        }
    }
}

class PriorityQueue {

}

const list = [42, 29, 18,14, 7 ,18, 12, 11, 5];
hp = new MinHeap(list)
hp.print
console.log(hp.elements)


module.exports.MinHeap = MinHeap;
module.exports = PriorityQueue