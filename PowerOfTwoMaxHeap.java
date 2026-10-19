import java.util.ArrayList;
import java.util.NoSuchElementException;

public class PowerOfTwoMaxHeap {

    private final ArrayList<Integer> heap;
    private final int childExponent;
    private final int numChildren; // 2^x children per node

    /**
     * Constructor to initialize the Power of Two Max Heap.
     * @param childExponent The exponent x, where each parent node has 2^x children.
     */
    public PowerOfTwoMaxHeap(int childExponent) {
        if (childExponent < 0) {
            throw new IllegalArgumentException("Child exponent x must be non-negative.");
        }
        this.heap = new ArrayList<>();
        this.childExponent = childExponent;
        this.numChildren = 1 << childExponent; // 2^x children using bitwise left shift
    }

    /**
     * Inserts a new value into the heap.
     */
    public void insert(int value) {
        heap.add(value);
        siftUp(heap.size() - 1);
    }

    /**
     * Removes and returns the maximum element from the heap.
     */
    public int popMax() {
        if (heap.isEmpty()) {
            throw new NoSuchElementException("Heap is empty.");
        }

        int maxVal = heap.get(0);
        int lastVal = heap.remove(heap.size() - 1);

        if (!heap.isEmpty()) {
            heap.set(0, lastVal);
            siftDown(0);
        }

        return maxVal;
    }

    private void siftUp(int index) {
        int insertedValue = heap.get(index);
        while (index > 0) {
            int parentIndex = (index - 1) >> childExponent;
            if (insertedValue > heap.get(parentIndex)) {
                heap.set(index, heap.get(parentIndex));
                index = parentIndex;
            } else {
                break;
            }
        }
        heap.set(index, insertedValue);
    }

    private void siftDown(int index) {
        int size = heap.size();
        int parentValue = heap.get(index);

        while (true) {
            int firstChildIndex = (index << childExponent) + 1;
            if (firstChildIndex >= size) {
                break;
            }

            int maxChildIndex = firstChildIndex;
            int maxChildValue = heap.get(firstChildIndex);
            int lastChildIndex = Math.min(firstChildIndex + numChildren, size);

            for (int i = firstChildIndex + 1; i < lastChildIndex; i++) {
                if (heap.get(i) > maxChildValue) {
                    maxChildValue = heap.get(i);
                    maxChildIndex = i;
                }
            }

            if (maxChildValue > parentValue) {
                heap.set(index, maxChildValue);
                index = maxChildIndex;
            } else {
                break;
            }
        }
        heap.set(index, parentValue);
    }

    public static void main(String[] args) {
        PowerOfTwoMaxHeap heap = new PowerOfTwoMaxHeap(2);
        heap.insert(10);
        heap.insert(20);
        heap.insert(15);
        System.out.println("Max element: " + heap.popMax());
    }
}